# encoding: utf-8
from exchange_lib import *

headers = {
    "Host": "api.m.jd.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3235 MMWEBSDK/20210902 Mobile Safari/537.36 MMWEBID/2219 MicroMessenger/8.0.15.2020(0x28000F3D) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
    "content-type": "application/json;charset=UTF-8",
    "accept": "*/*",
    "origin": "https://wqs.jd.com",
    "x-requested-with": "com.tencent.mm",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://wqs.jd.com/order/orderlist_jdm.shtml?sceneval=2&jxsid=16564750712163202978&orderType=waitReceipt&ptag=7155.1.13",
    "accept-encoding": "gzip,deflate",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
  }

args = parseArgs()

order_type = 128 if args.order_type == 1 else 1024 if args.order_type == 2 else 4096 if args.order_type == 0 else -1
if order_type == -1:
    print("Error in command line parameters 'order_type'")
    exit()
# order_type = 128 # 待收货
# order_type = 1024 # 已完成
# order_type = 4096 # 全部
url = f"https://api.m.jd.com/client.action?t=1656512727912&loginType=2&loginWQBiz=golden-trade&appid=m_core&client=Linux%20aarch64&clientVersion=&build=&osVersion=AndroidOS&screen=400*712&networkType=unknown&partner=&forcebot=&d_brand=UnknownPhone&d_model=UnknownPhone&lang=zh-CN&scope=&sdkVersion=&openudid=oTGnpnCOH5qxp9VHZQLl_FYW7JnY&uuid=43400397072854318&functionId=order_list_m&body=%7B%22appType%22%3A3%2C%22bizType%22%3A%222%22%2C%22source%22%3A%22-1%22%2C%22deviceUUId%22%3A%22%22%2C%22platform%22%3A3%2C%22uuid%22%3A%2243400397072854318%22%2C%22sceneval%22%3A%222%22%2C%22systemBaseInfo%22%3A%22%7B%5C%22brand%5C%22%3A%5C%22UnknownPhone%5C%22%2C%5C%22model%5C%22%3A%5C%22UnknownPhone%5C%22%2C%5C%22system%5C%22%3A%5C%22AndroidOS%5C%22%2C%5C%22pixelRatio%5C%22%3A2.700000047683716%2C%5C%22screenWidth%5C%22%3A400%2C%5C%22screenHeight%5C%22%3A712%2C%5C%22windowWidth%5C%22%3A400%2C%5C%22windowHeight%5C%22%3A637%2C%5C%22version%5C%22%3A%5C%22%5C%22%2C%5C%22statusBarHeight%5C%22%3Anull%2C%5C%22platform%5C%22%3A%5C%22Linux%20aarch64%5C%22%2C%5C%22language%5C%22%3A%5C%22zh-CN%5C%22%2C%5C%22fontSizeSetting%5C%22%3Anull%2C%5C%22SDKVersion%5C%22%3A%5C%22%5C%22%2C%5C%22albumAuthorized%5C%22%3Afalse%2C%5C%22benchmarkLevel%5C%22%3A0%2C%5C%22bluetoothEnabled%5C%22%3Afalse%2C%5C%22cameraAuthorized%5C%22%3Afalse%2C%5C%22enableDebug%5C%22%3Afalse%2C%5C%22locationAuthorized%5C%22%3Afalse%2C%5C%22locationEnabled%5C%22%3Afalse%2C%5C%22microphoneAuthorized%5C%22%3Afalse%2C%5C%22notificationAlertAuthorized%5C%22%3Afalse%2C%5C%22notificationAuthorized%5C%22%3Afalse%2C%5C%22notificationBadgeAuthorized%5C%22%3Afalse%2C%5C%22notificationSoundAuthorized%5C%22%3Afalse%2C%5C%22safeArea%5C%22%3A%7B%5C%22bottom%5C%22%3A0%2C%5C%22height%5C%22%3A0%2C%5C%22left%5C%22%3A0%2C%5C%22right%5C%22%3A0%2C%5C%22top%5C%22%3A0%2C%5C%22width%5C%22%3A0%7D%2C%5C%22wifiEnabled%5C%22%3Afalse%7D%22%2C%22orderListTag%22%3A{order_type}%2C%22curTab%22%3A%22waitReceipt%22%2C%22page%22%3A1%2C%22pageSize%22%3A100%2C%22tenantCode%22%3A%22jgm%22%2C%22bizModelCode%22%3A%222%22%2C%22bizModeClientType%22%3A%22M%22%2C%22bizModeFramework%22%3A%22Taro%22%2C%22externalLoginType%22%3A1%2C%22token%22%3A%223852b12f8c4d869b7ed3e2b3c68c9436%22%2C%22appId%22%3A%22m91d27dbf599dff74%22%7D"

cookie_type = args.cookie_type if args.cookie_type != 'None' else 'mine'

ExchangeManagement(cookie_type=cookie_type)
findOrders(
    cookies=os.environ["JD_COOKIE"].split("&") if "JD_COOKIE" in os.environ else [],
    url=url,
    headers=headers,
    proxy_flag=True,
    hours_ago=args.hours_ago if args.hours_ago != 0 else 12,
    shop_name_prefix=args.shop_name,
    cookie_type=cookie_type
)