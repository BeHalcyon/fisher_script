#!/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称:exchange_9.9.py
Author: yangyang
功能：
Date: 2022-5-7
cron: 10 59 9,15 * * *
new Env("极速版10减2");
'''
from exchange_lib import *

if __name__ == "__main__":
    url = "https://api.m.jd.com/client.action?functionId=centerReceiveCoupon&appid=XPMSGC2019&monitorSource=&client=m&eu=9393466666362666&fv=1323833363836643"
    headers = {
        # "authority": "api.m.jd.com",
        # "Accept": "*/*",
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
        # "Connection": "keep-alive"
        # "User-Agent": ""
    }

    body_dict = {
        "extend": "D550270EB8017CE5A21E2296239BFEED62DF83A8550280B801D00BEF43263A3A4B6FEC15745E95CCAC610D2FED164A44B1DA7F79BF316E599EA2B24106BE59DE6B8A6160AC012ADDDE7362D4FAC56DBEA5EA86FBEC0B6379777090D3FC6C082847ABA2B1C26F0E78A475DB7E2EAC9CE9B336223E66EAD9BD395DF02F4D55E0F275F838E2BC1B086A5B0BBD0306869BCF3E7D61BEF354ECE95FE2D4C57BE6142D57823A172A2572C1A0ACE8A16CCA4D2B509DB18974D20BFAE297B02ACF3045835F23ED8D2B8A7DA6BC7BA31FBBBD40063BF1611BFA19E40CDDC876733FD3F9A8",
        "rcType": "1",
        "source": "couponCenter_app",
        "random": "6776471",
        "couponSource": "1",
        "extraData": "{\"log\":\"1655208909066~1HgRuqs4MNKMDFiQmRHVDAxMQ==.U3RRcmZSelxwY1t0VjlkJgchJWdXBgA9KlNuUmthTnMadSpTPAoNIQs0Ni0mGA8hFz03cQIiMFYmBgkFHA==.68e049d1~5,1~FBFD419887579997EF4829338C8DFB275B44B0E5~0qlczlp~C~SBVDVBMDbm4fFEZZWxENbBtVCBgLdRoKdBp7G0IVRRsZEVcDHw9/Hw9wFQkAbx8CGAIHBh9DFRUTXQIeC38eD3EfD3ZsHQgbAwMGHkMUbhsVXkNXFwkAGhBERRENFQgHDAABAw4KDg8FAQYPAAsHER8URVJSEQ0VTUVNQUcRGhBAU1IVDRtXX0FHR0JHVhQfFUddXxsPaAcaBwAPHwEbCAAVBB8Gax4VXFkVDQodG1ZAEQwQAw8EVFZfUggGAFFQA1MPAFUBD1QPUAMDBABVU1AHAQoTFRddQxQIFXpaWUJBEVhHXkUOXhUaEUMVAwAPAAYBBgoOBgoHAQ8dG19YEQwQGgJQAw5cAl8ABwYFARoPClNRX1JbUwIBDgEBDlUDGg9XCwxQUQdRU1JRDlQNVFtTB1JQB1IFVVZRWgUAVgNWBQoCV1AVGxtXSVcRCRRcfUNaQWVTQ0N4dmNfZwRQVlMDXVN3ZBEfFFxBFAkVcFZeXllWE39cVBgRGxVXUE8XCREPBAMECxUbG0JaRxEJbQQDBh8EAQlsFRdBXBQIbBR+fhcPExUXUl1SQFhfVxUbGwgbGRECBhwCGAEVGxsIDwEBCxQeFQ8ADgQNBw8DBQUFBAUABQEaCAILBgsABQEBBQsEAQ8FChcfEQcQahoRXlhYEwMXVVVQVFFQR0MVFRNYXxEJFEcVGhFUXhsLG0IAHQccBxQfFVRfbk8XCREGAxUaEVVTGwsbR1JdUl1aCwUAAA8FDgQRHxRfXRQJbAYVARUFbh8UUFtZVBUNGwAPAAYBBgoPAQABBA5PCHgFcHRLR2NcdH90dX9FagBsQmBick96XgwEG2R1YHZvcUdtYWxjYFRfR2dgdVJHcnZKWnpyRFp1WWVUeU8OaXV8Y0lhYHt+bkpTbnFge29wVHNfZVwLUXNDc359cWZUdlxjYnleWmZ+TFtGfHB+Ant1VHV8CXN2dWRFB3lJcmB0YmxQeltVCnZeRFBzVUZwfXcDYXFbWQV2BV5+f1lAUHFIbl50YUR0ZH1kaWFxXVZ8dg9xfGBwd3tlUUh/TEBidXtwf3BbCnNQX0F5ZnN8R3ZNfnt+Y3YPZWJud3pRdGdyB1V1enVDZ3hjXk9+RH9BVWRUZGZ9AV9gZUBGZ3BFfnBda1V1d357c2BcWXlOclN7fWR8cGBBGHlbdgF4YF5+e1pBBX5MXHJiUwB8dGUHYWBhXV0ZBwsGXFNWCldMQRoCSUlHc0dhcXVwdGYGZWIGQXluBXlmblVYb2VbYmB5Xnx8YnNwfHBlbmF6Y29sYWV3aGFdeXNgf118Zl9XdWNAB1JxB2hTaHRmZXJgYWV1ZURvZ39zXGJkZ3lzYlNhf3NKY3VbfFdld2FiYWhwb3JLdVNgZWN9cWZgU3tdZlVwY1txdWYGeHB/Y2RxXXB8cGVlUnxgCWNlcmdodWRYcXFsBQRLA0ICVQFaURUbG1xKUhEJFBBK~1djfvq6\",\"sceneid\":\"couponNinePointNineHome\"}"
    }

    ExchangeManagement(
        url=url,
        headers=headers,
        headers_user_agent_random_flag=False,
        user_agent="jdapp;android;10.5.2;;;appBuild/96428;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1655122900598%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22EG%3D%3D%22%2C%22ad%22%3A%22EJvuZwZtYwYnCtqzDtrwDK%3D%3D%22%2C%22od%22%3A%22YtLwCzc0DQG3ZNOzEQS2Zq%3D%3D%22%2C%22ov%22%3A%22Ctq%3D%22%2C%22ud%22%3A%22EJvuZwZtYwYnCtqzDtrwDK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046010 Mobile Safari/537.36",
        body_dict=body_dict,
        batch_size=6,
        other_batch_size=4,
        second_ahead=0.20,
        sleep_time=0.00,
        thread_number=40,
        append_flag=False,
        log_flag=False,
        sign_flag=False,
        day_or_week='day',
        post_flag=True,
        print_type="cmd",
        proxy_flag=False,
        coupon_type="9.9",
        cookie_type="cookie")\
    .executeInDesktop(
        clock_list=[0, 10, 20],
        debug_flag=False
    )
