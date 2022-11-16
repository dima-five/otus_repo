import json
import csv
from csv import DictReader
from examples.hw_lesson_5.file_path import FilePath


users_data_list = []
new_users_list = []
dic_keys = ['name', 'gender', 'address', 'age']
count_users = 0  # count of users

print(FilePath().get_file_path(file_name='users.json'))

with open(FilePath().get_file_path(file_name='users.json'), mode='r') as json_file:
    users_data = json.loads(json_file.read())
    for item in users_data:
        data = item['name'], item['gender'], item['address'], item['age']
        new_users_list.append(data)
        count_users += 1

"""__________________________csv_________________________________"""

count_books = 0   # count of books
list_books = []
dict_list_books = []
dic_keys_books = ['title', 'author', 'pages', 'genre']
with open(FilePath().get_file_path(file_name='books.csv'), newline='') as csv_file:
    # reader_csv_file = csv.reader(csv_file)
    reader_csv_file = DictReader(csv_file)
    for row in reader_csv_file:
        data_books = row["Title"], row["Author"], row["Pages"], row["Genre"]
        list_books.append(data_books)
        count_books += 1
# print(count_books)
# print(list_books)

for item in list_books:
    new_dict = dict(zip(dic_keys_books, item))
    dict_list_books.append(new_dict)   # list contains data books

with open('upload_books_from_csv_file.json', 'w') as file:
    users_file = json.dumps(dict_list_books, indent=2)
    file.write(users_file)

"""_______________write_to_json_file________________________"""

for item in new_users_list:
    new_dict = dict(zip(dic_keys, item))
    users_data_list.append(new_dict)  # list contains data users

count_start = 0
count_end = 7
for item in range(count_users):
    users_data_list[item]["books"] = dict_list_books[count_start:count_end]
    count_start = count_end
    count_end = count_end + 7

with open('example.json', 'w') as file:
    users_file = json.dumps(users_data_list, indent=2)
    file.write(users_file)
    file.close()

"""___________________notes_______________________________"""
# for item in new_users_list:
#     new_dict = dict(zip(dic_keys, item))
#     users_data_list.append(new_dict)  # list contains users
# # print(users_data_list)
#
# with open('example.json', 'w') as file:
#     users_file = json.dumps(users_data_list, indent=2)
#     file.write(users_file)

# last_user = users_data[-1]["index"]
# for value in range(last_user + 1):
#     data_list = []
#     name_user = "name: " + users_data[value]["name"]
#     data_list.append(name_user)
#     gender_user = "gender:" + users_data[value]["gender"]
#     data_list.append(gender_user)
#     address_user = "address: " + users_data[value]["address"]
#     data_list.append(address_user)
#     age_user = "age: " + str(users_data[value]["age"])
#     data_list.append(age_user)
#     users_data_list.append(data_list)