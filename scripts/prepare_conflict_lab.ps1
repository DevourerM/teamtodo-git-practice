$ErrorActionPreference = "Stop"

Write-Host "Issue #5 冲突实验准备器" -ForegroundColor Cyan
Write-Host "它会从当前最新 main 创建两个远程分支，并让它们修改同一行。" -ForegroundColor Yellow
Write-Host ""

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $root

if (git status --porcelain) {
    Write-Host "工作区不是干净状态。请先 Commit / stash / restore 后再运行。" -ForegroundColor Red
    exit 1
}

git switch main
git pull

foreach ($b in @("lab/conflict-a", "lab/conflict-b")) {
    if (git branch --list $b) {
        Write-Host "本地已存在分支 $b。为避免覆盖，请先删除或改名。" -ForegroundColor Red
        exit 1
    }
}

# A 分支
git switch -c lab/conflict-a
$content = Get-Content teamtodo.py -Raw -Encoding UTF8
$content = $content.Replace("=== TeamTodo ===", "=== TeamTodo CLI ===")
Set-Content teamtodo.py -Value $content -Encoding UTF8
git add teamtodo.py
git commit -m "lab: change menu title to TeamTodo CLI"
git push -u origin lab/conflict-a

# B 分支，重新从 main 开始
git switch main
git switch -c lab/conflict-b
$content = Get-Content teamtodo.py -Raw -Encoding UTF8
$content = $content.Replace("=== TeamTodo ===", "=== TeamTodo Practice ===")
Set-Content teamtodo.py -Value $content -Encoding UTF8
git add teamtodo.py
git commit -m "lab: change menu title to TeamTodo Practice"
git push -u origin lab/conflict-b

git switch main
Write-Host ""
Write-Host "准备完成。" -ForegroundColor Green
Write-Host "下一步：先为 lab/conflict-a 提 PR 并 Merge；再为 lab/conflict-b 提 PR。" -ForegroundColor White
Write-Host "第二个 PR 将很可能出现冲突，此时按教材 Issue #5 章节处理。" -ForegroundColor White
