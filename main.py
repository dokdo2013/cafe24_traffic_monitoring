import requests
import time
from bs4 import BeautifulSoup
import toastSms # 알림 서비스 추가 (필요에 맞게 변경)
toast = toastSms.toast # nhn cloud의 sms 전송 기능 이용

def get_data():
    url = "http://wws16-004.localnet.kr/throttle-me/{카페24 ID}/throttle-me.asp" # 카페24 ID 입력해넣기 (윈도우 호스팅 전용)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    per_text = soup.select('body > center > table:nth-child(2) > tr:nth-child(2) > td:nth-child(3)')[0].text
    per = float(per_text)
    return per

while True:
    now_percent = get_data()
    if now_percent >= 80.0: # 트래픽 80% 이상일 때 실행
        msg = "카페24 트래픽 알림입니다. 현재 트래픽 사용량 : {}%".format(now_percent)
        toast.send_message("01012345678", msg)
    time.sleep(600) # 10분 간격으로 실행
