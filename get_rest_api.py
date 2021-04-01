"""
Учимся пользоваться REST API используя flask
Отрабатываем метод GET
"""

from flask import Flask, jsonify


app = Flask(__name__)

users = [
    {'name': 'Denis',
     'nic': 'Den',
     'password': 22355221},
    {'name': 'Den',
     'nic': 'ilia',
     'password': 87865654},
    {'name': 'Sergei',
     'nic': 'Serq',
     'password': 87865654},
    {'name': 'Nataha',
     'nic': 'Nat',
     'password': 87865654}
]


@app.route('/', methods=['GET'])  # По запросу GET отдаем данные.
def get_info():
    return jsonify(users)


@app.route('/get_one/<string:name>', methods=['GET'])  # Возвращаем данные по параметру.
def get_one(name):
    for i in users:
        if i['name'] == name:
            return jsonify(i)  # Передаем найденую информацию.
        else:
            pass

    return jsonify(f'Мы не нашли пользователя с таким именем - {name}')


# Возвращаем данные по нескольким параметрам.
@app.route('/get_list/<string:name_1>/<string:name_2>', methods=['GET'])
def get_list(name_1, name_2):
    get_user = []
    # Полученные параметры помещаются в список.
    param = [name_1, name_2]
    for elem in param:  # Проходим циклом по полученым элементам
        for i in users:
            if i['name'] == elem:
                # Если есть совпадение,тогда добавляем в список
                get_user.append(i)
            else:
                pass

    return jsonify(get_user)


if __name__ == '__main__':
    app.run()
