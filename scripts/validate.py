#!/usr/bin/env python3
from __future__ import annotations
import argparse, sys, xml.etree.ElementTree as ET
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default=".")
    root = Path(ap.parse_args().root)
    projects = sorted(root.rglob("*.csproj"))
    if not projects:
        print("no csproj files", file=sys.stderr); return 1
    for p in projects:
        try:
            ET.parse(p)
        except ET.ParseError as exc:
            print(f"{p}: {exc}", file=sys.stderr); return 1
    cs = sorted((root / "src").rglob("*.cs"))
    if not cs:
        print("no C# sources", file=sys.stderr); return 1
    for p in cs:
        text = p.read_text(encoding="utf-8")
        if "namespace " not in text:
            print(f"{p}: missing namespace", file=sys.stderr); return 1
        if text.count("{") != text.count("}"):
            print(f"{p}: unbalanced braces", file=sys.stderr); return 1
    print(f"csharp validation ok ({len(cs)} files)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
