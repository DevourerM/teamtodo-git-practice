# GitHub 网页最常用区域

## Code
看文件、分支、Commit、Clone 地址。

## Issues
任务 / Bug / 需求。先读清楚验收条件再写代码。

## Pull requests
合并请求。核心是比较：

```text
base: main  ← compare: 你的功能分支
```

PR 中最重要的区域：

- Conversation：总体讨论和状态
- Commits：这个 PR 含哪些提交
- Checks：CI 是否通过
- Files changed：实际代码 diff 与逐行 Review

## Actions
查看 CI。失败时不要只看“红叉”，要点进去展开失败步骤的日志。

## Settings
仓库管理员使用。常见内容：Rulesets / Branch protection、Actions 权限、Pages 等。
