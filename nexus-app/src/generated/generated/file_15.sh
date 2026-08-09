cd ai-prompt-spec

# 初始化 git
git init
git add .
git commit -m "Initial commit: AI Prompt Engineering Guide & Agent Spec Tool"

# 推送到 GitHub
# 先在 GitHub 新建一个空仓库（不要勾选 README）
git branch -M main
git remote add origin git@github.com:<你的用户名>/ai-prompt-spec.git
git push -u origin main