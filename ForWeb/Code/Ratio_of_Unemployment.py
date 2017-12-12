"""ProjectPSIT2017"""
import pandas as pd
import pygal
def main():
    """ReadData & Plotgraph"""
    chart = pygal.Pie(title=' Ratio of Unemployment, Rate by sex')
    datalist = []
    address = 'C:/Users/HP/Documents/GitHub/Main_Psit_Project2017/Data/Unemployed_Male-Female_Percentage_2550-2559.csv'
    data = pd.read_csv(address)
    datalist.append(data)
    liststr = [str(i) for i in datalist]
    datalist = liststr[0].split()
    datalist = datalist[2:]
    for i in datalist:
        if i in '1011121314151617181920':
            datalist.remove(i)
    male = []
    male.append(datalist[0])
    female = []
    female.append(datalist[1])
    male = [float(i) for i in male]
    female = [float(i) for i in female]
    chart.add('Male', male)
    chart.add('Female', female)
    chart.render_in_browser()
main()
