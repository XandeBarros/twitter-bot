import tweepy
import logging
from config import create_api
from weather import get_weather
from data import date
import time

HALF_DAY = 43200

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def postTweet(api, text):
  api.update_status(text)
  logger.info("Posting...")

def main():
  api = create_api()
  weatherStatus = get_weather()
  dataString = date()

  tweet = f"{dataString} {weatherStatus} E vale lembrar: Não dê palco pra maluco ;)"

  while True:
    postTweet(api, tweet)
    logger.info("Até amanhã ;)") 
    time.sleep(HALF_DAY)


if __name__ == "__main__":
  main()