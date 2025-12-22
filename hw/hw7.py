import sqlite3

connect = sqlite3.connect('students.db')
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (50) NOT NULL,
            age INTEGER NOT NULL,
            course INTEGER NOT NULL
        )
''')
connect.commit()

def create_user(name, age, course):
    cursor.execute(
        'INSERT INTO students(name, age, course) VALUES(?,?,?)',
        (name, age, course)
    )
    connect.commit()
    print(f'пользователь {name} добавлен !!')
# create_user("Diana", 20, 2)

def get_users():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    for i in students:
        print(f'id: {i[0]}, name: {i[1]}, age: {i[2]}, course: {i[3]}')
get_users()



def update_user_name(row_id, new_name):
    cursor.execute(
        'UPDATE students SET name = ? WHERE id = ?',
        (new_name, row_id)
    )
    connect.commit()
    print('пользователь обновлен!')
# update_user_name(2, 'Meerim')

def delete_user(row_id):
    cursor.execute(
        'DELETE FROM students WHERE id = ?',
        (row_id,)
    )
    connect.commit()
    print('Пользователь удален!!')
# delete_user(1)

def get_by_id(user_id):
    cursor.execute(
        'SELECT id, name, age, course FROM students WHERE id = ?',
        (user_id,)
    )
    user = cursor.fetchone()

    if user:
        print(f'id: {user[0]}, name: {user[1]}, age: {user[2]}, course: {user[3]}')
    else:
        print('Пользователь не найден')
print()
get_by_id(2)
