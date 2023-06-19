import os


# Create a project directory for each site will be crawled
def create_project_directory(directory):
    if not os.path.exists(directory):
        print('creating project ' + directory)
        os.makedirs(directory)


# queue and crawled files
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, "crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


#  create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# append new data to existing file
def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')


# delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()


# read a file and convert each line to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results


# iterate through a set, each item will be a new line in the set
def set_to_file(links, file):
    with open(file, "w") as f:
        for line in sorted(links):
            f.write(line + "\n")
