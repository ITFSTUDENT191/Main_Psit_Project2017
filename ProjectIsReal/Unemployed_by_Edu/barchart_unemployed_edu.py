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
    plt.xticks([4, 11, 18, 25, 32, 39, 46, 53, 60, 67], xtick)
    plt.bar([1, 8, 15, 22, 29, 36, 43, 50, 57, 64], y_1, label="Primary School or lower", width=1, color="cyan")
    plt.bar([2, 9, 16, 23, 30, 37, 44, 51, 58, 65], y_2, label="Junior High School", width=1, color="skyblue")
    plt.bar([3, 10, 17, 24, 31, 38, 45, 52, 59, 66], y_3, label="Senior High School", width=1, color="cadetblue")
    plt.bar([4, 11, 18, 25, 32, 39, 46, 53, 60, 67], y_4, label="Vocational Certificate", width=1, color="blue")
    plt.bar([5, 12, 19, 26, 33, 40, 47, 54, 61, 68], y_5, label="High Vocational Certificate", width=1, color="royalblue")
    plt.bar([6, 13, 20, 27, 34, 41, 48, 55, 62, 69], y_6, label="Bachelor’s degree or higher", width=1, color="midnightblue")
    plt.title("People in Thailand who are unemployed in percentage\n(Educational background)", fontsize="15", color="orange")
    plt.xlabel("Years")
    plt.ylabel("Percent of people")
    plt.legend()
    plt.show()
main()
