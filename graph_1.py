"""Plot Graph to Show Unemployed people in Thailand"""

import matplotlib.pyplot as plt
def main():
    """Plot graph from people in Thailand who are unemployed"""
    x = range(2550, 2560)
    y = [508475, 521980, 572336, 402181, 264339, 259094, 283520, 322675, 340561, 377466]
    plt.plot(x, y, color="red", marker="o", label=("Number of people who are unemployed"))
    plt.title("People in Thailand who are unemployed in number")
    plt.xlabel("Years")
    plt.ylabel("Number of people")
    plt.legend()
    plt.show()
main()
