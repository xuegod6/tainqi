# Django开发环境python3版
postgresql-dev \ alpine集成pg
alpine-sdk \  alpine的pandas支持
## 启动
```
# make run
```
## 停止
```
# make stop
```

# 目录
```
.
├── Makefile  #启动器
├── README.md  
├── app       #后台
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── src
│   │   ├── xuegod
│   │   ├── test.log
│   └── uwsgi.ini
│   └── run.sh
├── docker-compose.yml
└── nginx    #前端
    ├── Dockerfile
    └── nginx.conf
```
