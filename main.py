import tweepy


consumer_key = 'FZv7bY6C8ctED9YnX7vTIkhBZ'
consumer_secret = 'NdP7ZR3bcHUyAxbOkZhSpl5oHPMbqESbE52HlNhg1LdQIWSp'
access_token = '272478864-aW6JHauUmxP0vyLECJvHcL9JqSzfYggdJCSMnII1'
access_token_secret = 'adMoEoUwJNCBiGdLCeRYwlIdKxuZrWUSg5iduo6SywI49'


class TweetsListener(tweepy.StreamListener):

    def on_connect(self):
        print("Estoy conectado!")

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print("Error", status_code)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


stream = TweetsListener()
streamingApi = tweepy.Stream(auth=api.auth, listener=stream)
streamingApi.filter(
    # follow=["151179935"],
    track=["Coronavirus"],

)  # Ciudad de Mexico
