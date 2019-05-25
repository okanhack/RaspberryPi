"""
スイッチと連動してLEDを光らせるプログラム
"""
# ライブラリの読み込み
import RPi.GPIO as GPIO
import time

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

# キーボードの割込み例外が発生するまで無限ループ
try :
    while True:
        # スイッチのOn/Offに連動してLEDを点ける
        GPIO.output(LED_PIN, GPIO.input(SWITCH_PIN))
        time.sleep(0.01)
    
except KeyboardInterrupt:
    pass

# GPIOの設定をクリア
GPIO.cleanup()
