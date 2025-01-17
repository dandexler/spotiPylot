<img src="images/spotiPylot_github_large_final.png" height=250></img>

## The collaborative Spotify playlist generator. Built in Python.
### Collaborate with friends, family, and colleagues on a Spotify playlist. Find music everyone is likely to enjoy!

<br>
Current Version: V1.2
<br>
Status: Functional Concept

## Overview
User Problem: Collaborative playlists are enjoyable and facilitate social interaction between friends and colleagues. However, they can be time-consuming to generate and there is no guarantee each collaborator will enjoy all tracks.

Proposed Solution: Analyze the audio features of users' selected playlists. Use these features to quickly produce a playlist comprised of tracks all contributors are likely to enjoy based on their inputs.
## Next Steps
<ul>
  <li> <strike> Allow custom input of users/playlists </strike> </li>
  <li> Modify clustering algorithm for improved playlists </li>
  <li> Build a front-end interface to interact with the application remotely </li>
  <li> Customize playlist based on user historical like/dislike </li>
  <li> Engineer new features based on other data available in Spotify Web API </li>
</ul>

## Getting Started

Latest version:
```
cd <YOUR_DIRECTORY>
git clone https://www.github.com/dandexler/spotiPylot
```
Concept is contained within the code/concept.ipynb Jupyter Notebook.

## Methodology
The methodology utilizes principal component analysis with fuzzy c-means clustering in scikit-fuzzy.

## Examples
Coming soon.

You may view the input playlists used for demonstration of the concept at:
<a href ="https://open.spotify.com/playlist/2V4jDbJJT7S575jdvrBuzV">User 1 </a>
<a href ="https://open.spotify.com/playlist/3gEikQyspYXdGwOdZwiFOj">User 2 </a>
<a href ="https://open.spotify.com/playlist/2I9p1xsjQGKljEviMQM5Lm">User 3 </a>

You may see the playlist generated from this project at:
<a href="https://open.spotify.com/playlist/4HQZWfYLja8sps8Gkk10EY">git init Playlist </a>

## Built With
<a href = "https://github.com/pandas-dev/pandas"> pandas 1.0.1 </a>
<br> <a href="https://github.com/mwaskom/seaborn"> seaborn 0.10.0 </a>
<br> <a href="https://github.com/scikit-fuzzy/scikit-fuzzy"> scikit-fuzzy 0.2 </a>
<br><a href = "https://github.com/scikit-learn/scikit-learn"> scikit-learn 0.22.1 </a>
<br><a href = "https://github.com/plamere/spotipy"> spotipy 2.9.0 </a>


## Authors
David Andexler

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
Aggarwal, Charu C., Alexander Hinneburg, and Daniel A. Keim. "On the surprising behavior of distance metrics in high dimensional space." International conference on database theory. Springer, Berlin, Heidelberg, (2001).

Baadel, S., Thabtah, F., and Lu, J. "Overlapping clustering: A review," 2016 SAI Computing Conference, London, (2016): 233-237.

Bezdek, J. "Pattern Recognition with Fuzzy Objective Function Algoritms", Plenum Press, New York, (1981).

Dunn, J. "A Fuzzy Relative of the ISODATA Process and Its Use in Detecting Compact Well-Separated Clusters", Journal of Cybernetics 3: (1973): 32-57.

Zadeh, L.A. "Fuzzy sets." Information and control 8.3 (1965): 338-353.
