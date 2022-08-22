# -*- encoding:utf-8 -*-
from datetime import datetime

import requests
import json

datetime_now = datetime.now()
datetime_now = datetime_now.strftime('%Y-%m-%d %H:%M:%S')
class SendMessage():
    def __init__(self):
        self.appID = 'wx5f01b45ee1f686b6'
        self.appsecret = '8315ebf2743dfe2f2be138b08afeacce'
        self.access_token = self.get_access_token()
        self.opend_ids = self.get_openid()

    def get_access_token(self):
        """
        获取微信公众号的access_token值
        """
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'. \
            format(self.appID, self.appsecret)
        print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
        }
        response = requests.get(url, headers=headers).json()
        access_token = response.get('access_token')
        print(access_token)
        return access_token

    def get_openid(self):
        """
        获取所有粉丝的openid
        """
        next_openid = ''
        url_openid = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s&next_openid=%s' % (
            self.access_token, next_openid)
        ans = requests.get(url_openid)
        print(ans.content)
        open_ids = json.loads(ans.content)['data']['openid']
        url_template_send = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(
            self.access_token)
        body = {

            "touser": open_ids,

            "template_id": "iq6FkV7-bXEcaNDNDsYhqQSdIdzfdP8c-2dvCRetUGY",
            "url": "http://weixin.qq.com/download",


            "data": {

                "nowData": {

                    "value": datetime_now,

                    "color": "#57E6E2"

                },




            }
        }
        response = requests.post(url_template_send, data=body)
        return open_ids

    def sendmsg(self, msg):
        """
        给所有粉丝发送文本消息
        """
        url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(self.access_token)
        if self.opend_ids != '':
            for open_id in self.opend_ids:
                body = {
                    "touser": open_id,
                    "msgtype": "text",
                    "text":
                        {
                            "content": msg
                        }
                }
                data = bytes(json.dumps(body, ensure_ascii=False).encode('utf-8'))
                print(data)
                response = requests.post(url, data=data)
                # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
                result = response.json()
                print(result)
        else:
            print("当前没有用户关注该公众号！")

    def upload_media(self, media_type, media_path):
        """
        上传临时文件到微信服务器，并获取该文件到meida_id
        """
        url = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token={}&type={}'.format(self.access_token,
                                                                                              media_type)
        print(url)
        meida = {
            'media': open(media_path, 'rb')
        }
        rsponse = requests.post(url, files=meida)
        parse_json = json.loads(rsponse.content.decode())
        print(parse_json)
        return parse_json.get('media_id')

    def send_media_to_user(self, media_type, media_path):
        """
        给所有粉丝发送媒体文件，媒体文件以meida_id表示
        """
        media_id = self.upload_media(media_type, media_path)
        url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}'.format(self.access_token)
        if self.opend_ids != '':
            for open_id in self.opend_ids:
                if media_type == "image":
                    body = {
                        "touser": open_id,
                        "msgtype": "image",
                        "image":
                            {
                                "media_id": media_id
                            }
                    }
                if media_type == "voice":
                    body = {
                        "touser": open_id,
                        "msgtype": "voice",
                        "voice":
                            {
                                "media_id": media_id
                            }
                    }
                data = bytes(json.dumps(body, ensure_ascii=False).encode('utf-8'))
                print(data)
                response = requests.post(url, data=data)
                # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
                result = response.json()
                print(result)
        else:
            print("当前没有用户关注该公众号！")


if __name__ == "__main__":
    data = 'Hello,3Nod!'
    sends = SendMessage()
    sends.get_openid()
    # sends.sendmsg(data)
    # sends.send_media_to_user("image", './test.png')
