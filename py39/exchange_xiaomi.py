

from exchange_lib import *

cookie = ''

headers = {
    "Host": "m.mi.com",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://m.mi.com",
    "x-requested-with": "com.tencent.mm",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://m.mi.com/w/mishop_activity?_rt=weex&pageid=861&sign=e86407ce821e68e65aec6c7cdbab9dad&pdl=jianyu&g_device_id=xmlitedevice_urrjpnxhe9rfj00h",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    # "cookie": ".thumbcache_2959214a7e70e5f2bd017e23a2a3e462=KifJ0TJXA5D66fNHvMYtIakmi27D8KNo8Q2jNvDBF+GbRYXw6CUX+jHYIh2x+Ja3GZP+2Nsv3GTABOXDsVs3pw%3D%3D"
  }

url = "https://m.mi.com/v1/activity/page_draw_query"

body_dict = "activity_codes=0Tg3B8vHw8Xcrs57JfEmeA=="

args = parseArgs()

ExchangeManagement(
    url=url,
    headers=headers,
    headers_user_agent_random_flag=False,
    user_agent="Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3263 MMWEBSDK/20210902 Mobile Safari/537.36 MMWEBID/2219 MicroMessenger/8.0.15.2020(0x28000F3D) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram",
    body_dict=body_dict,
    batch_size=args.batch_size if args.batch_size > 0 else 12,
    other_batch_size=0,
    second_ahead=0,
    sleep_time=0,
    thread_number=args.thread_number if args.thread_number > 0 else 40,
    append_flag=False,
    log_flag=False,
    sign_flag=False,
    day_or_week='day',
    post_flag=True,
    print_type="cmd",
    proxy_flag=args.proxy_flag if args.proxy_flag else True,
    coupon_type="xiaomi",
    cookie_type=args.cookie_type if args.cookie_type != 'None' else 'xiaomi') \
    .executeInDesktop(
    clock_list=[10],
    debug_flag=args.debug_flag if args.debug_flag else False
)
