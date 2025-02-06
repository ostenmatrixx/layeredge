import asyncio
from utils import main, data, logging

private_keys = data.get("private_keys", [])
if len(private_keys) >= 5:
    print(f"It seems you want to farm above 5 account!!."
          f"\nKindly check tg group for passcode: https://t.me/bot_arena_chat")
    prompt = input("Enter passcode: ")
    if int(prompt.strip()) == 12345:
        pass
    else:
        raise Exception("INVALID CODE!")

proxies = data.get('proxies')

if proxies:
    logging.info('Bot configured with Proxies!')
else:
    logging.warning('Bot NOT configured with Proxies!!')

referral_code = data.get("referral_code")
asyncio.run(main(private_keys, referral_code))
