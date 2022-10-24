# encoding: utf-8
from exchange_lib import *
try:
    import jieba.analyse
except Exception:
    print("Error in importing jieba module, please run 'pip install jieba' in command line.")
    exit()

jieba.setLogLevel(jieba.logging.INFO)

def generateComment(pname):
    try:
        name = jieba.analyse.textrank(pname, topK=5, allowPOS='n')[0]
    except:
        name = "宝贝"

    datas = {
        "start": [
            "考虑买这个$之前我是有担心过的，因为我不知道$的质量和品质怎么样，但是看了评论后我就放心了。",
            "买这个$之前我是有看过好几家店，最后看到这家店的评价不错就决定在这家店买 ",
            "看了好几家店，也对比了好几家店，最后发现还是这一家的$评价最好。",
            "看来看去最后还是选择了这家。",
            "之前在这家店也买过其他东西，感觉不错，这次又来啦。",
            "这家的$的真是太好用了，用了第一次就还想再用一次。",
            "其实一直都想入手一款$，但找不到合适的。",
            "做工看的出很优秀，手感也很好，和描述几乎一致。",
            "这个价格来说很具性价比，但是质量还是很不错的,装东西够用了,非常合适，质量也好，"
            "没感觉到什么难闻的味，能收纳好多东西，结实，实用，方便，厚度和 颜色都是我想要的，最重要的是高度刚刚好"
        ],
        "mid": [
            "收到货后我非常的开心，因为$的质量和品质真的非常的好！",
            "拆开包装后惊艳到我了，这就是我想要的$!",
            "快递超快！包装的很好！！很喜欢！！！",
            "包装的很精美！$的质量和品质非常不错！",
            "收到快递后迫不及待的拆了包装。$我真的是非常喜欢",
            "真是一次难忘的购物，这辈子没见过这么好用的东西！！",
            "收纳很漂亮很可爱，材质做工很好！无异味！大小尺寸齐全",
            "这个价位很满意了，拿回来一会儿就装好",
            "接头是那种很有韧性的胶、敲打的过程中不会裂开",
            "很有包容性、装好以后不会晃动、很稳，物流也快、五星好评"
        ],
        "end": [
            "经过了这次愉快的购物，我决定如果下次我还要买$的话，我一定会再来这家店买的。",
            "不错不错！",
            "我会推荐想买$的朋友也来这家店里买",
            "真是一次愉快的购物！",
            "大大的好评!以后买$再来你们店！(￣▽￣)",
            "大家可以买来试一试，真的是太爽了，一晚上都沉浸在爽之中",
            "这种物件，不但轻便，而且在自己拼装完成后有一种成就的喜悦，真是宿舍家居良品",
            "自己组装成功，跟价格相称，比较简易",
            "操作比较方便。到时候也好拆卸，没想到这么便宜竟然这么好。",
            "东西很不错，木头也不错。",
            "特别好，而且功能百搭。",
            "没有色差，大小合适，组装简单，质量很好"
        ]
    }
    return (random.choice(datas["start"]) + random.choice(datas["mid"]) + random.choice(datas["end"])).replace("$", name)


def getOrderList(cookies, shop_name=''):
    url = 'https://wq.jd.com/bases/orderlist/list?order_type=8&start_page=1&page_size=100'
    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "connection": "keep-alive",
        "content-type": "application/x-www-form-urlencoded",
        'origin': 'https://comment.m.jd.com',
        "referer": "https://wqs.jd.com/order/orderlist_merge.shtml?jxsid=16355625882984298965&orderType=all&ptag=7155.1.11",
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    result = {}
    for cookie in cookies:
        result[cookie] = []
        headers['cookie'] = cookie
        req = requests.get(url, headers=headers).json()
        # print(req)
        if 'orderList' not in req:
            continue
        for order_list in req['orderList']:

            if shop_name in order_list['shopInfo']['shopName']:

                for j in order_list['buttonList']:
                    if j['id'] == 'toComment':
                        cname = j['name']  # 评价按钮名字
                if cname is None:
                    continue

                oid = order_list['orderId']
                shopId = order_list['shopInfo']['shopId']
                for order_item in order_list['productList']:
                    pid = order_item['skuId']
                    name = order_item['title']
                    result[cookie].append({
                        'name': name,
                        'oid': oid,
                        'pid': pid,
                        'cname': cname,
                        'shopId': shopId,
                        'shopName': order_list['shopInfo']['shopName'],
                        'comment': generateComment(name)
                    })
    return result

def commentOrders(comment_orders_dict, proxy_flag=False):
    url = "https://api.m.jd.com/api?appid=jd-cphdeveloper-m&functionId=sendEval&loginType=2&sceneval=2&g_login_type=1&g_ty=ajax&appCode=ms0ca95114"
    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "connection": "keep-alive",
        "content-type": "application/x-www-form-urlencoded",
        'origin': 'https://comment.m.jd.com',
        "referer": "https://comment.m.jd.com/",
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    log_num = 0
    for value in comment_orders_dict.values():
        log_num += len(value)
    logs = getLogs(num=log_num)
    log_num = 0
    order_id_set = set()
    for cookie, orders in comment_orders_dict.items():
        headers['cookie'] = cookie
        for order in orders:
            body = {
                "productId": order['pid'],
                "orderId": order['oid'],
                "score": 5,
                "content": order['comment'],
                "commentTagStr": 1,
                "userclient": 29,
                "anonymous": 0,
                "syncsg": 0,
                "scence": 101100000
            }

            response = requests.post(url=url, headers=headers, data=generateBody(body, logs[log_num]), proxies=getProxies(proxy_flag)).json()

            if 'errMsg' in response and response['errMsg'] == 'success':
                printT(f"{getUserName(cookie)}: 评价成功！店铺：{order['shopName']}, 内容：{order['comment']}")
            else:
                printT(f"{getUserName(cookie)}: 评价失败！店铺：{order['shopName']}, 日志：{response}")

            if order['oid'] not in order_id_set:

                se_url = f'https://wq.jd.com/eval/SendDSR'
                se_data = {
                    'userclient': '29',
                    'orderId': order['oid'],
                    'otype': 5,
                    'DSR1': 5,
                    'DSR2': 5,
                    'DSR3': 5,
                    'DSR4': 5,
                    'g_login_type': '0',
                    'g_ty': 'ls'
                }
                se_req = requests.get(se_url, headers=headers, params=se_data, proxies=getProxies(proxy_flag)).json()
                if se_req['errMsg'] == 'success':
                    order_id_set.add(order['oid'])
                    printT(f"{getUserName(cookie)}: 评价服务成功！店铺：{order['shopName']}")
                else:
                    printT(f"{getUserName(cookie)}: 评价服务失败！店铺：{order['shopName']}")

            log_num += 1
            time.sleep(random.randint(5, 10))


if __name__ == '__main__':

    args = parseArgs()

    ExchangeManagement(cookie_type=args.cookie_type if args.cookie_type != "None" else "mine")
    cookies = os.environ['JD_COOKIE'].split("&")
    os.environ['proxy_ip'] = args.proxy_ip if len(args.proxy_ip) else "127.0.0.1:7890"
    result = getOrderList(cookies, shop_name=args.shop_name)
    for key, value in result.items():
        for item in value:
            print(getUserName(key), item)
    commentOrders(result, proxy_flag=args.proxy_flag if args.proxy_flag else False)
