import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def tweet_everyday(api):
  return False

def main():
  api = create_api()

if __name__ == "__main__":
  main()