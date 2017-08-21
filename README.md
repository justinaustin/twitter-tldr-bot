# twitter-tldr-bot
A [Twitter bot](https://twitter.com/tldr_please) based on the [newspaper3k](https://github.com/codelucas/newspaper/) and [tweepy](https://github.com/tweepy/tweepy) libraries.


For example, sending "https://www.nytimes.com/2017/07/06/upshot/blue-cities-want-to-make-their-own-rules-red-states-wont-let-them.html?smid=tw-nytimes&smtyp=cur" to the bot will cause it to reply with:
```
Blue Cities Want to Make Their Own Rules. Red States Won’t Let Them.: States have banned local ordinances on minimum wage increases, paid sick days and lesbian, gay, bisexual and transgender rights. They’ve banned “sanctuary cities.” They’ve even banned a number of bans (it’s now illegal for Michigan cities to ban plastic bags, for Texas towns to ban fracking). When cities overstep their bounds, he said this year, they “should have to pay a price for it.”Where States Curb Local Control Policies in these states block or limit local laws. Cleveland, in other words, was trying to ensure that local projects created local jobs, alleviating local poverty. They disagree on who started the fight: states in stripping municipal power, or cities in seizing new roles that weren’t theirs to begin with.
```


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