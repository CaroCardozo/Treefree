import tweepy
import json

consumer_key = "yzF2JNeH9wqVshw4HK5BUsaJt"
consumer_secret = "1CBKid206ULCLoBYbLgBXdllAS5uy2qhfxQzNZJizb2lkKyQUC"
access_token = "1265638460-e8DI13EbgDFEy0pHf3jffywXw5JaMmEtNy6RmdZ"
access_token_secret = "o7B6HdtASELC6pXaQ46BUuPRqpap5vmUg0KESZidhv2n7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit_notify=True,wait_on_rate_limit=True)

recover_person = 0

tweet_info = open("C:\\Users\\anaca\\Documents\\Caro\\Hackathons\\Twitter\\TweetInfo.txt","a")

q = ["I beat cancer", "I a a be"]
for tweet in tweepy.Cursor(api.search, q , result_type = "recent", include_entities = False, include_rts = False, tweet_node = "extended").items(10):

    info = tweet._json['text']
    id_tweet = tweet._json['id']
    username_tweet = tweet._json['user']['screen_name']
    link_tweet = "https://twitter.com/" + str(username_tweet) + "/status/" + str(id_tweet)
    status = "Congratulations! We are so happy to hear that, come to our website to meet your own virtual tree "
    congrats = status + link_tweet
    user_id = tweet._json['user']['id']
    

    if not "RT" in info:
        recover_person += 1
        api.update_status(congrats)
        api.send_direct_message(user_id, text = "We are so happy and proud that you win this battle with cancer. For that, we want to honor you with a virtual tree on your name, you can visit it on our website. You deserve it.")
        tweet_info.write(str(tweet._json['user']['screen_name']) + ":" + "\n" + str(tweet._json['text']) + "\n \n")
        print (info)
       
       #here goes everything to the json extracting info, all the things goes here literally

#print (recover_person)

#api.update_status("hello from tweepy")
#api.destroy_status("1289568046688825344")

#data_me = api.me()
#json_data = json.dumps(data._json,indent = 4)
#print(json.dumps(data_me._json,indent = 4))
#id_ultimo_tweet = data._json["status"]["id"]
#print (id_ultimo_tweet)
#api.create_favorite(id_ultimo_tweet)
#api.retweet(id_ultimo_tweet)
#api.update_status("okay", in_reply_to_status_id = id_ultimo_tweet)


#data_img = api.media_upload("C:\\Users\\anaca\\Documents\\Caro\\Hackathons\\Twitter\\tree.jpg")
#print (data_img)

