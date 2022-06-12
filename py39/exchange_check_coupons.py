# encoding: utf-8
# -*- coding: utf-8 -*
'''
项目名称:exchange_check_coupons.py
Author: yangyang
功能：
Date: 2022-5-22
cron: 0 23 14,20 * * *
new Env("优惠券通知");
'''
from exchange_lib import *


if __name__ == '__main__':

    ExchangeManagement(cookie_type="cookie")

    cookies = os.environ["JD_COOKIE"].split('&') if "JD_COOKIE" in os.environ else []

    summary = "优惠券速览"
    content = ""
    for cookie in cookies:
        content += findCoupons(cookie)
    print(content)
    sendNotification(summary=summary, content=content)

    printT("通知发送成功")

