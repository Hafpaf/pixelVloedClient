# PixelVloed Client

This client is intended to introduce new users to pixelflut and work with the [PixelVloed C server](https://github.com/JanKlopper/pixelvloed). It should run on anything that takes Python but have only been tested on an X86_64 Linux machine.

## Setup
* **Use cable**, an ethernet connection is faster, more stable and more fun than using a WiFi connection. A bonus is also that other people won't kill you for slowing down their WiFi.

* Inside `client.py`, set IP and port to match the server:
```python
IP = "xxx.xxx.xxx.xxx"
PORT = 5005
```

## Run client
```python
python client.py
``` 
or 
```python
./client.py
```
