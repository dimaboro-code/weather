import requests


cities = {
  'London': '?MmnqT&lang=ru',
  'Шереметьево': '?MmnqT&lang=ru', 
  'Череповец': '?MmnqT&lang=ru'
}


def get_weather(cities: dict):
  url_form = 'https://wttr.in/{}{}'
  
  for city in cities:
    url = url_form.format(city, cities[city])
    response = requests.get(url)
    response.raise_for_status()
    yield response.text


if __name__ == '__main__':
  for weather in get_weather(cities):
    print(weather)