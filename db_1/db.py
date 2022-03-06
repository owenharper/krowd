import sqlite3

conn=sqlite3.connect("krowd.db")
cur=conn.cursor()
def create_table():
    cur.execute("""CREATE TABLE krowd(
            tokenId interger,
            img blob,
            used interger
            )""")
def insert(tokenId,imgpath):
    blob=blobify(imgpath)
    dtuple=(tokenId,imgpath,0)
    cur.execute("INSERT INTO krowd VALUES (?,?,?)",dtuple)

def blobify(imgpath):
    with open(imgpath,'rb') as f:
        blob = f.read()
    return blob
insert(1,"C:\\Users\\Owenh\\Pictures\\1_FSkUtK8pYPBSNeaVotU4Ug.png")

conn.commit()
conn.close()

