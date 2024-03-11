import random
import csv

def quicksort(n):
    if len(n) <= 1:
        return n
    else:
        l_list = []
        m_list = []
        r_list = []
        q = random.choice([x for x in n])
        for a in n:
            if a['Company_Size'] < q['Company_Size']:
                l_list.append(a)
            elif a['Company_Size'] > q['Company_Size']:
                r_list.append(a)
            else:
                m_list.append(a)
        return quicksort(l_list) + m_list + quicksort(r_list)

with open ('vacancy.csv',encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    reader = quicksort(reader)
    companies_with_classtutor = []
    for row in reader:
        if row['Role'] == "Классный руководитель":
            companies_with_classtutor.append(row)
            companies_with_classtutor = quicksort(companies_with_classtutor)
            the_least_people  = companies_with_classtutor[0]
            print(f'В компании {the_least_people['Company']} есть заданная профессия: {the_least_people['Role']}, з/п в такой компании составит: {the_least_people['Salary']}')
















