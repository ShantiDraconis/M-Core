#!/usr/bin/env python3
"""Varre todos os branches de um clone git atrás de "provas" dos 7 problemas.

Uso: proof_scan.py <repo_dir> <saida.json>

Para cada arquivo .lean (deduplicado por blob) encontra declarações theorem/lemma/def/
example/instance/abbrev cuja CONCLUSÃO começa por um alvo (enunciado, terminal ou obrigação).
Classifica:
  * hypotheses: binders explícitos antes do ':' final (argumentos = condicional)
  * file_sorry / file_axiom: o arquivo usa sorry/admit ou declara axiom
Também registra alegações textuais (state := .proved, CLOSED_MATH = true, etc.) em qualquer arquivo.
"""
import json, os, re, subprocess, sys
from collections import defaultdict

TARGETS = {
    # enunciados
    "RiemannHypothesis": "riemann", "BealConjecture": "beal", "FermatLastTheorem": "beal(ponte)",
    "PneqNP": "pvsnp", "PneNP": "pvsnp", "ClayStatementA": "navier-stokes",
    "HodgeConjecture": "hodge", "BSDFull": "bsd", "BSDRank": "bsd", "BSDConjecture": "bsd",
    "ClayYM": "yang-mills", "YangMillsMassGap": "yang-mills", "MassGap": "yang-mills",
    # terminais do registro
    "FiniteSpanApproximatesChi": "riemann", "ConcreteUniformLogDNBound": "riemann",
    "UniformLogBound": "riemann", "RiemannOffCriticalZero": "riemann(refutação)",
    "GCDLowerBoundProducer": "beal", "BealUniversalGCDTarget": "beal",
    "GCDLowerBoundSmallExponents": "beal",
    "ActualNSToSignedGainCore": "navier-stokes", "NavierStokesStabilizationTarget": "navier-stokes",
    "EnstrophyAPrioriBound": "navier-stokes",
    "UniversalFailure": "pvsnp", "G21Pointwise": "pvsnp", "SATNotInP": "pvsnp",
    "P01ConstructionGap": "pvsnp(P01)", "P01MachineConstruction": "pvsnp(P01)",
    "ConcreteAlgebraicityPayload": "hodge", "HodgeRealizationTarget": "hodge", "MiddleCodimension": "hodge",
    "BSDRealizableTarget": "bsd", "RankOpen": "bsd", "RefinedOpen": "bsd", "RankResidual": "bsd",
    "B60ConcretePhysicalAdapter": "yang-mills", "YangMills4DGapTarget": "yang-mills",
    "ConstructiveYM4D": "yang-mills",
}
TARGET_RX = re.compile(r"\b(" + "|".join(sorted(TARGETS, key=len, reverse=True)) + r")\b")
DECL_RX = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*"
                     r"(theorem|lemma|def|example|instance|abbrev)\b", re.M)
CLAIM_RX = re.compile(r"(state\s*:=\s*\.proved|CLOSED_MATH\s*[:=]\s*(?:true|True|1)|"
                      r"\"CLOSED_MATH\"\s*:\s*true|OPEN_MATH\s*[:=]\s*(?:false|False)|"
                      r"\"OPEN_MATH\"\s*:\s*false|PROVED_UNCONDITIONAL|MILLENNIUM_SOLVED)", re.I)
CLAIM_EXT = (".lean", ".md", ".json", ".yaml", ".yml", ".txt", ".toml")


def git(repo, *args, inp=None):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True, input=inp,
                          check=False).stdout


def strip_comments(code):
    code = re.sub(r"/-.*?-/", lambda m: "\n" * m.group(0).count("\n"), code, flags=re.S)
    return re.sub(r"--[^\n]*", "", code)


def split_signature(sig):
    """Retorna (binders, conclusão) separando no ':' de nível zero mais à direita
    antes de ':='."""
    depth, last = 0, -1
    for i, ch in enumerate(sig):
        if ch in "([{⦃⟨": depth += 1
        elif ch in ")]}⦄⟩": depth -= 1
        elif ch == ":" and depth == 0 and not sig[i:i+2] == ":=" and (i == 0 or sig[i-1] != ":"):
            last = i
    if last < 0:
        return sig, ""
    return sig[:last], sig[last+1:]


def scan_decls(code):
    out = []
    starts = [m.start() for m in DECL_RX.finditer(code)] + [len(code)]
    for a, b in zip(starts, starts[1:]):
        chunk = code[a:b]
        kind = DECL_RX.match(chunk).group(1)
        head = chunk.split(":=", 1)[0] if ":=" in chunk else chunk.split(" where", 1)[0]
        head = " ".join(head.split())
        m = re.match(r"(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*"
                     r"(theorem|lemma|def|example|instance|abbrev)\s*([^\s(:{\[⦃]*)\s*(.*)", head)
        if not m:
            continue
        name, rest = m.group(2), m.group(3)
        binders, concl = split_signature(rest)
        concl = concl.strip()
        c = re.sub(r"^(Nonempty\s*\(?|¬\s*|Not\s*\(?|\(\s*)+", "", concl)
        t = TARGET_RX.match(c)
        if not t:
            continue
        hyps, depth, buf = [], 0, ""
        for ch in binders:
            if ch == "(":
                depth += 1
                if depth == 1:
                    buf = ""; continue
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    if ":" in buf: hyps.append(buf.strip())
                    continue
            if depth >= 1: buf += ch
        inst = re.findall(r"\[[^\]]*\]", binders)
        lineno = code[:a].count("\n") + 1
        out.append({"kind": kind, "name": name, "line": lineno, "conclusion": concl[:200],
                    "target": t.group(1), "problem": TARGETS[t.group(1)],
                    "negated": concl.startswith("¬") or concl.startswith("Not"),
                    "explicit_hypotheses": len(hyps), "hypotheses": [h[:120] for h in hyps[:6]],
                    "typeclass_args": len(inst)})
    return out


def main(repo, outp):
    refs = git(repo, "for-each-ref", "--format=%(refname)", "refs/remotes/origin").decode().split()
    refs = [r for r in refs if not r.endswith("/HEAD")] or ["HEAD"]
    blob_paths = defaultdict(set)   # blob -> {(ref, path)}
    text_blobs = defaultdict(set)
    for ref in refs:
        for line in git(repo, "ls-tree", "-r", ref).decode("utf-8", "replace").splitlines():
            meta, path = line.split("\t", 1)
            _, typ, blob = meta.split()
            if typ != "blob":
                continue
            short = ref.replace("refs/remotes/origin/", "")
            if path.endswith(".lean"):
                blob_paths[blob].add((short, path))
            elif path.endswith(CLAIM_EXT):
                text_blobs[blob].add((short, path))
    findings, claims = [], []
    allblobs = list(blob_paths) + list(text_blobs)
    if allblobs:
        data = git(repo, "cat-file", "--batch", inp=("\n".join(allblobs) + "\n").encode())
        pos = 0
        contents = {}
        while pos < len(data):
            nl = data.index(b"\n", pos)
            hdr = data[pos:nl].decode().split()
            if len(hdr) < 3:
                pos = nl + 1; continue
            sha, size = hdr[0], int(hdr[2])
            contents[sha] = data[nl+1:nl+1+size]
            pos = nl + 1 + size + 1
        for blob, locs in blob_paths.items():
            raw = contents.get(blob, b"").decode("utf-8", "replace")
            code = strip_comments(raw)
            decls = scan_decls(code)
            has_sorry = bool(re.search(r"\b(sorry|admit)\b", code)) or bool(
                re.search(r"(exact|refine|apply)\s+\?_\s*$|:=\s*\?_\s*$", code, re.M))
            section_hyps = bool(re.search(r"^\s*variable\b[^\n]*\([^)]*:", code, re.M))
            axioms = re.findall(r"^\s*axiom\s+(\S+)", code, re.M)
            for d in decls:
                d.update({"blob": blob, "file_sorry": has_sorry, "file_axioms": axioms[:8],
                          "section_variables": section_hyps,
                          "locations": sorted(locs)[:5], "n_locations": len(locs)})
                findings.append(d)
            for m in CLAIM_RX.finditer(raw):
                claims.append({"blob": blob, "text": raw[max(0, m.start()-60):m.end()+60].replace("\n", " "),
                               "locations": sorted(locs)[:3], "n_locations": len(locs)})
        for blob, locs in text_blobs.items():
            raw = contents.get(blob, b"").decode("utf-8", "replace")
            for m in CLAIM_RX.finditer(raw):
                claims.append({"blob": blob, "text": raw[max(0, m.start()-80):m.end()+80].replace("\n", " "),
                               "locations": sorted(locs)[:3], "n_locations": len(locs)})
    res = {"repo": os.path.basename(repo.rstrip("/")), "refs": len(refs),
           "lean_blobs": len(blob_paths), "text_blobs": len(text_blobs),
           "findings": findings, "claims": claims}
    json.dump(res, open(outp, "w"), indent=1, ensure_ascii=False)
    unc = [f for f in findings if f["explicit_hypotheses"] == 0 and not f["negated"] and not f["section_variables"]]
    print(f"{res['repo']}: refs={len(refs)} lean_blobs={len(blob_paths)} achados={len(findings)} "
          f"sem_hipóteses={len(unc)} limpos_sem_hip={sum(1 for f in unc if not f['file_sorry'] and not f['file_axioms'])} "
          f"alegações={len(claims)}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
