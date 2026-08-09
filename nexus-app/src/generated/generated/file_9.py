import sys
from .check import check_agent_code
from .generate import generate_readme

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "check":
        code = sys.stdin.read()
        for issue in check_agent_code(code):
            print(issue)
    elif cmd == "generate":
        generate_readme()
    else:
        print("用法: python -m src [check|generate]")

if __name__ == "__main__":
    main()