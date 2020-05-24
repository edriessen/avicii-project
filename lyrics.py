import lyricsgenius, json, io, re


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
        with io.open('songs/{}/{}-{}-{}.txt'.format(artist_name, i+1, album_name, song_title), 'w', encoding='utf-8') as f:
            f.writelines(lyrics.split('\\n'))


if __name__ == '__main__':
    songs = [
        "the reaper",
        'family',
        'see the way',
        "ps I hope you're happy",
        "push my luck",
        "takeaway",
        "Call You Mine",
        "Do You Mean",
        "kills you slowly",
        "who do you love",
    ]
    save_lyrics(songs, 'The Chainsmokers', 'World War Joy')
