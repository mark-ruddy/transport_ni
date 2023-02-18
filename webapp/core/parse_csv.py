import csv

def parse_soa_vacancies(soa):
    dataset = csv.reader(open('static/soa_vacancies.csv', "r"), delimiter=",")
    for row in dataset:
        # if soa == row[0] or soa in row[0]:
        if soa == row[0]:
            return row
    return ['', '']
