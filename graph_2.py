"""Plot Graph to Show Unemployed people in Thailand"""

import matplotlib.pyplot as plt
def main():
    """Plot graph from people in Thailand who are unemployed"""
    x = range(10)
    y = [1.376, 1.384, 1.489, 1.04, 0.679, 0.657, 0.71, 0.836, 0.88, 0.98]
    xtick = ("2550", "2551", "2552", "2553", "2554", "2555", "2556", "2557", "2558", "2559")
    plt.xticks(x, xtick)
    plt.plot(x, y, color="blue", marker="o", label=("Percentage of people who are unemployed"))
    plt.title("People in Thailand \nwho are unemployed in percentage", fontsize="15", color="orange")
    plt.xlabel("Years")
    plt.ylabel("Percent of people")
    plt.legend()
    plt.show()
main()
