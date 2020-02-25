import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def get_users():

    # purpose: Prompts the user for Spotify usernames or Spotify IDs. Appends these usernames to a list
    # params: None
    # return: list of usernames (validated when retrieving playlists)
    cont = 'y'
    users = []
    while cont == 'y':
        user = input('Enter Spotify username or user ID: ').strip()
        users.append(user)
        cont = input("Enter another user? [y/n] ").lower().strip()
        while cont not in ['y', 'n']:
            cont = input('Invalid response. Enter another user? [y/n]').lower().strip()
    print('Users selected: ', users, '\n')
    return users


def get_playlists(spotify, users):

    # purpose: Allows user to select playlists to include in the analysis
    # params: users - List of Spotify usernames or user IDs
    #         spotify - Spotify Web API object
    # requires: import pandas as pd
    # returns: all_playlists - DataFrame of selected playlist names, description, id, tracks, total tracks

    # Playlist information DataFrame
    playlist_information = pd.DataFrame(columns=['name', 'description', 'id', 'tracks', 'total_tracks'])

    # For each user, show information for each public playlist. User selects whether to include playlist.
    for user in users:
        print("\nUser: ", user)
        try:
            user_pls = spotify.user_playlists(user, limit=50, offset=0)
        except:
            print(' "{}" is an invalid Spotify username. Check the username or renew Spotify token.'.format(user))
            continue

        # Playlist identifying information
        for user_pl in user_pls['items']:
            playlist = [user_pl['name'],
                        user_pl['description'],
                        user_pl['id'],
                        user_pl['tracks']['href'],
                        user_pl['tracks']['total']]
            playlist_series = pd.Series(playlist, index=playlist_information.columns)
            print("Playlist Information: ")
            print(playlist_series)  # Display the playlist information before adding

            # User chooses whether to include playlist
            cont = input('\nInclude playlist? [y/n] [> next user, q=done] ').lower().strip()
            while cont not in ['y', 'n', '>', 'q']:
                cont = input('\nInvalid selection. Include playlist? [y/n] [> - next user, q - done] ').lower().strip()
            if cont == 'y':
                playlist_information = playlist_information.append(playlist_series, ignore_index=True)
                print("\n")
            elif cont == 'n':
                print("\n")
            elif cont == '>':
                print('New user. \n')
                break
            else:
                print('\nDone adding playlists. Continuing.\n')
                playlist_information = playlist_information.sort_values(by=['name']).reset_index(drop=True)
                return playlist_information
    playlist_information = playlist_information.sort_values(by=['name']).reset_index(drop=True)
    return playlist_information


def get_track_features(spotify, playlist_information):
    # purpose: get audio features for each track in the selected playlists
    # params: spotify - Spotify Web API object
    #         playlist_information - Dataframe of playlist information
    # returns: Dataframe of track features for all selected user playlists

    start = 0
    # Initialize empty dataframe with features of interest
    track_info_dataframe = pd.DataFrame(columns=['playlist_name',
                                                 'artist_name',
                                                 'track_name',
                                                 'track_id',
                                                 'danceability',
                                                 'energy',
                                                 'key',
                                                 'loudness',
                                                 'mode',
                                                 'speechiness',
                                                 'acousticness',
                                                 'instrumentalness',
                                                 'liveness',
                                                 'valence',
                                                 'tempo',
                                                 'type',
                                                 'id',
                                                 'uri',
                                                 'track_href',
                                                 'analysis_url',
                                                 'duration_ms',
                                                 'time_signature'])

    # For each playlist, pull out each track and acquire corresponding audio features
    for id in playlist_information['id']:
        playlist_tracks = spotify.playlist(id, fields=['tracks'])
        for track in playlist_tracks['tracks']['items']:
            track_info_list = [playlist_information['name'].iloc[start],
                               track['track']['artists'][0]['name'],
                               track['track']['name'],
                               track['track']['id']]
            features = spotify.audio_features(track['track']['id'])
            track_info_list = track_info_list + [value for key, value in features[0].items()]
            track_info_series = pd.Series(track_info_list, index=track_info_dataframe.columns)
            track_info_dataframe = track_info_dataframe.append(track_info_series, ignore_index=True)
            track_info_dataframe
        start += 1
    return track_info_dataframe


def plot_distributions(df, drop=None):
    # purpose: Creates distribution plots in seaborn for numeric DataFrames
    # params: df - a pandas DataFrame
    #         drop - a list of column names passed in as strings to remove from dataframe before generating plots
    # return: for each playlist, variable - plots shaded kernel density estimate in console

    # Argument validation
    if not all(isinstance(column, str) for column in drop):
        raise TypeError("Dropped columns must be a list of strings.")

    # Plot kernel density
    palette = sns.color_palette('colorblind')
    for var in df.drop(columns=drop).columns:
        palette_index = 0
        p = None
        for user_playlist in df['playlist_name'].unique():
            p = sns.kdeplot(df[df['playlist_name'] == user_playlist][var],
                            label=user_playlist,
                            shade=True,
                            color=palette[palette_index])
            palette_index += 1  # Adds 1 to palette index
            if palette_index > (len(palette) - 1):  # Cycles back through palette colors if enough playlists
                palette_index = 0
        p.set_title('{} distribution'.format(var).title())
        plt.legend()
        plt.show()