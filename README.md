# Sentiment plot of music albums


# Analysing your favourite artist

Plotting the sentiment of the songs of one of your favourite artists takes two steps:

1. Analyse the song texts.
2. Plot the sentiment data.

Let's dig in.

# 1. Analyse the songtexts

To run an analysis, you'll need a connection to the Google Cloud Natural Language API. Set up a project in the Google Cloud console and add your `credentials.json` to the project root folder. After that, you'll need a `.txt` file for each song that you want to analyse. Format each song file this way: `albumname_songtitle.txt`. For the song Wake Me Up by Avicii, this would be: `true_wakemeup.txt`. When you have the files ready, you can use `analyse.py` to run the sentiment analysis. You can call `save_array_of_dicts_to_excel()`. The function takes two arguments:

- Array of dicts (the songs). Use the `get_song_sentiment('songs/avicii')` function to generate this list. Refer to the correct path location of your songs. In my example, the path is `songs/avicii`.
- Name extension of Excel file. The function will save the file to the `output/` folder. The file name will be `song_sentiment_your_extension.xlsx`.


`save_array_of_dicts_to_excel(get_song_sentiment('songs/avicii'), 'avicii_discography' )`

# 2. Plot the sentiment data

You can visualise the data from the `visualise.py` file. You can call the `scatter_plot_from_datafrome` function. It takes three arguments:


Here's a full example:

`scatter_plot_from_dataframe(convert_xlsx_into_dataframe('output/song_sentiment_jj_first_three_discography.xlsx'), 'album', 28)`

### Using custom album colours.

<<<<<<< HEAD
When you set the colour type to `'album'`, you'll need to pass the album colors into the `scatter_plot_from_dataframe` function. Set the album colours in a dictionary where the key is the album name and the value is the HEX colour. Here's the dictionary I used for Avicii's album:
=======
When you set the colour type to `'album'`, you'll need to modify a part of the `visualise.py` file. Look for the part that says `if color_filter=='album'`. Modify the values inside the if statement to match your album names and colours of choice. Here's the example I used for Avicii's albums:
>>>>>>> d4753aaab78dc3ee78638eedcfbb4a3224aa8fba

```
{
    'true': '#0E4691',
    'stories': '#DC5463',
    'avicii': '#EABE67',
}
```

# Preparing a plot for print

Making your plot ready for print is easy. Simply save it as an `.eps` file. Open it in your editor of choice and remove all the unwanted elements (e.g. the graph elements and white background). After that, save it in your format of choice.

# To do

The project is currently in a rough state. Things I'll be working on are:

- Updating the project code to make it easier to use.
- Make it easier to prepare a plot for print.
