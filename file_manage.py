import os

# Creating a new file
def create_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

#Add data into an existing file
def add_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data +'\n')

#Delete contents in a file
def delete_contents(path):
	with open(path, 'w'):
		pass

# Converting contents in a file to a set
def file_to_set(file_name):
	result = set()
	with open(file_name, 'rt') as f:
		for line in f:
			result.add(line.replace('\n', ''))
		return result

# Converting contents in a set into a file
def set_file(set_name, file_name):
	delete_contents(file_name)
	for link in set_name:
		add_to_file(file_name, link)

# All the data obtained is stored in this directory
def create_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

# Creating files with links in queue and those already crawled, to avoid repetition
def create_file(directory_name, base_url):
	queue = directory_name + '/queue.txt'
	crawled = directory_name + '/crawled.txt'
	out_of_domain = directory_name + '/out_of_domain.txt'
	if not os.path.isfile(queue):
		create_file(queue, base_url)
	if not os.path.isfile(crawled):
		create_file(crawled, '')
	if not os.path.isfile(out_of_domain):
		create_file(out_of_domain, '')
