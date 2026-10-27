#!/bin/bash
# 高雄王爺信仰 VR：在本機開啟網站（3D 模型、旁白、VR 都能使用）
# 使用方法：雙擊這個檔案。要結束時，關閉這個終端機視窗即可。

cd "$(dirname "$0")" || exit 1

PORT=8000
while lsof -iTCP:$PORT -sTCP:LISTEN >/dev/null 2>&1; do PORT=$((PORT+1)); done

URL="http://localhost:$PORT/index.html"
echo "======================================"
echo " 高雄王爺信仰 VR 本機網站已啟動"
echo " 網址：$URL"
echo " 要結束時，直接關閉這個視窗。"
echo "======================================"

( sleep 1.5
  if [ -d "/Applications/Google Chrome.app" ]; then open -a "Google Chrome" "$URL"; else open "$URL"; fi
) &

python3 -m http.server "$PORT" --bind 127.0.0.1 2>/dev/null
