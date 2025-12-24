import sqlite3
connect = sqlite3.connect('tvshows.db')
cursor = connect.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS tvshows(
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               name VARCHAR(50) NOT NULL, 
               episodes INTEGER NOT NULL,
               rating INTEGER NOT NULL)''')
connect.commit()
def create_tvshow(name, episodes, rating):
    cursor.execute('INSERT INTO tvshows(name, episodes, rating) VALUES(?,?,?)', (name, episodes, rating))
    connect.commit()
    print(f'TV show {name} added!')
def get_all_tvshows():
    cursor.execute('SELECT * FROM tvshows')
    show = cursor.fetchall()
    for i in show:
        print(*i)
get_all_tvshows()
def update_tvshow(id, rating):
    cursor.execute('UPDATE tvshows SET rating = ? WHERE id = ?', (rating, id))
    connect.commit()
    print(f'TV show with id {id} updated!')


