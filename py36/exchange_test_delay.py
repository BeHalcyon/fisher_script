from exchange_lib import *


def testRequestDelayThread(url, headers, body_dict, proxy_flag, thread_id, res_dict={}, post_flag=True):
    printT("Calculating request delay test...")

    start_time = time.time()
    try:
        if post_flag:
            res = requests.post(url=url, verify=False, headers=headers,
                          data=body_dict, proxies=getProxies(proxy_flag), timeout=3)
        else:
            res = requests.get(url=url, verify=False, headers=headers,
                          data=body_dict, proxies=getProxies(proxy_flag), timeout=3)
        # res_dict[thread_id] = time.time() - start_time
        res_dict[thread_id] = res.elapsed.total_seconds()
        # print(res.headers)
        print(res_dict[thread_id], time.time() - start_time)
        d = datetime.datetime.fromtimestamp(int(res.headers['X-API-Request-Id'].split('-')[-1]) / 1000)
        str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")


        # print(time.time() - start_time, res_dict[thread_id])
        # printT(f"Current IP address and Port: {res.raw._connection.sock.socket.getsockname()}")
    except Exception:
        return


def testRequestDelay(url, headers, body_dict, sleep_time=0.03, proxy_flag=False, post_flag=True):
    printT("Calculating request delay...")
    headers = json.loads(json.dumps(headers))
    if "Cookie" in headers: headers['Cookie'] = ""
    if "cookie" in headers: headers['cookie'] = ""
    thread_number, threads, res_dict = 30, [], {}
    for i in range(thread_number):
        threads.append(threading.Thread(target=testRequestDelayThread,
                                        args=(url, headers, body_dict, proxy_flag, i, res_dict, post_flag, )))
    for i in range(thread_number):
        threads[i].start()
        time.sleep(sleep_time)
    for i in range(thread_number):
        threads[i].join()
    res = sorted(res_dict.values())
    res_dict = collections.Counter([int(100*x+1)/100.0 for x in res])

    # import matplotlib.pyplot as plt
    #
    # params = {
    #     'figure.figsize': '8, 4'
    # }
    # plt.rcParams.update(params)
    # plt.bar(res_dict.keys(), res_dict.values(), width=0.01)
    # plt.show()

    printT(res_dict)
    res = [x[0] for x in res_dict.most_common(3)]
    if len(res):
        result = min(res) + 0.02
        printT(f"Request delay: {result}s.")
        return result
    else:
        printT("Warning: The proxy is not available! Set the delay to 0.12ms.")
        return 0.12


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
    body_dict = {
        'activityId': '3H885vA4sQj6ctYzzPVix4iiYN2P',
        'scene': '1',
        'args': 'key=6E3ED4217CA5BA50CC868072587749279A819E91EC8217F49BC1DB9DC674DA27CF93291755C086262CF2BD2DADDD8138_bingo,roleId=A921D0996A757D3D319487D17C0F25FE0F6830D8485A69E35623B13BFBA59D1E7C2386D90F3D9D3A6D752ADCDEAB0529AA56BDE4467494DC5590AEB5C7C950D03EA337E197D9AF250FA7148376C8A9C2C3FC8B2D9632A67F79B5A98776BF5B6C94F3F3F8F3770E265EF7D6CAD2E5F1B98EE03623B492E1C2B96EBC7500E20DAB9C2BBC9CBBA7AA027CBB17434C77651F9DE32AEAE13EA4C6B7660D4FD53E63FF_bingo,strengthenKey=3FE987FADD098B5D46BA38B21875A5EBD8C02F19572CB3C5CC0385902CD416A2FE3B5DC71CEBCF672000554484FB93E5_bingo'
    }
    url = 'https://api.m.jd.com/client.action?functionId=lite_newBabelAwardCollection&client=wh5&clientVersion=1.0.0'

    args = parseArgs()

    requests.packages.urllib3.disable_warnings()

    os.environ["PROXY_IP"] = args.proxy_ip if len(args.proxy_ip) else 'http://127.0.0.1:7890'

    if args.proxy_flag:
        printT(f"The proxy ip is set to {os.environ['PROXY_IP']}")

    testRequestDelay(url, headers, body_dict,
                     sleep_time=0,
                     proxy_flag=args.proxy_flag if args.proxy_flag else False,
                     post_flag=True)
