import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.path import Path


def annotate_axis_with_labels_by_x_values_y_values(annotate, axis, labels, x_values, y_values):
    for i, txt in enumerate(labels):
        annotate_label = txt
        annotate_x = x_values[i] + .02
        annotate_y = y_values[i]

        if annotate == 'index':
            annotate_label = str(i + 1)
        if annotate == 'index title':
            annotate_label = str(i + 1) + ': ' + annotate_label

        axis.annotate(annotate_label, (annotate_x, annotate_y), size=6, va='center', ha='left')


class VisualiseSentiment():
    """Class to visualise sentiment data from Google's Natural Language API"""

    def __init__(self, dataframe, show_grid, annotate='', save=''):
        """Initialise attributes for plots"""
        # generic plot options
        self.dataframe = dataframe
        self.show_grid = show_grid
        self.annotate = annotate
        self.save = save
        # default scatter settings
        self.scatter_dot_color = 'sentiment'
        self.scatter_dot_fill = True
        self.scatter_dot_amplifier = 0
        # default path settings
        self.path_colors = ['black']
        self.path_styles = ['-']
        self.path_widths = [2]
        self.path_types = ['bezier']
        self.path_length = 99
        self.path_dot_colours = '#111111'

    def set_scatter_options(self, dot_color='', dot_fill='', dot_amplifier=''):
        """Change options for scatter plot"""
        if dot_color != '':
            self.scatter_dot_color = dot_color
        if dot_fill != '':
            self.scatter_dot_fill = dot_fill
        if dot_amplifier != '':
            self.scatter_dot_amplifier = dot_amplifier

    def scatter_plot(self):
        """Plot sentiment data by score and magnitude in a scatter plot"""
        x_values = self.dataframe['score']
        y_values = self.dataframe['magnitude']
        fig = plt.figure()
        ax = fig.add_subplot(111)
        grid_color = '#aaaaaa'

        # set max values for grid based on max values of dataframe
        max_y = max(y_values) + 1
        max_x = min(x_values) * -1
        if max(x_values) > max_x:
            max_x = max(self.dataframe['score'])
        max_x = max_x + 0.1

        # set colors for scatter plot
        colors = []
        if self.scatter_dot_color == 'sentiment':
            for value in self.dataframe['score']:
                if value < 0:
                    colors.append('red')
                elif value > 0:
                    colors.append('green')
                else:
                    colors.append(grid_color)
        else:
            colors.append(self.scatter_dot_color)

        # define sizes of each dot
        sizes = []
        if self.scatter_dot_amplifier == 0:
            sizes = 28
        else:
            for size in self.dataframe['magnitude']:
                sizes.append(size * self.scatter_dot_amplifier)

        # plot the data
        if self.scatter_dot_fill:
            ax.scatter(x_values, y_values, c=colors, s=sizes, alpha=.7, zorder=2)
        else:
            ax.scatter(x_values, y_values, facecolor='none', edgecolor=colors, s=sizes, alpha=1, zorder=2)

        # hide spines
        for spine in ax.spines:
            ax.spines[spine].set_visible(False)

        # disable grid if passed
        if self.show_grid:
            plt.ylabel('magnitude')
            plt.xlabel('sentiment')
            ax.xaxis.label.set_color(grid_color)
            ax.tick_params(axis='x', colors=grid_color)
            ax.yaxis.label.set_color(grid_color)
            ax.tick_params(axis='y', colors=grid_color)
            ax.set_ylim(ymin=0, ymax=max_y)
            ax.set_xlim(xmin=max_x * -1, xmax=max_x)
            ax.plot([0, 0], [0, max_y], c=grid_color, linewidth=1, zorder=1)
        else:
            ax.get_yaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            ax.axis('off')

        # annotate songs if passed
        if self.annotate in ['title', 'index', 'index title']:
            annotate_axis_with_labels_by_x_values_y_values(
                axis=ax,
                annotate=self.annotate,
                labels=self.dataframe['title'],
                x_values=x_values,
                y_values=y_values,
            )

        # save or show plot
        if self.save:
            plt.savefig(self.save, transparent=True)
            plt.close()
        else:
            plt.show()

    def set_path_options(self, colors='', styles='', widths='', types='', length='', dot_colours=''):
        """Change options for path plot(s)"""
        if colors != '':
            self.path_colors = colors
        if styles != '':
            self.path_styles = styles
        if widths != '':
            self.path_widths = widths
        if types != '':
            self.path_types = types
        if length != '':
            self.path_length = length
        if dot_colours != '':
            self.path_dot_colours = dot_colours

    def path_plot(self):
        """Plot sentiment data by score and magnitude as one or multiple paths"""
        x_values = self.dataframe['score']
        y_values = self.dataframe['magnitude']
        fig = plt.figure()
        ax = fig.add_subplot(111)

        # plot dots
        if self.path_dot_colours != 'none':
            ax.scatter(x_values, y_values, c=self.path_dot_colours, s=25, alpha=1, zorder=4)
            annotate_axis_with_labels_by_x_values_y_values(
                axis=ax,
                annotate=self.annotate,
                labels=self.dataframe['title'],
                x_values=x_values,
                y_values=y_values,
            )

        # draw paths
        for index, path_type in enumerate(self.path_types):
            verts = []
            codes = []
            for i, item in enumerate(x_values):
                if i <= self.path_length:
                    vert_x = item
                    vert_y = y_values[i]
                    verts.append((vert_x, vert_y))
                    if i == 0:
                        codes.append(Path.MOVETO)
                    elif i >= len(x_values) - 1:
                        codes.append(Path.LINETO)
                    else:
                        if path_type == 'bezier':
                            codes.append(Path.CURVE4)
                        else:
                            codes.append(Path.LINETO)

            path = Path(verts, codes)
            patch = mpatches.PathPatch(path, facecolor='none', lw=self.path_widths[index], linestyle=self.path_styles[index],
                                       edgecolor=self.path_colors[index], zorder=3)
            ax.add_patch(patch)

        # adjust x and y limits
        graph_correction_x = 0.1
        graph_correction_y = 0.5
        ax.set_xlim(min(x_values) - graph_correction_x, max(x_values) + graph_correction_x)
        ax.set_ylim(min(y_values) - graph_correction_y, max(y_values) + graph_correction_y)

        # hide grid
        if not self.show_grid:
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            ax.axis('off')

        # save or show plot
        if self.save:
            plt.savefig(self.save, transparent=True)
            plt.close()
        else:
            plt.show()


