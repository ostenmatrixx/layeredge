import random
import colorlog


def get_random_user_agent():
    base_user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{chrome_version} Safari/{webkit_version}",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{chrome_version} Safari/{webkit_version}",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{chrome_version} Safari/{webkit_version}",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/{webkit_version} (KHTML, like Gecko) Firefox/{firefox_version}",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:{firefox_version}) Gecko/20100101 Firefox/{firefox_version}",
    ]

    webkit_version = f"{random.randint(500, 600)}.{random.randint(0, 50)}"
    chrome_version = f"{random.randint(80, 100)}.0.{random.randint(4000, 5000)}.{random.randint(100, 150)}"
    firefox_version = f"{random.randint(80, 100)}.0"

    user_agent = random.choice(base_user_agents).format(
        webkit_version=webkit_version,
        chrome_version=chrome_version,
        firefox_version=firefox_version
    )

    return user_agent


headers = {
    "authority": "referralapi.layeredge.io",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    # "if-none-match": 'W/"18d-DMBpfZJLWTa3s639F+U01JBs3HI"',
    "origin": "https://dashboard.layeredge.io",
    "priority": "u=1, i",
    "referer": "https://dashboard.layeredge.io/",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": get_random_user_agent()
}

# colog formatter
formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s: %(asctime)s: %(message)s',
    log_colors={
        'DEBUG': 'green',
        'INFO': 'cyan',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white'
    },
    datefmt='%Y-%m-%d %H:%M:%S'
)

handler = colorlog.StreamHandler()
handler.setFormatter(formatter)

logger = colorlog.getLogger()
logger.addHandler(handler)
logger.setLevel(colorlog.INFO)
