import time
import requests

HEADERS1 = {
    "Host": "api.eol.cn",
    "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64;rv: 77.0) Gecko / 20100101Firefox / 77.0",
    "Accept": "application / json, text / plain, * / *",
    "Accept - Language": "zh - CN, zh;q = 0.8, zh - TW;q = 0.7, zh - HK;q = 0.5, en - US;q = 0.3, en;q = 0.2",
    "Accept - Encoding": "gzip, deflate, br",
    "Content - Type": "application / json;charset = utf - 8",
    "Content - Length": "193",
    "Origin": "https:// gkcx.eol.cn",
    "Connection": "keep - alive",
    "Referer": "https: // gkcx.eol.cn / school / 178 / provinceline"
}
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
    'Referer': 'https://gkcx.eol.cn'
}
url_specialty = '''https://static-data.eol.cn/www/2.0/school/178/info.json'''
response = requests.get(url_specialty, headers=HEADERS,timeout =0.5)
time.sleep(0.3)
info = (response.json())['data']['pro_type_min']['43']
print(info[0])
