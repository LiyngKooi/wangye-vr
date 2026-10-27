高雄王爺信仰文化 VR 導覽 — 離線包使用說明
Kaohsiung Wangye Belief Culture VR Tour — Offline Package Guide

================================================================
1. 快速啟動 Quick Start
================================================================

建議使用啟動腳本開啟（這樣 3D 模型、音效與背景圖才能正確載入）：

• Mac 用戶：雙擊「備用啟動-Mac.command」
• Windows 用戶：雙擊「備用啟動-Windows.bat」

腳本會自動在本機開啟一個小型網頁伺服器，並用瀏覽器打開首頁：
http://127.0.0.1:8000/index.html

================================================================
2. 手動啟動 Manual Start
================================================================

若啟動腳本無法使用，請在終端機（Terminal / 命令提示字元）進入此資料夾，執行：

  python3 -m http.server 8000

或（Windows 若無 python3）：

  python -m http.server 8000

然後用瀏覽器開啟：

  http://127.0.0.1:8000/index.html

================================================================
3. 重要提醒 Important Notes
================================================================

• 請勿直接用「檔案 → 開啟」的方式打開 index.html（file:// 協定會導致 3D 模型與音效無法載入）。
• 必須透過 http://127.0.0.1:8000 這類本地伺服器網址瀏覽。
• 建議使用 Chrome、Edge、Safari 或 Firefox 的最新版本。
• Meta Quest 3 請使用 Meta Quest Browser，並點擊畫面下方的「ENTER VR」進入沉浸式 360° 模式。

================================================================
4. 場景一覽 Scene List
================================================================

index.html  首頁 / Home
p02.html    操作教學 / Tutorial
p03.html    文化觀察者 / Cultural Observer
p04.html    文化脈絡 / Cultural Context
p05.html    廟埕 360° VR / Temple Square 360° VR
p07.html    木作王船 / Wooden Wangye Boat
p12.html    學習成果 / Learning Outcome

================================================================
5. 資料夾說明 Folder Structure
================================================================

index.html, p02.html ... p12.html   各場景頁面
lib/                                本地程式庫（tailwindcss、model-viewer、three.js 等）
media/                              圖片、音效、3D 模型素材
備用啟動-Mac.command                 Mac 啟動腳本
備用啟動-Windows.bat                Windows 啟動腳本
請先看我-3D開啟方式.txt              3D 模型開啟方式說明

================================================================
6. 技術支援
================================================================

此離線包由 Lovable 專案自動產生，專案網址：
https://wangyeboatproject.lovable.app
