import json
from math import sin, cos, sqrt, atan2, radians


def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл %s не найден" % filepath)


def get_biggest_bar(data):
    biggest_bar = data[0]
    for bar in data:
        if bar['Cells']['SeatsCount'] > biggest_bar['Cells']['SeatsCount']:
            biggest_bar = bar
    return biggest_bar


def get_smallest_bar(data):
    smallest_bar = data[0]
    for bar in data:
        if bar['Cells']['SeatsCount'] < smallest_bar['Cells']['SeatsCount']:
            smallest_bar = bar
    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    rad = 6373.0
    lon1 = radians(longitude)
    lat1 = radians(latitude)
    max_distance = 9999999
    closest_bar = None

    for bar in data:
        lon2 = radians(bar["Cells"]["geoData"]["coordinates"][0])
        lat2 = radians(bar["Cells"]["geoData"]["coordinates"][1])
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = rad * c
        if max_distance > distance:
            closest_bar = [bar, distance]
            max_distance = distance

    return closest_bar

if __name__ == '__main__':

    all_bars = load_data(input("Введите путь к файлу с барами: "))

    x = float(input("Введите долгота(пример - 37.609253): "))
    y = float(input("Введите широту(пример - 55.741227): "))

    print("Самый большой бар - %s, количество мест - %s" % (
        get_biggest_bar(all_bars)['Cells']['Name'],
        get_biggest_bar(all_bars)['Cells']['SeatsCount']))

    print("Самый маленький бар - %s, количество мест - %s" % (
        get_smallest_bar(all_bars)['Cells']['Name'],
        get_smallest_bar(all_bars)['Cells']['SeatsCount']))

    c_bar = get_closest_bar(all_bars, x, y)
    print("Ближайший бар называется -  %s, находится по адресу - %s , расстояние до него - %s км" % (
        c_bar[0]["Cells"]["Name"],
        c_bar[0]["Cells"]["Address"],
        '%.1f' % round(c_bar[1], 1)
    ))


