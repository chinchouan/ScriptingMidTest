# 格式化輸入與提示
print('-' * 30)
print('        員工薪資輸入')
print('    若姓名處未輸入則代表結束')
print('-' * 30)
# 創造空串列用來存取每個人的資料
dict_list = []
# 無限詢問直到名字輸入為空
while True:
    eName = input('請輸入姓名:')
    if eName == '':
        break
    eSalary = int(input('請輸入薪資:'))
    print()
    # 把個人資料存入字典
    dict_list.append({'eName': eName, 'eSalary': eSalary})
print('-' * 30)
# 計算薪水總額與輸出每個人的薪水
total_salary = 0
for i in dict_list:
    total_salary += i['eSalary']
    print(f"員工{i['eName']:<5} 的薪資為 {i['eSalary']:>6,}")
print('-' * 30)
# 計算平均值
average_salary = round(total_salary / len(dict_list), 2) if total_salary != 0 else 0.00
# output
print(f'合計薪資:{total_salary:>16,}')
print(f'平均薪資:{average_salary:>19.2f}')
print('=' * 30)
