import sqlite3
conn = sqlite3.connect('shows.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Movies
              (MovieName TEXT,Actor TEXT,Actress TEXT, Year INT,Director TEXT)''')
cur.execute('''INSERT INTO Movies(MovieName,Actor,Actress,Year,Director)VALUES ('Dr.Strange Multiverse of Madness', 'Benedict Cumberbatch', 'Rachel McAdams', 2022,'Sam Raimi' )''')
cur.execute('''INSERT INTO Movies(MovieName,Actor,Actress,Year,Director)VALUES ('Spider-man No way home', 'Tom Holland', 'Zendaya', 2021,'Jon watts' )''')
cur.execute('''INSERT INTO Movies(MovieName,Actor,Actress,Year,Director)VALUES ('The Batman', 'Robert Pattinson', 'Zoe Kravits', 2022,'Matt Reeves' )''')
cur.execute('''INSERT INTO Movies(MovieName,Actor,Actress,Year,Director)VALUES ('Bumblebee', 'Dylan O Brien', 'Hailee Steinfild', 2018,'Travis Knight' )''')
cur.execute('''INSERT INTO Movies(MovieName,Actor,Actress,Year,Director)VALUES ('Spiderhead', 'Chris Hemsworth', 'Jurnee Smollett', 2022,'Joseph Kosinski' )''')
cur.execute('''SELECT * from Movies''')
result = cur.fetchall();
print(result)
conn.commit()
conn.close()