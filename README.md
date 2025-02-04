# LayerEdge Node Bot

If you're farming the [Layer Edge](https://dashboard.layeredge.io/) incentivized node project and find periodically starting the node, performing daily streaks a hassle, or you would like to sybil multiple accounts to maximize rewards without being detected, then this bot is for you.

## 🚀 Features

- Auto register/refer with referral code if account not created.
- Auto starts a light node.
- Auto claim daily streaks/node points every 24 hours.
- Colorful display of  dashboard points and referrals.
- Supports proxy integration.

## 📌 Setup

Follow these steps to set up and run the bot.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Anzywiz/LayerEdge-node-bot.git
cd LayerEdge-node-bot
```

### 2️⃣ Create and Activate a Virtual Environment

#### **Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

#### **Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure the Bot

Create a `config.json` file in the project directory with the following structure:

#### **For Linux/Mac:**

```bash
nano config.json
```

#### **config.json Example:**

```json
{
  "private_keys": ["your_private_key1", "your_private_key2"],
  "proxies": "https://username:password@proxy_address:port",
  "referral_code": "kejjtEBA"
}
```

- Replace `your_private_key1` and `your_private_key2` with your actual private keys of a registered or unregistered burner account.
- Set `proxies` in the format above or to `null` if you don't have one.

### 5️⃣ Run the Bot

```bash
python main.py
```

## 🔄 Updates

Stay tuned for updates and improvements!

## 🛠 Issues & Contributions

- If you encounter any issues, please report them in the **[Issues](https://github.com/Anzywiz/LayerEdge-node-bot/issues)** section.
- 💡 Want to improve the bot? Fork the repository, make your changes, and submit a **pull request (PR)**! Contributions are always welcome.

## 📜 License

This project is licensed under the **MIT License**.

⭐ **Don't forget to star the repo if you find it useful! Your support helps keep the project growing!** 😊

