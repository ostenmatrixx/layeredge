Here is the content formatted as a README.md with proper Markdown syntax:

---

# LayerEdge Node Bot

This bot automates the process of farming the LayerEdge incentivized node project. It helps you manage your nodes, claim rewards, and maximize your farming potential, including support for multiple accounts and proxies.

## 🚀 Features

- Auto-register and refer using your referral code if an account is not created.
- Automatically starts a light node.
- Automatically claims daily streaks and node points every 24 hours.
- Displays dashboard points and referrals with a colorful interface.
- Supports proxy integration for multiple accounts.

## 📌 Setup

Follow these steps to set up and run the bot.

### -- Clone the Repository --

```bash
git clone https://github.com/ostenmatrixx/layeredge.git
cd layeredge
```

### -- Create Virtual Environment --

#### **Linux/WSL:**

```bash
python3 -m venv venv
source venv/bin/activate
```

#### **Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### -- Install Dependencies --

```bash
pip install -r requirements.txt
```

### -- Generate Private Keys (Optional) --

#### **Linux/WSL:**

```bash
python3 key.py
```

#### **Windows:**

```bash
python key.py
```

Once the keys are generated, you can find your private keys in the `pk.txt` file.

### -- Running the Bot --

1. Import your private keys from `pk.txt` (skip this step if you generated keys using `key.py`).
2. Import proxies from `proxy.txt` (1 proxy = 1 private key).
3. Open `config.py`, go to line 36, and enter your own referral code.

#### Run `config.py` in the terminal:

#### **Linux/WSL:**

```bash
python3 config.py
```

#### **Windows:**

```bash
python config.py
```

This will generate the `config.json` file with your proxies, private keys, and referral code.

### -- Start the Bot --

Once the configuration is set up, you can start the bot.

#### **Linux/WSL:**

```bash
python3 main.py
```

#### **Windows:**

```bash
python main.py
```

---

This is now ready to be copied into a `README.md` file!
