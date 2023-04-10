import requests


''' Погода
Получение данных о погоде в трех городах в нужном формате.
Для каждого города задаются собственные настройки вывода информации.
Данные о погоде запрашиваются у сервиса wttr.in
Вывод осуществляется в консоль
Программа не требует ввода данных
'''


cities = {
  'London': '?MmnqT&lang=ru',
  # 'San Francisco': '?nTqu&lang=en', - понравилась идея регулировать формат
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