#!/usr/bin/python3

# *_*coding:utf8 *_*
# @Time : 2020/5/19 16:43
# @Author : FengLin
# @Email : damon__dong@163.com
# @File : Recorder.py

import wave
import time
from pyaudio import PyAudio, paInt16


class Recorder:
    def __init__(self):
        self.chunk = 1024
        self.framerate = 16000  # 采样率
        self.NUM_SAMPLES = 2000  # 采样点
        self.channels = 1  # 一个声道
        self.sampwidth = 2  # 两个字节十六位
        self.TIME = 2  # 条件变量，可以设置定义录音的时间

    def save_wave_file(self, file_name, data):
        wf = wave.open(file_name, 'wb')  # 二进制写入模式
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.sampwidth)  # 两个字节16位
        wf.setframerate(self.framerate)  # 帧速率
        wf.writeframes(b"".join(data))  # 把数据加进去，就会存到硬盘上去wf.writeframes(b"".join(data))
        wf.close()

    def radio(self, file_name):
        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1,
                         rate=self.framerate, input=True,
                         frames_per_buffer=self.NUM_SAMPLES)
        my_buf = []
        count = 0
        # time.sleep(3)
        print('开始录音')

        while count < self.TIME * 13:
            string_audio_data = stream.read(self.NUM_SAMPLES)
            my_buf.append(string_audio_data)
            count += 1
            # print('...')
        self.save_wave_file(file_name, my_buf)
        stream.close()

        print('录音完毕')

    def read_file(self, file_name):
        wf = wave.open(file_name, 'rb')
        p = PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(), rate=wf.getframerate(), output=True, )
        print('开始放音')
        while True:
            data = wf.readframes(self.chunk)
            if data == b'':
                break
            stream.write(data)
            # print('...')
        wf.close()
        stream.close()
        p.terminate()

    def main(self):
        self.radio("record.pcm")
        print('录音完毕')
        self.read_file("record.pcm")
        print('放音完毕')


if __name__ == "__main__":
    run = Recorder()
    run.main()
