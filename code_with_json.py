""" Создать (не программно) текстовый файл, 
в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль 
каждой компании, а также среднюю прибыль. Если фирма получила 
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь 
с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь 
(со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, 
“firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в 
соответствующий файл. """
import json

# reading from file
with open("to_json.txt", 'r', encoding='utf-8') as file:
    for line in file:
        str = file.readlines()

tmp = []
result = {}
for line in str: # deleting '\n' from strings
    if line.endswith('\n'):
        line = line[::-1]
        line = line[1:]
        line = line[::-1]
    tmp.append(line)

print(tmp)
str = tmp
tmp = []
elem = []
profit_count = 0
profit_summary = 0

for itm in str:
    itm = itm.split(' ')
    print(itm)
    profit = int(itm[2]) - int(itm[3])
    if profit >= 0:
        profit_summary += profit
        profit_count += 1
    elem = [itm[0], profit]
    tmp.append(tuple(elem))
    profit = 0
tmp = [dict(tmp)]
elem = {'average_profit': profit_summary/profit_count}
tmp.append(elem)

str = tmp

with open("lesson5_7.json", 'w') as j_file:
    json.dump(str, j_file)