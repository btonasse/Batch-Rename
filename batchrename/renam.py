import os
class BatchRename():
	def __init__(self, path: str, prefix: str, extension: str) -> None:
		if not os.path.isdir(path):
			raise ValueError(f"The path {path} is not a valid directory.")
		self.path = path
		self.prefix = prefix
		self.extension = extension
		
		# Get list of files in selected folder
		self.files = self.get_list_of_files()
		if not self.files:
			raise TypeError(f"No files with extension {self.extension} found in {self.path}")

		# Determine how many leading zeroes to add to the file number
		self.padding = len(str(len(self.files)))
	
	def generate_full_file_name(self, file_index: int) -> str:
		"""
		Using all relevant instance attributes, generate the final full name of the renamed file.
		"""
		numbering = str(file_index+1).rjust(self.padding, '0')
		return self.prefix + '_' + numbering + '.' + self.extension

	def get_list_of_files(self) -> list:
		"""
		Returns list of files in the selected folder with the selected extension
		"""
		return [file for file in os.listdir(self.path) if file.lower().endswith(self.extension.lower())]

	def generate_confirmation_message(self) -> str:
		"""
		Generates number of files to be converted and the file naming convention that will be used
		"""
		new_name = self.prefix + '_[NUMBER].' + self.extension
		return f"Do you want to rename {len(self.files)} files in {self.path} to {new_name}?"

	def rename_all_files(self) -> bool:
		"""
		Iterate through self.files and rename all to the selected naming convention
		"""
		for i, file in enumerate(self.files):
			new_name = self.generate_full_file_name(i)
			os.rename(os.path.join(self.path, file), os.path.join(self.path, new_name))
		return True
	
if __name__ == '__main__':
	pass