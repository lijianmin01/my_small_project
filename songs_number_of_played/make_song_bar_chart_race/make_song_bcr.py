import pandas as pd
import bar_chart_race as bcr

df = pd.read_csv('../create_finally_date/finnally_table.csv',index_col=0)

bcr.bar_chart_race(df,filename='说唱新时代歌曲播放量排名变化.mp4')