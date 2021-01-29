# coding = utf-8
"""
@All-project: Spider
@author: ZWNONG
@file: lesson.py
@time: 2020-07-08 20:19:54
"""
import os
from 语音控制电脑.Recorder import Recorder
from 语音控制电脑.voice_recognition import VoiceRecognition
import subprocess  # 使用Popen

# 语音控制电脑
"""
1、录音 获取音频
2、音频 转换成 文字指令
3、执行
"""
# 指令集
recorder = Recorder()
voice_recognition = VoiceRecognition()
command_list = {
    "打开QQ": r"C:\Program Files (x86)\QQ\Bin\QQ.exe"
}
# 开启录音功能  .pcm 为音频格式
while True:
    recorder.radio('record.pcm')
    # 录音识别
    word = voice_recognition.get_text_from_voice('record.pcm')
    print(word)
    # 推出条件
    if "退出" in word:
        os.kill(os.getpid(), 9)

    for command in command_list:
        print(command)
        if command in word:
            # 执行指令
            excute_command = command_list[command]
            subprocess.Popen(excute_command, shell=True)
            break
