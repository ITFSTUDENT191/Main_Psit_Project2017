"""ProjectPSIT2017"""
import pandas as pd
import pygal
def main():
    """ReadData & Plotgraph"""
    chart = pygal.Pie(title='A graph of employed and unemployed from 2550 to 2559 (Percentage)') #สร้างกราฟ, กำหนดรูปแบบกราฟ และตั้งชื่อกราฟ
    datalist = [] #ลิสต์เปล่าๆเตรียมรับข้อมูล
    address = 'C:/Users/HP/Documents/GitHub/Main_Psit_Project2017/Data/Unemployed_South_sex_Percentage.csv' #บอกที่อยู่ไฟล์ CSV
    data = pd.read_csv(address) #สั่งอ่าน
    datalist.append(data) #จับสิ่งที่อ่านได้เข้าลิสต์ที่เตรียมไว้
    lisstr = [str(i) for i in datalist] #เปลี่ยนประเภทของข้อมูลทั้งหมดในลิสต์เป็นสตริง
    datalist = lisstr[0].split() #จับแยกข้อมูลแล้วเก็บใส่ลิสต์ที่ชื่อ datalist
    datalist = datalist[3:] #ลบหัวข้อในข้อมูลออกเพื่อให้เหลือแต่ตัวเลข
    years = [] #ลิสต์สำหรับเก็บข้อมูลปี
    for i in datalist:
        if i in '1011121314151617181920': #เช็คว่าเป็นเลข 0-20 มั้ย
            datalist.remove(i) #ถ้าใช่ สั่งลบออก เพราะไม่ใช่สิ่งที่ต้องการ
    for i in datalist: #สั่งวนลูปใน datalist
        if i[:3] == '255': #ถ้าตัวนั้นขึ้นต้นด้วย 255 (เป็นเลขนำหน้าปี)
            years.append(i) #เก็บเข้าลิสต์ปี
            datalist.remove(i) #ลบทิ้ง
    datalist = [float(i) for i in datalist] #เปลี่ยนประเภทข้อมูลจากสตริงเป็นจำนวนจริง ไม่งั้นสร้างกราฟไม่ได้เพราะเป็นสตริง
    for i in range(len(years)): #วนลูปตามความยาวของลิสต์ปี
        chart.add(years[i], datalist[i]) #แอดข้อมูลเข้ากราฟเป็น years ตำแหน่งที่ i กับ datalist ตำแหน่งที่ i (iวิ่งเป็นตัวเลข)
    chart.render_in_browser() #สั่งเรนเดอร์กราฟ
main()
