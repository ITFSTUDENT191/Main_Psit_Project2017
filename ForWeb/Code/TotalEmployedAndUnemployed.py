"""ProjectPSIT2017"""
import pandas as pd
import pygal
def main():
    """ReadData & Plotgraph"""
    chart = pygal.Bar(title=' Graph of total employed and unemployed ')
    datalist = []
    address = 'C:/Users/HP/Documents/GitHub/Main_Psit_Project2017/Data/TotalEmployedAndUnemployed.csv'
    data = pd.read_csv(address)
    datalist.append(data)
    liststr = [str(i) for i in datalist]
    datalist = liststr[0].split()
    datalist = datalist[3:]
    years = []
    em = []
    un = []
    for i in datalist:
        if i in '1011121314151617181920':
            datalist.remove(i)
    for i in datalist:
        if i[:3] == '255':
            years.append(i)
            datalist.remove(i)
    for i in range(len(datalist)):
        if i%2 == 0:
            em.append(datalist[i])
        else:
            un.append(datalist[i])
    em = [float(i) for i in em]
    un = [float(i) for i in un]
    chart.x_labels = [i for i in years]
    chart.add('Employed', em)
    chart.add('Unemployed', un)
    chart.render_in_browser()
main()
