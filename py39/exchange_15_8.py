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
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        'origin': 'https://pro.m.jd.com',
        "Referer": "https://prodev.m.jd.com/jdlite/active/3H885vA4sQj6ctYzzPVix4iiYN2P/index.html?sid=bf6ae253e73f472d5ec294810f46665w&un_area=7_502_35752_35860"
    }
    body_dict = {
        'activityId': '3H885vA4sQj6ctYzzPVix4iiYN2P',
        'scene': '1',
        'args': 'key=4C884367B622BB96ABD488103A5036F58B08100D4FEC967D97AA8854BC13AF4A50BE6F7B01529B9D56C52BEAB5EB5235_bingo,roleId=A921D0996A757D3D319487D17C0F25FE701307BE103D49F3D1562C7CF5D02F01F1043E437093D585B4730F630A66804F8AE429E9F2C40EE1F0580E482F388FEEF1F5A8A69753844555247364707E6E41040F01DEE945DF4C10432FB4875EA6DF48164CC736ACE898EE9E8947855DBC30CD8BF4D53E7EA1B873BAAE1052D9BB9748A8F83F1E3CD76509AFB2939FC10B6AE2ADCB50653791DF313F8F7BF0AF7AE7_bingo,strengthenKey=3FE987FADD098B5D46BA38B21875A5EBD8C02F19572CB3C5CC0385902CD416A23D357AD5C32B073932D1986E4D335028_bingo'
    }
    url = 'https://api.m.jd.com/client.action?functionId=lite_newBabelAwardCollection&client=wh5&clientVersion=1.0.0'

    ExchangeManagement(
        url=url,
        headers=headers,
        headers_user_agent_random_flag=True,
        user_agent="",
        body_dict=body_dict, batch_size=6,
        other_batch_size=5,
        second_ahead=0.17,
        sleep_time=0.025,
        thread_number=12,
        append_flag=False,
        log_flag=True,
        sign_flag=False,
        day_or_week='day',
        post_flag=True,
        proxy_flag=True,
        print_type="cmd",
        coupon_type="15-8",
        cookie_type="cookie")\
    .executeInDesktop(
        clock_list=[9, 12, 15, 18, 20],
        debug_flag=True
    )
