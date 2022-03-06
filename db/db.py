import mysql.connector

def connect_db(username, password, database):
    mydb=mysql.connector.connect(host="localhost", username=username,password=password,database=database)
    return mydb

def create_db(mydb,name):
    cur=mydb.cursor()
    cur.execute("CREATE DATABASE "+name)
    return cur

def show_db(cur):
    cur.execute("SHOW DATABASES")
    for i in cur:
        print(i)

def add_column(cur,table,column):
    cur.execute("ALTER TABLE "+table+" ADD COLUMN "+column)


def show_table(cur):
    cur.execute("SHOW TABLES")
    for i in cur:
        print(i)

def create_table(cur,name):
    cur.execute("CREATE TABLE "+name+" (token_id VARCHAR(255),imgpath VARCHAR(1024),used BOOLEAN)")

def insert_nft(mydb,token_id,imgpath,owner):
    cur=mydb.cursor()
    sql="INSERT INTO NFT (token_id,imgpath,used,owner) VALUES (%s,%s,%s)"
    arg=(token_id,imgpath,False,owner)
    cur.execute(sql,arg)
    mydb.commit()

def select_id(cur,id):
    cur.execute("SELECT * FROM NFT WHERE token_id='"+id+"'")
    r=cur.fetchall()
    return r


def print_table(cur):
    cur.execute("SELECT * from NFT")
    r=cur.fetchall()
    for i in r:
        print(i)

def drop_table(cur,tbname):
    cur.execute("DROP TABLE IF EXISTS " + tbname)

def nft_used(cur,id):
    cur.execute("UPDATE NFT SET used='1' WHERE token_id='"+id+"'")

def transfer(cur,id,owner):
    cur.execute("UPDATE NFT SET owner='"+owner+"' WHERE token_id='"+id+"'")

mydb=connect_db("root","y&PA8aiuEBXVCy*","krowd")
#drop_table(mydb.cursor(),"NFT")
#create_table(mydb.cursor(),"NFT")
add_column(mydb.cursor(),"NFT","owner VARCHAR(256)")
#insert_nft(mydb,"yourpassworrd","C:\\Users\\Owenh\Pictures\\0fa13065-a0b4-462f-8e73-e7b7997d9736-cover.png")
#print_table(mydb.cursor())
#print_table(mydb.cursor())
