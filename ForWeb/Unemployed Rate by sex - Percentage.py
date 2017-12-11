"""ProjectPSIT2017"""
import pandas as pd
import pygal
def main():
    """ReadData & Plotgraph"""
    chart = pygal.Bar(title=' Graph of Unemployment (Percentage), Rate by Sex, Whole Kingdom: 2550 - 2559 ')
    datalist = []
    address = 'C:/Users/HP/Desktop/Unemployed Rate by sex - Percentage.csv'
    data = pd.read_csv(address)
    datalist.append(data)
    lisstr = [str(i) for i in datalist]
    datalist = lisstr[0].split()
    datalist = datalist[3:]
    years = []
    male = []
    female = []
    for i in datalist:
        if i in '11121314151617181920':
            datalist.remove(i)
    for i in datalist:
        if i[0:3] == '255':
            years.append(i)
            datalist.remove(i)
    for i in range(len(datalist)):
        if i%2 == 0:
            male.append(datalist[i])
        else:
            female.append(datalist[i])
    male = [float(i) for i in male]
    female = [float(i) for i in female]
    chart.x_labels = [i for i in years]
    chart.add('Male', male)
    chart.add('Female', female)
    chart.render_in_browser()
main()
