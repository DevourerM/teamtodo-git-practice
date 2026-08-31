# TeamTodo Git Practice

这是《Git & GitHub 从零到多人协作：TeamTodo 项目驱动实战教材》的配套仓库。

仓库地址：`https://github.com/DevourerM/teamtodo-git-practice`

## 这不是一个“看答案”的仓库

`main` 故意只保留起始版本。你要通过 GitHub 的 **Issues** 按顺序完成任务，并且每个任务都走标准协作流程：

```text
读 Issue → 同步 main → 建分支 → 开发 → status/diff → 测试
→ add → commit → push → Pull Request → Review → CI → Merge → 清理分支
```

## 第一次开始

```bash
git clone https://github.com/DevourerM/teamtodo-git-practice.git
cd teamtodo-git-practice
python -m unittest discover -s tests -v
python teamtodo.py
```

如果测试显示 `OK`，环境就准备好了。

## 练习主线

请打开仓库顶部 **Issues**：

- Issue #1：为任务增加优先级
- Issue #2：在任务列表中显示优先级
- Issue #3：根据 Code Review 修改现有 PR
- Issue #4：观察 GitHub Actions / CI
- Issue #5：制造并解决一次合并冲突
- Issue #6：独立实现任务搜索

教材会在第一次完整流程中非常细地带你做；后面的任务逐渐减少提示。

## 项目结构

```text
.
├─ teamtodo.py
├─ tests/
│  └─ test_teamtodo.py
├─ docs/
│  ├─ COURSE_MAP.md
│  ├─ GITHUB_WEB_GUIDE.md
│  └─ GIT_CHEATSHEET.md
├─ scripts/
│  ├─ check_environment.ps1
│  └─ prepare_conflict_lab.ps1
├─ .github/
│  ├─ workflows/ci.yml
│  ├─ PULL_REQUEST_TEMPLATE.md
│  └─ ISSUE_TEMPLATE/
├─ CONTRIBUTING.md
├─ .gitignore
└─ README.md
```

## 最重要的规则

1. 不直接在 `main` 上做功能开发。
2. 一个 Issue 对应一个主要分支、一个主要 PR。
3. Commit 前先看 `git status` 和 `git diff`。
4. PR 合并前看 `Files changed` 和 `Checks`。
5. Reviewer 让你修改时，继续 Push 原分支；不要重新开 PR。
6. 出错时先 `git status`，不要第一反应 `reset --hard`。

更详细的操作说明请看教材 PDF 与 `docs/` 目录。
