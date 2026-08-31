# 协作规范（CONTRIBUTING）

## 1. 开始一个任务

```bash
git switch main
git pull
git switch -c feature/你的功能名
```

## 2. 修改后先自检

```bash
git status
git diff
python -m unittest discover -s tests -v
```

## 3. Stage 与 Commit

初学阶段建议明确添加文件：

```bash
git add teamtodo.py tests/test_teamtodo.py
git commit -m "feat: add task priority"
```

Commit 前缀建议：

- `feat:` 新功能
- `fix:` 修复问题
- `test:` 测试
- `docs:` 文档
- `refactor:` 重构
- `chore:` 工程/配置

## 4. Push 与 PR

第一次推送新分支：

```bash
git push -u origin feature/你的功能名
```

到 GitHub 创建 PR，确认：

```text
base: main
compare: feature/你的功能名
```

## 5. Review 修改

收到修改意见后，在原分支继续：

```bash
git add ...
git commit -m "fix: address review feedback"
git push
```

原 PR 会自动更新。

## 6. Merge 后收尾

```bash
git switch main
git pull
git branch -d feature/你的功能名
```
