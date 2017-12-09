"""Plot Graph to Show Unemployed people in Thailand"""

import matplotlib.pyplot as plt
def main():
    """Plot graph from people around Thailand who are unemployed"""
    x = range(10)
    y_ban = [1.2, 1.4, 1.3, 1.0, 0.7, 0.6, 0.7, 0.8, 1.0, 0.9]
    y_nor = [1.4, 1.2, 1.3, 0.9, 0.6, 0.6, 0.6, 0.7, 0.8, 0.9]
    y_neas = [1.4, 1.4, 1.5, 1.0, 0.7, 0.7, 0.7, 0.7, 0.8, 0.9]
    y_sou = [1.3, 1.5, 1.8, 1.3, 0.8, 0.7, 1.0, 1.2, 1.1, 1.4]
    y_mid = [1.4, 1.4, 1.5, 1.1, 0.7, 0.7, 0.7, 0.9, 0.9, 1.0]
    xtick = ("2550", "2551", "2552", "2553", "2554", "2555", "2556", "2557", "2558", "2559")
    plt.xticks(x, xtick)
    plt.plot(x, y_ban, color="green", marker="o", label=("Bangkok"))
    plt.plot(x, y_nor, color="red", marker="o", label=("North"))
    plt.plot(x, y_neas, color="blue", marker="o", label=("North-East"))
    plt.plot(x, y_sou, color="pink", marker="o", label=("South"))
    plt.plot(x, y_mid, color="purple", marker="o", label=("Middle"))
    plt.title("People around Thailand \nwho are unemployed in percentage", fontsize="15", color="orange")
    plt.xlabel("Years")
    plt.ylabel("Percent of people")
    plt.legend()
    plt.show()
main()
