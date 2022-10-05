# Bitly URL shortener

The script does:
1. If you enter any URL, it converts it to short link (using service www.bitly.com).
2. If you enter a short link, it displays a number of clicks for this link for all the time.

## Getting Started
Just run the script "python main.py"

```
python main.py
```
### Prerequisites
1. You need to install the python interpreter, "requests", "python-dotenv" modules.
2. Get your token here: https://app.bitly.com/settings/api/
3. Save token to the environment variable "BITLY_TOKEN". 

```
pip install -r requests.txt
pip install python-dotenv
```
### Usage
Note: put your link into "" if it contains symbols '='
1. Enter bitlink or any url

Example: "https://yandex.ru/pogoda/nizhny-novgorod?lat=56.236426&lon=43.846158"

Bitlink for your url:  https://bit.ly/3LXoM09

2. Enter bitlink or any url

https://bit.ly/3LXoM09

The number of clicks is  8
## Authors

* **Evgeny Melnikov** - *Initial work* - [Evgeny Melnikov](https://github.com/MelnikovEI)

## Acknowledgments

* Inspired by [Devman](https://dvmn.org/)
