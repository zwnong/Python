# coding = utf-8
# 线程
import threading


def sum(a):
    print(a + 1)


threads = []
for i in range(3):
    # print(i)
    # 创建线程
    t = threading.Thread(target=sum, args=(i,))
    # 添加到list
    threads.append(t)
for j in threads:
    j.start()
