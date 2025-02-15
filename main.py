import asyncio
from utils import main, data, logging

private_keys = data.get("private_keys", [])


proxies = data.get('proxies', [])

if proxies:
    logging.info('Bot configured with Proxies!')
else:
    logging.warning('Bot NOT configured with Proxies!!')

referral_codes = data.get("referral_codes", [])
asyncio.run(main(private_keys, referral_codes))
