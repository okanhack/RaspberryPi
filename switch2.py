#coding:utf-8
"""
スイッチイベントによってLEDを光らせるプログラム
"""

import RPi.GPIO as GPIO
import time

def btn_callback(gpio_no):
    """
    スイッチの状態に変更があった時に実行する処理
    """
    GPIO.output(LED_PIN, GPIO.input(SWITCH_PIN))

# 使用するピン番号の定義
SWITCH_PIN = 14
LED_PIN = 18

# ピン番号の指定モードをBCMに設定
GPIO.setmode(GPIO.BCM)

# スイッチのピンを入力ピンとして定義
# プルダウン抵抗を有効にする
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LEDピンを出力ピンとして定義
# 初期値はLOW
GPIO.setup(LED_PIN, GPIO.OUT, initial = GPIO.LOW)

# イベント検出を有効にする
# 検出するイベントは、立ち上がり、立ち下がりの両方を検知（BOTH）
GPIO.add_event_detect(SWITCH_PIN, GPIO.BOTH, bouncetime=30)

# イベントを検出した時にコールバックする関数を設定
GPIO.add_event_callback(SWITCH_PIN, btn_callback)

# キーボードの割込み例外が発生するまで実行
try :
    while True:
        # イベントを待機
        time.sleep(1)
    
except KeyboardInterrupt:
    pass

# イベント検知を解除する
GPIO.remove_event_detect()

# GPIOの設定をクリア
GPIO.cleanup()
