# -*- coding: utf-8 -*-
import tweepy
import time
import cf

auth = tweepy.OAuthHandler(cf.CA, cf.CS)
auth.set_access_token(cf.AT, cf.AS)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.user.name) #ツイート主の名前
        print(status.id) #ツイートのID
        print(status.text) #ツイート内容
        #api.create_favorite(status.id) #これのコメント解除したら#あなーるをいいねしてくれる
    
    def on_error(self, status_code):
        if status_code == 420:
            print("420番エラーが発生しました\nAPIのリミット制限です。\n詳細はこちらを御覧ください。\n https://developer.twitter.com/ja/docs/basics/response-codes")
        else:
            print("よくわからんエラーが発生しました。\n詳細はこちらをご覧ください。\n https://developer.twitter.com/ja/docs/basics/response-codes")

myStream = tweepy.Stream(auth = api.auth, listener = MyStreamListener())

myStream.filter(track=["#あなーる"])