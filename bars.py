import json
import os
from math import sqrt


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    return max(data, key=lambda bar: bar['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda bar: bar['SeatsCount'])


def get_closest_bar(data, latitude, longitude):
    return min(data, key=lambda data: get_distance(latitude, longitude, data['geoData']['coordinates']))


def get_distance(x1, y1, point):
    return sqrt((x1 - point[0])**2 + (y1 - point[1])**2)


if __name__ == '__main__':

    all_bars = load_data(input("Введите путь к файлу с барами: "))

    x = float(input("Введите долгота(пример - 37.609253): "))
    y = float(input("Введите широту(пример - 55.741227): "))

    print("Самый большой бар - %s, количество мест - %s" % (
        get_biggest_bar(all_bars)['Name'],
        get_biggest_bar(all_bars)['SeatsCount']))

    print("Самый маленький бар - %s, количество мест - %s" % (
        get_smallest_bar(all_bars)['Name'],
        get_smallest_bar(all_bars)['SeatsCount']))

    c_bar = get_closest_bar(all_bars, x, y)
    print("Ближайший бар называется -  %s, находится по адресу - %s" % (c_bar["Name"], c_bar["Address"]))
