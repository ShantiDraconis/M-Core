#!/bin/bash
# usage: POINCARE_T2_fetch.sh <repo-dir> <outdir> < paths.txt
# Fetches the blobs of the given paths (HEAD) in one batched promisor fetch, then writes each to <outdir>/<path>.
repo=$1; out=$2; mkdir -p "$out"
tmp=$(mktemp); while read -r p; do git -C "$repo" ls-tree HEAD -- "$p" | awk '{print $3"\t"$4}'; done > "$tmp"
cut -f1 "$tmp" | git -C "$repo" -c fetch.negotiationAlgorithm=noop fetch -q origin --no-tags --no-write-fetch-head --recurse-submodules=no --stdin 2>&1 | tail -2
while IFS=$'\t' read -r oid p; do mkdir -p "$out/$(dirname "$p")"; git -C "$repo" cat-file blob "$oid" > "$out/$p"; done < "$tmp"
wc -l < "$tmp"; rm -f "$tmp"
