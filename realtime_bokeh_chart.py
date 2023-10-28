from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, curdoc
from bokeh.layouts import layout
from datetime import datetime
import random
from functools import partial
import pandas as pd

df = pd.read_csv('tips.csv')
x_data = df['Total_bill']
y_data = df['Tip']
source = ColumnDataSource(data=dict(x=x_data, y=y_data))

# Dummy-Daten für das Beispiel
# x_data = [datetime.now()]
# y_data = [random.randint(0, 100)]
# source = ColumnDataSource(data=dict(x=x_data, y=y_data))

# Bokeh-Figure erstellen
plot = figure(title='Echtzeitdiagramm', x_axis_label='Total Bill', y_axis_label='Tip', width=800, height=400)
line = plot.scatter('x', 'y', source=source, line_width=2)

# Daten in Echtzeit aktualisieren
def update_data():
    df = pd.read_csv('tips.csv')
    new_data = dict(x=df['Total_bill'], y=df['Tip'])
    source.stream(new_data, rollover=None)

# Bokeh-Layout erstellen
layout = layout([[plot]])

# Echtzeitaktualisierung alle 1000 Millisekunden
# curdoc().add_periodic_callback(partial(update_data), 1000)
update_data()

# Die Webanwendung öffnen (normalerweise unter http://localhost:5006/)
curdoc().title = "Echtzeitdiagramm mit Bokeh"
curdoc().add_root(layout)

'''
cli-befehl um Server zu starten:
bokeh serve realtime_bokeh_chart.py
'''