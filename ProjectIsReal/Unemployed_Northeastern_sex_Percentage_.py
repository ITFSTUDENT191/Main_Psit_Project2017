"""ProjectPSIT2017"""
import pandas as pd
import pygal
def main():
    """ReadData & Plotgraph"""
    chart = pygal.Bar(title='A graph of employed and unemployed from 2550 to 2559 (Percentage)') #Name of graph
    datalist = [] #List for keep data
    address = 'C:/Users/HP/Documents/GitHub/Main_Psit_Project2017/Data/Unemployed_Northeastern_sex_Percentage.csv' #Address file
    data = pd.read_csv(address) #Readfile
    datalist.append(data) #append data to list
    lisstr = [str(i) for i in datalist] #Change type of data to str & keep it to [lisstr]
    datalist = lisstr[0].split() #Split data and keep it to [datalist]
    datalist = datalist[3:] #Remove Word
    years = [] #List for keep years
    for i in datalist:
        if i in '1011121314151617181920': #Check Number 0-20
            datalist.remove(i) #Remove Number
    for i in datalist:
        if i[:3] == '255':
            years.append(i) #Add to years list
            datalist.remove(i)
    datalist = [float(i) for i in datalist] #Change Type datalist to float
    for i in range(len(years)):
        chart.add(years[i], datalist[i])
    chart.render_in_browser() #RenderGraph
main()
