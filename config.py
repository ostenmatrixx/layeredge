import json
import random

def generate_config(pk_file, proxy_file, ref_file):
    # Read the private keys from pk.txt
    with open(pk_file, 'r') as pk_f:
        private_keys = [line.strip() for line in pk_f.readlines()]

    # Read the proxies from proxy.txt
    with open(proxy_file, 'r') as proxy_f:
        proxies = [line.strip() for line in proxy_f.readlines()]

    # Read the referral codes from ref.txt
    with open(ref_file, 'r') as ref_f:
        referral_codes = [line.strip() for line in ref_f.readlines()]

    # Check if the number of private keys matches the number of proxies
    if len(private_keys) != len(proxies):
        raise ValueError("The number of private keys does not match the number of proxies.")

    # Create the mapping for wallets to proxies
    wallets_to_proxies = {
        private_keys[i]: {
            "proxy": proxies[i]
        } for i in range(len(private_keys))
    }

    # Prepare the configuration data
    config_data = {
        "private_keys": private_keys,
        "proxies": proxies,
        "referral_codes": referral_codes,
        "wallets_to_proxies": wallets_to_proxies
    }

    # Write the config data to config.json
    with open('config.json', 'w') as json_f:
        json.dump(config_data, json_f, indent=4)

    print("config.json has been generated successfully.")

# Example usage
pk_file = 'pk.txt'      # Path to your pk.txt file
proxy_file = 'proxy.txt'  # Path to your proxy.txt file
ref_file = 'ref.txt'    # Path to your ref.txt file

generate_config(pk_file, proxy_file, ref_file)
