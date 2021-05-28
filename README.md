# The Avicii project: exploring sentiment data using Python

You can use this project to analyse music lyrics (text) for sentiment using Google Natural Language API.
It also allows you to explore the sentiment data using visualisation. 
I personally use the visuals to make my own t-shirts of musics that I like.  [Read the origin story](http://www.edriessen.com/projects/the-avicii-project/) to find out why I created this project.

![avicii project dataviz hero image](sample_dataviz/avicii_tim_plot_hero.PNG)


# Creating a dataviz of the lyrics of your favourite artist

Good to see that you want to give my repository a try. The process is split into three parts:

1. Analyse the song texts
2. Scatter plot visualisation to review the sentiment data
3. Creative path visualisation (data art)

I'll use Avicii's posthumous album TIM as an example in this readme. Let's dig in.

# 1. Analyse the songtexts

To run an analysis, you'll need a connection to the Google Cloud Natural Language API.  Set up a project in the Google Cloud console and add your `credentials.json` to the project root folder. 

After setting it up, you'll need a `.txt` file for each song that you want to analyse. I use https://www.azlyrics.com to get my lyrics. Format each `.txt` file like this: `song index-album name-song title.txt`. 

>  **Example**: For the song Peace of Mind by Avicii, the first song on the album TIM, the file name would be: `1-tim-peace of mind.txt`. 

Store the text files somehwere inside the project folder (the folder `/songs` is listed in the `.gitignore`).  

When you have the files ready, you can use `analyse.py` to run the sentiment analysis and store the results in a csv file. You'll have to provide two arguments:

- path to the folder that contains the text files to analyse, e.g. `songs/avicii tim`.
- name of the csv file that will be stored in the output folder, e.g. `avicii tim`. 

Here's the example listed in `analyse.py`:

```python
if __name__ == '__main__':
    path_to_songs = 'songs/avicii_tim'
    csv_file_name = 'avicii tim'
    analyse_files_and_store_in_csv(path_to_songs, csv_file_name)
```
With the analysis done, you can continue to section 2. 

### Optional: Fetch lyrics automatically from Genius.com
You have the option to fetch the lyrics using the `lyrics.py` file. To use the script, you have to generate an access key on https://genius.com/api-clients. Store the access key in a json file called `credentials-genius.json` with this format:

```
{
  "access-key": "your access key here"
}
```

After that, enter the song titles, artist, and album as appropriate in `lyrics.py`. You will need to create the appropriate folder under the songs folder (for example, for Lady Gaga, you will need to create a `Lady Gaga` folder: `songs/Lady Gaga`). The script will generate the text files and put them in the folder.

_Small changes in the lyrics can impact the visual.
So be sure to check the lyrics when you get them automatically._

# 2. Scatter plot visualisation to review the sentiment data

I've created a class to help you visualise the data. First, we will discuss the scatter plot. A visualisation that helps you explore the sentiment data and get familiar with the results. (You can review `run-example.py` if reading isn't your thing.)

The first thing you'll need to do is load the results from your analysis into a dataframe. And after that, create an instance of the VisualiseSentiment class:

```Python
from visualise_sentiment import VisualiseSentiment

df = pd.read_csv('output/avicii tim.csv').sort_values(by='index')

viz_buddy = VisualiseSentiment(
    dataframe=df,
    show_grid=True,
    annotate='index',
)
```
The class takes four arguments:

- dataframe: the data you want to visualise.
- show_grid: boolean that enables or disables grids in plots.
- annotate (optional): string to set annotation values:
	- `''` for no annotation (default)
	- `'index'` to annotate with the index of the data
	- `'title'` to annotate with the title of the text
	- `'index title'` to annotate with both index and title
- save (optinal): name of the file to save the plot to (e.g. `'example_viz.png'`). Default value is `''` and shows the plot (`plt.show()`).

After creating the instance, you can visualise the results easily using the `scatter_plot()` method. This generates the following results:

![Avicii Time Scatter default](sample_dataviz/example_scatter_default.png)

You can modify some of the scatter plot options using the `set_scatter_options()` method:

```python
viz_buddy.set_scatter_options(
    dot_color='#f0123a',
    dot_fill=False,
    dot_amplifier=25,
)
viz_buddy.scatter_plot()
```
Which results in:

![Avicii Time Scatter custom](sample_dataviz/example_scatter_custom.png)

# 3. Creative path visualisation (data art)

This is where the magic happens. Using paths & patches from Matplotlib, you can draw a line from data point to data point. It creates a sort of abstract 'connect the dots' drawing. 

Using the `plot_path()` method, you get the following result by default:

![Avicii Time Path Basic](sample_dataviz/example_path_default.png)

Let's have a look at a clean version of the plot:

![Avicii Time Path Basic Cleaned](sample_dataviz/example_path_clean.png)

Wow, that is some nice abstract data visualisation right?! :)

There are some some options you can set using the `set_path_options()` method: 

```python
viz_buddy.show_grid = False
viz_buddy.set_path_options(
    colors=['#ff1a55', '#ff1a55'],
    styles=['--', '-'],
    widths=[1, 2],
    types=['', 'bezier'],
    # length=99,
    # dot_colours='#ff0000',
 )
    
 viz_buddy.plot_path()
```

_Make sure the lists you provide for the path options have the same length. You have two options for line types: `'bezier'` draws a bezier curve. Anything else (e.g. `''` draws a straight line._

And again the result:

![Avicii Time Path Custom](sample_dataviz/example_path_custom1.png)

This setup nicely shows both the straight path and the bezier curves that are generated.

Here's another example that plots the same line several times with different colours and widths:

```python
viz_buddy.show_grid = False
viz_buddy.set_path_options(
    colors=['#E6E6E6', '#F2C641', '#E52133', '#A40454', '#02388F', '#ffffff'],
    styles=['-', '-', '-', '-', '-', '-'],
    widths=[38,30,22,14,8,2],
    types=['bezier', 'bezier', 'bezier', 'bezier', 'bezier', 'bezier'],
    length=99,
    dot_colours='none',
)
    
viz_buddy.plot_path()
```
And the image:

![Avicii Time Path Custom Multi Colours](sample_dataviz/example_path_custom2.png)

No real purpose for this one, but it's good to know your options :)

#### Optinal: Edge Plot

I have included an option to draw a different kind of path. 
As discussed, the path is normally drawn based on the order of the songs on an album (or index column in the dataframe). 
But if you want, you can change it to an edge shape. 
This draws a line across the outermost points in the data set. 

Here's an example of the data of Avicii's TIM: 

![Avicii Edge Path Straight](sample_dataviz/example_edge_path_straight.png)

And the version with a curved path:

![Avicii Edge Path Curved](sample_dataviz/example_edge_path_curved.png)

Technically, it works like this:

- The script finds the data point with lowest score in the dataframe. 
If there are multiple, it selects the one with the highest magnitude.
- Next, it goes looking for the next data point with a higher score and higher magnitude. 
If there aren't any, it picks the nearest point with a higher score.
- After that, it keeps on looking for data points with a higher score and a max difference of 1.1 in magnitude. 
Again, if there aren't any matches, it picks the nearest point with a higher score.
- When there are no values with a higher scores left, it flips it search. Looking for lower scores and lower magnitudes.
This last check picks up all the remaining data points for the path.

When the edge path order is defined, it adds a copy of the first row of the dataframe as the last row. 
This closes the path into a full loop.

To use this edge path option, you have to filter the data frame. 
You can pass a `start_at` parameter, to have the path start at a point of choosing. 

```python
from custom_path import sort_df_by_starting_point

df = pd.read_csv('output/avicii tim.csv').sort_values(by='index')

df_filtered = sort_df_by_starting_point(
  df=df,
  start_at='bad-reputation'
)
```
# To do

Things I'll be working on are:

_Nothing. Feel free to contact me with requests._
