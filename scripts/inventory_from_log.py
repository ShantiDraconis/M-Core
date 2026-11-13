#!/usr/bin/env python3
"""Extrai o inventário regenerado do log do job `Proof inventory`.

Quando o inventário commitado está desatualizado, o job imprime os arquivos novos
como tar.gz em base64 entre BEGIN-INVENTORY-BUNDLE e END-INVENTORY-BUNDLE. Este
script lê o log baixado (com ou sem o carimbo de hora do Actions no começo de cada
linha) e grava inventory/PROOF_INVENTORY.json e .md no diretório atual.

Uso: python3 scripts/inventory_from_log.py LOG
"""
import base64
import io
import re
import sys
import tarfile

CARIMBO = re.compile(r"^\d{4}-\d\d-\d\dT[\d:.]+Z ")


def main(caminho):
    dentro, partes = False, []
    for linha in open(caminho, encoding="utf-8", errors="replace"):
        linha = CARIMBO.sub("", linha.rstrip("\r\n"))
        if linha == "BEGIN-INVENTORY-BUNDLE":
            dentro, partes = True, []
            continue
        if linha == "END-INVENTORY-BUNDLE":
            dentro = False
            continue
        if dentro:
            partes.append(linha.strip())
    if not partes:
        sys.exit("nenhum bloco BEGIN-INVENTORY-BUNDLE no log")
    dados = base64.b64decode("".join(partes))
    with tarfile.open(fileobj=io.BytesIO(dados), mode="r:gz") as tar:
        for m in tar.getmembers():
            if not m.isfile() or not m.name.startswith("inventory/") or ".." in m.name:
                sys.exit(f"membro inesperado no pacote: {m.name}")
        tar.extractall(".", filter="data")
    print("inventário extraído em inventory/")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
