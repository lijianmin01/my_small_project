import pandas as pd
import numpy as np

# 日期从字符串 转成日期格式
import datetime


def t_datetime(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d")


# 计算两个日期之间相隔的天数
def get_day_nums(begin_date, end_date):
    begin_date = datetime.datetime.strptime(begin_date, "%Y/%m/%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    # 最后一天也算数
    return int((end_date - begin_date).days) + 1

#获取两个日期间的所有日期
import datetime
def getEveryDay(begin_date,end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list

date_list = getEveryDay('2020-08-22','2021-02-14')

# 制作最后的总表
fin_table = []
# 添加日期
fin_table.append(date_list)

df = pd.read_csv("song_playtimes.csv")
print(df)



playtime = list(df['playtime'].values)
date = list(df['date'].values)
song = list(df['song'].values)
song.insert(0,'date')

for i in range(len(date)):
    # 获取播放日期与今天的日期相差天数
    after_days = get_day_nums(date[i], '2021-02-14')
    # 每次累加的天数
    ## 估计每天增长的天数是一样的
    plus_num = int(playtime[i] / after_days)
    # 根据总表的数据添加数据
    every_song_date_cnt = []
    # 该歌曲是否已经被播放
    flag = 0
    play_sum = 0
    for every_date_index in range(len(date_list)):
        if (flag == 0):
            # 是否到播出日期
            ## datetime.datetime.strptime(begin_date, "%Y/%m/%d")
            ### if(t_datetime(date_list[every_date_index])>=date[i]):
            if (t_datetime(date_list[every_date_index]) >= datetime.datetime.strptime(date[i], "%Y/%m/%d")):
                flag = 1
                play_sum += plus_num
                every_song_date_cnt.append(play_sum)
            else:
                every_song_date_cnt.append(0)
        else:
            play_sum += plus_num
            every_song_date_cnt.append(play_sum)

    # 将该歌曲播放变化量写入总表
    fin_table.append(every_song_date_cnt)

fin_table = np.array(fin_table).T

fin_table = pd.DataFrame(fin_table, columns=song)

fin_table.to_csv("finnally_table02.csv", index=0)
