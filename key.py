from eth_account import Account
from web3 import Web3
import time

num_keys = 5  # Set the number of key pairs you wanted to generate !

with open("pk.txt", "a") as priv_file, open("ad.txt", "a") as pub_file:
    for _ in range(num_keys):
        private_key = Account.create()._private_key.hex()
        address = Account.from_key(private_key).address
        priv_file.write(f"{private_key}\n")
        pub_file.write(f"{address}\n")
        print(f"Private Key: {private_key}")
        print(f"Address: {address}")
        time.sleep(0)

print("Key generation completed. Private and public keys have been saved.")
