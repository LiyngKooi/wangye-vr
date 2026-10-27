#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
產生 lib/models-data-p06.js
================================================================
把 p06 的兩個模型（神龕、神像）編成 base64，合併進
window.__VR_MODEL_BASE64__，讓它們能在 file:// 下正常載入。

使用方式：把這支檔案放在離線包的根目錄（跟 index.html 同層），
然後在終端機執行：

    cd ~/Downloads/你的資料夾
    python3 make-models-data-p06.py

【務必先壓縮模型再跑這支腳本】
原始檔各 54 MB、約 190 萬個三角形，未壓縮直接編碼會產生
約 150 MB 的 JS 檔，瀏覽器會解析到當掉。壓縮指令：

    cd media
    npx @gltf-transform/cli simplify P06_Deity_Shrine.glb tmp.glb --ratio 0.08 --error 0.001
    npx @gltf-transform/cli meshopt tmp.glb P06_Deity_Shrine.glb --level high
    npx @gltf-transform/cli simplify P06_golden_deity_statue_3d_model.glb tmp2.glb --ratio 0.08 --error 0.001
    npx @gltf-transform/cli meshopt tmp2.glb P06_golden_deity_statue_3d_model.glb --level high
    rm tmp.glb tmp2.glb
================================================================
"""
import base64
import os
import sys

MODELS = [
    'P06_Deity_Shrine.glb',
    'P06_golden_deity_statue_3d_model.glb',
]

SIZE_WARN_MB = 12   # 壓縮後應遠低於此值；超過就是還沒壓
OUT = os.path.join('lib', 'models-data-p06.js')


def main():
    if not os.path.isdir('media') or not os.path.isdir('lib'):
        sys.exit('找不到 media/ 或 lib/ 資料夾，請在離線包根目錄執行這支腳本。')

    entries = []
    oversized = []

    for name in MODELS:
        path = os.path.join('media', name)
        if not os.path.exists(path):
            sys.exit('找不到檔案：%s' % path)

        mb = os.path.getsize(path) / 1048576
        status = 'OK' if mb <= SIZE_WARN_MB else '過大'
        print('  %-42s %7.2f MB  %s' % (name, mb, status))
        if mb > SIZE_WARN_MB:
            oversized.append((name, mb))

        with open(path, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode('ascii')
        entries.append("  '%s':\n    '%s'" % (name, encoded))

    if oversized:
        print()
        print('警告：以下檔案看起來還沒壓縮 ——')
        for name, mb in oversized:
            print('  %s（%.2f MB，base64 後約 %.2f MB）' % (name, mb, mb * 1.37))
        print()
        if input('仍要繼續產生嗎？(y/N) ').strip().lower() != 'y':
            sys.exit('已中止。請先執行檔頭註解裡的壓縮指令。')

    js = (
        '/* p06 場景模型（神龕、神像）— 由 make-models-data-p06.py 產生，請勿手動編輯。\n'
        '   合併進既有的 window.__VR_MODEL_BASE64__，不覆蓋其他場景的模型。 */\n'
        'window.__VR_MODEL_BASE64__ = Object.assign(\n'
        '  window.__VR_MODEL_BASE64__ || {},\n'
        '  {\n' + ',\n'.join(entries) + '\n'
        '  }\n'
        ');\n'
    )

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(js)

    print()
    print('已寫入 %s（%.2f MB）' % (OUT, os.path.getsize(OUT) / 1048576))
    print('接著重新整理 p06.html，點神龕與神像即可看到 3D 模型。')


if __name__ == '__main__':
    main()
