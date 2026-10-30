#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path

def lint_srt(srt_path):
    content = Path(srt_path).read_text(encoding="utf-8")
    blocks = content.strip().split("\n\n")

    issues = []
    for b in blocks:
        lines = b.splitlines()
        if len(lines) >= 3:
            idx = lines[0]
            timestamp = lines[1]
            text = " ".join(lines[2:])

            # Check character count per line (max 38 chars for mobile 9:16)
            if len(text) > 42:
                issues.append(f"Subtitle #{idx} exceeds mobile character safety: {len(text)} chars (Max 42). Text: '{text[:25]}...'")

    return {
        "file": str(srt_path),
        "status": "FAIL" if len(issues) > 0 else "PASS",
        "total_issues": len(issues),
        "issues": issues
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--srt", required=True)
    args = p.parse_args()

    res = lint_srt(args.srt)
    print(res)

if __name__ == "__main__":
    main()
