"""Plot Graph to Show Unemployed people in Thailand"""

import matplotlib.pyplot as plt
def main():
    """Plot graph from people in Thailand who are unemployed"""
    x = range(10)
    y = [508475, 521980, 572336, 402181, 264339, 259094, 283520, 322675, 340561, 377466]
    xtick = ("2550", "2551", "2552", "2553", "2554", "2555", "2556", "2557", "2558", "2559")
    plt.xticks(x, xtick)
    plt.plot(x, y, color="red", marker="o", label=("Number of people who are unemployed"))
    plt.title("People in Thailand \nwho are unemployed in number", fontsize="15", color="orange")
    plt.xlabel("Years")
    plt.ylabel("Number of people")
    plt.legend()
    plt.show()
main()
