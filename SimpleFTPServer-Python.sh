#!/bin/bash
pip install pyftpdlib
python -m pyftpdlib
# ftp://127.0.0.1:2121
# -i 指定 IP 地址（默认为本机的 IP 地址）
# -p 指定端口（默认为2121）
# -w 写权限（默认为只读）
# -d 指定目录 （默认为当前目录）
# -u 指定用户名登录
# -P 设置登录密码
# python -m pyftpdlib -u admin -P admin -p 21
