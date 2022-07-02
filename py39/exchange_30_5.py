#!/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称:exchange_15_5.py
Author: yangyang
功能：
Date: 2022-5-7
cron: 10 59 9,23 * * *
new Env("极速版15减5");
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
        'args': 'key=6E3ED4217CA5BA50CC868072587749279A819E91EC8217F49BC1DB9DC674DA27CF93291755C086262CF2BD2DADDD8138_bingo,roleId=A921D0996A757D3D319487D17C0F25FE0F6830D8485A69E35623B13BFBA59D1E7C2386D90F3D9D3A6D752ADCDEAB0529AA56BDE4467494DC5590AEB5C7C950D03EA337E197D9AF250FA7148376C8A9C2C3FC8B2D9632A67F79B5A98776BF5B6C94F3F3F8F3770E265EF7D6CAD2E5F1B98EE03623B492E1C2B96EBC7500E20DAB9C2BBC9CBBA7AA027CBB17434C77651F9DE32AEAE13EA4C6B7660D4FD53E63FF_bingo,strengthenKey=3FE987FADD098B5D46BA38B21875A5EBD8C02F19572CB3C5CC0385902CD416A2FE3B5DC71CEBCF672000554484FB93E5_bingo'
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
        discount="5",
        batch_size=args.batch_size if args.batch_size > 0 else 12,
        other_batch_size=0,
        second_ahead=0,
        sleep_time=0,
        thread_number=args.thread_number if args.thread_number > 0 else 20,
        append_flag=False,
        log_flag=True,
        sign_flag=False,
        day_or_week='day',
        post_flag=True,
        proxy_flag=True,
        coupon_type="30-5",
        cookie_type=args.cookie_type if args.cookie_type != 'None' else 'cookie') \
    .executeInDesktop(
        clock_list=[0, 10, 20],
        debug_flag=args.debug_flag if args.debug_flag else False
    )