$ErrorActionPreference = "Stop"
Write-Host "TeamTodo 环境检查" -ForegroundColor Cyan
Write-Host ""

$ok = $true
foreach ($cmd in @("git", "python")) {
    if (Get-Command $cmd -ErrorAction SilentlyContinue) {
        Write-Host "[OK] $cmd" -ForegroundColor Green
    } else {
        Write-Host "[缺失] $cmd" -ForegroundColor Red
        $ok = $false
    }
}

if (Get-Command gh -ErrorAction SilentlyContinue) {
    Write-Host "[可选 OK] gh (GitHub CLI)" -ForegroundColor Green
} else {
    Write-Host "[可选] 未安装 gh；不影响正常 Git/PR 学习。" -ForegroundColor Yellow
}

if ($ok) {
    Write-Host ""
    git --version
    python --version
    Write-Host ""
    Write-Host "核心环境可用。" -ForegroundColor Green
}
