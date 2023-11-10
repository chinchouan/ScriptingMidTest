from pkg.modu import print_json, process_data, read_json, write_json

# 輸入檔案名稱
MENU_FILE = 'menu.json'
# 輸出檔案名稱
OUTPUT_FILE = 'output.json'
# 讀入menu.json檔
menu_dict = read_json(MENU_FILE)
# 輸出轉成字典後的menu
print_json(menu_dict)
# 加入主菜
add_string = {"name": "海鮮燉飯", "price": 239, "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"}
for i in menu_dict['categories']:
    if i['name'] == '主菜':
        i['items'].append(add_string)
# 輸入折扣並進行更動
discount = float(input('請輸入折扣率(0.0 ~ 1.0): '))
process_data(menu_dict, discount)
# 確認打折後並寫入檔案
print_json(menu_dict)
write_json(menu_dict, OUTPUT_FILE)
