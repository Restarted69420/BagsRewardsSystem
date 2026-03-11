from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

RPC = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("BOT_PRIVATE_KEY")

w3 = Web3(Web3.HTTPProvider(RPC))

def distribute_rewards(wallet, reward_percent):

    print(f"Sending reward to {wallet}: {reward_percent}% of creator fees")

    # Real implementation should:
    # 1. read creator fee pool
    # 2. calculate wallet payout
    # 3. send blockchain transaction