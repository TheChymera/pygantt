import os
from ..plot import gantt
TESTPATH=os.path.dirname(__file__)

def test_dates(tmp_path):
	out_file = os.path.join(tmp_path,'dates.png')
	print(f'Check output: {out_file}')
	gantt(f'{TESTPATH}/data/dates.csv',
		save_as=out_file,
		)

def test_count(tmp_path):
	out_file = os.path.join(tmp_path,'count.png')
	print(f'Check output: {out_file}')
	gantt(f'{TESTPATH}/data/count.csv',
		save_as=out_file,
		)
