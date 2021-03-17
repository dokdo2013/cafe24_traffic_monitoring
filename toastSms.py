import requests
import json

class toastSms:
    def send_message(phone, message):
        apiKey = "" # apiKey 입력
        url = "https://api-sms.cloud.toast.com/sms/v2.3/appKeys/{}/sender/sms".format(apiKey)
        data = {
            "body": message,
            "sendNo": '01012345678', # 발신번호 입력
            "recipientList": [{
                "recipientNo": phone
            }]
        }
        headers = {'content-type': 'application/json' }
        res = requests.post(url, headers=headers, data=json.dumps(data))
        print(phone, message) # 발신내용 출력
