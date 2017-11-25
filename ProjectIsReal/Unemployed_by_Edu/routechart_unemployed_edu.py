"""Plot Graph to Show Unemployed people in Thailand"""

import matplotlib.pyplot as plt
def main():
    """Plot graph from people in Thailand who are unemployed"""
    x = range(10)
    y_01 = [0.777, 0.767, 0.805, 0.51, 0.345, 0.355, 0.305, 0.405, 0.3, 0.42]
    y_02 = [2.06, 2.16, 2.2575, 1.49, 0.93, 1.1975, 0.905, 1.175, 1.03, 1.246]
    y_03 = [1.9725, 1.83, 1.88, 1.2475, 0.8025, 1.0825, 0.875, 0.9725, 1.13, 1.136]
    y_04 = [1.91, 2.3625, 2.56, 1.61, 1.025, 1.22, 1.095, 1.1925, 1.136, 1.606]
    y_05 = [2.915, 2.7825, 3.1525, 1.97, 1.33, 1.7625, 1.625, 1.307, 1.436, 1.63]
    y_06 = [2.505, 2.34, 2.5425, 2.2975, 1.37, 1.69, 1.57, 1.54, 1.63, 1.45]
    xtick = ("2550", "2551", "2552", "2553", "2554", "2555", "2556", "2557", "2558", "2559")
    plt.xticks(x, xtick)
    plt.plot(x, y_01, color="red", marker="o", label=("Primary School or lower"))
    plt.plot(x, y_02, color="green", marker="o", label=("Junior High School"))
    plt.plot(x, y_03, color="blue", marker="o", label=("Senior High School"))
    plt.plot(x, y_04, color="orange", marker="o", label=("Vocational Certificate"))
    plt.plot(x, y_05, color="pink", marker="o", label=("High Vocational Certificate"))
    plt.plot(x, y_06, color="brown", marker="o", label=("Bachelor’s degree or higher"))
    plt.title("People in Thailand who are unemployed in percentage\n(Educational background)", fontsize="13", color="orange")
    plt.xlabel("Years")
    plt.ylabel("Percent of people")
    plt.legend()
    plt.show()
main()
