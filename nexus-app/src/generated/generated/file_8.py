from pathlib import Path
from .check import load_specs

def generate_readme():
    """从 specs/ 生成文档索引"""
    lines = ["# Agent 规范索引\n", "| 规范 ID | 标题 | 级别 | 文件 |", "|---|---|---|---|"]
    for spec in load_specs():
        lines.append(f"| {spec['id']} | {spec['title']} | {spec['level']} | {spec['file']} |")
    (Path("docs") / "SPEC_INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    print("✅ 已生成 docs/SPEC_INDEX.md")