# -*- coding=utf8 -*-

DICT__NTGJ_HTTP_SERVER = {"IP": "ceshi.farmfriend.com.cn",
                            "scheme":"http",
                            "HTTP_PORT":"80",
                            "USERNAME": "worker",
                            "PASSWORD": "FarmKeeper@#1001",
                            "DIST_DIR": "/app/tomcatapi/",
                            "START_FILE": "apistart.sh",
                            "STOP_FILE": "apistop.sh",
                            "NOHUP_FILE": "nohup.out"
                        }


DICT__NTGJ_SERVER_DB = {"IP": "10.0.1.5",
                        "PORT": 3306,
                        "USERNAME": "work",
                        "PASSWORD": "srcRwk8WNcZemaSKflE9",
                        "FRAM_DB_NAME": "farmfriend"
                        }



DICT__HTTP_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
                     "Content-Type": 'application/json;charset=UTF-8'

                        }

DICT__SYS_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
                     "Content-Type": 'application/json;charset=UTF-8',
                     "FARMFRIEND_TOKEN":"eyJ1aWQiOiI3NSIsInRva2VuIjoiOWFmOGIxYjAtNmQ2MC00ZTQ2LTgxMGMtMjEyNDVjMjA5ZjcyIn0=",


                        }

DICT__Register_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/4.0'}


# 设置超时时间
TIMEOUT_2s = 2
TIMEOUT_3s = 3
TIMEOUT_5s = 5
TIMEOUT_10s = 10
TIMEOUT_15s = 15
TIMEOUT_20s = 20
TIMEOUT_30s = 30

