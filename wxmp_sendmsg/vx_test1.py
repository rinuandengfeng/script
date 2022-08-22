import json
from datetime import datetime

import requests

datetime_now = datetime.now()
datetime_now = datetime_now.strftime('%Y-%m-%d %H:%M:%S')


def get_weather():
    key = "5a885daf7f289ac2377e84d33e19d07d"
    url_weater = "https://restapi.amap.com/v3/weather/weatherInfo?key={}&city={}&output={}".format(key, 410100, "JSON")

    weater_data = requests.get(url_weater)

    lives = json.loads(weater_data.text)
    lives = lives["lives"][0]

    return {
        "city": lives["city"],
        "weather": lives["weather"],
        "winddirection": lives["winddirection"],
        "temperature": lives["temperature"],
        "windpower": lives["windpower"],
        "humidity": lives["humidity"],
        # "reporttime": lives["reporttime"],
    }


def get_openid():
    """
    获取所有粉丝的openid
    """
    access_token = "60_r8NsMf7EViqrswoeiQHzfEJPoYMO_4vvsSpRzwZAGnkJV53w7godWWRPD5BQsRbMl_3FaiIjM1YwSNK20wmwdokSIWOwCk9AgW49P9S5YJCh0ZNy51gIvwNjJ-DarduY5Zf2SkaBG4EGTzONEFSfACAABO"
    # next_openid = ''
    # url_openid = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=%s' % (
    #     access_token, next_openid)
    # ans = requests.get(url_openid)
    # print(ans.content)
    # open_ids = json.loads(ans.content)['data']['openid']
    url_template_send = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(
        access_token)
    weather_info = get_weather()

    body = {

        "touser": "oJToj5wUzLx-pOP0lI7209g72kbY",

        "template_id": "swZtS9IhJ4DBv0jA2nypFB-bBRzVKvBBhhYv4ruenc0",
        "url": "http://weixin.qq.com/download",

        "data": {

            "nowDate": {

                "value": datetime_now,

                "color": "#57E6E2",

            },
            "city": {
                "value": weather_info["city"],

                "color": "#57E6E2",
            },
            "weather": {
                "value": weather_info["weather"],
                "color": "#57E6E2",
            },
            "temperature": {
                "value": weather_info["temperature"],
                "color": "#57E6E2",
            },
            "winddirection": {
                "value": weather_info["winddirection"],
                "color": "#57E6E2",
            },
            "humidity": {
                "value": weather_info["humidity"],
                "color": "#57E6E2",
            },
            "windpower": {
                "value": weather_info["windpower"],
                "color": "#57E6E2",
            },

        }
    }
    response = requests.post(url_template_send, json=body)
    print(response.text)
    return "成功！"


get_openid()

# get_weather()
