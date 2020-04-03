# -*- coding: utf-8 -*-
# モジュールのインポート
# gpiozeroパッケージのMCP3008モジュール
from gpiozero import MCP3008
# 時間制御のためのtimeモジュール
from time import sleep



# MCP3008モジュールの値の取得（チャンネル0, GPIO8）
light = MCP3008(channel=0, device=0)
led_pin = ___       # GPIO23番PIN

# LEDの初期設定




# 光センサの値の取得
while True:
    try:
        # 光センサの値を100倍して代入
        cds = int(light.value * 100)
        print(cds)
        # 閾値を超えたとき
        if cds >= ____:
            # LEDを消灯する
            pi.digitalWrite(led_pin, pi.____)
        # 閾値を超えないとき
        else:
            # LEDを点灯する
            pi.digitalWrite(led_pin, pi.____)
        # 1秒待機
        sleep(1)
    except KeyboardInterrupt:
        break
    finally:
        pi.digitalWrite(led_pin, pi.LOW)
