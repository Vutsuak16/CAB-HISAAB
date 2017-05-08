from bokeh.models.widgets import PreText, Select, TextInput,DataTable, DateFormatter, TableColumn,RadioButtonGroup
import pandas as pd
import datetime
from bokeh.layouts import widgetbox,row
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.io import curdoc


numdays=3
base = datetime.date.today()
date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]
print date_list
x=[date_list,date_list,date_list,date_list]
y=[[2.0, 1.0, 4.0], [4.0, 7.0, 8.0],[12.0,11.0,12.0],[1.0,1.0,1.0]]
source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(plot_height=400, plot_width=400, title="cab-hisaab",x_axis_type="datetime",y_range=[0,100])

plot.multi_line('x','y',source=source,color=["firebrick", "navy","red","green"])

money = TextInput(title="MONEY", value="0.0")
cash_lalit = TextInput(title="Paid by Lalit", value="0.0")
cash_aditya = TextInput(title="Paid by Aditya", value="0.0")
cash_kaustuv = TextInput(title="Paid by Kaustuv", value="0.0")
cash_mvsn = TextInput(title="Paid by MVSN", value="0.0")

def update_data(attrname, old, new):

	m=float(money.value)
	l = float(cash_lalit.value)
	a = float(cash_aditya.value)
	k = float(cash_kaustuv.value)
	b=float(cash_mvsn.value)
	
	x=[date_list,date_list,date_list,date_list]
	y[0][2]=l
	print 
	y[1][2]=a
	y[2][2]=k
	y[3][2]=b

	print a

	source.data = dict(x=x, y=y)


for i in [money,cash_lalit,cash_aditya,cash_kaustuv,cash_mvsn]:
	i.on_change('value', update_data)


inputs = widgetbox(money,cash_lalit,cash_aditya,cash_kaustuv,cash_mvsn)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "CAB-HISAAB"
