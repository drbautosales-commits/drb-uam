@echo off
chcp 65001 >nul
echo ============================================
echo   UAM Research Project - Local Server
echo ============================================
echo.

:: Python 서버로 실행 (포트 8080)
echo Starting local server at http://localhost:8080
echo.
echo Press Ctrl+C to stop the server
echo.

:: 브라우저에서 자동으로 열기
start http://localhost:8080/uam-intro.html

:: Python HTTP 서버 시작
python -m http.server 8080

pause

