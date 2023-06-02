from pprint import pprint
import csv
from transformate_data import correct_data, delite_dublicate_data

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    contacts_new = (delite_dublicate_data(correct_data(contacts_list)))




    with open("phonebook_new.csv", 'w', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=",")
        datawriter.writerows(contacts_new)





