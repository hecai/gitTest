import configparser
import os

config = configparser.ConfigParser()  # 拿到一个配置对象
parent_dir = os.path.dirname(os.path.abspath(__file__))
config.read(parent_dir + "/config.txt")
# config.read('config.txt', encoding='utf-8')  # 读取配置文件，注意编码
print(config.sections())  # 再次打印sections，可以看到有结果
host = config.get("email", "MAILHOST")
user = config.get("email", "MAILUSER")
pwd = config.get("email", "MAILPWD")

print(host)
print(user)
print(pwd)
