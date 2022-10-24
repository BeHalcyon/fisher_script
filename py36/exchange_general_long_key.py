#!/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称:exchange_general_long_key.py
Author: Fisher
功能：适配定点抢长key类券，需在fisher_configure.json文件内创建对应对象并填写"discount"、“activityId”和"clock_list"参数；不需填写长key，会根据activityId和discount自动搜索
Date: 2022-5-12
cron: 0 59 9,13,19,23 * * *
new Env("适配长key券");
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

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        'origin': 'https://pro.m.jd.com',
        "Referer": "https://prodev.m.jd.com/mall/active/3WWbQbmmcqceFHsJbat8Zv1GJaTG/index.html"
    }

    body_dict = {
        'activityId': '4TFZNrP43yHwUV3QvJrEvcK53yjM',
        'scene': '1',
        # "args": "key=71A0B43A5801A76425DDBF4945A31FD0A482428781387C293E94FE5D03130B8290CB83F3DEC7A6BC983EBAD60BB41090_bingo,roleId=9BD67B901DB469651E99E6F7D3AD5D4C1AA34CF13B4798B7631A80C978D94B238519E7CFEACA3172B01DA4825405A9DF008A5736EE708F9F4CC1789FE2954CAB0263CD293EAF6D72A4391D16068BA147C40F89C0442154D15341E07CCEBBA886CAE551448E5C321B3502EFCEC85ABADD5B568D52236F53017161146D0CB29D26CD99AC01EED9FA85BCA728275411591E2941E0E19C557799258FB3E209E132D6_bingo,strengthenKey=19F512DCD8EE34ABE9C4FB4A92C2F42AE84B9E1109B76B738665CAD2CB9C6FC3_bingo"
        "args": "key=3DDD4FEE153EDE4F35C6F88EE2E6B0E49BD9CE09F02D3C0AA15513971D7D389ED4783B3577241CE3AD9CF93B4916BF47_bingo,roleId=CBA252302CA43DD8492A5C2BB15E348D8DB7DBDFCD70E07A4B7351090783521AFE55E69D64CAE1EDBE989BACFC81D94CBB81AC1F577723DFF9EB26B402E07D8106A25909D15C0C2B436CFE2542B89FE27AF72604A4B815DC880C2C087938C579F2F2CD22FDC08402E7692AF5E3FFF0F25810D208F7217DF27A4AA244D3F75147B18AE19450BBDBC8E2CD3E613B25500A356AB6ADDF084C5A08C512A0F7B62435_bingo,strengthenKey=19F512DCD8EE34ABE9C4FB4A92C2F42ADA4942001794CD9B77862303197584D9_bingo"
    }
    url = 'https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&client=wh5&clientVersion=1.0.0'

    args = parseArgs()

    ExchangeManagement(
        url=url,
        headers=headers,
        headers_user_agent_random_flag=True,
        user_agent="",
        body_dict=body_dict,
        activitiId_random_flag=False,
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
        proxy_flag=args.proxy_flag if args.proxy_flag else False,
        proxy_ip=args.proxy_ip if len(args.proxy_ip) else "",
        coupon_type=args.coupon_type if args.coupon_type != 'None' else '15-5',
        cookie_type=args.cookie_type if args.cookie_type != 'None' else 'heyang') \
    .executeInDesktop(
        debug_flag=args.debug_flag if args.debug_flag else False
    )