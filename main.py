import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, url):
    shorten_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': 'Bearer {}'.format(token)}
    body = {"long_url": url}
    post_response = requests.post(shorten_url, headers=headers, json=body)
    post_response.raise_for_status()
    return post_response.json()['link']


def count_clicks(token, bitlink):
    headers = {'Authorization': 'Bearer {}'.format(token)}
    url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
    parsed_bitlink = urlparse(bitlink)
    short_link = f"{parsed_bitlink.netloc}{parsed_bitlink.path}"
    bitlink_url = url_template.format(short_link)
    response = requests.get(bitlink_url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, url):
    headers = {'Authorization': 'Bearer {}'.format(token)}
    url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
    parsed_url = urlparse(url)
    short_url = f"{parsed_bitlink.netloc)}{parsed_url.path}"
    bitlink_url = url_template.format(short_url)
    response = requests.get(bitlink_url, headers=headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    try:
        input_link = input('Enter bitlink or any url\n')
        if is_bitlink(token, input_link):
            print('The number of clicks is ', count_clicks(token, input_link))
        else:
            print('Bitlink for your url: ', shorten_link(token, input_link))
    except requests.exceptions.HTTPError:
        print('Entered url is not valid!')
