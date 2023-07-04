import os

specific_folder = 'C:/Users/IvelinIvanov/PycharmProjects/Python_OOP/class_and_static_methods'

root_directories = [os.path.abspath(os.path.join(specific_folder, item)) for item in os.listdir(specific_folder) if os.path.isdir(os.path.join(specific_folder, item))]

for directory in root_directories:
    print(directory)