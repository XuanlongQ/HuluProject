"""
@author: zhangjun.xue
@time: 2020/3/30 14:20
@file: threading_queue.py.py
@desc: 多线程去消费一个队列的例子
"""
 
import threading
import time
import queue
 
 
# 下面来通过多线程来处理Queue里面的任务：
def work(q):
    while True:
        if q.empty():
            return
        else:
            t = q.get()
            print("当前线程sleep {} 秒".format(t))
            time.sleep(1)
 
 
def main():
    q = queue.Queue()
    for i in range(10):
        q.put(i)  # 往队列里生成消息
    # 单线程
    # work(q)
 
    # 多线程
    thread_num = 20
    threads = []
    for i in range(thread_num):
        t = threading.Thread(target=work, args=(q,))
        # args需要输出的是一个元组，如果只有一个参数，后面加，表示元组，否则会报错
        threads.append(t)
 
    for i in range(thread_num):
        threads[i].start()
    for i in range(thread_num):
        threads[i].join()
 
 
if __name__ == "__main__":
    start = time.time()
    main()
    print('耗时：', time.time() - start)