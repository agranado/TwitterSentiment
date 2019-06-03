import tweepy #The Twitter API
from tkinter import * #For the GUI
from time import sleep
from datetime import datetime
from textblob import TextBlob #For Sentiment Analysis
import matplotlib.pyplot as plt #For Graphing the Data

os.chdir('/Users/alejandrog/MEGA/Caltech/datascience/twitter')
import secret
from secret import consumer_key, consumer_secret, access_token, access_token_secret
#This script connect to twitter and uses a hashtag to retrieve tweets in real time
#It has to be stopped manually which is not ideal

def get_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return(auth)

auth = get_auth()
api = tweepy.API(auth)

#Until her


#GUI
root = Tk()

label1 = Label(root, text="Search")
E1 = Entry(root, bd =5)

label2 = Label(root, text="Sample Size")
E2 = Entry(root, bd =5)

def getE1():
    return E1.get()

def getE2():
    return E2.get()

#def getData(keyword,numberOfTweets):
    # getE1()
    # keyword = getE1()
    #
    # getE2()
    # numberOfTweets = getE2()
    # numberOfTweets = int(numberOfTweets)

#Where the tweets are stored to be plotted
polarity_list = []
numbers_list = []
number = 1
filename = 'twitter1.json'
for tweet in tweepy.Cursor(api.search, keyword, lang="es").items(numberOfTweets):
    try:
        analysis = TextBlob(tweet.text)
        analysis = analysis.sentiment
        polarity = analysis.polarity
        polarity_list.append(polarity)
        numbers_list.append(number)
        number = number + 1

        with open(filename,'a') as f:
            f.write(json.dumps(tweet._json))
            f.write("\n")

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

#Plotting
axes = plt.gca()
axes.set_ylim([-1, 2])

plt.scatter(numbers_list, polarity_list)

averagePolarity = (sum(polarity_list))/(len(polarity_list))
averagePolarity = "{0:.0f}%".format(averagePolarity * 100)
time  = datetime.now().strftime("At: %H:%M\nOn: %m-%d-%y")

plt.text(0, 1.25, "Average Sentiment:  " + str(averagePolarity) + "\n" + time, fontsize=12, bbox = dict(facecolor='none', edgecolor='black', boxstyle='square, pad = 1'))

plt.title("Sentiment of " + keyword + " on Twitter")
plt.xlabel("Number of Tweets")
plt.ylabel("Sentiment")
plt.show()

### use as function
#getData("brozo", 1000)

submit = Button(root, text ="Submit", command = getData)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
submit.pack(side =BOTTOM)

root.mainloop()
