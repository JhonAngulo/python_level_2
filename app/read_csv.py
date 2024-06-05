import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    print(data[0])