# ゆあがりPJのサーバ

e.g. http://210.140.162.51/flaskr/api/v0/bantoL

## IPアドレス
 210.140.162.51/flaskr
 yuagari.mi5.jp

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
+ 保存画像
  - /var/www/html/theta.png
 
### /api/v0/banto[LR]
Edisonにサーボデータを送る


+ angle
  - 0 - 179

### /api/v0/getdata
GET パラメータ
- c : 返す数 e.g ?c=2


こんなJSON返す

```
{
  "AccX": [
    "10.0", 
    "10.0"
  ], 
  "AccY": [
    "10.0", 
    "10.0"
  ], 
  "AccZ": [
    "10.0", 
    "10.0"
  ], 
  "Humi": [
    "10.0", 
    "10.0"
  ], 
  "Lx": [
    "10.0", 
    "10.0"
  ], 
  "MagX": [
    "10.0", 
    "10.0"
  ], 
  "MagY": [
    "10.0", 
    "10.0"
  ], 
  "MagZ": [
    "10.0", 
    "10.0"
  ], 
  "N": [
    "5", 
    "4"
  ], 
  "Press": [
    "10.0", 
    "10.0"
  ], 
  "Temp": [
    "10.0", 
    "10.0"
  ], 
  "Uv": [
    "10.0", 
    "10.0"
  ]
}
```

