import os
import tweepy
from dotenv import load_dotenv
from reward_engine import calculate_reward
from wallet_distributor import distribute_rewards

load_dotenv()

api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_SECRET")

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access, access_secret)
api = tweepy.API(auth)

def announce_rewards(wallet, reward):
    msg = f"Bags Reward System 💰\nWallet {wallet[:6]}... earned {reward:.6f}% creator fees!"
    api.update_status(msg)

def process_wallet(wallet, tokens, nfts):
    reward = calculate_reward(tokens, nfts)
    distribute_rewards(wallet, reward)
    announce_rewards(wallet, reward)

if __name__ == "__main__":

    wallets = [
        {"wallet":"0x123", "tokens":500000, "nfts":3},
        {"wallet":"0xabc", "tokens":1200000, "nfts":25},
    ]

    for w in wallets:
        process_wallet(w["wallet"], w["tokens"], w["nfts"])