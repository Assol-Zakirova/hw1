import sqlite3
connect = sqlite3.connect('students_info.db')
cursor = connect.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20))
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(id INTEGER PRIMARY KEY AUTOINCREMENT,
    grade INTEGER, classes TEXT,  student_id INTEGER, FOREIGN KEY (student_id) REFERENCES students(id))
''')
connect.commit()
def create_students(name):
    cursor.execute('INSERT INTO students(name) VALUES(?)', (name,))
    connect.commit()
    print(f'User {name} was added to the table')
def create_grades(student_id, classes, grade):
    cursor.execute('INSERT INTO grades(student_id, grade, classes) VALUES(?, ?, ?)', (student_id, grade, classes))
    connect.commit()
    print(f'The grade {grade} was added to the table')

def get_students():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    for i in students:
        print(i)
get_students()
# create_students('Assol')
# create_students('Mariyam')
# create_students('Azima')
# create_students('Aizhan')
# create_grades(3, 'Calculus', 90)
# create_grades(2, 'Programming', 80)
# create_grades(1, 'Data science', 95)
# create_grades(4, 'Human computer interaction', 85)
# create_grades(1, 'Applied statistics', 100)

def get_students_grade():
    cursor.execute('''
    SELECT students.name, grades.grade, grades.classes
    FROM students LEFT JOIN grades ON student_id = students.id''')
    students = cursor.fetchall()
    for i in students:
        print(f'{i[0]} got {i[1]} mark on {i[-1]}')
get_students_grade()

def max_grade():
    cursor.execute('SELECT MAX(grade) FROM grades')
    max_ = cursor.fetchone()
    print(max_)
max_grade()

def count_grade():
    cursor.execute('SELECT COUNT(grade) FROM grades')
    count = cursor.fetchone()
    print(count)
count_grade()

def min_grade():
    cursor.execute('SELECT MIN(grade) FROM grades')
    min_ = cursor.fetchone()
    print(min_)
min_grade()

def get_student_mark():
    cursor.execute('''
        SELECT student_id, COUNT(*)
        FROM grades
        GROUP BY student_id
    ''')
    students = cursor.fetchall()
    print(students)

get_student_mark()

def calculus_student():
    cursor.execute('''
        SELECT name
        FROM students
        WHERE id IN (
            SELECT student_id FROM grades 
            WHERE classes = 'Calculus'
        )
    ''')

    users = cursor.fetchall()
    print(users)
calculus_student()

def create_my_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS my_view AS
        SELECT
            students.name,
            grades.classes,
            grades.grade
        FROM students
        LEFT JOIN grades ON students.id = grades.student_id
    ''')
    connect.commit()

# create_my_view()


def get_student_grades_join():
    cursor.execute('SELECT * FROM my_view')
    users = cursor.fetchall()
    print(users)

get_student_grades_join()

