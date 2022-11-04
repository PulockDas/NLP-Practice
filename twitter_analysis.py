import GetOldTweets3 as got

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('CoronaOutbreak') \
        .setSince("2020-01-01") \
        .setUntil("2020-04-01") \
        .setMaxTweets(10)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets

get_tweets()