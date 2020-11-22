import matplotlib.pyplot as plt


def small():
    x = [3, 3, 4, 4, 3]
    y = [4, 3, 3, 4, 4]
    plt.plot(x, y, 'ro:')


def medium():
    x = [2, 2, 5, 5, 2]
    y = [5, 2, 2, 5, 5]
    plt.plot(x, y, 'gs--')


def large():
    x = [1, 1, 6, 6, 1]
    y = [6, 1, 1, 6, 6]
    plt.plot(x, y, 'bp-')


small()
medium()
large()
plt.show()
