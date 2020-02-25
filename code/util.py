import pandas as pd

def getUsers():
    # purpose: Prompts the user for Spotify usernames or Spotify IDs. Appends these usernames to a list
    # params: None
    # return: list of usernames (validated when retrieving playlists)
    cont = 'y'
    users = []
    while cont == 'y':
        user = input('Enter Spotify username or user ID: ')
        users.append(user)
        cont = input("Enter another user? [y/n] ").lower().strip()
        while cont not in ['y', 'n']:
            cont = input('Invalid response. Enter another user? [y/n]').lower().strip()
    print('Users selected: ', users, '\n')
    return users


def getPlaylists(spotify, users):
    # purpose: Allows user to select playlists to include in the analysis
    # params: users - List of Spotify usernames or user IDs
    #         spotify - Spotify Web API object
    # requires: import pandas as pd
    # returns: all_playlists - DataFrame of selected playlist names, description, id, tracks, total tracks

    # Playlist information DataFrame
    playlist_information = pd.DataFrame(columns=['name', 'description', 'id', 'tracks', 'total_tracks'])

    # For each user, show information for each public playlist. User selects whether to include playlist.
    for user in users:
        try:
            user_pls = spotify.user_playlists(user, limit=50, offset=0)
        except:
            print(' "{}" is an invalid Spotify username. Removing.'.format(user))
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