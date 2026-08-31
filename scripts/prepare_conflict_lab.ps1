$ErrorActionPreference = "Stop"

Write-Host "Issue #5 conflict lab setup" -ForegroundColor Cyan
Write-Host "This creates two remote branches from main that modify the same line." -ForegroundColor Yellow
Write-Host ""

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $root

if (git status --porcelain) {
    Write-Host "The working tree is not clean. Commit, stash, or restore changes first." -ForegroundColor Red
    exit 1
}

git switch main
git pull

$existingBranch = git branch --list "lab/conflict-a"
if ($existingBranch) {
    Write-Host "Local branch lab/conflict-a already exists. Delete or rename it first." -ForegroundColor Red
    exit 1
}

$existingBranch = git branch --list "lab/conflict-b"
if ($existingBranch) {
    Write-Host "Local branch lab/conflict-b already exists. Delete or rename it first." -ForegroundColor Red
    exit 1
}

# Branch A
git switch -c lab/conflict-a
$content = Get-Content teamtodo.py -Raw -Encoding UTF8
$content = $content.Replace("=== TeamTodo ===", "=== TeamTodo CLI ===")
Set-Content teamtodo.py -Value $content -Encoding UTF8
git add teamtodo.py
git commit -m "lab: change menu title to TeamTodo CLI"
git push -u origin lab/conflict-a

# Branch B starts from main again
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
Write-Host "Setup complete." -ForegroundColor Green
Write-Host "Next: merge a PR for lab/conflict-a, then open a PR for lab/conflict-b." -ForegroundColor White
Write-Host "The second PR should now show a merge conflict. Follow the Issue #5 instructions." -ForegroundColor White
