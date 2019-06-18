# 🎧 Spotify Data Visualization Project
A full-stack data project utilizing audio features data from the official Spotify Web API.  In the first notebook **Data Retrieval** we pull all the tracks saved in my Spotify music library along with audio features for each track and save it to a .csv.  In the **Data Exploration** notebook we do some exploratory analysis on the tracks as well as get an intuitive sense of the mean of each audio feature by listening to selected tracks.  In the last notebook, **Data Clustering** we use K-Means clustering algorithm to find natural groupings of tracks based on the features and save them to playlists.  

# 🌱 Motivation
Main motivation for this project was to get practical experience in all the steps of a data project including (automated) data retrieval, data exploration, as well as data modeling using Python, getting familiar with Jupyter Notebooks, and learn about API endpoints.

# 📓 Notebooks
Data Retrieval: [github](https://github.com/rtedwards/spotify-data-visualizations/blob/master/notebooks/spotify-data-retrieval.ipynb) | [nbviewer](https://nbviewer.jupyter.org/github/rtedwards/spotify-data-visualizations/blob/master/notebooks/spotify-data-retrieval.ipynb)  
Data Exploration: [github](https://github.com/rtedwards/spotify-data-visualizations/blob/master/notebooks/spotify-data-exploration.ipynb) | [nbviewer](https://nbviewer.jupyter.org/github/rtedwards/spotify-data-visualizations/blob/master/notebooks/spotify-data-exploration.ipynb)  
Data Clustering: [github](https://github.com/rtedwards/spotify-data-visualizations/blob/master/notebooks/spotify-data-clustering.ipynb) | [nbviewer](https://nbviewer.jupyter.org/github/rtedwards/spotify-data-visualizations/blob/master/notebooks/spotify-data-clustering.ipynb)

# 📁 Datasets
My Spotify "liked" songs

# 🛠️ Tools
## 🖥️ APIs

+ [Spotify Web API](https://developer.spotify.com/documentation/web-api/)

## 🐍 Python Libraries

+ [Spotipy](https://spotipy.readthedocs.io/en/latest/) - access to Spotify Web API with python
+ [IPython](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html) - embedding html for Spotify player
+ [Pandas](https://pandas.pydata.org/), [Numpy](https://www.numpy.org/) - data analysis
+ [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/) - data visualization
+ [scikit-learn](https://scikit-learn.org/stable/modules/clustering.html#clustering) - K-Means algorithm


# Tasks

- [x] Create dataset from Spotify library  
- [x] Exploratory data analysis  
- [x] Build an intuition for audio features by listening to songs through embedded Spotify player  
- [x] Use K-Means clustering to find clusters  
- [x] Create playlists based on found clusters and save them to my profile  
- [ ] Find clusters within cluster to find subgenres
- [ ] Use another clustering method that works with mixed data type -- continuous and categorical data  
