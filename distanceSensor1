#coding:utf-8

"""
距離センサーを使って距離を表示するプログラム
"""
# ライブラリの読み込み
import RPi.GPIO as GPIO
import time

def getTime(PIN, start=1, end=0):
  """
  超音波を発生させてから受信するまでの時間を計測する関数
  """
  if start == 0: end = 1
    t_start = 0
    t_end = 0
    
    # ECHO_PINがHIGHである時間を計測
    while GPIO.input(PIN) == end:
      t_start = time.time()  
    while GPIO.input(PIN) == start:
      t_end = time.time()
    
    # 終了時間と開始時間の差が超音波が往復する時間
    return t_end - t_start

def getDistance(TRIG_PIN, ECHO_PIN):
  """
  距離を計測する関数
  """
  # TRIGピンを0.3[s]だけLOW
  GPIO.output(TRIG_PIN, GPIO.LOW)
  time.sleep(0.3)
    
  # TRIGピンを0.00001[s]だけ出力(超音波発射）
  GPIO.output(TRIG_PIN, True)
  time.sleep(0.00001)
  GPIO.output(TRIG_PIN, False)
    
  # 受信するまでの時間を計測
  t = getTime(ECHO_PIN)
    
  # 距離[cm] = 音速[cm/s] * 時間[s] / 2(片道)
  distance = V * t / 2

# 使用するBCM番号の定義
TRIG_PIN = 14
ECHO_PIN = 15

# 音速 約340m/s
V = 34000

# ピン番号の指定モードをBCMに設定
GPIO.setmode(GPIO.BCM)

# TRIGピンを出力ピン、ECHOピンを入力ピンとして定義
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# 距離を10回測る
for x range(10):
  distance = getDistance()
  print(distance, "cm")
	time.sleep(1)

# GPIOの設定をクリア
GPIO.cleanup()
