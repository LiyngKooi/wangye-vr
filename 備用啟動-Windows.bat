@echo off
chcp 65001 >nul
title Kaohsiung Wangye VR - Local Server
cd /d "%~dp0"

rem ===== 高雄王爺信仰 VR：在本機開啟網站（Windows）=====
rem 雙擊這個檔案即可。要結束時，關閉這個黑色視窗。

set "PY="
where py >nul 2>nul && set "PY=py -3"
if not defined PY (
  python --version >nul 2>nul && set "PY=python"
)
if not defined PY (
  echo.
  echo [!] 找不到 Python。請到 https://www.python.org/downloads/ 下載安裝，
  echo     安裝時務必勾選 "Add python.exe to PATH"，裝好後再雙擊一次這個檔案。
  echo     Python was not found. Please install it from python.org
  echo     and tick "Add python.exe to PATH".
  echo.
  pause
  exit /b 1
)

set PORT=8000
:findport
netstat -ano | findstr /r /c:":%PORT% .*LISTENING" >nul
if not errorlevel 1 (
  set /a PORT+=1
  goto findport
)

set "URL=http://127.0.0.1:%PORT%/index.html"
echo ======================================
echo  高雄王爺信仰 VR 本機網站已啟動
echo  網址 URL: %URL%
echo  要結束時，直接關閉這個視窗。
echo  Close this window to stop the server.
echo ======================================

set "CHROME="
if exist "%ProgramFiles%\Google\Chrome\Application\chrome.exe" set "CHROME=%ProgramFiles%\Google\Chrome\Application\chrome.exe"
if exist "%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe" set "CHROME=%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
if exist "%LocalAppData%\Google\Chrome\Application\chrome.exe" set "CHROME=%LocalAppData%\Google\Chrome\Application\chrome.exe"

start "" /b %PY% -m http.server %PORT% --bind 127.0.0.1
timeout /t 2 /nobreak >nul

if defined CHROME (
  start "" "%CHROME%" "%URL%"
) else (
  start "" "%URL%"
)

echo.
echo 網站執行中。按任意鍵或關閉這個視窗即可停止。
echo Server is running. Press any key or close this window to stop.
pause >nul
