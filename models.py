import sqlite3 as sql
from flask import session
from passlib.hash import sha256_crypt

def insertUser(request):
    con = sql.connect("database.db")
   
    sqlQuery = "select username from users where (username ='" + request.form['username'] + "')"
    cur = con.cursor()
    cur.execute(sqlQuery)
    row = cur.fetchone()
    
    if not row:
        cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (form['username'], sha256_crypt.encrypt(request.form['password'])))
        con.commit()
        print "added user successfully"

    con.close()
    return not row


def authenticate(request):
    con = sql.connect("database.db")
    sqlQuery = "select password from users where username = '%s'"form['username']  
    cursor = con.cursor()
    cursor.execute(sqlQuery)
    row = cursor.fetchone()
    con.close()
    if row:
       return sha256_crypt.verify(request.form['password'], row[0])
    else:
       return False


def sow2():
    try:
        con = sql.connect("database.db")
        print "connectedgood"
        sqlQuery = "SELECT * from genre"
        cursor = con.cursor()
        cursor.execute(sqlQuery)
        rows = cursor.fetchall()
        con.close()
        return rows
    except:    
      print "fail hai"

def genre():
    try:
        con = sql.connect("database.db")
        print "db connectivity successfull"
        sqlQuery = "select * from genre"
        cursor = con.cursor()
        cursor.execute(sqlQuery)
        rows = cursor.fetchall()
        con.close()
        return rows
    except:    
      print "db connectivity failed"   

def playgo(id):
    try:
        con = sql.connect("database.db")
        print "db connectivity successfull"
        cursor = con.cursor()
        cursor.execute("SELECT * from song where sgenreid=%s"%(id))
        rows = cursor.fetchall()
        print("hey play go")
        for row in rows:
            print(row)
        con.close()
        return rows
    except:    
      print "db connectivity failed"         

def artist():
    try:
        con = sql.connect("database.db")
        print "db connectivity successfull"
        sqlQuery = "SELECT * from artist"
        cursor = con.cursor()
        cursor.execute(sqlQuery)
        rows = cursor.fetchall()
        con.close()
        return rows
    except:    
      print "db connectivity failed"

def song_upload(data):
    try:
        con = sql.connect("database.db")
        print "db connectivity successfull"
        cursor = con.cursor()
        print(data['s_name'])
        cursor.execute("INSERT INTO song (sname,sgenreid,sartistid,splay,uname) VALUES (?,?,?,?,?)", (data['s_name'] , data['cat_id'], data['art_id'],0, data['u_name']))
        con.commit()
        print("hey")
        cursor.execute("select * from song")
        rows = cursor.fetchall()
        con.close()

        return len(rows)
    except:    
        return -1

def playlist(uname , sid, sname):
    try:
        con = sql.connect("database.db")
        print "db connectivity successfull"
        cursor = con.cursor()
        cursor.execute("INSERT INTO playlist (uname , sid, sname, pname) VALUES (? , ?,?, ?)", (uname, sid, sname,p_name))
        con.commit()
        con.close()
        return "success"
    except:    
      print "db connectivity failed" 



def fetch_genre(id):
    try:
        print(id)
        con = sql.connect("database.db")
        print "db connectivity successfull"
        cursor = con.cursor()
        print("hey fetch_genre")
        cursor.execute("SELECT * from song where sgenreid='%s'"%(id))
        print("success")
        rows = cursor.fetchall()
        for row in rows :
            print row
        con.close()
        return rows
    except:    
      print "db connectivity failed" 

def fetch_artist(id):
    try:
        con = sql.connect("database.db")
        print "db connectivity successfull"
        cursor = con.cursor()
        print("hey fetch_artist")
        cursor.execute("SELECT * from song where sartistid='%s'"%(id))
        print("success")
        rows = cursor.fetchall()
        for row in rows :
            print row
        con.close()
        return rows
    except:    
      print "db connectivity failed" 




def guest_songs(num):
    try:
        con = sql.connect("database.db")
        print "db connectivity successfull"
        cursor = con.cursor()
        print("hey fetch_playlist of guest")
        print("SELECT * from playlist where uname=%s"%(name))
        cursor.execute("SELECT * from playlist where uname='%s' AND pname='%s'"%(name, p_name))
        print("success")
        rows = cursor.fetchall()
        for row in rows :
            print row
        con.close()
        return rows
    except:    
      print "db connectivity failed" 








def fetch_playlist(name,  p_name):
    try:
        print(name)
        con = sql.connect("database.db")
        print "db connectivity successfull"
        cursor = con.cursor()
        print("hey fetch_playlist")
        print("SELECT * from playlist where uname=%s"%(name))
        cursor.execute("SELECT * from playlist where uname='%s' AND pname='%s'"%(name, p_name))
        print("success")
        rows = cursor.fetchall()
        for row in rows :
            print row
        con.close()
        return rows
    except:    
      print "db connectivity failed" 


def playlist_names(name):
    try:
        print(name)
        con = sql.connect("database.db")
        print "db connectivity successfull"
        cursor = con.cursor()
        print("hey fetch_playlist_names of user")
        print("SELECT * from playlist where uname=%s"%(name))
        cursor.execute("SELECT * from playlist where uname='%s'"%(name))
        print("success")
        rows = cursor.fetchall()
        data = []
        for row in rows :
            data.append(row[3])
        con.close()
        newset = set(data)
        data = list(newset)

        return data
    except:    
      print "db connectivity failed" 



def playlist_names(name):
    try:
        print(name)
        con = sql.connect("database.db")
        print "db connectivity successfull"
        cursor = con.cursor()
        print("hey fetch_playlist_names of user")
        print("SELECT * from playlist where uname=%s"%(name))
        cursor.execute("SELECT * from playlist where uname='%s'"%(name))
        print("success")
        rows = cursor.fetchall()
        data = []
        for row in rows :
            data.append(row[3])
        con.close()
        newset = set(data)
        data = list(newset)

        return data
    except:    
      print "db connectivity failed" 



def fetch_trending():
    try:
        con = sql.connect("database.db")
        print "db connectivity successfull"
        sqlQuery = "SELECT * FROM song ORDER BY splay DESC LIMIT 10"
        cursor = con.cursor()
        cursor.execute(sqlQuery)
        rows = cursor.fetchall()
        con.close()
        return rows
    except:    
      print "db connectivity failed"


def fetch_devotional():
    try:
        con = sql.connect("database.db")
        print "db connectivity successfull"
        sqlQuery1 = "select * from song where sgenreid in (1,5,8,13)"
        sqlQuery2 = "select * from song where sartistid in (6,7,10,11)"
        cursor1 = con.cursor()
        cursor2 = con.cursor()
        cursor1.execute(sqlQuery1)
        rows1 = cursor1.fetchall()
        cursor2.execute(sqlQuery2)
        rows2 = cursor2.fetchall()
        con.close()
        rows = set(rows)
        return  list(rows)
    except:    
      print "db connectivity failed"


def fetch_hiphop():
    try:
        con = sql.connect("database.db")
        print "db connectivity successfull"
        sqlQuery1 = "select * from song where sgenreid in (2,3,4,6,7,9,10)"
        sqlQuery2 = "select * from song where sartistid in (1,2,3,4,5,8,9)"
        cursor1 = con.cursor()
        cursor2 = con.cursor()
        cursor1.execute(sqlQuery1)
        rows1 = cursor1.fetchall()
        cursor2.execute(sqlQuery2)
        rows2 = cursor2.fetchall()
        con.close()
        rows = set(rows1 + rows2)
        return  list(rows)
    except:    
      print "db connectivity failed"



def update_songcount(id):
    try:
        con = sql.connect("database.db")
        print "db connectivity successfull"
        cursor = con.cursor()
        cursor.execute("UPDATE song SET splay=splay+1 WHERE sid=%s"%(id))
        con.commit()
        con.close()
    except:    
      print "db connectivity failed"

def update_password(request):
    try:
        con = sql.connect("database.db")
        print "db connectivity successfull"
        sqlQuery="UPDATE users SET password='%s' WHERE username='%s'"%(password,username)
        cursor = con.cursor()
        cursor.execute(sqlQuery)
        con.commit()
        con.close()
    except:    
      print "db connectivity failed"
