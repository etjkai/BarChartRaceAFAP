import pandas as pd
import bar_chart_race as bcr

df = pd.read_excel("Output Data Prep_BU.xlsx", index_col=0)
df.index = pd.to_datetime(df.index)

bcr.bar_chart_race(
    df=df,
    filename='AFAP Savings Journey (BU) v2.mp4',
    orientation='h',
    sort='desc',
    n_bars=6,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=15,
    interpolate_period=True,
    label_bars=True,
    bar_size=.80,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%d %b %y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .15,
                                      's': f'Total: {v.nlargest(6).sum():,.0f}',
                                      'ha': 'right', 'size': 8, 'family': 'Courier New'},
    # perpendicular_bar_func='median',
    period_length=375,
    figsize=(4.5, 2.7),
    dpi=288,
    cmap='set3',
    title='AFAP Savings (BU) FY20',
    title_size='',
    bar_label_size=7,
    tick_label_size=5,
    shared_fontdict={'family' : 'Helvetica', 'color' : '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False)  