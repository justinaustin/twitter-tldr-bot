# twitter-tldr-bot
A [Twitter bot](https://twitter.com/tldr_please) based on the [newspaper3k](https://github.com/codelucas/newspaper/) and [tweepy](https://github.com/tweepy/tweepy) libraries.

## Try it out!
This bot is currently running! Send a direct message on Twitter containing a link to an article to [@tldr_please](https://twitter.com/tldr_please) and the bot will reply with a summary of the article.

## Usage
Clone and install the necessary requirements:
```sh
git clone git@github.com:justinaustin/twitter-tldr-bot.git
cd twitter-tldr-bot/
pip3 install -r requirements.txt
python3 nltk-download.py
```
The last line downloads data needed by the [Natural Language Tookit](http://www.nltk.org/). 

Next, register at [apps.twitter.com](https://apps.twitter.com) in order to get access tokens. Copy the `CONSUMER_KEY`, `CONSUMER_SECRET`, `ACCESS_TOKEN`, and `ACCESS_SECRET` into the `credentials.py` file.


Finally, run the bot with `python3 bot.py`
