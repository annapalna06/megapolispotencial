import csv

with open('vacancy.csv',encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))

    reader = sorted(reader, key=lambda x: x["Salary"])
    reader = reader[::-1]
    company = []
    salary = []
    top3 = []
    k = 0
    for row in reader:
        if row['Company'] not in company:
            company.append(row)
            salary.append(row['Salary'])
            company = sorted(company,key=lambda x: x['Salary'])
            while k!=3:
                for row in company:
                    top3.append(row)
                    k+=1
        print(f'{top3['Company']}-{top3['Role']}-{top3['Salary']}')




with open('vacancy_new.csv','w',newline='') as file:
    file = csv.DictWriter(file, fieldnames=['company','role','Salary'],delimiter=';')
    writer.writeheader()
    writer.writerows(company)




