import requests


PAYLOAD = {
  'M': '',
  'm': '',
  'n': '',
  'q': '',
  'T': '',
  'lang': 'ru'
}
  
CITIES = [
  'London',
  'Шереметьево',
  'Череповец'
]


def get_weather(city):
    url = 'https://wttr.in/' + city
    response = requests.get(url, PAYLOAD)
    response.raise_for_status()
    return response.text


def main():
  for city in CITIES:
    print(get_weather(city))
  

if __name__ == '__main__':
  main()