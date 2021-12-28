import os


if __name__ == '__main__':
	'''
	path = 'C:\\Users\\btona\\Pictures\\Natal 2021'
	filename = 'Natal2021'
	files = os.listdir(path)
	padding = len(str(len(files)))

	for i, file in enumerate(files):
		numbering = str(i+1).rjust(padding, '0')
		extension = file[-4:]
		new_name = filename + '_' + numbering + extension
		print(f"File '{file}' renamed to {new_name}")
		os.rename(os.path.join(path, file), os.path.join(path, new_name))
	'''