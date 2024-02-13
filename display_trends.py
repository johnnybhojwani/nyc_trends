# I would like to see a wordcloud and a printout of all the most popular trends in New York City. I only care about
# trends that have a tweet volumn of over 50,000. Use the file nyc_trends.py to extract the information and display 
# it to the screen as well as in a wordcloud. Create a dictionary that will hold the tweet name as the key and the
# tweet volume as the value. The dictionary must be named tweet_dict. You will need to install the library wordcloud
# for the script to display the wordcloud. For reference, the wordclod should look exactly like the image - trends_original.png

# Create a VE for the wordcloud library and make sure the VE is not pushed to your GitHub repo.


# nyc_trends is an object imported from the file nyc_trends.py
from nyc_trends import nyc_trends

from wordcloud import WordCloud
import matplotlib.pyplot as plt



#print out the type of object 'nyc_trends' is to see what object you are dealing with.



#Create a new dictionary to hold the trend name and trend volume
#use this variable name only for the wordcloud to work
tweet_dict = {}


# iterate through the nyc_trends object to extract the tweet name and the tweet volume
# and append it to the tweet_dict dictionary








#display the wordcloud
wordcloud = WordCloud(colormap="prism", background_color="white").generate_from_frequencies(tweet_dict)
plt.imshow(wordcloud)
wordcloud.to_file('trends.png')
plt.show()






