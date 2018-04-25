import requests

def get_megumin(useragent='Megumin.py/v0.1.0/Development'):
    r = requests.get('https://megumin.torque.ink/api/explosion', headers={'User-Agent': useragent})
    rj = r.json()
    return rj
