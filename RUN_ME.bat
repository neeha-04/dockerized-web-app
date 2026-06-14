@echo off
cd /d "%~dp0"
cls
echo.
echo  ================================================================
echo   DEVOPS MONITOR - Dockerized Flask + Nginx + Gunicorn App
echo  ================================================================
echo.
echo  Make sure Docker Desktop is open and running!
echo.
echo  [1/3] Building and starting containers...
echo.
docker-compose up -d --build 2>nul
echo.
echo  [2/3] Containers started successfully!
echo.
echo  [3/3] Ready!
echo.
echo  ================================================================
echo   ACCESS THE APP:
echo   --^> Open browser and go to: http://localhost
echo  ================================================================
echo.
echo  QUICK REFERENCE:
echo   Start app   : .\start.bat
echo   Stop app    : docker-compose down
echo   View logs   : docker-compose logs -f
echo   Rebuild     : docker-compose up -d --build
echo  ================================================================
echo.
echo  --- LIVE LOGS (Ctrl+C to stop watching) ---
echo.
docker-compose logs -f