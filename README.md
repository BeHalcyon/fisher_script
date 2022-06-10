

### 简介
个人学习，加密代码，请勿使用！

### 本地环境

#### 1. 拉库
```bash
git clone https://github.com/BeHalcyon/fisher_script.git
```

#### 2. 项目根目录下创建fisher_configure.json文件，模板：
```json
{
  "interface":{
    "JDLITE_LOG_API": "http://x.x.x.x:5889/log",
    "JD_SIGN_API": "http://x.x.x.x:x/x",
    "JD_SIGN_API_TOKEN": ""
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
  "cookies": {
    "ws_cookies": [
      "pin=xxxxxxxx;wskey=xxxxxxxxxxxxxx;unionwsws=xxxxxxxxxxxxxxxxxx;",
      "pin=xxxxxxxx;wskey=xxxxxxxxxxxxxx;unionwsws=xxxxxxxxxxxxxxxxxx;",
      "pin=xxxxxxxx;wskey=xxxxxxxxxxxxxx;unionwsws=xxxxxxxxxxxxxxxxxx;",
      "pin=xxxxxxxx;wskey=xxxxxxxxxxxxxx;unionwsws=xxxxxxxxxxxxxxxxxx;"
    ],
    "plus_cookies": [
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;"
    ],
    "test_cookies": [
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;"
    ],
    "cookies": [
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;",
      "pt_key=xxxxxxxxxxx;pt_pin=xxxxxxxxxxxx;"
    ]
  }
}
```

#### 3. 参数介绍

```python
ExchangeManagement(
                 url="", # 必须：包含functionId及相关内容的url；字符串类型
                 headers={}, # 可选：请求头，不包含cookie及content-length；字典类型
                 headers_user_agent_random_flag=True, # 必须：请求头中的user-agent是否随机；Boolean类型
                 user_agent="", # 可选：当headers_user_agent_random_flag为False时有效，用于设定固定user-agent；字符串类型
                 body_dict={}, # 可选：请求体，包含"body"、"args"等关键字；字典类型
                 batch_size=6, # 必须：周期内首批需要运行的账号数，所有batch_size内账号全部抢到后，才开始考虑其他账号；整型
                 other_batch_size=4, # 可选：周期内次批一次性需要运行的账号数；整型
                 second_ahead=0.3, # 必须：线程启动的提前秒数，线程的冷冻时间；例如提前0.40s准备启动线程，依赖于设备资源；浮点类型
                 sleep_time=0.03, # 必须：每个线程的等待时间，每次post的等待时间，依赖于网络传输速率；浮点类型
                 thread_number=12, # 必须：线程数量，post次数，可根据thread_number*sleep_time粗略计算当场运行时间
                 append_flag=True, # 可选：batch_size内权重最高的账号是否增加一次机会；Boolean类型
                 log_flag=False, # 必须：是否需要log，为True时默认极速版；Boolean类型
                 sign_flag=False, # 必须：是否需要sign，为True时默认点点券；Boolean类型
                 day_or_week='day', # 必须：周期为day或week；字符串类型
                 post_flag=True, # 必须：是否为post类型的request；Boolean类型
                 print_type="one of [cmd, file], default to cmd", # 可选：日志为直接输出或文件类型输出；字符串类型
                 coupon_type="", # 必须：券名
                 cookie_type="one of [wskey, test, cookie, plus]", # 必须：测试时选择test，部署时选择cookie；字符串类型
                 ). \
executeInDesktop(clock_list=[0, 10, 14, 20, 22], # 定时任务；
                 debug_flag=False # 是否需要调试，为False时为部署（整点运行），为True时为调试（下一分钟运行）；Boolean类型
                )
```
#### 4. 在青龙运行（尚未完善）
```python
ExchangeManagement(...).executeInQingLong()
```