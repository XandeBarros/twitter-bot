from dotenv import load_dotenv
load_dotenv()

import tweepy
import os

def create_api():
  '''Credentials'''

  api_key = os.getenv("API_KEY")
  api_secret = os.getenv("API_SECRET")
  access_token = os.getenv("ACCESS_TOKEN")
  access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

  auth = tweepy.OAuthHandler(api_key, api_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

  try:
      api.verify_credentials()
  except Exception as e:
      print("Error creating API")
      raise e
  print("API created")
  return api