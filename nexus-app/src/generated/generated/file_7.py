import re
from pathlib import Path

SPEC_DIR = Path(__file__).parent.parent / "specs"

def load_specs():
    """加载所有 .spec.md 规范文件"""
    for spec_file in SPEC_DIR.glob("*.spec.md"):
        content = spec_file.read_text(encoding="utf-8")
        yield {
            "id": re.search(r"^id: (.+)$", content, re.M).group(1),
            "title": re.search(r"^title: (.+)$", content, re.M).group(1),
            "level": re.search(r"^level: (.+)$", content, re.M).group(1),
            "content": content,
            "file": spec_file.name,
        }

def check_agent_code(code_text):
    """检查 agent 代码是否违反规范"""
    issues = []
    for spec in load_specs():
        if spec["id"] == "naming":
            if "agent_" not in code_text:
                issues.append(f"❌ 命名规范：代码中必须包含 `agent_` 前缀")
        if spec["id"] == "security":
            dangerous = ["rm -rf", "eval(", "exec("]
            for d in dangerous:
                if d in code_text:
                    issues.append(f"❌ 安全规范：禁止使用 `{d}`")
    return issues

if __name__ == "__main__":
    import sys
    code = sys.stdin.read()
    for issue in check_agent_code(code):
        print(issue)
    print("✅ 检查完成")