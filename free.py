import tweepy
from time import sleep
from termcolor import cprint

#============ CONFIGURATION ==========================

# the @ of the accounts you want to reply to. You can add more or just keep one
bots_to_reply_to = ["beanz_sales_bot", "azuki_sales"]

# the actual reply that will be posted 
reply_message = "FREE"

# The api infos of your own account. Find those data by completing you twitter developper profile at 
# https://developer.twitter.com/en/portal/dashboard
api_key = "your api key"
api_secret = "your api secret"
bearer_token = " your bearer token"
access_token = "your access token"
access_token_secret = "your access token secret"

# ======================================================

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

last_ids = {}

for bot_account in bots_to_reply_to:
    last_ids[bot_account] = [0, client.get_user(username=bot_account).data.id]

while True:

    for bot_account in bots_to_reply_to:
        bot_id = last_ids[bot_account][1]
        last_tweet = client.get_users_tweets(id=bot_id, max_results=5, exclude =["retweets", "replies"])[0][0]

        if last_ids[bot_account][0] == last_tweet.id:
            sleep(5)
            continue

        else:
            try:
                client.create_tweet(in_reply_to_tweet_id= last_tweet.id, text=reply_message)
                cprint(f'=> @{bot_account}: {last_tweet.text[:25]}...', "cyan")
                cprint(f'=> we replied: {reply_message}', "green")
                last_ids[bot_account][0] = last_tweet.id
            except:
                pass
        
    



        
        
        








