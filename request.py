import requests
import time

class RouterRequester:
    def __init__(self):
        self.url_1 = "http://192.168.8.1:80/goform/goform_set_cmd_process"
        self.url_2 = "http://192.168.8.1:80/goform/goform_set_cmd_process"
        self.cookies_1 = {"pageForward": "home", "arp_scroll_position": "0"}
        self.cookies_2 = {"pageForward": "home", "arp_scroll_position": "136.8000030517578"}
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://192.168.8.1",
            "Referer": "http://192.168.8.1/index.html",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Connection": "close"
        }
    
    def send_request_1(self):
        data = {"isTest": "false", "goformId": "LOGIN", "username": "YWRtaW4=", "password": "MjEyMzJmMjk3YTU3YTVhNzQzODk0YTBlNGE4MDFmYzM="}
        response = requests.post(self.url_1, headers=self.headers, cookies=self.cookies_1, data=data)
        return response

    def send_request_2(self):
        data = {"isTest": "false", "band_state": "yes", "band_list": "21,0,0,0,32,1,0,0", "wcdma_list": "0,0,0", "tds_list": "0,0", "zeact": "2", "goformId": "TZ_SET_LOCK_BAND"}
        response = requests.post(self.url_2, headers=self.headers, cookies=self.cookies_2, data=data)
        return response
