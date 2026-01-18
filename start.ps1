$ErrorActionPreference = "Stop"

Write-Host "------------------------------------------" -ForegroundColor Cyan
Write-Host "   Garage Pro - Starting Management App   " -ForegroundColor Cyan
Write-Host "------------------------------------------" -ForegroundColor Cyan
Write-Host "Info: Access the site at http://localhost:5000" -ForegroundColor Gray
Write-Host "Note: Press Ctrl+C to stop the application and clean up." -ForegroundColor Yellow
Write-Host ""

try {
    # Check if docker is available
    if (-not (Get-Command "docker-compose" -ErrorAction SilentlyContinue)) {
        throw "docker-compose not found. Please install Docker Desktop."
    }

    # Start the containers
    docker-compose up --build
}
catch {
    Write-Host "`n[!] Error: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "[!] Tip: Make sure Docker Desktop is running!" -ForegroundColor Yellow
}
finally {
    Write-Host "`n------------------------------------------" -ForegroundColor Cyan
    Write-Host "   Cleaning up containers... please wait   " -ForegroundColor Cyan
    docker-compose down
    Write-Host "   Application stopped successfully.       " -ForegroundColor Green
    Write-Host "------------------------------------------" -ForegroundColor Cyan
}


