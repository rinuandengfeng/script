import json
from fastapi import FastAPI
import requests

app = FastAPI()


@app.get('/')
def levelqueryyq():
    url = "https://xcx.www.gov.cn/ebus/gwymp/api/r/levelqueryyq/StatiQuery"
    headers = {
        "x-tif-sid": "c3de3aebb24720d8ce13c4a665e7daf254",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,\
         like Gecko) Chrome/53.0.2785.143 Safari/537.36\
          MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    }

    content = requests.post(url, headers=headers, json={})
    raw = content.text

    # 将响应内容转化为json对象
    raw = json.loads(raw)
    # 高风险地区
    highlist = raw['data']['highlist']
    middlelist = raw['data']['middlelist']
    lowlist = raw['data']['lowlist']

    return {
        "code": 200,
        # "data":{
        #     "highlist":highlist,
        #     "middlelist":middlelist,
        #     "lowlist":lowlist,
        # }
        "data": raw,
    }
