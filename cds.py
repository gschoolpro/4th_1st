# -*- coding: utf-8 -*-
# モジュールのインポート
# gpiozeroパッケージのMCP3008モジュール
from gpiozero import MCP3008
# 時間制御のためのtimeモジュール
from time import sleep

# MCP3008モジュールの値の取得（チャンネル0, GPIO8）
light = MCP3008(channel=0, device=0)

# 光センサの値の取得
while True:
    # 光センサの値を3.3倍して代入
    cds = light.value * 3.3
    # 桁数を3つにして丸め込み
    print (round(cds,3))
    # 1秒待機
    sleep(1)
