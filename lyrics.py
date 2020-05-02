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
        "I Forgot That You Existed",
        "Cruel Summer",
        'Lover',
        "The Man",
        "The Archer",
        "I Think He Knows",
        "Miss Americana & the Heartbreak Prince",
        "Paper Rings",
        "Cornelia Street",
        "Death By a Thousand Cuts",
        "London Boy",
        "Soon You’ll Get Better",
        "False God",
        "You Need to Calm Down",
        "Afterglow",
        "Me!",
        "It’s Nice to Have a Friend",
        "Daylight",
    ]
    save_lyrics(songs, 'Taylor Swift', 'Lover')
