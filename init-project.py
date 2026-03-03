#!/usr/bin/env python3
"""
项目模板生成器
一键创建标准化的项目结构

用法:
    ./init-project.py <模板类型> <项目名>
    
示例:
    ./init-project.py python my-app
    ./init-project.py web my-site
    ./init-project.py skill my-skill
"""

import sys
import os
import shutil
from pathlib import Path
from datetime import datetime

# 模板定义
TEMPLATES = {
    "python": {
        "description": "Python 项目",
        "dirs": ["src/{name}", "tests", "docs", "scripts"],
        "files": {
            "README.md": """# {name}

{description}

## 安装

```bash
pip install -e .
```

## 使用

```python
import {name}
```

## 开发

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest
```
""",
            ".gitignore": """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# 虚拟环境
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# 测试
.pytest_cache/
.coverage
htmlcov/

# 环境变量
.env
.env.local
""",
            "pyproject.toml": """[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{name}"
version = "0.1.0"
description = "{description}"
readme = "README.md"
requires-python = ">=3.8"
license = {{text = "MIT"}}
authors = [
    {{name = "Your Name", email = "your.email@example.com"}}
]
keywords = ["python", "template"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "black>=22.0",
    "ruff>=0.1.0",
    "mypy>=1.0",
]

[project.urls]
Homepage = "https://github.com/crazyyoung01/{name}"
Repository = "https://github.com/crazyyoung01/{name}"

[tool.setuptools.packages.find]
where = ["src"]

[tool.black]
line-length = 88
target-version = ['py38']

[tool.ruff]
line-length = 88
select = ["E", "F", "I", "N", "W", "UP", "B", "C4", "SIM"]

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
""",
            "src/{name}/__init__.py": '''"""
{name} - {description}
"""

__version__ = "0.1.0"
__author__ = "Your Name"


def hello() -> str:
    """示例函数"""
    return "Hello from {name}!"
''',
            "src/{name}/py.typed": "",
            "tests/__init__.py": "",
            "tests/test_basic.py": '''"""
基础测试
"""

import pytest
from {name} import hello


def test_hello():
    """测试 hello 函数"""
    result = hello()
    assert result == "Hello from {name}!"
    assert isinstance(result, str)
''',
            "docs/README.md": "# 文档\n\n项目文档目录",
            "scripts/setup.sh": """#!/bin/bash
# 项目初始化脚本

set -e

echo "🚀 初始化 {name}..."

# 创建虚拟环境
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 升级 pip
echo "⬆️  升级 pip..."
pip install --upgrade pip

# 安装开发依赖
echo "📥 安装依赖..."
pip install -e ".[dev]"

# 初始化 git
echo "📁 初始化 git..."
git init
git add .
git commit -m "Initial commit: 项目初始化"

echo "✅ 初始化完成！"
echo ""
echo "开始使用:"
echo "  source venv/bin/activate"
echo "  pytest"
"""
        }
    },
    
    "web": {
        "description": "Web 前端项目",
        "dirs": ["src", "public", "docs", "scripts"],
        "files": {
            "README.md": """# {name}

{description}

## 技术栈

- HTML5
- CSS3
- JavaScript (ES6+)

## 项目结构

```
{name}/
├── src/          # 源代码
├── public/       # 静态资源
├── docs/         # 文档
└── scripts/      # 脚本工具
```

## 开发

```bash
# 启动本地服务器
npx serve public

# 或使用 Python
python -m http.server 8080 -d public
```
""",
            ".gitignore": """# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Build
dist/
build/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
""",
            "public/index.html": '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 {name}</h1>
            <p>{description}</p>
        </header>
        
        <main>
            <section class="intro">
                <h2>欢迎使用</h2>
                <p>这是一个全新的 Web 项目！</p>
                <button id="demo-btn" class="btn">点击演示</button>
            </section>
        </main>
        
        <footer>
            <p>&copy; {year} {name}. All rights reserved.</p>
        </footer>
    </div>
    
    <script src="js/main.js"></script>
</body>
</html>
''',
            "public/css/style.css": '''/* 基础样式 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --primary: #3b82f6;
    --primary-dark: #2563eb;
    --text: #1f2937;
    --bg: #f9fafb;
    --card-bg: #ffffff;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: var(--text);
    background: var(--bg);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

header {
    text-align: center;
    padding: 3rem 0;
}

header h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

header p {
    font-size: 1.25rem;
    color: #6b7280;
}

.intro {
    background: var(--card-bg);
    border-radius: 1rem;
    padding: 2rem;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.intro h2 {
    margin-bottom: 1rem;
}

.btn {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    margin-top: 1rem;
    background: var(--primary);
    color: white;
    border: none;
    border-radius: 0.5rem;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.2s;
}

.btn:hover {
    background: var(--primary-dark);
}

footer {
    text-align: center;
    padding: 2rem 0;
    color: #6b7280;
}
''',
            "public/js/main.js": '''/**
 * {name} - 主脚本
 */

// 等待 DOM 加载
document.addEventListener('DOMContentLoaded', () => {
    console.log('🚀 {name} 已加载');
    
    // 演示按钮
    const demoBtn = document.getElementById('demo-btn');
    if (demoBtn) {
        demoBtn.addEventListener('click', () => {
            alert('你好！{name} 正在运行 🎉');
        });
    }
});

/**
 * 示例函数
 * @param {string} name - 名称
 * @returns {string} 问候语
 */
function greet(name) {
    return `Hello, ${name}!`;
}

// 导出（如果使用模块）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { greet };
}
''',
            "src/README.md": "# 源代码\n\nJavaScript/CSS 源文件目录",
            "docs/README.md": "# 文档\n\n项目文档目录",
            "scripts/setup.sh": """#!/bin/bash
# 项目初始化脚本

echo "🚀 初始化 {name}..."

# 初始化 git
git init
git add .
git commit -m "Initial commit: 项目初始化"

echo "✅ 初始化完成！"
echo ""
echo "开始使用:"
echo "  cd {name}"
echo "  python -m http.server 8080 -d public"
echo "  # 然后打开 http://localhost:8080"
"""
        }
    },
    
    "skill": {
        "description": "Claude Code Skill",
        "dirs": ["scripts"],
        "files": {
            "README.md": """# {name}

{description}

## 安装

将本目录复制到 `~/.claude/skills/{name}/`

```bash
mkdir -p ~/.claude/skills/{name}
cp -r * ~/.claude/skills/{name}/
```

## 使用

在 Claude Code 中：

```
Skill: {name}
```

## 开发

参考 Claude Code Skill 文档进行开发。
""",
            "{name}.md": '''# {name}

## 描述

{description}

## 触发条件

- 用户明确请求使用本 skill
- 特定关键词触发

## 执行步骤

1. **步骤一**: 描述第一步做什么
2. **步骤二**: 描述第二步做什么
3. **步骤三**: 描述第三步做什么

## 示例

### 示例 1

输入：
```
用户输入示例
```

输出：
```
预期输出
```

## 注意事项

- 注意事项 1
- 注意事项 2

## 相关

- 相关 Skill 1
- 相关 Skill 2
''',
            "scripts/install.sh": """#!/bin/bash
# 安装脚本

SKILL_NAME="{name}"
SKILL_DIR="$HOME/.claude/skills/$SKILL_NAME"

echo "📦 安装 $SKILL_NAME..."

# 创建目录
mkdir -p "$SKILL_DIR"

# 复制文件
cp "$SKILL_NAME.md" "$SKILL_DIR/"
cp README.md "$SKILL_DIR/"

echo "✅ 安装完成！"
echo ""
echo "使用方法："
echo "  在 Claude Code 中运行: Skill: $SKILL_NAME"
"""
        }
    }
}


def list_templates():
    """列出所有可用模板"""
    print("📋 可用模板:\n")
    for name, info in TEMPLATES.items():
        print(f"  {name:12} - {info['description']}")
    print()


def create_project(template_name: str, project_name: str):
    """创建项目"""
    
    # 检查模板是否存在
    if template_name not in TEMPLATES:
        print(f"❌ 未知模板: {template_name}")
        print(f"可用模板: {', '.join(TEMPLATES.keys())}")
        sys.exit(1)
    
    # 检查项目名是否合法
    if not project_name:
        print("❌ 项目名不能为空")
        sys.exit(1)
    
    if not project_name.replace('-', '').replace('_', '').isalnum():
        print("❌ 项目名只能包含字母、数字、连字符(-)和下划线(_)")
        sys.exit(1)
    
    # 检查目录是否已存在
    if os.path.exists(project_name):
        print(f"❌ 目录已存在: {project_name}")
        sys.exit(1)
    
    template = TEMPLATES[template_name]
    
    print(f"🚀 创建 {template['description']}: {project_name}")
    
    # 创建目录
    for dir_path in template["dirs"]:
        full_path = dir_path.format(name=project_name)
        os.makedirs(os.path.join(project_name, full_path), exist_ok=True)
        print(f"  📁 {full_path}/")
    
    # 创建文件
    year = datetime.now().year
    for file_path, content in template["files"].items():
        full_path = file_path.format(name=project_name)
        full_content = content.format(
            name=project_name,
            description=template['description'],
            year=year
        )
        
        # 确保父目录存在
        parent = os.path.dirname(os.path.join(project_name, full_path))
        if parent:
            os.makedirs(parent, exist_ok=True)
        
        # 写入文件
        with open(os.path.join(project_name, full_path), 'w') as f:
            f.write(full_content)
        print(f"  📝 {full_path}")
        
        # 如果是脚本，添加执行权限
        if full_path.endswith('.sh'):
            os.chmod(os.path.join(project_name, full_path), 0o755)
    
    print(f"\n✅ 项目 {project_name} 创建成功！")
    print(f"\n下一步:")
    print(f"  cd {project_name}")
    print(f"  ./scripts/setup.sh  # 运行初始化脚本")


def main():
    """主函数"""
    # 检查参数
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'help']:
        print(__doc__)
        print()
        list_templates()
        sys.exit(0)
    
    if len(sys.argv) < 3:
        print("❌ 缺少参数")
        print(f"用法: {sys.argv[0]} <模板类型> <项目名>")
        print()
        list_templates()
        sys.exit(1)
    
    template_name = sys.argv[1]
    project_name = sys.argv[2]
    
    create_project(template_name, project_name)


if __name__ == "__main__":
    main()
