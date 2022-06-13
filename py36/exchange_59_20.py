#!/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: exchange_59_20_1.py
Author: Fisher
功能：
Date: 2022-5-12
cron: 0 59 9,13,17,21,23 * * *
'''

from exchange_lib import *

if __name__ == "__main__":

    ExchangeManagement(
        url="",
        headers={},
        headers_user_agent_random_flag=False,
        user_agent="okhttp/3.12.1;jdmall;android;version/11.0.2;build/97565;",
        body_dict={},
        batch_size=4,
        other_batch_size=4,
        second_ahead=0.3,
        sleep_time=0.03,
        thread_number=12,
        append_flag=False,
        log_flag=False,
        sign_flag=True,
        day_or_week='week',
        post_flag=True,
        proxy_flag=True,
        coupon_type="59-20_1",
        cookie_type="wskey") \
    .executeInDesktop(
        clock_list=[0, 10, 14, 18, 22],
        debug_flag=False
    )
