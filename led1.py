#coding:utf-8

"""
LEDを５回点滅させるプログラム
"""
# ライブラリの読み込み
import RPi.GPIO as GPIO
import time

# 使用するBCM番号の定義
LED_PIN = 2

# ピン番号の指定モードをBCMに設定
GPIO.setmode(GPIO.BCM)

# LEDピンを出力ピンとして定義
GPIO.setup(LED_PIN, GPIO.OUT)

# HIGH(On)/LOW(Off)を5回繰り返す
for x range(5):
	GPIO.output(LED_PIN, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)

# GPIOの設定をクリア
GPIO.cleanup()
