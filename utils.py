import asyncio
import logging
import time
import requests
from eth_account import Account
from eth_account.messages import encode_defunct
from typing import Optional
from datetime import datetime
from headers import headers
import json

try:
    # Load data from the JSON file
    with open('config.json', "r") as file:
        data = json.load(file)
except FileNotFoundError:
    raise FileNotFoundError(f"config.json file does not exist. Create one!")
except json.JSONDecodeError:
    raise ValueError(f"The config file is not a valid JSON file.")


def get_response(url: str, payload: Optional[dict] = None):
    """Make request with optional proxy support from config"""
    try:
        proxies = data.get('proxies')

        request_params = {
            'url': url,
            'headers': headers,
            'timeout': (3.05, 20),
            **({"proxies": {"http": proxies, "https": proxies}} if proxies else {})
        }
        if payload:
            response = requests.post(**request_params, json=payload)
        else:
            response = requests.get(**request_params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)
    except Exception as e:
        raise e


def short_address(wallet_address):
    address = f"{''.join(wallet_address[:5])}..{''.join(wallet_address[-5:])}"
    return address


def get_wallet_details(wallet_address):
    url = f"https://referralapi.layeredge.io/api/referral/wallet-details/{wallet_address}"
    wallet_info = get_response(url)['data']
    return wallet_info


def get_node_status(wallet_address):
    url = f"https://referralapi.layeredge.io/api/light-node/node-status/{wallet_address}"
    node_status = get_response(url)['data']
    return node_status


def register_wallet(wallet_address, referral_code):
    url = f"https://referralapi.layeredge.io/api/referral/register-wallet/{referral_code}"
    payload = {
        "walletAddress": f"{wallet_address}"
    }
    response = get_response(url, payload=payload)
    resp_message = response['message']
    logging.info(f"User {short_address(wallet_address)}: {resp_message}")
    return response


def sign_message(private_key: str, message: str) -> str:
    """
    Sign a message using an Ethereum private key.

    Args:
        private_key (str): The private key to sign with
        message (str): The message to sign

    Returns:
        str: The signature in hexadecimal format with 0x prefix
    """
    encoded_message = message.encode('utf-8')
    account = Account.from_key(private_key)
    signed_message = account.sign_message(encode_defunct(encoded_message))
    # Convert to proper hex format with 0x prefix
    return '0x' + signed_message.signature.hex()


def start_node(private_key):
    account = Account.from_key(private_key)
    wallet_address = str(account.address)

    timestamp = int(time.time() * 1000)
    message = f'Node activation request for {wallet_address} at {timestamp}'
    signature = sign_message(private_key, message)

    url = f"https://referralapi.layeredge.io/api/light-node/node-action/{wallet_address}/start"
    payload = {
        "sign": signature,
        "timestamp": timestamp
    }
    response = get_response(url, payload=payload)
    message = response['message']
    logging.info(f"User {short_address(wallet_address)}: {message}")

    start_timestamp = response['data']['startTimestamp']
    return start_timestamp


def claim_node_points(private_key):
    account = Account.from_key(private_key)
    wallet_address = str(account.address)

    timestamp = int(time.time() * 1000)
    message = f'I am claiming my daily node point for {wallet_address} at {timestamp}'
    signature = sign_message(private_key, message)

    url = "https://referralapi.layeredge.io/api/light-node/claim-node-points"
    payload = {
        "sign": signature,
        "timestamp": timestamp,
        "walletAddress": wallet_address
    }
    response = get_response(url, payload=payload)
    claim_msg = response['message']
    logging.info(f"User {short_address(wallet_address)}: {claim_msg}")
    return response


def get_time_left(target_timestamp):
    current_timestamp = int(datetime.now().timestamp())
    return target_timestamp - current_timestamp


def convert_time_left(time_left):
    """
    convert to human-readable time
    :param time_left:
    :return:
    """

    hours = int(time_left / 3600)
    minutes = int((time_left % 3600) / 60)
    seconds = int(time_left % 60)

    display_time_left = f"{hours} Hours {minutes} Mins" if hours > 0 else \
        f"{minutes} Minutes {seconds} Secs" if minutes > 0 else \
        f"{seconds} Seconds"

    return display_time_left


def verify_user(wallet_address, referral_code):
    try:
        user_details = get_wallet_details(wallet_address)
        # logging.info(f"User {short_address(wallet_address)}: User already registered!")
    except Exception as e:
        if 'user not found' in str(e):
            logging.warning(
                f"User {short_address(wallet_address)}: User NOT found. Registering user with ref code...")
            register_wallet(wallet_address, referral_code)
        else:
            raise e


def display_dashboard_logs(wallet_address):
    user_details = get_wallet_details(wallet_address)
    node_points = user_details['nodePoints']
    daily_streak = user_details['dailyStreak']
    referrals = user_details['referrals']
    total_points_ref = user_details['totalPoints']
    logging.info(
        f"User {short_address(wallet_address)}: Node points: {node_points}. Daily streak: {daily_streak}/7. "
        f"Referrals: {len(referrals)}. Referral Earnings: {total_points_ref}")


async def run_node(private_key, referral_code='kejjtEBA'):
    while True:
        account = Account.from_key(private_key)
        wallet_address = str(account.address)
        try:
            # check if the wallet account has been registered
            verify_user(wallet_address, referral_code)

            # grab user details  and display points
            display_dashboard_logs(wallet_address)

            # check if the light node has started running
            status = get_node_status(wallet_address)
            start_timestamp = status['startTimestamp']
            if start_timestamp:
                logging.info(f"User {short_address(wallet_address)}: Node already running")
            else:
                logging.info(f"User {short_address(wallet_address)}: Starting node...")
                start_node(private_key)
                logging.info(f"User {short_address(wallet_address)}: Node running...")

            logging.info(f"User {short_address(wallet_address)}: Waiting 1hr till next ping...")
            await asyncio.sleep(60 * 60 * 1)
        except Exception as e:
            logging.error(f"User {short_address(wallet_address)}: An Error occurred!\n{e}")
            await asyncio.sleep(10)


async def claim_daily_node_points(private_key):
    # claim streak node points
    while True:
        try:
            wallet_address = Account.from_key(private_key).address
            logging.info(f"User {short_address(wallet_address)}: Claiming node points...")

            claim_node_points(private_key)
            await asyncio.sleep(60 * 60 * 6)
        except Exception as e:
            wallet_address = Account.from_key(private_key).address
            if 'can not claim node points twice in 24 hours, come back after 24 hours!' in str(e):
                logging.warning(f"User {short_address(wallet_address)}: You have already claimed today's reward!")
            else:
                logging.error(f"User {short_address(wallet_address)}: {e}")
            await asyncio.sleep(60 * 60 * 6)


async def main(private_keys: list):
    # Create tasks for both functions for each private key
    tasks = []
    for private_key in private_keys:
        tasks.append(run_node(private_key))
        tasks.append(claim_daily_node_points(private_key))

    # Run all tasks concurrently
    await asyncio.gather(*tasks)
