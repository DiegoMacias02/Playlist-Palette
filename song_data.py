from authenticate import sp
from select_playlist import selected_name, selected_id
from lyrics_sentiment import get_lyrics, analyze_sentiment
# Import SpotifyException for better error handling
from spotipy.exceptions import SpotifyException

if selected_id:
    try:
        selected_playlist = sp.playlist(selected_id)
    except SpotifyException as e:
        print(f"Error fetching playlist {selected_name}: {e}")
        # Exit if there's an issue fetching the playlist
        exit()

    # List to store the songs
    songs = []
    # List to store the sentiments and scores
    sentiments_scores = []
    # List to store the audio features
    audio_features_list = []

    # Loop over each item in the playlist
    for item in selected_playlist["tracks"]["items"]:
        song = item["track"]
        name = song["name"]
        artist = song["artists"][0]["name"]
        song_id = song['id']
        
        songs.append((name, artist))
        
        lyrics = get_lyrics(name, artist)
        sentiment, score = analyze_sentiment(lyrics)
        sentiments_scores.append((sentiment, score))
        
        features = sp.audio_features([song_id])[0]
        audio_features_list.append(features)

    # Example logic to process and use sentiment scores and audio features
    # Modify this part according to your specific requirements for image generation
    # This could involve calculating averages, identifying dominant sentiment, etc.
    average_sentiment = sum(score for _, score in sentiments_scores) / len(sentiments_scores)
    # Placeholder for calling image generation with analyzed data
    # generate_playlist_cover(average_sentiment, audio_features_list, other_parameters)

    # For demonstration, printing the collected data
    print(f"Songs in playlist '{selected_name}':")
    for song in songs:
        print(f" - {song[0]} by {song[1]}")
    print(f"Average sentiment score: {average_sentiment}")
    # You might want to print or process audio features similarly

else:
    print(f"Playlist '{selected_name}' not found.")
