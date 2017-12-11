"""ProjectPSIT2017"""
import pandas as pd
import pygal
def main():
    """ReadData & Plotgraph"""
    chart = pygal.Bar(title='Supply & Demand, Rate by faculty')
    datalist = []
    address = 'C:/Users/HP/Documents/Github/Main_Psit_Project2017/Data/Skill.csv'
    data = pd.read_csv(address)
    datalist.append(data)
    liststr = [str(i) for i in datalist]
    datalist = liststr[0].split()
    datalist = datalist[3:]
    supply = []
    demand = []
    faculty = []
    for i in datalist:
        if i in '1011121314151617181920':
            datalist.remove(i)
            for i in datalist:
                if i.isalpha():
                    datalist.remove(i)
                    faculty.append(i)
    for i in range(len(datalist)):
        if i%2 == 0:
            supply.append(datalist[i])
        else:
            demand.append(datalist[i])
    demand = [float(i) for i in demand]
    supply = [float(i) for i in supply]
    chart.x_labels = [i for i in faculty]
    chart.add('Supply', supply)
    chart.add('Demand', demand)
    chart.render_in_browser()
main()
