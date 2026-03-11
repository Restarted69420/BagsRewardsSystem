import math

TOKEN_STEP = 100000
BASE_PERCENT = 0.005
NFT_BONUS = 0.05
MAX_NFTS = 20

def calculate_reward(tokens, nfts):

    if tokens <= 0:
        return 0

    base = math.floor(tokens / TOKEN_STEP) * BASE_PERCENT

    valid_nfts = min(nfts, MAX_NFTS)
    bonus = valid_nfts * NFT_BONUS

    final_reward = base * (1 + bonus)

    return final_reward