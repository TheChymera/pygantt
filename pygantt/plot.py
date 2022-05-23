import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import os

def gantt(schedule,
	title="",
	show=False,
	save_as=False,
	):
	"""Plot Gantt Chart based on CSV input file.

	Parameters
	----------
	schedule : str
		Path to CSV schedule file with columns which include "Task", "start", "end", "color", and "completion".
		Row values should include datetime or integers under "start" and "end", matplotlib interpretable color values under "color", and integers from 0 to 100 under "completion".
	title : str, optional
		String to use as plot title.
	show : bool, optional
		Whether to show the plot in a graphical window.
	save_as : str, optional
		Path under which to save the plot.

	Notes
	-----
	* Parameterize and/or enable dynamic duration markers (currently days for nummerical mode and weeks for date mode).
	"""

	# Data read-in
	schedule = os.path.abspath(os.path.expanduser(schedule))
	df = pd.read_csv(schedule)
	df.head()

	# is this numerical?
	numerical = all(df.start.astype(str).str.isnumeric()) and all(df.end.astype(str).str.isnumeric())

	# Convert dates to datetime format
	if not numerical:
		df.start = pd.to_datetime(df.start)
		df.end = pd.to_datetime(df.end)

	# Compute Duration
	df['duration'] = df.end-df.start
	if not numerical:
		df.duration = df.duration.apply(lambda x: x.days+1)
	else:
		df['duration'] += 1

	# Sort in ascending order of start date
	df = df.sort_values(by='start', ascending=True)

	# Project level variables
	p_start = df.start.min()
	p_end = df.end.max()
	if not numerical:
		p_duration = (p_end-p_start).days+1
	else:
		p_duration = p_end-p_start+1


	# Add relative date
	if not (all(df.start.astype(str).str.isnumeric()) and all(df.end.astype(str).str.isnumeric())):
		df['rel_start']=df.start.apply(lambda x: (x-p_start).days)
	else:
		df['rel_start']=df.start.apply(lambda x: x-p_start)

	# Create custom x-ticks and x-tick labels
	x_ticks = [i for i in range(p_duration+1)]
	if not numerical:
		x_labels = [(p_start+dt.timedelta(days=i)).strftime('%d-%b') for i in x_ticks]
	else:
		x_labels = [p_start+i for i in x_ticks]

	# PLOTTING
	df['w_comp'] = round(df.completion*df.duration/100,2)
	df.head()

	fig, ax = plt.subplots(figsize=(18,3))
	plt.title(title, size=18)

	#Light bar for entire task
	plt.barh(y=df.Task, left=df.rel_start, width=df.duration, alpha=0.3, color=df.color)

	#Darker bar for completed part
	plt.barh(y=df.Task, left=df.rel_start, width=df.w_comp, alpha=1, color=df.color)

	ax.invert_yaxis()
	if numerical:
		plt.xticks(ticks=x_ticks[::1], labels=x_labels[::1])
		ax.xaxis.set_ticklabels([])
	else:
		plt.xticks(ticks=x_ticks[::7], labels=x_labels[::7])
	plt.tick_params(
		left=False,
		bottom=False,
		)

	plt.xlim([0, p_duration])
	plt.grid(axis='x')
	if save_as:
		save_as = os.path.abspath(os.path.expanduser(save_as))
		plt.savefig(save_as)
	if show:
		plt.show()
