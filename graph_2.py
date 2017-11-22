"""Plot Graph to Show Unemployed people in Thailand"""

import matplotlib.pyplot as plt
def main():
    """Plot graph from people in Thailand who are unemployed"""
    x = range(2550, 2560)
    y = [0.9961, 1.0056, 1.0836, 0.7522, 0.4894, 0.4752, 0.5152, 0.5883, 0.6165, 0.6787]
    plt.plot(x, y, color="blue", marker="o", label=("Percentage of people who are unemployed"))
    plt.title("People in Thailand who are unemployed in percentage")
    plt.xlabel("Years")
    plt.ylabel("Percent of people")
    plt.legend()
    plt.show()
main()
