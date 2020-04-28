import lyricsgenius

# generate an api key and paste it
# https://genius.com/api-clients
genius = lyricsgenius.Genius("api-key-here")

def save_lyrics(songs, artist_name, album_name):
    for i in range(len(songs
    )):
        song_title = songs[i]
        song = genius.search_song(song_title, artist_name)
        lyrics = song.lyrics
        with open('songs/{}/{}_{}_{}.txt'.format('_'.join(artist_name.split(' ')), i+1, album_name, '-'.join(''.join(song_title.split('\'')).split(' '))), 'w') as f:
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
