#!/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称:exchange_15_8.py
Author: yangyang
功能：
Date: 2022-5-7
cron: 20 59 8,11,14,17,19 * * *
new Env("极速版15减8");
'''

from exchange_lib import *

if __name__ == "__main__":

    headers = {
        "Host": "api.m.jd.com",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        # "Connection": "keep-alive",
        "origin": "https://prodev.m.jd.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "content-Type": "application/x-www-form-urlencoded",
        "x-requested-with": "com.jd.jdlite",
        'origin': 'https://pro.m.jd.com',
        "referer": "https://prodev.m.jd.com/"
        # "Referer": "https://prodev.m.jd.com/jdlite/active/3H885vA4sQj6ctYzzPVix4iiYN2P/index.html?sid=bf6ae253e73f472d5ec294810f46665w&un_area=7_502_35752_35860"
    }
    body_dict = {
        'activityId': '3H885vA4sQj6ctYzzPVix4iiYN2P',
        # 'activityId': 'JzXcsas7voDtg8FdSjHNdnW1Wjw',
        # 'activityId': 'Da41jakjlsd56Aks432SFd1SfDh',
        'scene': '1',
        'args': 'key=4C884367B622BB96ABD488103A5036F58B08100D4FEC967D97AA8854BC13AF4A50BE6F7B01529B9D56C52BEAB5EB5235_bingo,roleId=A921D0996A757D3D319487D17C0F25FE701307BE103D49F3D1562C7CF5D02F01F1043E437093D585B4730F630A66804F8AE429E9F2C40EE1F0580E482F388FEEF1F5A8A69753844555247364707E6E41040F01DEE945DF4C10432FB4875EA6DF48164CC736ACE898EE9E8947855DBC30CD8BF4D53E7EA1B873BAAE1052D9BB9748A8F83F1E3CD76509AFB2939FC10B6AE2ADCB50653791DF313F8F7BF0AF7AE7_bingo,strengthenKey=3FE987FADD098B5D46BA38B21875A5EBD8C02F19572CB3C5CC0385902CD416A23D357AD5C32B073932D1986E4D335028_bingo',
        "platform": "1", "orgType": "2", "openId": "-1", "pageClickKey": "-1",
        "eid": "UH6XXTQ3BYGGLOTIZR3PQ3TAIBYFGPUAJTZ3A3C3R2DSHFFYQZXZLVKTKTZG2UWE65FLRTIRQWLIPE2QRH7IEZ5RWA",
        "fp": "69a1a886f8708147784c6a233a83dce2", "shshshfp": "a9215c4ee5c7cbe022e3e447a472b939",
        "shshshfpa": "8e117fa4-7d85-34d6-7e31-016ec2cc0b14-1649602438", "shshshfpb": "w0b5mA97CnoifQBOqSV2sPw",
        "childActivityUrl": "https%3A%2F%2Fprodev.m.jd.com%2Fjdlite%2Factive%2F3H885vA4sQj6ctYzzPVix4iiYN2P%2Findex.html%3Fsid%3D5d16d6a94e8ddaabe3d4cc3bdc588d9w%26un_area%3D7_502_35752_35860",
        "userArea": "-1", "client": "-1", "clientVersion": "-1", "uuid": "-1", "osVersion": "-1", "brand": "-1",
        "model": "-1", "networkType": "-1",
        "jda": "122270672.1651820416462743475770.1651820416.1655304725.1655352182.88", "sdkToken": "",
        "token": "X3CD5PMYHSTOXEFV6TEBZXL3QHMB5VLA4ZKZ7QSB6RIASCRXR4OQICGAKA4IUDR2RZS7O75GXTBHQ",
        "jstub": "CBYD5IY3QLB3DWQVZUXVTYP3EDFR2BNWLUWVQQ5RF7VK3LAEUKL7RYM3T37HASQTMUB5PHOPQEYO2CGV2LGGN5XXYGXHBJQV5ZSHJDI",
        "pageClick": "Babel_Coupon", "couponSource": "manual", "couponSourceDetail": "-100", "channel": "通天塔会场",
        "batchId": "874861901", "headArea": "605715ec560d6508f7403b91b677d79c", "mitemAddrId": "",
        "geo": {"lng": "", "lat": ""}, "addressId": "6402218628", "posLng": "112.638777", "posLat": "32.797323",
        "focus": "", "innerAnchor": "", "cv": "2.0", "floor_id":"79986892"
    }

    body_dict = {
        'activityId': '3H885vA4sQj6ctYzzPVix4iiYN2P',
        # 'activityId': 'JzXcsas7voDtg8FdSjHNdnW1Wjw',
        # 'activityId': 'Da41jakjlsd56Aks432SFd1SfDh',
        'scene': '1',
        'args': 'key=4C884367B622BB96ABD488103A5036F58B08100D4FEC967D97AA8854BC13AF4A50BE6F7B01529B9D56C52BEAB5EB5235_bingo,roleId=A921D0996A757D3D319487D17C0F25FE701307BE103D49F3D1562C7CF5D02F01F1043E437093D585B4730F630A66804F8AE429E9F2C40EE1F0580E482F388FEEF1F5A8A69753844555247364707E6E41040F01DEE945DF4C10432FB4875EA6DF48164CC736ACE898EE9E8947855DBC30CD8BF4D53E7EA1B873BAAE1052D9BB9748A8F83F1E3CD76509AFB2939FC10B6AE2ADCB50653791DF313F8F7BF0AF7AE7_bingo,strengthenKey=3FE987FADD098B5D46BA38B21875A5EBD8C02F19572CB3C5CC0385902CD416A23D357AD5C32B073932D1986E4D335028_bingo'
    }

    url = 'https://api.m.jd.com/client.action?functionId=lite_newBabelAwardCollection&client=wh5&clientVersion=1.0.0&screen=1080x1701&sid=5d16d6a94e8ddaabe3d4cc3bdc588d9w&uuid=16496913392821345390631.304.1655352241347&area=7_502_35752_35860'

    ExchangeManagement(
        url=url,
        headers=headers,
        headers_user_agent_random_flag=False,
        user_agent="jdltapp;android;3.8.18;;;appBuild/2318;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1655352551144%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22EG%3D%3D%22%2C%22ad%22%3A%22CzUmCzvsYzSnCtYzDNq0ZG%3D%3D%22%2C%22od%22%3A%22YtLwCzc0DQG3ZNOzEQS2Zq%3D%3D%22%2C%22ov%22%3A%22Ctq%3D%22%2C%22ud%22%3A%22CzUmCzvsYzSnCtYzDNq0ZG%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jd.jdlite%22%7D;Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045836 Mobile Safari/537.36",
        body_dict=body_dict, batch_size=6,
        other_batch_size=5,
        second_ahead=0.18,
        sleep_time=0.025,
        thread_number=12,
        append_flag=False,
        log_flag=True,
        sign_flag=False,
        day_or_week='day',
        post_flag=True,
        proxy_flag=False,
        print_type="cmd",
        coupon_type="15-8",
        cookie_type="cookie")\
    .executeInDesktop(
        clock_list=[9, 12, 15, 18, 20],
        debug_flag=False
    )
