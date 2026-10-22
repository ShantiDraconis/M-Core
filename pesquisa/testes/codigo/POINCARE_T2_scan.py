"""POINCARE P-T2 static scan of fetched Lean files (no build). Strips comments, then counts risky tokens.
usage: python3 -I POINCARE_T2_scan.py <dir> [<dir> ...]   (prints per-pattern counts and file:line hits)"""
import os, re, sys

PATS = {
    "axiom-decl": r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|unsafe\s+)*axiom\b",
    "sorry": r"\bsorry\b", "admit": r"\badmit\b", "native_decide": r"\bnative_decide\b",
    "implemented_by": r"implemented_by", "extern": r"@\[\s*extern", "unsafe": r"\bunsafe\b",
    "addDecl/Env.add": r"addDecl|Environment\.add|replayDecl|addAndCompile", "Kernel.": r"\bKernel\.",
    "skipKernelTC": r"skipKernelTC", "ofReduceBool": r"ofReduceBool|reduceBool|Lean\.reduceBool",
    "run_cmd/elab/meta": r"\brun_cmd\b|\brun_elab\b|\brun_meta\b|#eval\b",
    "elab/macro defs": r"^\s*(?:@\[[^\]]*\]\s*)?(?:elab_rules|elab|macro_rules|macro|syntax|declare_syntax_cat)\b",
    "initialize": r"^\s*(?:builtin_)?initialize\b|@\[\s*init\b",
    "import Lean": r"^\s*import\s+Lean(\.|\s|$)",
    "debug/opt": r"set_option\s+(?:debug\.|trace\.|maxHeartbeats\s+0|maxRecDepth)",
}
RX = {k: re.compile(v, re.M) for k, v in PATS.items()}


def strip_comments(src):
    out, i, n, depth = [], 0, len(src), 0
    while i < n:
        if src.startswith("/-", i):
            depth += 1; i += 2; continue
        if depth and src.startswith("-/", i):
            depth -= 1; i += 2; continue
        if depth:
            out.append("\n" if src[i] == "\n" else " "); i += 1; continue
        if src.startswith("--", i):
            j = src.find("\n", i); j = n if j < 0 else j; out.append(" " * (j - i)); i = j; continue
        if src[i] == '"':  # string literal
            j = i + 1
            while j < n and src[j] != '"':
                j += 2 if src[j] == "\\" else 1
            out.append(" " * (j + 1 - i)); i = j + 1; continue
        out.append(src[i]); i += 1
    return "".join(out)


def main():
    files = []
    for d in sys.argv[1:]:
        for root, _, fs in os.walk(d):
            files += [os.path.join(root, f) for f in fs if f.endswith(".lean")]
    files.sort()
    tot_lines = 0; counts = {k: 0 for k in PATS}; hits = []
    for f in files:
        src = open(f, encoding="utf-8", errors="replace").read()
        tot_lines += src.count("\n") + (0 if src.endswith("\n") else 1)
        s = strip_comments(src)
        for k, rx in RX.items():
            for m in rx.finditer(s):
                counts[k] += 1
                ln = s.count("\n", 0, m.start()) + 1
                hits.append((k, f, ln, src.splitlines()[ln - 1].strip()[:110]))
    print(f"files {len(files)} lines {tot_lines} mean {tot_lines / max(len(files), 1):.1f}")
    print("counts:", {k: v for k, v in counts.items()})
    for k, f, ln, txt in hits[:60]:
        print(f"  [{k}] {f}:{ln}: {txt}")


main()
