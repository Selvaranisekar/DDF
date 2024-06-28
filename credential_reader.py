import csv


def read_credentials_from_csv(csv_file_path):
    credential_list = []
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            username, password = row[0].split(',')
            credential_list.append((username.strip(), password.strip()))

    return credential_list
