import sqlite3

conn=sqlite3.connect("krowd.db")
cur=conn.cursor()


cur.execute("""CREATE TABLE krowd(
            tokenId interger,
            img blob,
            used interger
            )""")
conn.commit()
conn.close()