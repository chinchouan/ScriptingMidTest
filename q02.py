print('-' * 30)
print('        員工薪資輸入')
print('    若姓名處未輸入則代表結束')
print('-' * 30)
dict_list = []
while True:
    eName = input('請輸入姓名:')
    if eName == '':
        break
    eSalary = int(input('請輸入薪資:'))
    print()
    dict_list.append({'eName': eName, 'eSalary': eSalary})
print('-' * 30)
total_salary = 0
for i in dict_list:
    total_salary += i['eSalary']
    print(f"員工{i['eName']:<5} 的薪資為 {i['eSalary']:>6,}")
print('-' * 30)
average_salary = round(total_salary / len(dict_list), 2) if total_salary != 0 else 0.00
print(f'合計薪資:{total_salary:>16,}')
print(f'平均薪資:{average_salary:>19.2f}')
print('=' * 30)
