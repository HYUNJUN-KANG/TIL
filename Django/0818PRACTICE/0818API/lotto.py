

import requests

url = "http://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=924"

response = requests.get(url).json()

print(response)