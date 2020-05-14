import tweepy
from bots.config import authenticate


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f'{tweet.user.name}----->{tweet.text}\n\n')

    def on_error(self, status):
        print('Error detected')


if __name__ == '__main__':
    api = authenticate()
    tweets_listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=['pycharm', 'python'], languages=['en'])