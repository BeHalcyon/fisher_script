#!/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称:exchange_15_8_test.py
Author: yangyang
功能：
Date: 2022-5-7
cron: 10 59 9,13,19,23 * * *
new Env("京东59减20万券齐发");
'''

from exchange_lib import *

if __name__ == "__main__":

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        'origin': 'https://pro.m.jd.com',
        "Referer": "https://prodev.m.jd.com/jdlite/active/3H885vA4sQj6ctYzzPVix4iiYN2P/index.html?sid=bf6ae253e73f472d5ec294810f46665w&un_area=7_502_35752_35860"
    }
    body_dict= {
        "batchId": "859658610"
    }
    url = f'https://api.m.jd.com/client.action?functionId=volley_ExchangeAssetFloorForColor&appid=coupon-activity&client=wh5&area=17_1381_50718_53772&geo=%5Bobject%20Object%5D&t={int(round(time.time()*1000))}&eu=5663338346331693&fv=9323932366232313'

    ExchangeManagement(
        url=url,
        headers=headers,
        headers_user_agent_random_flag=True,
        user_agent="",
        body_dict=body_dict,
        activitiId_random_flag=True,
        batch_size=12,
        other_batch_size=4,
        second_ahead=0.25,
        sleep_time=0.02,
        thread_number=12,
        append_flag=False,
        log_flag=False,
        sign_flag=False,
        day_or_week='day',
        post_flag=True,
        proxy_flag=False,
        print_type="cmd",
        coupon_type="59-20_3_2",
        cookie_type="cookie")\
    .executeInDesktop(
        clock_list=[0, 10, 14, 20, 22],
        debug_flag=False
    )