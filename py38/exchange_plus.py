#!/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称:exchange_plus.py
Author: yangyang
功能：
Date: 2022-5-12
cron: 0 59 9,13,19,23 * * *
new Env("plus权益-无验证券模板");
'''

from exchange_lib import *

if __name__ == "__main__":

    headers = {
        "Host": "rsp.jd.com",
        "accept": "application/json, text/plain, */*",
        "user-agent": "jdapp;android;10.5.2;;;appBuild/96428;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1654535539316%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22EG%3D%3D%22%2C%22ad%22%3A%22CzUmCzvsYzSnCtYzDNq0ZG%3D%3D%22%2C%22od%22%3A%22YtLwCzc0DQG3ZNOzEQS2Zq%3D%3D%22%2C%22ov%22%3A%22Ctq%3D%22%2C%22ud%22%3A%22ENY1DNGnCNC1DNC0EJY4BJHtDNvvC2Y1DNUzCm%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045946 Mobile Safari/537.36",
        "origin": "https://plus.m.jd.com",
        "x-requested-with": "com.jingdong.app.mall",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://plus.m.jd.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    # Coco
    url = f'https://rsp.jd.com/resource/lifePrivilege/receive/v1?lt=m&an=plus.mobile&uniqueId=60946520270113&_={int(round(time.time()*1000))}'
    # 万达
    url = f'https://rsp.jd.com/resource/lifePrivilege/receive/v1?lt=m&an=plus.mobile&uniqueId=60946520269991&_={int(round(time.time()*1000))}'
    # 肯德基
    url = f'https://rsp.jd.com/resource/lifePrivilege/receive/v1?lt=m&an=plus.mobile&uniqueId=60947948441996&_={int(round(time.time()*1000))}'

    # 烧仙草 coco
    url = f'https://rsp.jd.com/resource/lifePrivilege/receive/v1?lt=m&an=plus.mobile&uniqueId=71704511585025&_={int(round(time.time()*1000))}'

    url = f'https://rsp.jd.com/resource/lifePrivilege/receive/v1?lt=m&an=plus.mobile&uniqueId=71704534652075&_={int(round(time.time() * 1000))}'


    url = f'https://rsp.jd.com/resource/lifePrivilege/receive/v1?lt=m&an=plus.mobile&uniqueId=71705057879950&_={int(round(time.time() * 1000))}'

    # 体检
    url = f'https://rsp.jd.com/resource/lifePrivilege/receive/v1?lt=m&an=plus.mobile&uniqueId=71705009647680&_={int(round(time.time() * 1000))}'

    # 烧仙草
    url = f'https://rsp.jd.com/resource/lifePrivilege/receive/v1?lt=m&an=plus.mobile&uniqueId=71704988678033&_={int(round(time.time() * 1000))}'

    # 万达
    url = f'https://rsp.jd.com/resource/lifePrivilege/receive/v1?lt=m&an=plus.mobile&uniqueId=71704447587533&_={int(round(time.time() * 1000))}'

    args = parseArgs()

    ExchangeManagement(
        url=url,
        headers=headers,
        headers_user_agent_random_flag=True,
        user_agent="",
        body_dict={},
        batch_size=args.batch_size if args.batch_size > 0 else 12,
        other_batch_size=0,
        second_ahead=0,
        sleep_time=0,
        thread_number=args.thread_number if args.thread_number > 0 else 20,
        log_flag=False,
        sign_flag=False,
        day_or_week='day',
        post_flag=False,
        proxy_flag=args.proxy_flag if args.proxy_flag else True,
        print_type="cmd",
        coupon_type="plus_quanyi",
        cookie_type=args.cookie_type if args.cookie_type != "None" else "mine_coupons").\
    executeInDesktop(
        clock_list=[0, 10],
        debug_flag=args.debug_flag if args.debug_flag else True)