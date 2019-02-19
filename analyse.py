from connect import client
from google.cloud.language import enums
from google.cloud.language import types
import os, xlsxwriter

def get_sentiment_from_text(text):
    text = u''+text
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    return(sentiment)


def get_song_sentiment(folder):
    files = os.listdir(folder+'/')
    songs = []
    for index, file in enumerate(files):
        if index < 199 :
            song_name = file.split('.')[0]
            song = open(folder+'/'+file, 'r')
            song_parts = song_name.split('_')
            song_album = song_parts[0]
            song_title = song_parts[1]
            song_text = song.read()
            song_sentiment = get_sentiment_from_text(song_text)
            song_magnitude = song_sentiment.magnitude
            song_score = song_sentiment.score
            song = {
                'title': song_title,
                'album': song_album,
                'score': song_score,
                'magnitude': song_magnitude
            }
            songs.append(song)
    return songs


def get_sentiment_single_song_from_file(file):
    song = open(file, 'r').read()
    song_lines = song.split('\n')
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
    return (lines_with_sentiment)


def save_array_of_dicts_to_excel(array_of_dicts, file_name):
    workbook = xlsxwriter.Workbook('output/song_sentiment_'+file_name+'.xlsx')
    worksheet = workbook.add_worksheet()
    songs = array_of_dicts
    print(songs)
    row = 0
    col = 0
    for index, key in enumerate(array_of_dicts[0]):
        print(index, key)
        worksheet.write(row, col + index, key)

    for song in songs:
        print(song)
        row += 1
        for index, key in enumerate(song):
            print(index, song[key])
            worksheet.write(row, col + index, song[key])

    workbook.close()


save_array_of_dicts_to_excel(get_song_sentiment('songs/avicii'), 'avicii_discography' )


