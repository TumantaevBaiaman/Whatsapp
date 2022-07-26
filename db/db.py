from db_data import user, password, db_name, ip
import psycopg2


try:
    connection = psycopg2.connect(
        host=ip,
        user=user,
        password=password,
        database=db_name,
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"server version: {cursor.fetchone()}")

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS list(
                id_order bigint NOT NULL);
                """
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS info_user(
                id_order bigint NOT NULL,
                user_name varchar(50) NOT NULL,
                phone varchar(50) NOT NULL,
                product varchar(255) NOT NULL,
                sku varchar(50) NOT NULL
                );
                """
        )

except Exception as ex:
    print("Error")

finally:
    pass



# with connection.cursor() as cursor:
#     cursor.execute(
#         """CREATE TABLE users_db_tel_bot(
#             id serial PRIMARY KEY,
#             id_user bigint NOT NULL,
#             first_name varchar(50) NOT NULL,
#             nick_name varchar(50) NOT NULL);
#             """
#     )