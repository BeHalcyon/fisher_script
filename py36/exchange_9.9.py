#!/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称:exchange_9.9.py
Author: yangyang
功能：
Date: 2022-5-7
cron: 10 59 9,15 * * *
new Env("券后9.9");
'''
from exchange_lib import *

if __name__ == "__main__":
    url = "https://api.m.jd.com/client.action?functionId=centerReceiveCoupon&appid=XPMSGC2019&monitorSource=&client=m&eu=9393466666362666&fv=1323833363836643"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://h5.m.jd.com",
        "x-request-with": "com.jingdong.app.mall",
        "referer": "https://h5.m.jd.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }

    body_dict = {
        "extend": "99B44833B345B4A50B4461BA428C486452A145C34CF01C4F0091027322F7B46A6DBED5621D640CDE44654C57EAEDCE2FB1DA7F79BF316E599EA2B24106BE59DE6B8A6160AC012ADDDE7362D4FAC56DBE64548CE5C5BC78B158505842F987A28847ABA2B1C26F0E78A475DB7E2EAC9CE951E1264EBEDEA9481C0A00E5E6FC5F9975F838E2BC1B086A5B0BBD0306869BCFD367D80407D0A972B439B54F2477E46D57823A172A2572C1A0ACE8A16CCA4D2B69D0591AF40E345ED3053BC511237628871A6C2AE1A0CE734ABBFAD76DDD086F3BF1611BFA19E40CDDC876733FD3F9A8",
        "rcType": "1",
        "source": "couponCenter_app",
        "random": "2919891",
        "couponSource": "1",
        "extraData": "{\"log\":\"1655478755605~1SnuhW7Rl6CMDF2d3NEdDAxMQ==.R0FGcUBBT0R2TENDQjo4Dz9HcUA+GEAtCkdbRWhBWkYNdgpHCQp8MTAtRBYkPSYqLS1BJhIMWUcCSyUTCA==.d36388e3~5,1~669FAB39CF9A561BA579C728C64E7D691CC6A720~1w5qn1e~C~SxNAWREIYm0fGkdXWhILbxZXAxQJBhQKDBsBARhBH0YbHBFcBhQOAx0NAB90DXkfCR0JBwAdQBYfEF0HHgEAFQ4EHXIDBR4IHgMIAxVDEmwYFlRAVxIJCh8bREMTDhYCBAwFBw8LDgQGBQ0EAgoKBBEUEU5SVBMOFkdGTURHGh8bQFVQFg4RVF9ER0xHTFYSHRZEV1wbCmgMHw8GCR0CGAIDFQEfDW4VFVpbFg4AHhtTQBoJGwMJBldVVVEIAwBaVQhTCQJWAgVXD1UDCAELVVVSBAIAEBUSXUgRAxV8WFpBSxJYUUFbWw8DEh0WQBEICAYGDQcODwcEAQIDBxUSWVMRAxUdUAABAwYPVVINBQoHHQEGBgIEWAcEDVJdUgZXDFEeCwoJBQlWDwIJBAJRBFMBCAIBUAkEVQVQUgAAAVEKXQBYDwYEBBYfEF9AURoJG04IdHJuBGBpe2JhWmAAYVB8GQJHAVFUGh8bWUYTDhZ0XVZXX10TcFlTHxYYEVxYRhECEQAACAgGFh8QSlNBGgliDwEJGAcKAWQcEUpcGw1rE3l9EwobHBFZXV1FX1hQFh8QCAARFBEIBh4BGgARHhsJBAAKCxUcEwQHAQELAwILBQoGBgYHAwAfDAMCDgcPAgYHBwIFCgoFBRofGwYSbBgWWl1YEgkaVV9RVldSQEcQFRJSUhEDFUUTGBZQWxsKEU8AFwYeARYYEVFfb0UaCRsHARMYFlFWGwoRSlJXU19cCQYKAwAICgkRFRVdWxYOaAMVAB8IbhUVUl1bUxEIGwEFDQYNAAgGBgcDBAlOAnp2QVZdcgBeSQZ0dHVKYmFbamNwdUt/Xg0OFmRXU31TfHZQV2xIQ1xlTU1jYld9ZktwUWp7B11zWmRBe1sDTXEAbkZrBHF5Vk5DU2lIamFVeFgAd3ZbSnFTVwFhYmNVemUMVnZwUkRleQdAdFdocHdwBlR+A19nd3N5RXJ3VGd1Y3JocmhUWlRldWBzQFxAfF4ABHVIR1F3WE5efHpqcnJ0Wlt/W0F/cWBqcXJzdUtXYQdIeHYDCnoLRFV6cG1Bf2tDQnNZVmZ7ZQ1HdEhWAXZBXAF7dAVBUWEGXn5bVEp+XltzdVpUBHFocn94e25ae0NtZGJ4CFRvd2hkd0ZDUHoCAQZ4VAZKcndWcH5yVUx4SgB4d08AcH5nfQFzV2pqdm1+Y1V3Q1B+QVN4c3JBA35jUwIdCl1SBlxXAAROSBgFTUxHck1rS2N1dVZTYGZkTVV7bgJbZQFeV2MCC11lYX1QfFtlY3dccmZxWGlpdmhYYWRMcVZ3b35kWQNsZHNZbXByYHhUdn1ya3RieHZ1VGd6dWFPYGFidWJ3XGp2cXF+bHtRbVVgTH16d3h9d3lEeGR3c3JgZGBgenZUdnp/cWhQdWF4aU4CV1gMQElaFhgRX0pXEQIRG0o=~0ri634i\",\"sceneid\":\"couponNinePointNineHome\"}"
    }

    ExchangeManagement(
        url=url,
        headers=headers,
        headers_user_agent_random_flag=False,
        user_agent="jdapp;android;10.5.2;;;appBuild/96428;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1655122900598%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22EG%3D%3D%22%2C%22ad%22%3A%22EJvuZwZtYwYnCtqzDtrwDK%3D%3D%22%2C%22od%22%3A%22YtLwCzc0DQG3ZNOzEQS2Zq%3D%3D%22%2C%22ov%22%3A%22Ctq%3D%22%2C%22ud%22%3A%22EJvuZwZtYwYnCtqzDtrwDK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046010 Mobile Safari/537.36",
        body_dict=body_dict,
        batch_size=7,
        other_batch_size=4,
        second_ahead=0.22,
        sleep_time=0.005,
        thread_number=35,
        append_flag=False,
        log_flag=False,
        sign_flag=False,
        day_or_week='day',
        post_flag=True,
        print_type="cmd",
        proxy_flag=False,
        coupon_type="9.9",
        cookie_type="cookie") \
        .executeInDesktop(
        clock_list=[0, 10, 20],
        debug_flag=False
    )
