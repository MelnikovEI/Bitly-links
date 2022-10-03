import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, url):
    shorten_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': 'Bearer {}'.format(token)}
    body = {"long_url": url}
    response_post = requests.post(shorten_url, headers=headers, json=body)
    response_post.raise_for_status()
    return response_post.json()['link']


def count_clicks(token, bitlink):
    headers = {'Authorization': 'Bearer {}'.format(token)}
    url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
    parsed = urlparse(bitlink)
    link_in_bitlink_format = f"{(parsed.hostname if parsed.hostname else '')}{parsed.path}"
    url = url_template.format(link_in_bitlink_format)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, url):
    headers = {'Authorization': 'Bearer {}'.format(token)}
    url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
    parsed = urlparse(url)
    link_in_bitlink_format = f"{(parsed.hostname if parsed.hostname else '')}{parsed.path}"
    url_get_bitlink_info = url_template.format(link_in_bitlink_format)
    response = requests.get(url_get_bitlink_info, headers=headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    my_token = os.environ['BITLY_TOKEN']
    try:
        input_link = input('Enter bitlink or any url\n')
        if is_bitlink(my_token, input_link):
            print('The number of clicks is ', count_clicks(my_token, input_link))
        else:
            print('Bitlink for your url: ', shorten_link(my_token, input_link))
    except requests.exceptions.HTTPError:
        print('Entered url is not valid!')
