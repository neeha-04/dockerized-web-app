@echo off
cd /d "%~dp0"
cls
echo.
echo  ================================================================
echo   DEVOPS MONITOR - Starting App...
echo  ================================================================
echo.
echo  [1/2] Starting containers...
echo.
docker-compose up -d --build 2>nul
echo.
echo  [2/2] Done!
echo.
echo  ================================================================
echo   --^> http://localhost
echo  ================================================================
echo.
echo  --- LIVE LOGS (Ctrl+C to stop watching) ---
echo.
docker-compose logs -f