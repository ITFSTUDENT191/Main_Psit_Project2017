"""ProjectPSIT2017"""
import pandas as pd
import pygal
def main():
    """ReadData & Plotgraph"""
    chart = pygal.Bar(title='A graph of employed and unemployed from 2550 to 2559') #Name of graph
    datalist = [] #List for keep data
    address = 'E:/python project/github webdev/Main_Psit_Project2017/Data/Unemployed50-59.csv' #Address file
    data = pd.read_csv(address) #Readfile
    datalist.append(data) #append data to list
    lisstr = [str(i) for i in datalist] #Change type of data to str & keep it to [lisstr]
    datalist = lisstr[0].split() #Split data and keep it to [lis]
    datalist = datalist[2:] #Remove Word
    years = [] #List for keep years
    for i in datalist:
        if i in '0123456789': #Check Number 0-9
            datalist.remove(i) #Remove Number
    for i in datalist:
        if i[:3] == '255':
            years.append(i) #Add to years list
            datalist.remove(i)
    datalist = [int(i) for i in datalist] #Change Type datalist to int
    for i in range(len(years)):
        chart.add(years[i], datalist[i])
    chart.render_in_browser() #RenderGraph
main()
