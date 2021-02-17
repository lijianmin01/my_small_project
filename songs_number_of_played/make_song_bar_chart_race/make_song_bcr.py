import pandas as pd
from numpy import mean
import bar_chart_race as bcr


df = pd.read_csv('../create_finally_date/finnally_table02.csv',index_col=0)



# 自定义bar  前10 播放量的平均值
def func(values, ranks):
    values = list(values)
    # 降序
    return int(mean(sorted(values,reverse=True)[:10]))

bcr.bar_chart_race(df,title='说唱新时代歌曲播放量前十名变化情况',n_bars=10,bar_size=0.86,filter_column_colors=True,perpendicular_bar_func=func,filename='说唱新时代歌曲播放量排名变化02.mp4')



