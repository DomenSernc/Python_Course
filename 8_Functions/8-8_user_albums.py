def make_album(artist_name, album_title, number_of_songs=None ):
    album = {"artist": artist_name, "album": album_title}
    #artist and album are "keys", artist_name and album_title are "values" : key - value
    if number_of_songs:
        album["song_number"] = number_of_songs
    return album

while True:
    print("Enter album's artist and title: ")
    print("Enter 'q' to quit")

    a_artist = input("Album artist: ")
    if a_artist == "q":
        break
    
    a_title = input("Album title: ")
    if a_title == "q":
        break

    created_album = make_album(a_artist, a_title)
    print(f" One of my favourite music pieces is: {created_album}")