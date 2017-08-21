import json
import logging
import re

from credentials import (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_SECRET, 
                         ACCESS_TOKEN)
import tweepy
from tweepy.streaming import StreamListener
from newspaper import Article

NO_URL_MESSAGE = "The message you sent me did not have an article link in it."


def get_article(article_url):
    logging.info('Download and processing article ' + article_url)
    article = Article(article_url)
    article.download()
    article.parse()
    article.nlp()
    print('hi')
    return article


class DMListener(StreamListener):
    def __init__(self, api):
        self.dm_count = 0
        self.api = api

    def on_connect(self):
        logging.info('Connection established')

    def on_disconnect(self, notice):
        logging.warning('Connection lost: ', notice)

    def on_data(self, status):
        with open('status.dat', 'w') as f:
            f.write(str(status))
        if 'direct_message' in status:
            status = json.loads(status)
            screen_name = status['direct_message']['sender']['screen_name']
            if screen_name == 'tldr_please':
                return True
            text = status['direct_message']['text']
            logging.info('Received direct message')
            url = re.search('(?P<url>https?://[^\s]+)', text)
            if url is None:
                logging.info('No url found. Replying with NO_URL_MESSAGE')
                self.api.send_direct_message(screen_name, text=NO_URL_MESSAGE)
            else:
                logging.info('Url found. Replying with summary')
                url = url.group('url')
                article = get_article(url)
                text = article.title + ':\n' + article.summary
                self.api.send_direct_message(screen_name, text=text)
        return True
    
    def on_error(self, status):
        logging.error(status)


def main():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    stream = tweepy.Stream(auth, DMListener(api))
    while True:
        try:
            stream.userstream()
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
