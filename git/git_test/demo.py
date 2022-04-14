# coding:utf-8
# 导入模块
import yagmail


def send_msg():
    # 使用yagmail类创建对象（发件人邮箱，发件人授权码，发送人服务器）
    ya_obj = yagmail.SMTP(user="ganchao0314@163.com", password="EOFOWNLZLNCZMWPY", host="smtp.163.com")

    content = "你好！python"
    # 发送邮件（收件人，发送的主题，发送的内容）
    ya_obj.send("842673502@qq.com", "启动成功", content)

#入口
if __name__ == '__main__':
    send_msg()
