import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
import os
import time
import codecs
os.chdir('/Users/alejandrog/MEGA/Caltech/datascience/twitter')
from secret import consumer_key, consumer_secret, access_token, access_token_secret
#This script connect to twitter and uses a hashtag to retrieve tweets in real time
#It has to be stopped manually which is not ideal





def get_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return(auth)

auth = get_auth()
api = tweepy.API(auth)

#Until here, it seems to be pretty universal.

#About class methods:
#They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
#It can modify a class state that would apply across all the instances of the class. For example it can modify a class variable that will be applicable to all the instances.

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse

# Way 1
class MyListener(StreamListener):

    # def on_status(self,status):
    #     #when a tweet is published it arrives here:
    #     print(status.text.encode("ascii",errors='replace'))
    #     print("-"*10)

    def on_data(self, data):
        try:
            with codecs.open('FILENAME.json', 'a',encoding='iso-8859-1') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

# Way 2: https://stackoverflow.com/questions/33498975/unable-to-stop-streaming-in-tweepy-after-one-minute
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open('abcd.json', 'a')
        super(MyStreamListener, self).__init__()

    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            self.saveFile.write(data)
            self.saveFile.write('\n')
            return True
        else:
            self.saveFile.close()
            return False





# SCRIPT starts here:
# # # # # # # #
 # # # # # # #
#The Stream module listens to tweets in real time and triggers events in the listener,
#within the myStreamListener class we can redefine function that will process data
#Our MyListener implementation will save tweets to a .json file

runtime = 60 #for how long we want to stream tweets

#myStreamListener = MyListener() #overrides the listner method for capturing tweets
twitter_stream = Stream(auth, MyListener()) #create instance

hashtag='AMLO'
#async parameter will execute the stream in the background This works :
twitter_stream.filter(track=['AMLO'],languages=['es'],is_async=True) #execute with the desired keyword

time.sleep(runtime) #halts the control for runtime seconds

twitterstream.disconnect() #disconnect the stream and stop streaming and stop writing to output.json
