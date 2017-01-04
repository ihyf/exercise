# coding:utf-8
# 引入库
import pyaudio
import wave

# 定义数据流块
chunk = 1024

# 只读方式打开wav文件
f = wave.open(r"/Users/00301953/Desktop/hyf/资料/树莓派/请先扫描销售订单条形码.wav", "rb")

p = pyaudio.PyAudio()

# 打开数据流
stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                channels=f.getnchannels(),
                rate=f.getframerate(),
                output=True)

# 读取数据
data = f.readframes(chunk)

# 播放
while data != "":
    stream.write(data)
    data = f.readframes(chunk)

    # 停止数据流
stream.stop_stream()
stream.close()

# 关闭 PyAudi


