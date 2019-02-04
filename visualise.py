import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def disable_grid_form_axis(axis):
    axis.get_xaxis().set_visible(False)
    axis.get_yaxis().set_visible(False)


def scatter_plot_from_dataframe(dataframe, color_filter, magnitude_amplifier):
    fig, (ax1) = plt.subplots(frameon=False)
    # ax1.grid(color='#cccccc', axis='y')
    grid_color = '#cccccc'
    colors = []
    if color_filter=='album':
        for value in dataframe['album']:
            #jack johnson
            if value == 'BF':
                colors.append('#DBE2EB')
            elif value == 'onandon':
                colors.append('#009B94')
            elif value == 'inbetweendreams':
                colors.append('#EFCE10')
            # avicii
            elif value == 'true':
                colors.append('#0E4691')
            elif value == 'stories':
                colors.append('#DC5463')
            else:
                colors.append('#EABE67')
    elif color_filter=='sentiment':
        for value in dataframe['score']:
            if value < 0:
                colors.append('red')
            elif value > 0:
                colors.append('green')
            else:
                colors.append(grid_color)
    sizes = []
    for size in dataframe['magnitude']:
        sizes.append(size*magnitude_amplifier)
    x_values = dataframe['score']
    ax1.plot([0, 0], [0, max(dataframe['magnitude'])+1], c=grid_color, linewidth=1, zorder=1)
    ax1.scatter(x_values, dataframe['magnitude'], c=colors, s=sizes, alpha=0.5, zorder=2)
    plt.ylabel('magnitude')
    plt.xlabel('sentiment')
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.spines['bottom'].set_color(grid_color)
    ax1.spines['left'].set_color(grid_color)
    ax1.xaxis.label.set_color(grid_color)
    ax1.tick_params(axis='x', colors=grid_color)
    ax1.yaxis.label.set_color(grid_color)
    ax1.tick_params(axis='y', colors=grid_color)
    ax1.set_ylim(ymin=0, ymax=max(dataframe['magnitude'])+(max(dataframe['magnitude'])*0.1))
    ax1.set_xlim(xmin=(max(dataframe['score'])+0.1)*-1, xmax=max(dataframe['score'])+0.1)
    ax1.get_yaxis().set_visible(False)
    ax1.get_yaxis().set_visible(False)
    disable_grid_form_axis(ax1)
    plt.show()


def convert_xlsx_into_dataframe(xlsx_file):
    xls = pd.ExcelFile(xlsx_file)
    df = xls.parse(xls.sheet_names[0])
    return df

scatter_plot_from_dataframe(convert_xlsx_into_dataframe('output/song_sentiment_jj_first_three_discography.xlsx'), 'album', 28)