from aip import AipSpeech


class VoiceRecognition:
    def __init__(self):
        # https://cloud.baidu.com/doc/SPEECH/s/1k4o0bmc7
        """ 你的 APPID APPID SK """
        self.APP_ID = '你的APPID'
        self.API_KEY = '你的APPID'
        self.SECRET_KEY = '你的SK'

        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    # 读取文件
    def get_file_content(self, filepath):
        with open(filepath, 'rb') as fp:
            return fp.read()

    # 识别本地文件
    def get_text_from_voice(self, file_name):
        ret = self.client.asr(self.get_file_content(file_name), file_name.split(".")[-1], 16000, {
            'dev_pid': 1537,
        })

        return ret.get("result")[0] if ret["err_no"] == 0 else ""


if __name__ == '__main__':
    run = VoiceRecognition()
    result = run.get_text_from_voice("record.pcm")
    print(result)
