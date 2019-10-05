# Visualisation of the sentiment of music lyrics in Python

You can use this project to visualise sentiment data of music lyrics. It only includes the technical details. [Read the origin stor]([http://www.edriessen.com/avicii/)  to find out why I created it.

# Create a datviz of the lyrics your favourite artist

Good to see that you want to visualise the lyrics of one of your favourite artists (or just want to know more about this repository). The process is split into two parts:

1. Analyse the song texts.
2. Plot the sentiment data.

I'll use Avicii's posthumous album TIM as an example in this readme. Let's dig in.

# 1. Analyse the songtexts

To run an analysis, you'll need a connection to the Google Cloud Natural Language API. Set up a project in the Google Cloud console and add your `credentials.json` to the project root folder. After that, you'll need a `.txt` file for each song that you want to analyse. Format each song file this way: `songindex_albumname_songindex_songtitle.txt`. For the song Peace of Mind by Avicii, the first song on the album TIM, this would be: `1_tim_peace-of-mind.txt`. I store the textfiles of the albums I generate inside a `songs` folder in my project. 

When you have the files ready, you can use `analyse.py` to run the sentiment analysis. In this file, you call `save_array_of_dicts_to_excel()`. The function takes two arguments:

- Array of dicts (the songs). Use the `get_song_sentiment('songs/avicii_tim')` function to generate this list. Refer to the correct path location of your songs. In my example, the text files are located in `songs/avicii_tim`.
- Name extension of Excel file. The function will save the file to the `output/` folder. The file name will be `song_sentiment_your_extension.xlsx`.

A full example looks like this:

`save_array_of_dicts_to_excel(get_song_sentiment('songs/avicii_tim'), 'avicii_tim' )`

# 2. Visualise the sentiment data

You can visualise the data with the functions in `visualise.py` . There are two types of visualisations:

- Scatterplot - `scatter_plot_from_dataframe`
- Line plot - `plot_path_from_dataframe`

They both have a unique way of visualising the data. I'll give a basic and advanced example of both. 

## The scatterplot of your favourite music

```
scatter_plot_from_dataframe(
    dataframe=tim_df,
    magnitude_amplifier=28,
)
```

//sample image

```
scatter_plot_from_dataframe(
    dataframe=tim_df,
    magnitude_amplifier=0,
    album_color='purple',
    annotate='index',
    disable_grid=True,
)
```

## The line path of your favourite music

This one feels magical to me. Using the paths from Matplotlib, you can draw an organic looking line. It's drawn from one song to the next based on the index on the album. 

```
plot_path_from_dataframe(
    dataframe=tim_df
)
```

//sample image

```
plot_path_from_dataframe(
    dataframe=tim_df,
    show_dots=True,
    disable_grids=False,
    line_type='straight',
)

```
# To do

The project is currently in a rough state. Things I'll be working on are:

- Store data in csv instead of excel.
