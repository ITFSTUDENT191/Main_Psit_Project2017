"""ProjectPSIT2017"""
import pandas as pd
import pygal
def main():
    """ReadData & Plotgraph"""
    chart = pygal.Bar(title=' Total Imported Value ')
    datalist = []
    address = 'C:/Users/weerapat/Documents/GitHub/Main_Psit_Project2017/Data/ImportedValue.csv'
    data = pd.read_csv(address)
    datalist.append(data)
    liststr = [str(i) for i in datalist]
    datalist = liststr[0].split()
    datalist = datalist[2:]
    years = []
    for i in datalist:
        if i in '1011121314151617181920':
            datalist.remove(i)
    for i in datalist:
        if i[:3] == '255':
            years.append(i)
            datalist.remove(i)
    datalist = [float(i) for i in datalist]
    chart.x_labels = [i for i in years]
    chart.add('ImportedValue', datalist)
    chart.render_in_browser()
main()
