from visualise import scatter_plot_from_dataframe, plot_path_from_dataframe, convert_xlsx_into_dataframe
from analyse import analyse_files_and_store_in_excel

analyse_files_and_store_in_excel('songs/Avicii', 'avicii-tim-test')

df = convert_xlsx_into_dataframe('output/song_sentiment_avicii-tim-test.xlsx')

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
  disable_grids=True,
  line_type='c',
  line_color='black',
  emogrid=False,
)
