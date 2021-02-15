
import pandas as pd
import bar_chart_race as bcr

df = pd.read_csv('date.csv',index_col=0)

print(df)
#print(df)
# bcr.bar_chart_race(
#     # 传入的数据必须是pandas.DataFrame 格式
#     df=df,
#     # 方向
#     orientation='h',
#     # 排序
#     sort='desc', # 排序
#     n_bars=6, # 限制条形图数量
#     fixed_order=False,  # 固定标签
#     fixed_max=True, # 固定轴的最大值
#     steps_per_period=10,   # 帧数设置
#     interpolate_period=False,  # 插入时间
#     # label_bars=True,   # 是否有label
#     bar_size=.95,   # 设置bar宽度 取值 0~1 之间；
#     period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
#     # period_fmt='%B %d, %Y',  # 日期的格式设置
#     period_summary_func=lambda v, r: {'x': .99, 'y': .18,
#                                       's': r'Total weigth: {v.sum():,.0f}',
#                                       'ha': 'right', 'size': 8, 'family': 'Courier New'},
#     perpendicular_bar_func='median',
#     period_length=500,
#     # figsize=(5, 3),
#     # dpi=144,
#     # cmap='dark12',
#     title='COVID-19 Deaths by Country',
#     # title_size='',
#     # bar_label_size=7,
#     # tick_label_size=7,
#     shared_fontdict={'family' : 'DejaVu Sans', 'color' : '.1'},
#     scale='linear',
#     writer=None,
#     fig=None,
#     bar_kwargs={'alpha': .7},
#     filter_column_colors=False
# )

bcr.bar_chart_race(df,filename='动态条形图.mp4')