#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高雄王爺信仰 VR：一次生成全部場景的中英文旁白 mp3（免費，使用 edge-tts）

旁白文字已和網頁上顯示的文字完全一致（2026-09-30 文字校訂版）。

使用方法（在 Mac 終端機）：
    1. 把這個檔案放進 wangye-upload 資料夾（和 index.html 同一層）
    2. cd ~/Downloads/wangye-upload
    3. pip install edge-tts        （已安裝過可略過）
    4. python3 make_narration.py

mp3 會直接寫在同一個資料夾，覆蓋舊的 narration-pXX-zh.mp3／narration-pXX-en.mp3。
每個檔案生成後都會檢查大小，若是空檔會自動重試。
"""
import asyncio
import os

import edge_tts

# ===== 可以自己調整的設定 =====
VOICE_ZH = "zh-TW-HsiaoChenNeural"   # 台灣女聲；男聲可改 "zh-TW-YunJheNeural"
VOICE_EN = "en-US-JennyNeural"       # 英文女聲；男聲可改 "en-US-GuyNeural"
RATE_ZH = "-5%"                      # 語速：負數較慢，正數較快
RATE_EN = "-5%"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

NARRATION = {
    "p01": {  # 首頁・認識主題
        "zh": "歡迎進入高雄王爺信仰文化之旅，從沿海宮廟出發，認識王船、王醮、送王、遶境與陣頭文化。",
        "en": "Welcome to the Kaohsiung Wangye Faith Journey. Starting from a coastal temple, we will explore Wangye Boats, the Wangye Festival, the farewell ritual, the procession, and parade troupe culture.",
    },
    "p02": {  # 操作說明
        "zh": "在開始之前，請先找一個舒適、安全的位置。如果使用手機或平板，請滑動螢幕環顧四周，點擊發光圓點查看解說，並透過畫面上的按鈕切換場景。如果戴著 VR 頭盔，只要轉頭就能環顧四周；用控制器指向發光圓點並按下扳機即可查看解說，低頭就能看到切換場景的選單。使用 VR 時請留意身邊的空間，若感到頭暈或不適，請隨時暫停休息。準備好後，就讓我們一起展開這趟高雄王爺信仰文化之旅吧！",
        "en": "Before we begin, please find a comfortable and safe spot. On a phone or tablet, swipe to look around, tap the glowing dots to view information, and use the on-screen buttons to move between scenes. With a VR headset, simply turn your head to look around, point the controller at a glowing dot and pull the trigger to view information, and look down to find the menu for changing scenes. In VR, please stay aware of the space around you, and take a break whenever you feel dizzy or uncomfortable. When you are ready, let's begin the Kaohsiung Wangye Faith Journey together!",
    },
    "p03": {  # 文化觀察者
        "zh": "在這趟 VR 體驗中，你將成為一位「文化觀察者」。你可以探索廟宇空間、點選文化物件、聆聽雙語導覽，並完成文化理解任務。這是一趟文化學習之旅，我們以尊重的態度認識王爺信仰、王船工藝與祭典文化。你會在場景中看到神像、香爐、供品與信眾，但你的任務是觀察與理解，而不是模擬宗教儀式。體驗結束時，你會完成一張雙語文化導覽卡，練習以英文介紹高雄在地文化。",
        "en": "In this VR experience, you will become a cultural observer. You can explore the temple, select cultural objects, listen to the bilingual narration, and complete learning tasks. This is a cultural learning journey in which we respectfully learn about Wangye belief, Wangye Boat craftsmanship, and festival culture. You will see deity statues, incense burners, offerings, and worshippers in the scenes, but your task is to observe and understand, not to simulate religious rituals. At the end of the experience, you will complete a bilingual culture guide card and practice introducing local Kaohsiung culture in English.",
    },
    "p04": {  # 進入高雄沿海王爺信仰
        "zh": "一座城市的記憶不僅留在道路與建築，也留在信仰、工藝與祭典中。在高雄沿海地區，王爺信仰與地方生活緊密相連。廟宇是信仰中心，也是社區聚會與祭典準備的場域。王船是王爺信仰中的重要象徵，承載著祈求平安、寄託願景與凝聚社區的文化意涵。本體驗以高雄在地王爺信仰為主軸，其他地區資料僅供視覺參考。",
        "en": "A city's memory lives not only in roads and buildings, but also in beliefs, crafts, and festivals. In coastal Kaohsiung, Wangye belief is deeply connected to local life. Temples are centers for worship, community gatherings, and festival preparation. The Wangye Boat is an important symbol of Wangye belief, carrying the cultural meanings of praying for peace, holding hopes for the future, and bringing the community together. In this experience, we focus on Kaohsiung's local Wangye belief culture. Materials from other regions are used for visual reference only.",
    },
    "p05": {  # 廟埕
        "zh": "廟埕是王爺信仰文化中重要的公共與儀式空間。它是祭典準備的場域，是社區居民聚集交流的中心，也是陣頭展演與隊伍集合的地方。在這裡，我們看到燈籠、香爐、旗幟、供桌、志工與王船等元素，一起構成祭典起點的景象，象徵社群共同參與文化行動的開始。",
        "en": "The temple square is an important public and ritual space in Wangye belief culture. It is where festival preparations take place, where residents gather and connect, and where parade troupes perform and the procession assembles. Here, lanterns, incense burners, flags, offering tables, volunteers, and the Wangye Boat together form the opening scene of the festival, marking the moment when the community begins to take part in this cultural event together.",
    },
    "p06": {  # 正殿
        "zh": "正殿是廟宇的核心，安奉主祀神明，也是信眾祈求平安的所在。空間以中軸對稱展開，樑柱、神龕與供桌依序將視線引向神像。在這裡，香爐、供品與信眾的動作共同構成日常的信仰現場。我們以觀察者的身分，理解王爺信仰與祈求出海平安的文化意涵。",
        "en": "The main hall is the heart of the temple, where the principal deity is enshrined and where worshippers come to pray for peace. The space unfolds symmetrically along a central axis, and the beams, pillars, shrine, and offering table guide the eye toward the deity statue. Here, the incense burner, the offerings, and the movements of worshippers together form an everyday scene of living belief. As observers, we seek to understand the cultural meaning of Wangye belief and of praying for safety at sea.",
    },
    "p07": {  # 木作王船
        "zh": "接下來，我們來到王船製作與展示區。在王爺信仰文化中，王船是迎王、送王習俗與祭典中的重要文化載體。它不只是一艘船，也結合了信仰、工藝、地方記憶與社區參與。請仔細觀察王船。你可以看到船身、龍骨、甲板、船艙、桅杆、旗幟、龍目、彩繪與裝飾。這些細節都需要匠師的技藝與長時間累積的知識。有些王船會在祭典後送出，有些則被保存或展示，用來傳承工藝與地方記憶。",
        "en": "Next, we arrive at the Wangye Boat craft and display area. In Wangye belief culture, the Wangye Boat is an important cultural carrier. It is not just a boat. It connects belief, craft, local memory, and community participation. Look closely at the boat. You can see the boat body, keel, deck, cabins, masts, flags, dragon eyes, paintings, and decorations. These details require skill, knowledge, and time. Some Wangye Boats are sent off after festivals. Some are preserved or displayed to pass down craft and local memory.",
    },
    "p08": {  # 王船準備
        "zh": "王船的準備從來不是一個人的事。從廟方調度、工藝師造船、志工引導動線，到居民出錢出力、家庭備妥供品，整場祭典是靠許多人分工完成的。在這個場景裡，我們觀察不同角色如何各司其職。祭典的意義不只在儀式本身，也在於它把整個社區重新聚在一起的過程。",
        "en": "Preparing the Wangye Boat is never the work of one person. From the temple staff who coordinate, the craftspeople who build the boat, and the volunteers who guide the crowd, to the residents who give money and time and the families who prepare offerings, the whole festival is completed by many people working together. In this scene, we observe how each role does its part. The meaning of the festival lies not only in the ritual itself, but also in the way it brings the whole community together again.",
    },
    "p09": {  # 送王迎新
        "zh": "接下來，我們跟著王船走向海邊，進行送王迎新的儀式。王船在轎班的護送下，伴隨鼓陣、官將首與舞龍舞獅，緩緩前行，人潮沿路夾道相送。海風迎面吹來，象徵潔淨與新生，人們相信王船將隨著風浪遠去，帶走一整年的災厄，也迎回平安與福澤。請仔細觀察隊伍中的每一個角色，感受這場送王儀式的莊嚴與熱鬧。",
        "en": "Next, we follow the Wangye Boat to the sea for the ritual of sending off Wangye and welcoming renewal. Escorted by the palanquin bearers, and accompanied by the drum troupe, Guanjiangshou-style performers, and the dragon and lion dance, the boat moves slowly forward as crowds line the route. The sea breeze blows in, standing for purification and renewal, as people believe the boat will carry the year's misfortune away with the tide and bring back peace and blessings. Look closely at each role in the procession and feel both the solemn and the lively spirit of this farewell ritual.",
    },
    "p10": {  # 陣頭與遶境
        "zh": "接下來，我們走進遶境隊伍之中。鼓陣的節奏開路定調，神將與官將首在隊伍中護法壓陣，舞龍舞獅翻騰熱鬧，轎班扛著神轎穩步前行。每一個角色的臉譜、服飾與身體動作，都不是隨意設計，而是各自承載著角色身分與文化意涵。沿路夾道的居民與遊客，也用他們的參與，讓遶境成為地方社群共同凝聚的時刻。請仔細觀察隊伍中的聲音、身體與人群，感受陣頭文化背後的地方認同。",
        "en": "Next, we step into the procession itself. The drum troupe's rhythm leads the way and sets the pace, giant deity figures and Guanjiangshou-style guardians watch over the rear, dragon and lion dancers tumble through the crowd, and the palanquin bearers carry the sedan chair steadily forward. Every performer's painted face, costume, and body movement is designed with care, and each one carries its own role and cultural meaning. Residents and visitors lining the route take part too, turning the parade into a moment when the local community comes together. Look closely at the sound, the bodies, and the crowd, and feel the sense of local identity behind troupe culture.",
    },
    "p11": {  # 尾聲
        "zh": "夕陽為整場祭典鍍上一層金色的光。王船靜靜停在海邊，廟埕的燈火依舊，神將與官將首、鼓陣與龍獅，都還留在這片廣場之中。這趟旅程從廟埕出發，跟著王船的製作、王醮的準備、送王的儀式、陣頭與遶境的熱鬧，一路走到這裡。請再看看周圍的一切：復古單車、老照片、木作工藝。這些看似平凡的細節，其實都是這座城市與這座廟埕之間，一代又一代累積下來的地方記憶。",
        "en": "The setting sun gilds the whole festival in gold. The Wangye Boat now rests quietly by the shore, the temple square still lit, and the deity figures, Guanjiangshou, drum troupe, and dragon and lion dancers still remain across the plaza. This journey began at the temple square, following the boat's construction, the preparations for the Wangye Festival, the farewell ritual, and the lively troupes and procession, all the way to here. Take one more look around: the vintage bicycle, the old photographs, and the woodworking crafts. These small, ordinary details are, in fact, the local memory this city and this temple square have built together, generation after generation.",
    },
    "p12": {  # 學習成果
        "zh": "恭喜你完成高雄王爺信仰的探索之旅！在這趟旅程中，你認識了高雄沿海的廟埕空間、王爺信仰、木作王船工藝、祭典準備、送王迎新，以及陣頭文化。這些陣頭元素以概念化的方式呈現，幫助我們透過聲音、身體、服裝、隊形與社區參與，理解地方祭典文化。現在，回顧今天學到的中英文詞彙，選擇一個文化主題與學習等級，生成你的雙語文化導覽卡，並留下學習回饋。",
        "en": "Congratulations on completing the Kaohsiung Wangye Faith Journey! On this journey, you learned about coastal temple squares in Kaohsiung, Wangye belief, the craftsmanship of the wooden Wangye Boat, festival preparation, the farewell and renewal ritual, and parade troupe culture. These troupe elements were presented in a simplified way to help us understand local festival culture through sound, body movement, costume, formation, and community participation. Now, review the Chinese and English words you learned today, choose a cultural topic and a learning level, create your own bilingual culture guide card, and share your feedback.",
    },
}


async def make_one(text, voice, rate, path):
    await edge_tts.Communicate(text, voice, rate=rate).save(path)


async def main():
    failed = []
    for page, langs in NARRATION.items():
        for lang, text in langs.items():
            voice, rate = (VOICE_ZH, RATE_ZH) if lang == "zh" else (VOICE_EN, RATE_EN)
            path = os.path.join(OUT_DIR, f"narration-{page}-{lang}.mp3")
            for attempt in range(4):
                try:
                    await make_one(text, voice, rate, path)
                    if os.path.getsize(path) > 10_000:
                        print(f"OK  {os.path.basename(path)}  {os.path.getsize(path)//1024} KB")
                        break
                    raise RuntimeError("檔案是空的")
                except Exception as e:
                    print(f"重試 {os.path.basename(path)}（{e}）第 {attempt + 1} 次")
                    await asyncio.sleep(3)
            else:
                failed.append(os.path.basename(path))
    if failed:
        print("\n以下檔案生成失敗，請再執行一次：", ", ".join(failed))
    else:
        print("\n全部 24 個旁白檔案都已完成！")


if __name__ == "__main__":
    asyncio.run(main())
