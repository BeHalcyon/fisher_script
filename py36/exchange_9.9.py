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

    body_dict = {"extend":"ADE38779BE11ED01E2C9DA3F4E92429CBA2BDD4AC7B0F93E05E8FCC18BD296E6226AA9E4296AF3609B4C3F36D87A292DB1DA7F79BF316E599EA2B24106BE59DE6B8A6160AC012ADDDE7362D4FAC56DBEC4A8D747AE66F99664842F81E7F7470C47ABA2B1C26F0E78A475DB7E2EAC9CE9546A15AF65B9C2F4EF2B62731830A63675F838E2BC1B086A5B0BBD0306869BCFD7C0ECCF3F4A8C2352FAC998FF9E0BA357823A172A2572C1A0ACE8A16CCA4D2B9B62BC2EAFBFF64F49F8BDB897D4443B2696DCDECBB0773873BED9372FECEB7B3BF1611BFA19E40CDDC876733FD3F9A8","rcType":"1","source":"couponCenter_app","random":"9425341","couponSource":"1","extraData":"{\"log\":\"1655206260946~1hqTJWmMuYiMDFEelJVdDAxMQ==.dUxnYEZ0TGBhQHZPaisCERhrbBlxFCswCnVWZHlBaEssZwp1BDwfAS0MAD8GPjcXBR0RSTQwEHAeMBslOg==.c796572f~5,1~9249BEB080D84F5C49A6D2DC5D7F123CF1073969~16mrv92~C~SxNEWBsLb2oUEERbVRILaxddABkPeR4IdxQBCBxAFUUWGxpWBRgAeh0IcBUAZHUUAx4FCAAdRBcVE1AAFQp6GQB1HQFkdB0FGQgCABlMEmwcF15DWhUCABwXS0MTChcIBwECCgIGBw0JBgAHDAUMBBoeEkJdVBMKF01FQENMEBwXT1VQEg8bV1JDTEZEQFkSHRJFXV8WDWMGHAQOAx0GGQgAGAYUB20ZGlpbEg8KHRZUSxAKFwwJBlNUX1IFBAtQVgRcCQJSAw9UAlIIAgIHWlVSAAMKExgVVkISDxp8WF5AQRFVRVVECFkaHBNEFwMAAgINAAADCgYBCQEPHRZdUxAKFxUEUgQMXAJSAgwHAwYVCQhUU19SVlEJAAgGDghXBBgPVwYOW1ABVlxUUwlWDVRWUQxTVgBdA1dRU1oFDVQIVwMNDVFSEhkbV0RVGggSW3JFWEZnU0NOen1iWWALVlRUAV1TemYaHhJbThILEnJWXlNbXRJ5W1seExwXV1BCFQIQCQMMAgkSGRtCV0UaCGsDDAAdAwMJbBgVSl0SD2MSfHkVDxMYFVlcVEdXWVUSGRsIFhsaAwAbDR4DEhkbCAIDCgoSGRoJAgkGDQcCAQ4EAwMKBgcGGAgCBgQAAQMGDgMJAwMPBQcVFBABF2UcE1laWBMOFV5UVlNeVkVEFxUTVV0aCBJAGhwTU1wbCxZACxwBGwgSHRJWX25CFQIQAAQaHBNSURsLFkVZXFRaVQ0IBAcMAgAGGh4SWFISC2sEFQEYB2UeEldUX1YSDxsAAgINAAADCgMHCQwKTwVYflRbDGJ9VXd5dHVyR2EBakVvZHBIeF4MCRlvdGZxYHdFamNsY21WVEZhZ3pURXV0Slp3cE9bc15qUntIDGl1cWFCYGZ8cWhIVGxxYHZte1V1WGpaCVZxQ3Nzf3pnUnFTZWB+XFpmc05QR3p3cQR5clZ1fARxfXRiQgh/S3VidGJhUnFaUw15WEZXcVVGfX98Amd2VF8HcQdefnJbS1F3T2FYdmZGdGRwZmJgd1pZenQIc3xgfXVwZFdPcEpCZXd7cHJyUAt1V1BHe2FxfEd7T3V6eGR5CWdlbHd6XHZscwFSenx3RGV4Y1NNdUV5RlpiVmNkfQFSYm5BQGB/Q3x3X2tVeHV1enVnU197SXBTe3Bmd3FmRhd/WXEDeGBTfHBbRwJxSl51YFMAcXZuBmdnbltfHgULBlFRXQtRS0EcAE5LR3NKZGp8dXB5BGBmY1FwbGJuZmcEDFRnZnd9eVhlWWBieFl1d2VkeklyUWkDU1RtAGd4YghZf39UfHhnVAVSYWdgVHEGeWFzTXJmdHJCa2cFZVVgWHRxdXB1fXxzU2ZqYHV+fUdofnZOfGZwenBhZFBxeHV0eFB1T2FXdQQNcXRHWm5wU3J8cGJ0bnVddld8cEdibWNTVnlIAXNwCQEJSQhZSUBJWVUSGRtcR1AaCBIXRQ==~0p3rcsa\",\"sceneid\":\"couponNinePointNineHome\"}"}

    ExchangeManagement(
        url=url,
        headers=headers,
        headers_user_agent_random_flag=False,
        user_agent="jdapp;android;10.5.2;;;appBuild/96428;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1655122900598%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22EG%3D%3D%22%2C%22ad%22%3A%22EJvuZwZtYwYnCtqzDtrwDK%3D%3D%22%2C%22od%22%3A%22YtLwCzc0DQG3ZNOzEQS2Zq%3D%3D%22%2C%22ov%22%3A%22Ctq%3D%22%2C%22ud%22%3A%22EJvuZwZtYwYnCtqzDtrwDK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046010 Mobile Safari/537.36",
        body_dict=body_dict,
        batch_size=6,
        other_batch_size=4,
        second_ahead=0.28,
        sleep_time=0.00,
        thread_number=38,
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
