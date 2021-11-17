import matplotlib.pyplot as plt
import random
import numpy as np


def plot():
    x = [1, 2, 3, 4]
    y = [2, 4, 2, 6]
    y1 = [e + 1 for e in y]
    y2 = [e + 2 for e in y]
    plt.plot(x, y, 'b.')
    plt.plot(x, y1, 'ro')
    plt.plot(x, y2, 'kx')
    plt.show()


def line_chart():
    x = [1, 2, 3, 4]
    y = [2, 4, 2, 6]
    y1 = [e + 1 for e in y]
    y2 = [e + 2 for e in y]
    y3 = [e + 3 for e in y]
    plt.plot(x, y, 'b.-')
    plt.plot(x, y1, 'ro--')
    plt.plot(x, y2, 'kx-.')
    plt.plot(x, y3, 'c*:')
    plt.show()


def bar():
    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]
    plt.bar(x, y, color='blue', edgecolor='red')
    plt.show()


def pie():
    lbs = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen']
    vals = [50, 20, 10, 20]
    ran = random.randint(0, 10)
    if ran % 2 == 0:
        plt.pie(vals, labels=lbs)
    else:
        explode = (0, 0.1, 0.2, 0)
        plt.pie(vals, labels=lbs, explode=explode)
    plt.show()


def draw_sin():
    x = np.linspace(0, np.pi * 2, 100)
    y = [np.sin(e) for e in x]
    plt.plot(x, y, color='red')
    plt.show()


def draw_normal():
    mu, sigma = 0, 0.1
    s = np.random.normal(mu, sigma, 1000)
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu) ** 2 / (2 * sigma ** 2)), linewidth=2,
             color='r')
    plt.show()


if __name__ == '__main__':
    draw_normal()
