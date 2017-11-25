"""Plot Graph to Show Unemployed people in Thailand"""

import matplotlib.pyplot as plt
def main():
    """Plot graph from people in Thailand who are unemployed"""
    x = range(10)
    y_ban = [1.2, 1.4, 1.3, 1.0, 0.7, 0.6, 0.7, 0.8, 1.0, 0.9]
    y_nor = [1.4, 1.2, 1.3, 0.9, 0.6, 0.6, 0.6, 0.7, 0.8, 0.9]
    y_neas = [1.4, 1.4, 1.5, 1.0, 0.7, 0.7, 0.7, 0.7, 0.8, 0.9]
    y_sou = [1.3, 1.5, 1.8, 1.3, 0.8, 0.7, 1.0, 1.2, 1.1, 1.4]
    y_mid = [1.4, 1.4, 1.5, 1.1, 0.7, 0.7, 0.7, 0.9, 0.9, 1.0]
    xtick = ("2550", "2551", "2552", "2553", "2554", "2555", "2556", "2557", "2558", "2559")
    plt.xticks([4, 11, 18, 25, 32, 39, 46, 53, 60, 67], xtick)
    plt.bar([1, 8, 15, 22, 29, 36, 43, 50, 57, 64], y_ban, label="Bangkok", width=1, color="cyan")
    plt.bar([2, 9, 16, 23, 30, 37, 44, 51, 58, 65], y_nor, label="North", width=1, color="skyblue")
    plt.bar([3, 10, 17, 24, 31, 38, 45, 52, 59, 66], y_neas, label="North-East", width=1, color="cadetblue")
    plt.bar([4, 11, 18, 25, 32, 39, 46, 53, 60, 67], y_sou, label="South", width=1, color="blue")
    plt.bar([5, 12, 19, 26, 33, 40, 47, 54, 61, 68], y_mid, label="Middle", width=1, color="royalblue")
    plt.title("People around Thailand \nwho are unemployed in percentage", fontsize="15", color="orange")
    plt.xlabel("Years")
    plt.ylabel("Percent of people")
    plt.legend()
    plt.show()
main()
