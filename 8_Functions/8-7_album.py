def make_album(artist_name, album_title, number_of_songs=None ):
    album = {"artist": artist_name, "album": album_title}
    #artist and album are "keys", artist_name and album_title are "values" : key - value
    if number_of_songs:
        album["song_number"] = number_of_songs
    return album

best_seller = make_album("Pink Floyd", "Dark Side of The Moon")
print(best_seller)

best_seller = make_album("Daft Punk", "Random Access Memories")
print(best_seller)

best_seller = make_album("Rolling Stones", "Sticky Fingers")
print(best_seller)

best_seller = make_album("Beatles", "Let it Be", "12")
print(best_seller)

best_seller = make_album("Abba", "The Visitors", "9" )
print(best_seller)
