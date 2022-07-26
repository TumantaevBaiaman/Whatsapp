from db.db import connection


def add_id(data):
    id_order = data
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO list(id_order) VALUES (%s);", (id_order,))


def add_deatil(data):
    id_order = data['id']
    user_name = data['name']
    phone = data['phone']
    product = data['product']
    sku = data['sku']
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO info_user(id_order, user_name, phone, product, sku) VALUES (%s, %s, %s, %s, %s);", (id_order, user_name, phone, product, sku))


def get_data():
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_order FROM list;")
        for i in cursor.fetchall():
            data.append(i[0])
    return data


def get_data_info():
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_order FROM info_user;")
        for i in cursor.fetchall():
            data.append(i[0])
    return data


def get_data_whatsapp():
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT phone, product FROM info_user;")
        for i in cursor.fetchall():
            data.append([i[0], i[1]])
    return data
