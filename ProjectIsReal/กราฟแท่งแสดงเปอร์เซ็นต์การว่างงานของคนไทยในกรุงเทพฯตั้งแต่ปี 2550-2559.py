import pygal
line_chart = pygal.HorizontalBar()
line_chart.title = 'กราฟแสดงอัตราการว่างงานของคนในจังหวัดกรุงเทพมหานครตั้งแต่ปี 2550-2559'
percent = [1.2, 1.4, 1.3, 1.0, 0.7, 0.6, 0.7, 0.8, 1.0, 0.9]
for i in range(10):
    line_chart.add('255'+str(i), percent[i])
line_chart.render_in_browser()
