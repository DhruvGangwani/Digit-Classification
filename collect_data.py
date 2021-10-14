import pandas as pd
import os


def get_content(dir_name, index_range, column_size=1024):
	all_content = list()
	for ind in range(index_range):
		for file_name in sorted(os.listdir(dir_name)):
			if file_name.startswith(f'class_{ind}'):
				
				with open(os.path.join(dir_name, file_name), 'r') as f:
					content = f.readlines()
				str_number = ''
				for line in content:
					line = line.replace('\n', '')
					str_number+=line

				line_content = list(map(int, str_number))
				line_content.append(ind)
				all_content.append(line_content)
					
	cols = [f'x{str(x)}' for x in range(column_size)]
	cols.append('classes')
	content = pd.DataFrame(all_content, columns = cols)
	content.to_csv(dir_name+'.csv', index=False)


if __name__ == '__main__':
	dir_name = 'test'
	index_range = 10
	get_content(dir_name, index_range)

