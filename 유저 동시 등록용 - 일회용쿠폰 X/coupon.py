import requests
import os
import json

os.system('cls')
os.system('title KRR+ Coupon redeem')

coupon = input("쿠폰코드를 입력해주세요 : ")

base = "https://mcoupon.nexon.com/kartrush/coupon/api/v1/redeem-coupon-by-npacode"
header = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
  'Content-Type': 'application/json'
}

if not os.path.exists("users.txt"):
    print("users.txt 파일이 존재하지 않습니다.")
    exit()

with open("users.txt", "r", encoding="utf-8") as file:
    accounts = [line.strip().split(":") for line in file if line.strip()]


with open("fail.txt", "w", encoding="utf-8") as fail_file:
    fail_file.write("")

for account in accounts:
    if len(account) < 2:
        print(f"잘못된 형식의 계정 정보: {account}")
        continue

    user, name = account[0], account[1]
    data = {'npaCode': f"{user}", 'coupon': f"{coupon}", 'id': "null", 'name': f"{name}", 'world': "", 'region': "KR"}

    try:
        response = requests.post(base, headers=header, json=data)
        response_data = response.json()

        if response.status_code == 200:
            if response_data['result'] == False:
                reason = response_data.get("message", "알 수 없는 오류")
                print(f"쿠폰 등록 실패 - 계정: {user}, 사유: {reason}")
                with open("fail.txt", "a", encoding="utf-8") as fail_file:
                    fail_file.write(f"{user}:{reason}\n")
            else:
                print(f"쿠폰 등록 성공 - 계정: {user}")
        else:
            reason = f"HTTP 오류 코드 {response.status_code}"
            print(f"쿠폰 등록 실패 - 계정: {user}, 사유: {reason}")
            with open("fail.txt", "a", encoding="utf-8") as fail_file:
                fail_file.write(f"{user}:{reason}\n")
    except Exception as e:
        reason = f"예외 발생: {str(e)}"
        print(f"쿠폰 등록 실패 - 계정: {user}, 사유: {reason}")
        with open("fail.txt", "a", encoding="utf-8") as fail_file:
            fail_file.write(f"{user}:{reason}\n")