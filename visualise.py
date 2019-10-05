import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.path import Path


def disable_grid_form_axis(axis):
    axis.get_xaxis().set_visible(False)
    axis.get_yaxis().set_visible(False)


def scatter_plot_from_dataframe(dataframe, magnitude_amplifier=0, disable_grid=False, album_color='', annotate=''):
    #create figure
    fig, (ax1) = plt.subplots(frameon=False)
    grid_color = '#cccccc'

    #set max values for grid based on max values of dataframe
    max_magnitude = max(dataframe['magnitude']) + 1
    max_value = min(dataframe['score']) * -1
    if max(dataframe['score']) > max_value:
        max_value = max(dataframe['score'])
    max_value = max_value + 0.1

    #set colors for scatter plot
    colors = []
    if album_color=='':
        for value in dataframe['score']:
            if value < 0:
                colors.append('red')
            elif value > 0:
                colors.append('green')
            else:
                colors.append(grid_color)
    else:
        colors.append(album_color)

    #define sizes of each dot
    sizes = []
    if magnitude_amplifier == 0:
        sizes = 28
    else:
        for size in dataframe['magnitude']:
            sizes.append(size*magnitude_amplifier)

    #plot the data
    x_values = dataframe['score']
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
    ax1.set_ylim(ymin=0, ymax=max_magnitude)
    ax1.set_xlim(xmin=max_value*-1, xmax=max_value)

    #disable grid if passed
    if disable_grid:
        ax1.get_yaxis().set_visible(False)
        ax1.get_yaxis().set_visible(False)
        disable_grid_form_axis(ax1)
    else:
        ax1.plot([0, 0], [0, max_magnitude], c=grid_color, linewidth=1, zorder=1)

    #annotate songs if passed
    if annotate == 'title' or annotate == 'index':
        for i, txt in enumerate(dataframe['title']):
            annotate_label = txt
            annotate_x = dataframe['score'][i]
            if annotate == 'index':
                annotate_label = str(i+1)
                annotate_x = dataframe['score'][i]+0.02
            # ax1.annotate(str(i+1) + ': ' + txt, (dataframe['score'][i], dataframe['magnitude'][i]+0.2), size=6, va='center', ha='center')
            ax1.annotate(annotate_label, (annotate_x, dataframe['magnitude'][i]), size=6, va='center', ha='center')

    plt.show()


def plot_path_from_dataframe(dataframe, line_type='curved', disable_grids=True, show_dots=False):
    x_values = dataframe['score']
    y_values = dataframe['magnitude']
    verts = []
    codes = []
    for i, item in enumerate(x_values):
        verts.append((item, y_values[i]))
        if i == 0:
            codes.append(Path.MOVETO)
        elif i >= len(x_values) - 1:
            codes.append(Path.LINETO)
        else:
            if line_type == 'straight':
                codes.append(Path.LINETO)
            else:
                codes.append(Path.CURVE4)

    path = Path(verts, codes)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    if show_dots:
        ax.scatter(x_values, y_values, c='#111111', s=25, alpha=0.5, zorder=2)
        for i, txt in enumerate(dataframe['title']):
            ax.annotate(str(i + 1), (dataframe['score'][i] + 0.02, dataframe['magnitude'][i]), size=6, va='center', ha='center')


    patch = mpatches.PathPatch(path, facecolor='none', lw=2, edgecolor='black')
    ax.add_patch(patch)

    graph_correction = 0.04
    ax.set_xlim(min(x_values)-graph_correction, max(x_values)+graph_correction)
    ax.set_ylim(min(y_values)-graph_correction, max(y_values)+graph_correction)
    if disable_grids:
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.axis('off')

    plt.show()


def convert_xlsx_into_dataframe(xlsx_file):
    xls = pd.ExcelFile(xlsx_file)
    df = xls.parse(xls.sheet_names[0])
    print(df)
    df = df.sort_values(by='index')
    df = df.reset_index()
    return df

