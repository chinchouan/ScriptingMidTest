import json


def triangle_zhonxin(a: tuple, b: tuple, c: tuple):  # 預設輸入a, b, c為tuple
    # 計算重心(x, y)並四捨五路至整數
    x = round((a[0] + b[0] + c[0]) / 3)
    y = round((a[1] + b[1] + c[1]) / 3)
    return x, y


def read_json(file_name: str) -> dict:
    with open(file_name, 'r', encoding='UTF-8') as f:
        pi_dict = json.load(f)
    return pi_dict


def print_json(data: dict) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=4))


def process_data(data: dict, discount: float) -> None:
    for i in data['categories']:
        for j in i['items']:
            j['price'] = round(j['price'] * discount)


def write_json(data: dict, file_name: str) -> None:
    with open(file_name, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
