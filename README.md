# Bags Reward System

**Bags Reward System (BRS)** is an automated reward distribution and Twitter bot designed for coins deployed on **Bags.fm**.

The system rewards holders with a share of the **creator’s trading fees** based on:
- how many tokens they hold
- how many NFTs from the project they hold

The bot wallet collects creator fees and distributes them proportionally to eligible wallets.

---

# Core Idea

The goal of the Bags Reward System is to **incentivize long-term holding** of both:

• the project token  
• the project NFTs  

Holders that keep both receive significantly higher rewards.

The system is designed to be:
- transparent
- automated
- fair
- easy to integrate with new token launches

---

# Reward Rules

### Token Rewards
Every **100,000 tokens held** equals:

**0.005% of the creator's fees**

Example:

| Tokens Held | Base Fee Share |
|-------------|---------------|
| 100,000 | 0.005% |
| 500,000 | 0.025% |
| 1,000,000 | 0.05% |

Formula:

base_reward = floor(tokens / 100000) * 0.005%

---

### NFT Bonus

NFTs provide a **multiplier bonus** to rewards.

Each NFT adds:

**+5% bonus to rewards**

Rules:

• Maximum NFT bonus = **100%**  
• Maximum NFTs counted = **20**  
• **NFT bonus only applies if the wallet holds tokens**

Example:

| NFTs | Bonus |
|-----|------|
| 1 | +5% |
| 5 | +25% |
| 10 | +50% |
| 20 | +100% (max) |

---

### Final Reward Calculation

final_reward = base_reward * (1 + nft_bonus)

Example:

Wallet holds:

Tokens: 500,000  
NFTs: 10

Step 1 — Base reward:

floor(500000 / 100000) * 0.005% = **0.025%**

Step 2 — NFT bonus:

10 NFTs → **50% bonus**

Step 3 — Final reward:

0.025% × 1.5 = **0.0375% of creator fees**

---

# System Components

### 1. Reward Engine
Calculates token rewards and NFT bonuses.

### 2. Wallet Distributor
Uses the bot wallet to send reward payouts.

### 3. Twitter Bot
Automatically posts:

• reward announcements  
• holder achievements  
• distribution updates  

Example Tweet:

"Bags Reward System 💰  
Wallet 0x123... earned 0.0375% of creator fees!"

### 4. Holder Scanner (future upgrade)
Fetches token balances and NFT ownership directly from blockchain.

---

# Repository Structure

bags-reward-system/

bot.py  
reward_engine.py  
wallet_distributor.py  
requirements.txt  
README.md  

config/  
example_wallets.json  

---

# Installation

Clone the repository:

git clone https://github.com/yourname/bags-reward-system

Install dependencies:

pip install -r requirements.txt

---

# Environment Variables

Create a `.env` file:

TWITTER_API_KEY=
TWITTER_API_SECRET=
TWITTER_ACCESS_TOKEN=
TWITTER_ACCESS_SECRET=

BOT_PRIVATE_KEY=
RPC_URL=
TOKEN_CONTRACT=
NFT_CONTRACT=

---

# Running the Bot

python bot.py

The bot will:

1. Read wallet balances
2. Calculate rewards
3. Send payouts
4. Post Twitter updates

---

# Planned Features

Future upgrades may include:

• automatic Bags.fm token detection  
• real blockchain holder scanning  
• reward dashboards  
• Telegram + Discord bots  
• leaderboard system  
• anti-sybil wallet filtering  
• automated daily reward distributions  

---

# License

Open source – free to modify and integrate with your Bags.fm token project.