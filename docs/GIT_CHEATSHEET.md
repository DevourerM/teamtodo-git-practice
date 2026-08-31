# Git 最小命令速查

## 查看

```bash
git status
git diff
git log --oneline --graph --decorate --all
git branch
git remote -v
```

## 日常任务

```bash
git switch main
git pull
git switch -c feature/example

# 修改文件

git add <file>
git commit -m "feat: ..."
git push -u origin feature/example
```

## 后续继续修改同一个 PR

```bash
git add <file>
git commit -m "fix: address review feedback"
git push
```

## Merge 后

```bash
git switch main
git pull
git branch -d feature/example
```

## 撤销（先确认场景）

未 Commit 的单个文件：

```bash
git restore <file>
```

已经 Push / 已经共享的 Commit：优先考虑

```bash
git revert <commit>
```

不要在不清楚后果时使用：

```text
git reset --hard
git push --force
```
