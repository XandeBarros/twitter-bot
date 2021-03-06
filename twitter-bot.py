import tweepy
import time
import multiprocessing
import random
from config import create_api
from weather import get_weather
from data import get_date
from phrases import get_phrases

HALF_DAY = 43200
FIVE_MINUTES = 300
THIRTY_SECONDS = 30

def likeTweets(api, user):
  tweets = api.user_timeline(user, exclude_replies=True)

  for status in tweets:
    if not status.favorited:
      try:
        api.create_favorite(status.id)
        print(f"Favorited (@{user})")
      except Exception as e:
        print(f"Error on fav(@{user})")
    else:
      continue
    time.sleep(THIRTY_SECONDS)
    print("Waiting")

  time.sleep(FIVE_MINUTES)

def posting(api, weather, date, phrase):
  text = f"{weather} {date} {phrase}"

  if not len(text) > 280:
    print("Posting...")
    try:
      api.update_status(text)
      print("Posted ;)") 
    except Exception as e:
      print("Error on tweet")
      raise e
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

def postTweet(api):
  while True:
    weather = get_weather()
    date = get_date()
    phrases = get_phrases()
        
    phrase = random.choice(phrases)

    posting(api, weather, date, phrase)
    time.sleep(HALF_DAY)

def likeEveryNewTweet(api):
  userXande = "XDessau"
  userJuju = "juoliveira12_"
  
  while True:
    print("Searching new tweets...")
    
    likeTweets(api, userJuju)
    likeTweets(api, userXande)

    time.sleep(FIVE_MINUTES)

def trovsNewReply(api):
  while True:
    user = "916465001468170242"
    user = api.get_user(user)

    mentions = api.mentions_timeline()

    for mention in mentions:
      try:
        if mention.user.screen_name == user.screen_name and not mention.favorited:
          api.update_status(f"@{user.screen_name} É sobre isso!!!", mention.id)
          print("Posted to Trovs sz ;)")
          mention.favorite()
        time.sleep(THIRTY_SECONDS)
      except Exception as e:
        print("Error on reply to Trovs ;(")
        raise e
    time.sleep(FIVE_MINUTES)

def crovsNewReplay(api):
  while True:
    user = "972941310905774081"
    user = api.get_user(user)

    mentions = api.mentions_timeline()
    answers = ["vdd linda concordo", "estamos num total de zero dias sem falar bosta, nosso recorde é de zero dias", "verdade concordo, falou tudo, essa noite você não passa frio, pois tá coberto de razão", "falou muito e falou bosta, namoral..."]

    for mention in mentions:
      try:
        if mention.user.screen_name == user.screen_name and not mention.favorited:
          api.update_status(f"@{user.screen_name} {random.choice(answers)}", mention.id)
          print("Posted to Crovs sz")
          mention.favorite()
        time.sleep(THIRTY_SECONDS)
      except Exception as e:
        print("Error on reply to Crovs ;(")
        raise e

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

  p1 = multiprocessing.Process(target=postTweet, args=[api])
  p2 = multiprocessing.Process(target=likeEveryNewTweet, args=[api])
  p3 = multiprocessing.Process(target=followFollowers, args=[api])
  p4 = multiprocessing.Process(target=trovsNewReply, args=[api])
  p5 = multiprocessing.Process(target=crovsNewReplay, args=[api])
  
  p1.start()
  p2.start()
  p3.start()
  p4.start()
  p5.start()
  p1.join()
  p2.join()
  p3.join()
  p4.join()
  p5.join()
    
if __name__ == "__main__":
  main()