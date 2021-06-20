import tweepy
import time
import multiprocessing
from config import create_api
from weather import get_weather
from data import get_date
from phrases import get_phrases

HALF_DAY = 43200
FIVE_MINUTES = 300
THIRTY_SECONDS = 30

def postTweet(api):
  while True:
    weather = get_weather()
    date = get_date()
    phrases = get_phrases()
    aux = 0
    
    if aux > len(phrases):
      aux = 0

    phrase = phrases[aux]

    text = f"{weather} {date} {phrase}"

    if not len(text) > 280:
      print("Posting...")
      try:
        api.update_status(text)
        print("Posted ;)") 
      except Exception as e:
        print("Error on tweet")
        raise e
      time.sleep(HALF_DAY)
    else:
      text = f"{weather} {date}"
      reply = f"{phrase}"
      try:
        api.update_status(text)
        me = api.me().id
        last_tweet_id = api.user_timeline(me, count=1)[0].id
        api.update_status(reply, last_tweet_id)
        print("Posted and Replied ;)") 
      except Exception as e:
        print("Error on tweet")
        raise e
      time.sleep(HALF_DAY)
    aux += 1  

def likeEveryNewTweet(api, user):
  while True:
    print("Searching new tweets...")
    tweets = api.user_timeline(user, exclude_replies=True)

    for status in tweets:
      if not status.favorited:
        try:
          api.create_favorite(status.id)
          print("Favorited")
        except Exception as e:
          print("Error on fav")
      else:
        continue
      time.sleep(THIRTY_SECONDS)
      print("Waiting")

    time.sleep(FIVE_MINUTES)

def followFollowers(api):
  while True:
    followers = tweepy.Cursor(api.followers).items()

    for follower in followers:
      if not follower.following:
        try:
          follower.follow()
          print(f"Now Following {follower.name}")
        except tweepy.error.TweepError:
          pass
      time.sleep(THIRTY_SECONDS)
    time.sleep(FIVE_MINUTES)

def main():
  api = create_api()
  user = "XDessau"

  p1 = multiprocessing.Process(target=postTweet, args=[api])
  p2 = multiprocessing.Process(target=likeEveryNewTweet, args=[api, user])
  p3 = multiprocessing.Process(target=followFollowers, args=[api])
  
  p1.start()
  p2.start()
  p3.start()
  p1.join()
  p2.join()
  p3.join()
    
if __name__ == "__main__":
  main()