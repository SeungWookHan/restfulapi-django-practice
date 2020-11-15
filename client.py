import requests

with open('./sample3.jpeg', 'rb') as img:
    files = [
        ('send', img)
    ]
    # 101.101.208.153
    try:
        requests.post("http://127.0.0.1:8000/images/", files=files)
        print("이미지 전송 성공")
    except:
        print("이미지 전송 실패")
