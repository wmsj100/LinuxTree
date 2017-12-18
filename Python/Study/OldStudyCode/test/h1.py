import sqlite3
def convert(value):
    if value.startswith('~'):
        return value.strip('~')

    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('data.db')
curs = conn.cursor()

curs.execute('''
CREATE TABLE food (
id     TEXT      PRIMARY KEY,
desc   TEXT,
water  FLOAT£¬
kcal   FLOAT,
protein FLOAT,
sugar   FLOAT,
fiber   FLOAT,
carbs   FLOAT,
ash    FLOAT
)
''')

query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?)'

for line in open('NUTR_DEF.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)

curs.commit()
