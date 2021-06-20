import tweepy
import logging
import time
import multiprocessing
from config import create_api
from weather import get_weather
from data import date

HALF_DAY = 43200
FIVE_MINUTES = 300

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def postTweet(api, text):
  while True:
    logger.info("Posting...")
    api.update_status(text)
    logger.info("Posted ;)") 
    time.sleep(HALF_DAY)

def likeEveryNewTweet(api, user):
  while True:
    logger.info("Searching new tweets...")
    tweets = api.user_timeline(user, exclude_replies=True)

    for status in tweets:
      if not status.favorited:
        try:
          api.create_favorite(status.id)
          logger.info("Favorited")
        except Exception as e:
          logger.error("Error on fav", exc_info=True)
      time.sleep(FIVE_MINUTES)
      logger.info("Wainting")

def main():
  api = create_api()
  weatherStatus = get_weather()
  dataString = date()

  user = "XDessau"
  tweet = f"{dataString} {weatherStatus} E vale lembrar: No EAD todas as ativadades são em grupo ;)"

  p1 = multiprocessing.Process(target=postTweet, args=[api, tweet])
  p2 = multiprocessing.Process(target=likeEveryNewTweet, args=[api, user])
  
  p1.start()
  p2.start()
  p1.join()
  p2.join()
    
if __name__ == "__main__":
  main()