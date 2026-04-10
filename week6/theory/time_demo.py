import datetime

def time_demo():
    now = datetime.datetime.now()
    # 时间戳
    print(now.timestamp())
    # print(now)
    # print(now.year)
    # print(now.month)
    # print(now.day)
    # print(now.hour)
    # print(now.minute)
    # print(now.second)
    # print(now.microsecond)
    #
    print(now.strftime("%y-%m-%d %H:%M:%S"))
    print(now.strftime("%Y-%m-%d %H:%M:%S %p"))


# time_demo()


from datetime import datetime
stamp=datetime(2019,6,4)
print(str(stamp))
#
# import pandas as pd
#
# # 不同频率的Period示例
# freqs = ['D', 'M', 'Q', 'A-DEC', 'H', '2D', 'W-FRI']
# for freq in freqs:
#     p = pd.Period('2019-01-01', freq=freq)
#     print(f'{freq:8s} -> {p}')
