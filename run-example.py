from visualise import scatter_plot_from_dataframe, plot_path_from_dataframe
from analyse import analyse_files_and_store_in_csv
import pandas as pd

# analyse_files_and_store_in_csv('songs/avicii tim', 'avicii tim')
df = pd.read_csv('output/avicii tim.csv').sort_values(by='index').reset_index()

scatter_plot_from_dataframe(
    dataframe=df,
    magnitude_amplifier=0,
    disable_grid=False,
    annotate='index',
    album_color=''
)

plot_path_from_dataframe(
  dataframe=df,
  show_dots=True,
  disable_grids=False,
  line_type='c',
  line_color='black',
  emogrid=True,
)
