"""PSIT2017"""
import pygal
def main():
    """Render Employee or Unemployee"""
    chart = pygal.Line(title=u'Some different points')
    chart.x_labels = ('2550', '2551', '2552', '2553', '2554', '2555', '2556', '2557', '2558', '2559')
    num = int(input())
    if num == 1:
        chart.add('จำนวนผู้ว่างงาน', [508475, 521980, 572336, 402181, 264339, 259094, 283520, 322675, 340561, 377466])
    elif num == 2:
        chart.add('จำนวนผู้มีงานทำ', [36249454, 37016612, 37706321, 38037342, 38464667, 38939130, 38906889, 38077429, 38016169, 37692651])
    chart.render_in_browser()
main()
