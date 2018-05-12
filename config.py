# coding=utf-8



# tornado 配置
CONFIG = dict(

    log_console=False,
    log_file=True,
    log_level="WARNING",
    login_url = "/login",
    debug = "Ture",
    port = 8888,
    application = None,
)

LOG_CONFIG = dict(
    log_path="logs/log", # 末尾自动添加 @端口号.txt_日期
    when="D", # 以什么单位分割文件
    interval=1, # 以上面的时间单位，隔几个单位分割文件
    backupCount=30, # 保留多少历史记录文件
    fmt="%(asctime)s - %(name)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s",
)
