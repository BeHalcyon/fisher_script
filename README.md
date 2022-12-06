

### 简介
- fisher_script: 适用于某些app（如某东、某团、某米商城）各类券的抢购，包括小时购、短key类券（如哲学系10-9、59-20）、长key类券（如极速版限品类券、具有活动Id页面下的任何类券）、金融类券、plus类券等。
- 个人学习，请在24小时内删除！
- 所有仓库脚本请勿原地修改，如需要自定义功能，可在目录下创建新的文件。
- 为防滥用，ExchangeLib定时授权，如遇到证书过期，更新库文件；为防滥用，增加外部授权码，没有授权码降级可用。
- 缺少python基础的勿用、为盈利的勿用、残障CPU勿用
- 暂未在青龙环境下测试。
- **遇到问题后，请先把本文档看一遍。**
- Base64神秘内容：ZmlzaGVyX3NjcmlwdOWinuWKoOaOiOadg+egge+8jOmBv+WFjeWVhueUqOWMluOAguaOiOadg+eggeWPr+Wumuacn+WFjei0ueiOt+WPluOAggoKa05KeG11NURjOEhuS3N6ajBsYVdsMzdlNVBMV1Y3YUtZcmtITTFIT0dROD0g5pyJ5pWI5pyf6IezMjAyMi0xMS0zMCDnur/nqIvmlbDpmZDliLYyMApDaG5ZMXRxeFJidlFKenVGZlVwWnkzVEJSeW52dnl0THJWMkxlTFZqdStvPSDmnInmlYjmnJ/oh7MyMDIzLTAyLTAyIOe6v+eoi+aVsOmZkOWItjEwCgrlpoLmnpzkvaDlr7nmiqLliLjmhJ/lhbTotqPjgIHllpzmrKLmjqLntKLkuqTmtYHvvIzor7fogZTns7vmiJFCeUhhbGN5b24=

### 更新日志

| 版本     | 描述     |
| -------- | -------- |
| 20221202:v1.11 | 增加日志的命令行输出及log文件输出功能，文件默认存储到当前目录的logs目录下 |
| 20221202:v1.10 | 增加h5st接口 |
| 20221030:v1.9 | 修复若干bug，优化抢券逻辑 |
| 20221010:v1.8 | 没有什么卵用的更新（该版本仅测试过py37和py38可用，请匹配对应python环境！） |
| 20220916:v1.7 | 更新全品类59-20参数获取逻辑 |
| 20220915:v1.6 | 更新券后9.9（羊毛购）类券 |
| 20220904:v1.5 | 更新某团券类参数 |
| 20220822:v1.4 | 优化抢券时间分配 |
| 20220819:v1.3 | 支持精确到分钟的定时任务，如clock_list=[12.30, 14.50]，表示12点30分运行和14点50分运行，小数点后超过60无效 |
| 20220811:v1.2 | 进一步优化配置，支持长key和短key的索引（相关脚本为exchange_general_long_key.py和exchange_general_short_key.py） |
| 20220810:v1.1 | 支持某米商城券的抢购，相关脚本为：exchange_xiaomi.py |
| 20220804:v1.0 | 支持某团券的抢购，相关脚本为：exchange_mt.py |
| --- | --- |
| 20220731:v0.17 | 配置文件中增加券的索引参数（activityId和discount），适配通用脚本exchange_general_with_log.py，支持多券单脚本 |
| 20220720:v0.16 | 增加代理服务器接口，通过命令行参数--proxy_flag和--proxy_ip确定 |
| 20220711:v0.15 | 修复已知bug |
| 20220710:v0.14 | 增加命令行式自动评价功能（python exchange_evaluation.py --help），支持店铺的模糊查找修改，默认所有商品全部评价；优化sign获取 |
| 20220702:v0.13 | 增加命令行式参数设计功能，可灵活支持多脚本并行执行，参考**命令行交互** |
| 20220630:v0.12 | 增加订单查询功能；增加红包查询功能 |
| 20220625:v0.11 | 修复0点进入队列的异常号bug；增加授权；支持小时购类券；大幅降低高峰期调用log服务器的频率 |
| 20220624:v0.10 | 修复多轮启动后second_ahead无法重置的bug；日志内敏感pin字段加密； |
| 20220623:v0.9 | 配置文件修改为软加载方式，修改文件后不需要重新启动脚本，下一轮默认重新加载 |
| 20220622:v0.8 | 动态适配配置文件中的cookies类型，可自定义类型并在代码种设定cookie_type，支持前缀字段索引 |
| 20220621:v0.7 | 修复极速版类券高峰期可能获取log失败的bug |
| 20220620:v0.6 | 极速版类券可取消设定second_ahead参数，每场次自动化计算 |
| 20220618:v0.5 | 青龙代码适配，环境尚未适配 |
| 20220616:v0.4 | 提供真实及虚拟activityId的区分，分别用于参数生成及“很抱歉”情况的避免 |
| 20220614:v0.3 | 启动时间随机设置为59分0~10s，避免多进程或多设备的数据库写入冲突；修复获取log可能存在的网络异常|
| 20220612:v0.2 | 修复了0点输出及推送异常的bug；增加了body_activityid_random_flag参数 |
| 20220610:v0.1 | fisher_script: the coupons ExchangeLib |

验证是否更新成功：
```bash
python -c "import exchange_lib; print(exchange_lib.__version__)"
```
### 常见问题
#### 1. No module Named "requests"
解决方案：命令行输入 ```pip install requests```

#### 2. No module Named "Crypto"
解决方案：
- windows环境：[解决方案](https://blog.csdn.net/ragerabbitr/article/details/122058945?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-122058945-blog-125294237.pc_relevant_multi_platform_featuressortv2dupreplace&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-122058945-blog-125294237.pc_relevant_multi_platform_featuressortv2dupreplace&utm_relevant_index=1)
- linux环境：TODO

#### 3. Error in the configure file (fisher_configure.json)
解决方案：
1. 查询是否有中文标点符合
2. 查询配置文件中每项末尾是否包含额外字符
3. 是否将模板内中文注释删除
4. 脚本中的cookie_type是否存在于配置文件中"cookies"

### 本地环境

#### 1. 拉库
```bash
git clone https://github.com/BeHalcyon/fisher_script.git
```

#### 2. 选择python对应版本的项目作为项目根目录
命令行模式下输入python命令，判断版本
```bash
python --version
```
进入指定版本的根目录（例如Python版本为3.8.2）
```bash
cd ./py38
```

推荐版本：Python 3.9.2, Python 3.8.2, Python 3.7.9, Python 3.6.3。其他版本暂未测试，测试不通请先更换指定python版本。

#### 3. 项目根目录下创建fisher_configure.json文件

##### 模板（创建文件时需删除中文注释）：
```json
{
  "authorization_code": "xxxxxxxxxx",
  "interface":{
    "JDLITE_LOG_API": "http://x.x.x.x:5889/batchLog",
    "JD_SIGN_API": "http://x.x.x.x:x/x",
    "JD_SIGN_API_TOKEN": "xxxxxxxxxx"
  },
  "database": {
    "database_flag": "database_local",
    "database_remote": {
      "DATABASE_TYPE": "",
      "DATABASE_HOST": "",
      "DATABASE_PORT": "",
      "DATABASE_USER": "",
      "DATABASE_PASSWD": "",
      "DATABASE_DATABASE": ""
    }
  },
  "notification": {
    "WXPUSHER_APP_TOKEN": "",
    "WXPUSHER_UID": ""
  },
  "coupons": {
    "june-59-20": {
      "注释（部署时删除该条目）": "自定义对象。6月的59-20的key，写入args参数里，并设定定时为clock_list。对应执行脚本为python exchange_general_short_key.py -c your_cookies -C june-59-20",
      "args": "key=m7abt6e3r4ica9l9cfm7scdf3dc82f59,roleId=80139254",
      "clock_list": [0, 10, 14, 20]
    },
    "june-10-9": {
      "args": "key=m1a8t3eer2i4a4l6c2m2s9bd982f3b98,roleId=81264321",
      "clock_list": [0, 10, 14, 20]
    },
    "39-8": {
      "注释（部署时删除该条目）": "自定义对象。极速版某券的索引，需要填写activityId和discount进行索引，并设定定时为clock_list。对应执行脚本为python exchange_general_long_key.py -c your_cookies -C 39-8",
      "activityId": "3H885vA4sQj6ctYzzPVix4iiYN2P",
      "discount": "8",
      "clock_list": [9, 12, 15, 18]
    },
    "30-5": {
      "activityId": "3H885vA4sQj6ctYzzPVix4iiYN2P",
      "discount": "5",
      "clock_list": [18]
    },
    "15-3": {
      "activityId": "3H885vA4sQj6ctYzzPVix4iiYN2P",
      "discount": "3",
      "clock_list": [0]
    },
    "34.9-34.89": {
      "activityId": "2doZYAgSAX6kiGmfrL4ZwLHzHHxa",
      "discount": "34.89",
      "clock_list": [14]
    },
    "1200-1040": {
      "activityId": "3bfYsYLqfqHvem9pNnVAAdyVLoR3",
      "discount": "1040",
      "clock_list": [20]
    }
  },
  "cookies": {
    "ws_cookies": [
      "pin=xxxxxxxx;wskey=xxxxxxxxxxxxxx;unionwsws=xxxxxxxxxxxxxxxxxx;",
      "pin=xxxxxxxx;wskey=xxxxxxxxxxxxxx;unionwsws=xxxxxxxxxxxxxxxxxx;",
      "pin=xxxxxxxx;wskey=xxxxxxxxxxxxxx;unionwsws=xxxxxxxxxxxxxxxxxx;"
    ],
    "plus_cookies": [
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;"
    ],
    "cookies": [
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;"
    ],
    "any_name_of_cookies": [
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;"
    ]
  }
}
```

##### 参数解释：

- authorization_code：授权码，为空时可以开最多1个线程，用于测试

- JDLITE_LOG_API：极速版的log api，通用
    
- JD_SIGN_API：本库依赖的SIGN api，不通用
    
- JD_SIGN_API_TOKEN：本库依赖的SIGN api对应的token，不通用
    
- database_flag：为"database_remote"时需要设定database_remote参数，表示数据库存储到远程服务器（mysql），默认为"database_local"（sqlite），不需要设定database_remote参数。
    
- WXPUSHER_APP_TOKEN和WXPUSHER_UID：wxpusher的app token和个人uid
    
- ws_cookies、plus_cookies、cookies：分别为wskey格式的cookie、plus会员的cookie等，名称可自定义，需要与代码中的cookie_type对应。

##### JSON注意事项：
- 文件内所有字符均为英文，不能有中文符号（例如"，"）

- 中括号内最后一个元素的尾部没有","，其他元素尾部均有","

- 模板内所有的参数可以缺省，但不可以删除

- ws_cookies参数中，需要对字符串内的双引号及反斜杠进行转义：

以下为**错误**示例：
```json
{
  "ws_cookies": [
    "pin=xxxxxxx;wskey=xx\xxx;abc={"aasdfas":"asdfs\/dfgs"};"
  ]
}
```

以下为**正确**示例：
```json
{
  "ws_cookies": [
    "pin=xxxxxxx;wskey=xx\\xxx;abc={\"aasdfas\":\"asdfs\\/dfgs\"};"
  ]
}
```

#### 4. 库示例

##### 测试

- 命令行执行如下命令，无报错运行后说明环境部署成功。
```python
python ./exchange_check_coupons.py
```

- pycharm中，直接点击运行exchange_check_coupons.py，无报错运行后说明环境部署成功。

##### 代码

```python
ExchangeManagement(
                 url="", # 必须：包含functionId及相关内容的url；字符串类型
                 headers={}, # 可选：请求头，不包含cookie及content-length；字典类型
                 headers_user_agent_random_flag=True, # 必须：请求头中的user-agent是否随机；Boolean类型
                 user_agent="", # 可选：当headers_user_agent_random_flag为False时有效，用于设定固定user-agent；字符串类型
                 body_dict={}, # 可选：请求体，包含"body"、"args"等关键字；字典类型
                 activityId_random_flag=False, # 可选：是否选择随机的activityId，随机时设置为True，能够避免长期索引某activityId引起的抱歉
                 discount="", # 可选：设定指定的折扣值，当activityId_random_flag=False时有效；字符串类型
                 batch_size=6, # 必须：周期内首批需要运行的账号数，所有前batch_size个账号全部抢到后，才开始考虑其他账号；整型
                 other_batch_size=4, # 可选：周期内次批一次性需要运行的账号数，为0时默认每次根据权重选择batch_size个账号运行；整型
                 second_ahead=0.3, # 必须：线程启动的提前秒数，线程的冷冻时间；例如提前0.40s准备启动线程，依赖于设备资源；浮点类型
                 sleep_time=0.03, # 必须：每个线程的等待时间，每次post的等待时间，依赖于网络传输速率；浮点类型
                 thread_number=12, # 必须：线程数量，post次数，可根据thread_number*sleep_time粗略计算当场运行时间
                 append_flag=True, # 可选：batch_size内权重最高的账号是否增加一次机会；Boolean类型
                 log_flag=False, # 必须：是否需要log，为True时默认极速版；Boolean类型
                 sign_flag=False, # 必须：是否需要sign，为True时默认点点券；Boolean类型
                 day_or_week='day', # 必须：周期为day或week；字符串类型
                 post_flag=True, # 必须：是否为post类型的request；Boolean类型
                 proxy_flag=False, # 可选：是否选择代理，为False时默认不选择，为True时需保证127.0.0.1:7890为代理访问；Boolean类型
                 print_type="one of [cmd, file], default to cmd", # 可选：日志为直接输出或文件类型输出；字符串类型
                 coupon_type="", # 必须：券名；字符串类型
                 cookie_type="your_cookie_type_in_fisher_configure.json", # 必须：需要与fisher_configure.json对应。
                 ). \
executeInDesktop(clock_list=[0, 10, 14, 20, 22], # 定时任务；
                 debug_flag=False # 是否需要调试，为False时为部署（整点运行），为True时为调试（下一分钟运行）；Boolean类型
                )
```

##### 命令行交互
以下示例解释：以调试方式运行exchange_x_x.py脚本，设定线程数量为12，每轮次抢6个账号，cookie_type为fisher_configure.json配置文件中的"fisher1"字段的cookie
```bash
python exchange_x_x.py --debug_flag --thread_number 12 --batch_size 6 --cookie_type fisher1
```
以下示例解释：整点运行exchange_x_x.py脚本，设定线程数量为12，每轮次抢3个账号，cookie_type为fisher_configure.json配置文件中的"fisher2"字段的cookie
```bash
python exchange_x_x.py --thread_number 12 --batch_size 3 --cookie_type fisher2
```
以下示例解释：以调试方式运行exchange_x_x.py脚本，设定线程数量为脚本内默认的值，每轮次抢为脚本内默认个账号，cookie_type为脚本内默认的cookie_type
```bash
python exchange_x_x.py --debug_flag
```
以下示例解释：整点运行exchange_x_x.py脚本，设定线程数量为脚本内默认的值，每轮次抢为脚本内默认个账号，cookie_type为脚本内默认的cookie_type
```bash
python exchange_x_x.py
```

##### 命令行示例券
采用具有log验证的券，选择的ck为fisher_configure.json中具有"cookie"标识的分组，选择的券类型为fisher_configure.json中具有"39-8"标识的"coupons"，线程数量为30，只运行前20个账号。
```bash
python exchange_general_long_key.py --cookie_type cookie --coupon_type 39-8 --batch_size 20 --thread_number 30
python exchange_general_long_key.py -c cookie -C 39-8 -b 20 -t 30
```
通用类短key券，选择的ck为fisher_configure.json中具有"test_cookies"标识的分组，选择的券类型为fisher_configure.json中具有"july-10-9"标识的"coupons"，线程数为10， 只抢前10个没有抢到的号，以调试模式运行，增加代理，代理ip地址为127.0.0.1:7890
```bash
python exchange_general_short_key.py -cookie_type test_cookies --coupon_type july-10-9 --batch_size 10 --thread_number 10 --proxy_flag --proxy_ip 127.0.0.1:7890 --debug_flag
python exchange_general_short_key.py -c test_cookies -C july-10-9 -b 10 -t 10 -p -i 127.0.0.1:7890 -d
```
执行某米商城类券，线程数量为20
````bash
python exchange_xiaomi.py --cookie_type xiaomi -t 20
````

##### 几个参数的额外描述

| 参数     | 描述     |
| -------- | -------- |
| log_flag=False, sign_flag=False | 非校验类型的通用api，需填写url, headers, body_dict参数 |
| log_flag=True, sign_flag=False | 极速版log校验类型的api，需填写url, headers, body_dict参数 |
| log_flag=False, sign_flag=True | sign校验类型的api，无需填写url, headers, body_dict参数 |
| discount="8", activityId_random_flag=False | 券的优惠值，该args通常需要用log，即log_falg需设置为True |
| activityId_random_flag=True | 每场随机改变activityId，设定为True后会使用默认activityId，且discount失效 |
| second_ahead=0, sleep_time=0 | second_ahead为0时自动配准某东服务器整点，搭配线程睡眠时间为0，不间断请求时间 |

#### 5. 更新
- 更新前先进如仓库根目录
- 仓库内示例文件请勿修改，更新时会被覆盖。
- 自定义的文件（如配置文件）不会被覆盖，请放心食用。


```bash
git pull origin master
```

### 青龙环境（尚未完善）
```python
ExchangeManagement(...).executeInQingLong()
```