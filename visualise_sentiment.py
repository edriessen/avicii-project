import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.path import Path
# import matplotlib.patheffects as pe


class VisualiseSentiment():
    """Class to visualise sentiment data from Google's Natural Language API"""

    def __init__(self, dataframe, show_grid, annotate='', save=''):
        """Initialise attributes for plots"""
        # generic plot options
        self.dataframe = dataframe
        self.x_values = dataframe['score']
        self.y_values = dataframe['magnitude']

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

        self.path_dot_colors = '#111111'
        self.figsize = [6.4, 4.8]
        self.path_close = False
        self.path_capstyle = 'butt'
        self.path_joinstyle = 'miter'

        self.bg_shape_marker = ''
        self.path_bg_shape_size = 40000
        self.path_bg_shape_color = '#F2E8DC'

    def annotate_axis_with_labels(
            self,
            annotate,
            axis,
            labels,
    ):
        for i, txt in enumerate(labels):
            annotate_label = txt
            annotate_x = self.x_values[i] + .02
            annotate_y = self.y_values[i]

            if annotate == 'index':
                annotate_label = str(i + 1)
            if annotate == 'index title':
                annotate_label = str(i + 1) + ': ' + annotate_label

            axis.annotate(annotate_label, (annotate_x, annotate_y), color='#cccccc',
                          size=6, va='center', ha='left')

    def scatter_plot(self):
        """Plot sentiment data by score and magnitude in a scatter plot"""
        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(111)
        grid_color = '#aaaaaa'

        # set max values for grid based on max values of dataframe
        max_y = max(self.y_values) + 1
        max_x = min(self.x_values) * -1
        if max(self.x_values) > max_x:
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
            ax.scatter(self.x_values, self.y_values, c=colors, s=sizes, alpha=.7, zorder=2)
        else:
            ax.scatter(self.x_values, self.y_values, facecolor='none', edgecolor=colors, s=sizes, alpha=1, zorder=2)

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
            self.annotate_axis_with_labels(
                axis=ax,
                annotate=self.annotate,
                labels=self.dataframe['title'],
            )

        # save or show plot
        if self.save:
            plt.savefig(self.save, transparent=True)
            plt.close()
        else:
            plt.show()

    def path_plot(self):
        """Plot sentiment data by score and magnitude as one or multiple paths"""
        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(111)

        # plot dots
        if self.path_dot_colors != 'none':
            ax.scatter(self.x_values, self.y_values, c=self.path_dot_colors, s=25, alpha=1, zorder=4)
            self.annotate_axis_with_labels(
                axis=ax,
                annotate=self.annotate,
                labels=self.dataframe['title'],
            )

        # draw paths
        for index, path_type in enumerate(self.path_types):
            verts = []
            codes = []
            for i, item in enumerate(self.x_values):
                if i <= self.path_length:
                    vert_x = item
                    vert_y = self.y_values[i]
                    verts.append((vert_x, vert_y))
                    if i == 0:
                        codes.append(Path.MOVETO)
                    elif i >= len(self.x_values) - 1:
                        codes.append(Path.LINETO)
                    else:
                        if path_type == 'bezier':
                            codes.append(Path.CURVE4)
                        else:
                            codes.append(Path.LINETO)

            if self.path_close:
                verts.append((0,0))
                codes.append(Path.CLOSEPOLY)

            path = Path(verts, codes)

            # https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
            patch = mpatches.PathPatch(
                path,
                facecolor='none',
                lw=self.path_widths[index],
                linestyle=self.path_styles[index],
                edgecolor=self.path_colors[index],
                zorder=3,
                capstyle=self.path_capstyle,
                joinstyle=self.path_joinstyle,
            )

            ax.add_patch(patch)

        if self.bg_shape_marker:
            ax.scatter(
                [0],
                [self.y_values.mean()],
                color=self.path_bg_shape_color,
                edgecolor=self.path_colors[0],
                linewidth=1,
                zorder=2,
                s=self.path_bg_shape_size,
                marker=self.bg_shape_marker
            )

        graph_correction_x = 0.1
        graph_correction_y = 0.1
        ax.set_xlim(min(self.x_values) - graph_correction_x, max(self.x_values) + graph_correction_x)
        ax.set_xlim(-1 - graph_correction_x, 1 + graph_correction_x)
        ax.set_ylim(min(self.y_values) - graph_correction_y, max(self.y_values) + graph_correction_y)

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

    def web_plot(self, line_width_value=''):
        """Plot sentiment data by score and magnitude as web of paths"""
        x_values = self.dataframe['score']
        y_values = self.dataframe['magnitude']
        fig = plt.figure()
        ax = fig.add_subplot(111)

        # plot dots
        if self.path_dot_colors != 'none':
            ax.scatter(x_values, y_values, c=self.path_dot_colors, s=25, alpha=1, zorder=4)
            self.annotate_axis_with_labels(
                axis=ax,
                annotate=self.annotate,
                labels=self.dataframe['title'],
            )

        # draw web
        active_nodes = []

        for index, x_value in enumerate(x_values):
            for index2, x_value2 in enumerate(x_values):
                if index != index2:
                    if sorted((index, index2)) not in active_nodes:
                        verts = []
                        codes = []
                        verts.append((x_value, y_values[index]))
                        codes.append(Path.MOVETO)
                        verts.append((x_value2, y_values[index2]))
                        codes.append(Path.LINETO)
                        active_nodes.append(sorted((index, index2)))

                        line_width = .5
                        if line_width_value in ['score', 'magnitude']:
                            line_width = (abs(self.dataframe[line_width_value][index] - self.dataframe[line_width_value][index2]))

                        path = Path(verts, codes)

                        patch = mpatches.PathPatch(path, facecolor='none', lw=line_width*3, linestyle=self.path_styles[0],
                                                   edgecolor=self.path_colors[0], zorder=3)
                        ax.add_patch(patch)

        # adjust x and y limits
        graph_correction_x = 0.1
        graph_correction_y = 0.1
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




