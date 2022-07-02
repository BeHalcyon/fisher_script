#!/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称:exchange_10_2.py
Author: yangyang
功能：
Date: 2022-5-7
cron: 10 59 6,15 * * *
new Env("极速版10减2");
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
    body_dict = {
        'activityId': '3H885vA4sQj6ctYzzPVix4iiYN2P',
        'scene': '1',
        'args': 'key=DF6500A60EBB047C1539292254D320D7E80F9297D19486370D6A0DD220E76A1CD91818B1BCEE491D10789D7765041113_bingo,roleId=A921D0996A757D3D319487D17C0F25FE01264B7B8DA4DBEF981EF390D1DC02E92308FBC1CF805C8B6550E0A1EED8671F5360D7210975255E5A17758A1D4815AB567D73B11DD737D321A8D6DAD3B6E47D9856DB2370DFDE42DF7A403051EAE598426A548597D1A8C8B06DB2408647136E62AB87E9BDA89DC607FFF91F49DDF2D7D5654AE896C595FB0166D7DDD65C69887601704ADA6163C9D9D6BEB403BAD565_bingo,strengthenKey=3FE987FADD098B5D46BA38B21875A5EBD8C02F19572CB3C5CC0385902CD416A223A89D9BE16CD64801ED6D818465540C_bingo'
    }
    url = 'https://api.m.jd.com/client.action?functionId=lite_newBabelAwardCollection&client=wh5&clientVersion=1.0.0'

    args = parseArgs()

    ExchangeManagement(
        url=url,
        headers=headers,
        headers_user_agent_random_flag=True,
        user_agent="",
        body_dict=body_dict,
        activitiId_random_flag=False,
        discount="3",
        batch_size=args.batch_size if args.batch_size > 0 else 30,
        other_batch_size=0,
        second_ahead=0,
        sleep_time=0,
        thread_number=args.thread_number if args.thread_number > 0 else 20,
        append_flag=False,
        log_flag=True,
        sign_flag=False,
        day_or_week='day',
        post_flag=True,
        proxy_flag=False,
        print_type="cmd",
        coupon_type="10-3",
        cookie_type=args.cookie_type if args.cookie_type != "None" else "cookie") \
    .executeInDesktop(
        clock_list=[7, 16, 20],
        debug_flag=args.debug_flag if args.debug_flag else False
    )
