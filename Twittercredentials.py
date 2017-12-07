import tweepy

consumer_key = "PvwFjJVMmfTJZnrzgzbTwmpzZ";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "N0mzPeF6Ia3ZC0Yp7HAGZvciJou0XaauQdcXyu4xIhLyAwGrXN";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "30685591-htz4mMy6kZIbJkuCrm3sQRm1NHee9vwMag1NZA4p1";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "g07xCCKgGvqBfqzm2LMOJ5yymZldC8SiSKpPCJu00SQFJ";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



