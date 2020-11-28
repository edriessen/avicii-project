import lyricsgenius, json, io, re
from time import sleep


with open('credentials-genius.json') as f:
  data = json.load(f)

access_key = data["access-key"]

# generate an api key and paste it
# https://genius.com/api-clients
genius = lyricsgenius.Genius(access_key)

def save_lyrics(songs, artist_name, album_name):
    for i in range(len(songs )):
        song_title = songs[i]
        song = genius.search_song(song_title, artist_name)
        lyrics = song.lyrics
        lyrics = re.sub(r"\[.+\]\n", '', lyrics)
        correction = 4
        with io.open('songs/{}/{}-{}-{}.txt'.format(artist_name, i+1+correction, album_name, song_title), 'w', encoding='utf-8') as f:
            f.writelines(lyrics.split('\\n'))
        sleep(1)


if __name__ == '__main__':
    songs = [
        # "The Power Of Equality",
        # 'if i have to ask',
        # 'breaking the girl',
        # 'funky monks',
        'suck my kiss',
        'I could have lied',
        'mellowship slinky in b major',
        'give it away',
        'blood sugar sex magik',
        'under the bridge',
        'naked in the rain',
        'apache rose peacock',
        'the greeting song',
        'my lovely man',
        'sir pshycho sexy',
        'They\'re red hot',

    ]
    save_lyrics(songs, 'Red-Hot-Chili-Peppers', 'Blood Sugar Sex Magik')
