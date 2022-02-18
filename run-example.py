from visualise_sentiment import VisualiseSentiment
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('output/avicii tim.csv').sort_values(by='index')

    viz_buddy = VisualiseSentiment(
        dataframe=df,
        show_grid=False,
        annotate='index',
        # save='visuals/example.png'
    )

    viz_buddy.set_scatter_options(
        dot_color='#f0123a',
        dot_fill=False,
        dot_amplifier=25,
    )
    viz_buddy.scatter_plot()

    viz_buddy.set_path_options(
        colors=['#ff0000', '#000000'],
        styles=['--', '-'],
        widths=[1, 2],
        types=['', 'bezier'],
        # length=99,
        # dot_colours='#ff0000',
    )
    viz_buddy.path_plot()

    viz_buddy.set_path_options(
        colors=['#000000'],
        styles=['-'],
        widths=[1],
        types=[''],
        dot_colours='none',
    )

    viz_buddy.web_plot()
