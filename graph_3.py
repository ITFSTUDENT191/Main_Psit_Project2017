"""Plot Graph to Show Unemployed people in Thailand"""

import matplotlib.pyplot as plt
def main():
    """Plot graph from people in Thailand who are unemployed"""
    x = range(10)
    y_1 = [0.777, 0.767, 0.805, 0.51, 0.345, 0.355, 0.305, 0.405, 0.3, 0.42]
    y_2 = [2.06, 2.16, 2.2575, 1.49, 0.93, 1.1975, 0.905, 1.175, 1.03, 1.246]
    y_3 = [1.9725, 1.83, 1.88, 1.2475, 0.8025, 1.0825, 0.875, 0.9725, 1.13, 1.136]
    y_4 = [1.91, 2.3625, 2.56, 1.61, 1.025, 1.22, 1.095, 1.1925, 1.136, 1.606]
    y_5 = [2.915, 2.7825, 3.1525, 1.97, 1.33, 1.7625, 1.625, 1.307, 1.436, 1.63]
    y_6 = [2.505, 2.34, 2.5425, 2.2975, 1.37, 1.69, 1.57, 1.54, 1.63, 1.45]
    xtick = ("2550", "2551", "2552", "2553", "2554", "2555", "2556", "2557", "2558", "2559")
    plt.xticks([4, 10, 16, 22, 28, 34, 40, 46, 52, 58], xtick)
    plt.bar([1, 7, 13, 19, 25, 31, 37, 43, 49, 55], y_1, label="Partom or lower", width=0.5)
    plt.bar([2, 8, 14, 20, 26, 32, 38, 44, 50, 56], y_2, label="MattayomTon", width=0.5)
    plt.bar([3, 9, 15, 21, 27, 33, 39, 45, 51, 57], y_3, label="MattayomPly", width=0.5)
    plt.bar([4, 10, 16, 22, 28, 34, 40, 46, 52, 58], y_4, label="R She Wa", width=0.5)
    plt.bar([5, 11, 17, 23, 29, 35, 41, 47, 53, 59], y_5, label="Vichachep Kan Sung", width=0.5)
    plt.bar([6, 12, 18, 24, 30, 36, 42, 48, 54, 60], y_6, label="Udomsuksa", width=0.5)
    plt.title("EIEIZA", fontsize="15", color="orange")
    plt.xlabel("Years")
    plt.ylabel("Percent of people")
    plt.legend()
    plt.show()
main()
