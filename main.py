#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import app_tokens

#Variables that contains the user credentials to access Twitter API 
access_token =  app_tokens.ACCESS_TOKEN
access_token_secret =  app_tokens.ACCESS_TOKEN_SECRET
api_key =  app_tokens.API_KEY
api_secret =  app_tokens.API_SECRET


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        tweet = json.loads(data)
        print(tweet["text"] + '\n')
        return True

    def on_error(self, status):
        #print(status)
        pass


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)


    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['peter'])