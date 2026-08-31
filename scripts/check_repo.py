#!/usr/bin/env python3
"""Small dependency-free check for paper metadata."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
ARXIV = re.compile(r"arXiv\D+(\d{4}\.\d{4,5})")
REQUIRED = ("提交日期", "主要机构", "主方向")


def main() -> int:
    files = sorted(PAPERS.glob("*/*.md"))
    ids: dict[str, Path] = {}
    errors: list[str] = []

    if not files:
        errors.append("papers/ 下没有论文页面")

    for path in files:
        text = path.read_text(encoding="utf-8")
        for field in REQUIRED:
            if not re.search(rf"\*\*{re.escape(field)}\*\*:\s*[^—\n]+", text):
                errors.append(f"{path}: 缺少 {field}")
        match = ARXIV.search(text)
        if not match:
            errors.append(f"{path}: 缺少 arXiv ID")
            continue
        arxiv_id = match.group(1)
        if arxiv_id in ids:
            errors.append(f"arXiv ID 重复: {arxiv_id} ({ids[arxiv_id]}, {path})")
        ids[arxiv_id] = path
        for url in re.findall(r"https?://[^)\s]+", text):
            if not (url.startswith("https://arxiv.org/") or url.startswith("https://github.com/") or url.startswith("https://huggingface.co/") or url.startswith("https://nvlabs.github.io/") or url.startswith("https://financegym.github.io/") or url.startswith("https://miroeval-ai.github.io/") or url.startswith("https://ai9stars.github.io/") or url.startswith("https://mmdeepresearch-bench.github.io/")):
                errors.append(f"{path}: 外部链接需人工核对 {url}")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"ok: {len(files)} paper pages, {len(ids)} unique arXiv IDs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
