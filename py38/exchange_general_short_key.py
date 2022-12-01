#!/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称:exchange_general_short_key.py
Author: Fisher
功能：适配定点抢短key类券，需在fisher_configure.json文件内创建对应对象并填写"args"和"clock_list"参数
Date: 2022-5-12
cron: 0 59 9,13,19,23 * * *
new Env("适配短key券");
'''

from exchange_lib import *

import sys

if __name__ == "__main__":

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        'origin': 'https://pro.m.jd.com',
        "Referer": "https://prodev.m.jd.com/jdlite/active/3H885vA4sQj6ctYzzPVix4iiYN2P/index.html?sid=bf6ae253e73f472d5ec294810f46665w&un_area=7_502_35752_35860",
    }

    body_dict = {
        "activityId":"e9z6GPMVDF4fZ2X6NNwJfot4yxhS",
        "from":"H5node",
        "scene":"1",
        "args": "key=c1m3c0s0o6ae485e936c029467cb3391,roleId=83519576"
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
        discount="",
        batch_size=args.batch_size if args.batch_size > 0 else 10,
        other_batch_size=0,
        second_ahead=0,
        sleep_time=0.01,
        thread_number=args.thread_number if args.thread_number > 0 else 20,
        append_flag=False,
        log_flag=False,
        sign_flag=False,
        day_or_week='day',
        post_flag=True,
        proxy_flag=args.proxy_flag if args.proxy_flag else False,
        proxy_ip=args.proxy_ip if len(args.proxy_ip) else "",
        coupon_type=args.coupon_type if args.coupon_type != 'None' else 'general_coupons',
        cookie_type=args.cookie_type if args.cookie_type != 'None' else 'mine_coupons')\
    .executeInDesktop(
        debug_flag=args.debug_flag if args.debug_flag else False,
    )