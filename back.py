import pandas as pd
import plotly.express as px

def new_data():
	df = pd.read_csv('PA OFFICE.csv')
	global df_access
	df_new = df[['actor.display_name', 'event.published', 'event.type.category', 'target4.display_name']].copy()
	df_new['count'] = 1

	df_access = df_new.loc[df_new['event.type.category'] == 'ACCESS']
	df_access = df_access.dropna()
	table = df_access.groupby('actor.display_name').count().sort_values('count', ascending = False)['event.published']

	return table

def plot():
	fig = px.histogram(df_access, x = 'actor.display_name', title = 'Total number of entry/exit throught 1st Augusts work week (1st-5th days)').update_xaxes(categoryorder = 'total ascending')

	fig.update_layout(
    	xaxis_title = '',
    	yaxis_title = 'total number of events'
	)

	fig.update_traces(hovertemplate='Employee name: %{x} <br>Event number through week: %{y}')

	return fig

def line_plot():
	global full
	test = pd.melt(df_access, id_vars = 'actor.display_name', value_vars = 'event.published')
	test['hour'] = pd.to_datetime(test['value']).dt.hour
	full = test.sort_values(['actor.display_name', 'value'], ascending = [True, False]).reset_index(drop = True)
	fig = px.line(full, x = 'value', y = 'hour' , color = 'actor.display_name', markers = True)

	return fig

def final():
	full_save = full.drop(columns=['variable', 'hour'])

	return full_save