import requests, os, json
os.system('cls')
os.system('title KR+ Coupon redeem')
user = input("유저 회원코드를 입력해주세요 : ")
name = input("유저 네임 입력해주세요 : ")
coupon = input("쿠폰코드를 입력해주세요 : ")

base = "https://mcoupon.nexon.com/kartrush/coupon/api/v1/redeem-coupon-by-npacode"
header = {
  "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
  'Content-Type': 'application/json'
  }

data = {'npaCode': f"{user}", 'coupon': f"{coupon}", 'id': "null", 'name': f"{name}", 'world': "", 'region': "KR"}


aa = requests.post(base, headers=header, json=data)

  
response_data = aa.json()
    
if aa.status_code == 200:
  print(response_data['result'])
  if response_data['result'] == False:
      print("쿠폰 등록 실패")
      print("응답 내용:", response_data["message"])
  else:
      print("쿠폰 등록 성공!")
else:
    print("쿠폰 등록 실패. 응답 코드:", response.status_code)
    print("응답 내용:", response.text)