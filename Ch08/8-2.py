import pymysql as db

conn = db.connect(host='192.168.44.46',
                  user='psr',
                  password='1234',
                  db='psr',
                  charset='utf8')

cur = conn.cursor()
cur.execute("SELECT * FROM `USER1`")

for row in cur.fetchall():
    print('---------------')
    print('아이디 :', row[0])
    print('이름 :', row[1])
    print('휴대폰 :', row[2])
    print('나이 :', row[3])
    print('---------------')