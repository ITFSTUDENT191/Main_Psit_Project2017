"""PSITProject2017"""
import pandas as pd
import pygal
def main():
    """Main Function"""
    while 1:
        print('Welcome to my project !!!')
        print('Press [0] for Exit Program')
        print('Press [1] for Graph of Unemployment, Whole Kingdom')
        print('Press [2] for Graph of Unemployment, Rate by Sex')
        print('Press [3] for Graph of Unemployment, Rate by Region')
        print('Press [4] for Graph of Total Labor Force')
        print('Press [5] for Ratio of Unemployment')
        print('Press [6] for Graph of Total Employed & Unemployed')
        action = input()
        if action == '0':
            break
        elif action == '1':
            kingdom()
        elif action == '2':
            choose_sex()
        elif action == '3':
            region()
        elif action == '4':
            laborforce()
        elif action == '5':
            ratio()
        elif action == '6':
            total()
            
def kingdom():
    """ReadData & Plotgraph"""
    chart = pygal.Bar(title=' Graph of Unemployment (Number), Whole Kingdom: 2550 - 2559 ')
    datalist = []
    address = 'C:/Users/HP/Documents/GitHub/Main_Psit_Project2017/Data/Unemployed50-59_Number_.csv'
    data = pd.read_csv(address)
    datalist.append(data)
    lisstr = [str(i) for i in datalist]
    datalist = lisstr[0].split()
    datalist = datalist[2:]
    years = []
    for i in datalist:
        if i in '0123456789':
            datalist.remove(i)
    for i in datalist:
        if i[:3] == '255':
            years.append(i)
            datalist.remove(i)
    datalist = [float(i) for i in datalist]
    for i in range(len(years)):
        chart.add(years[i], datalist[i])
    chart.render_in_browser()

def choose_sex():
    """ChooseGraph Rate By Sex"""
    print('Press [1] for NumberGraph')
    print('Press [2] for PercentageGraph')
    print('Press [0] Back to Menu')
    action = input()
    if action == '1':
        sexnum()
    elif action == '2':
        sexper()
        
def sexnum():
    """ReadData & Plotgraph"""
    chart = pygal.Bar(title=' Graph of Unemployment (Number), Rate by Sex, Whole Kingdom: 2550 - 2559 ')
    datalist = []
    address = 'C:/Users/HP/Documents/GitHub/Main_Psit_Project2017/Data/Unemployed Rate by sex - Number.csv'
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

def sexper():
    """ReadData & Plotgraph"""
    chart = pygal.Bar(title=' Graph of Unemployment (Percentage), Rate by Sex, Whole Kingdom: 2550 - 2559 ')
    datalist = []
    address = 'C:/Users/HP/Documents/GitHub/Main_Psit_Project2017/Data/Unemployed Rate by sex - Percentage.csv'
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

def region():
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

def laborforce():
    """Choose way for graph"""
    print('Press [1] for Population in Labor force')
    print('Press [2] for Population not in Labor force')
    print('Press [0] Back to Menu')
    action = input()
    if action == '1':
        in_laborforce()
    elif action == '2':
        not_in_laborforce()
        
def in_laborforce():
    """ReadData & Plotgraph"""
    chart = pygal.Bar(title=' Graph of Total Labor force ')
    datalist = []
    address = 'C:/Users/HP/Documents/GitHub/Main_Psit_Project2017/Data/LaborForce_All.csv'
    data = pd.read_csv(address)
    datalist.append(data)
    liststr = [str(i) for i in datalist]
    datalist = liststr[0].split()
    datalist = datalist[3:]
    years = []
    male = []
    female = []
    for i in datalist:
        if i in '1011121314151617181920':
            datalist.remove(i)
    for i in datalist:
        if i[:3] == '255':
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

def not_in_laborforce():
    """ReadData & Plotgraph"""
    chart = pygal.Bar(title=' Graph of Population Who Not in Labor force ')
    datalist = []
    address = 'C:/Users/HP/Documents/GitHub/Main_Psit_Project2017/Data/Not_in_LaborForce_All.csv'
    data = pd.read_csv(address)
    datalist.append(data)
    liststr = [str(i) for i in datalist]
    datalist = liststr[0].split()
    datalist = datalist[3:]
    years = []
    male = []
    female = []
    for i in datalist:
        if i in '1011121314151617181920':
            datalist.remove(i)
    for i in datalist:
        if i[:3] == '255':
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

def ratio():
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

def total():
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
