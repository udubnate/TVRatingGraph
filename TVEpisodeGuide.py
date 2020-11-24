# Need to figure out how to connect to a IMDB dataset
# pip3 install IMDbPY

# need to figure out how to graph the dataset

# Test scenario. Community and The Office
# I want to be able to graph each Season, EP0101 show the average review in a bar or line chart. 
# Be able to click on it to show what the epsiode (or hover) details are

print("Hello World")

# Example Tutorial on Episode Rating
# https://imdbpy.readthedocs.io/en/latest/usage/series.html?highlight=episode%20rating#ratings


from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

series = ia.get_movie('0386676')

# adding new info set - adding episode details
ia.update(series, 'episodes') 

# getting episodes of the series 
episodes = series.data['episodes'] 

  
# traversing each key 
for i in episodes.keys(): 
      
    # printing season number 
    print("Season " + str(i)) 
      
    # traversing season i 
    for j in episodes[i]: 
          
        # getting title of episode 
        title = episodes[i][j]['title'] 
        rating = episodes[i][j]['rating']
          
        # printing title 
        print(" Ep" + str(j) + " : " + title + " : " + str(rating)) 