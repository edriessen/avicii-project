from connect import client
from google.cloud.language import enums
from google.cloud.language import types
import pandas as pd
import os


def get_sentiment_from_text(text):
    text = u''+text
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    content_length = len(document.content)
    if content_length > 5000:
        print('!! WARNING: content is over 5000!')
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    return(sentiment)


def get_song_sentiment(folder):
    files = os.listdir(folder+'/')
    songs = []
    for index, file in enumerate(files):
        if index < 199 :
            song_name = file.split('.')[0]
            song = open(folder+'/'+file, 'r')
            song_parts = song_name.split('-')
            song_index = song_parts[0]
            song_album = song_parts[1]
            song_title = song_parts[2]
            song_text = song.read()
            song_sentiment = get_sentiment_from_text(song_text)
            song_magnitude = song_sentiment.magnitude
            song_score = song_sentiment.score
            song = {
                'title': song_title,
                'index': song_index,
                'album': song_album,
                'score': song_score,
                'magnitude': song_magnitude
            }
            songs.append(song)
    return songs


def get_sentiment_single_song_from_file(file):
    song = open(file, 'r').read()
    song_lines = song.split('\n\n')
    lines_with_sentiment = []
    for line in song_lines:
        if line != '':
            line_sentiment = get_sentiment_from_text(line)
            line_magnitude = line_sentiment.magnitude
            line_score = line_sentiment.score
            lines_with_sentiment.append({
                'title': line,
                'score': line_score,
                'magnitude': line_magnitude
            })
    return lines_with_sentiment


def save_list_to_csv_with_name(list, file_name):
    df = pd.DataFrame(list)
    if not os.path.exists('output'):
        os.makedirs('output')
    df.to_csv('output/' + file_name + '.csv', index=False)


def analyse_files_and_store_in_csv(folder_path, file_name):
    save_list_to_csv_with_name(get_song_sentiment(folder_path), file_name)


if __name__ == '__main__':
    path_to_songs = 'songs/avicii_tim'
    csv_file_name = 'avicii tim'
    analyse_files_and_store_in_csv(path_to_songs, csv_file_name)

