"""ProjectPSIT2017"""
import pandas as pd
import pygal
def main():
    """ReadData & Plotgraph"""
    chart = pygal.Bar(title=' Graph of Unemployment (Percentage), Rate by region, Whole Kingdom: 2550 - 2559 ')
    datalist = []
    address = 'C:/Users/HP/Documents/GitHub/Main_Psit_Project2017/Data/Unemployed Rate by region.csv'
    data = pd.read_csv(address)
    datalist.append(data)
    lisstr = [str(i) for i in datalist]
    datalist = lisstr[0].split()
    datalist = datalist[5:]
    years = []
    central = []
    north = []
    northeast = []
    south = []
    for i in datalist:
        if i in '11121314151617181920':
            datalist.remove(i)
    for i in datalist:
        if i[0:3] == '255':
            years.append(i)
            datalist.remove(i)
    for i in range(len(datalist))[3::4]:
        south.append(datalist[i])
    for i in range(len(datalist))[2::4]:
        northeast.append(datalist[i])
    for i in range(len(datalist))[1::4]:
        north.append(datalist[i])
    for i in range(len(datalist))[::4]:
        central.append(datalist[i])
    central = [float(i) for i in central]
    north = [float(i) for i in north]
    northeast = [float(i) for i in northeast]
    south = [float(i) for i in south]
    chart.x_labels = [i for i in years]
    chart.add('Central', central)
    chart.add('North', north)
    chart.add('NorthEastern', northeast)
    chart.add('Southern', south)
    chart.render_in_browser()
main()
