# ゆあがりPJのサーバ

e.g. http://210.140.162.51/flaskr/api/v0/bantoL

## IPアドレス
 210.140.162.51/flaskr

## API
### /api/v0/alps

アルプスセンサーデータを受け取る

+ No 
+ MagX
+ MagY
+ MagZ
+ AccX
+ AccY
+ AccZ
+ Uv
+ Lx
+ Humi
+ Temp
+ Press

### /api/v0/theta

シータのデータを受け取る

+ base64

### /api/v0/banto[LR]
Edisonにサーボデータを送る


+ angle
  - 0 - 179


