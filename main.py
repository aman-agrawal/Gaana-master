from flask import Flask
from flask import session
from flask import render_template
from flask import request
from flask import  redirect
from flask import render_template
from flask import jsonify , url_for
from flask import send_file
import models as dbHandler
from werkzeug import secure_filename
import os

app = Flask(__name__)


###################### root ##################################################

@app.route('/')
def main():
  try :
    if 'username' in session :
      rows1=dbHandler.genre()
      rows2=dbHandler.artist()
      username = session['username']
      return render_template('main.html', genre = rows1 , artist = rows2, playlist = p_list)
    else:
      rows1 = dbHandler.genre()
      rows2 = dbHandler.artist()
      return render_template('guest.html', genre = rows1 , artist = rows2)
  except Exception as e:
    return str(e)



@app.route('/guests')
def guests_tr():
  try :
    rows1=dbHandler.genre()
    rows2=dbHandler.artist()
    return render_template('guest.html', genre = rows1 , artist = rows2)
  except Exception as e:
    return str(e)




@app.route('/main')
def main_tr():
  try :
    if 'username' in session :
      rows1=dbHandler.genre()
      rows2=dbHandler.artist()
      username = session['username']
      return render_template('main.html', genre = rows1 , artist = rows2, playlist = p_list)
    else:
      return redirect(url_for('guests'))
  except Exception as e:
    return str(e)

####################### login #################################################

@app.route('/login', methods=['POST', 'GET'])
def login():
  try :
    if 'username' in session :
        return redirect(url_for('main'))
    elif request.method == 'GET':
      if dbHandler.authenticate(request): 
            session['username'] = request.form['username']
            return redirect(url_for('main'))
      else:
        return render_template('login1.html' , message="Authentication failed.")
    return render_template('login1.html', message = "")
  except Exception as e:
    return str(e)




######################## logout #################################################
@app.route('/logout', methods=['POST', 'GET'])
def logout():
    if 'username' not in session:
        name = session.pop('username')
        return redirect(url_for('main'))
    
    return redirect(url_for('main'))

######################### register ################################################
@app.route('/register', methods=['POST', 'GET'])
def register():
  # print "",request.method
  if request.method=='POST':
    if dbHandler.insertUser(request):
      session['username'] = request.form['username']
      msg = "success in adding user"
      return redirect(url_for('main'))
    else:
      msg  = "registration failed"
      return render_template("register1.html", message=msg)
    
  return render_template('register1.html', message = "")


####################UPDATE PASSWORD #########################

@app.route('/update_pass', methods=['POST', 'GET'])
def update_p():
  if 'username' in session:
    if request.method=='POST':
      dbHandler.update_password(request)
      return redirect(url_for('main'))
    else :
      return render_template('update_p.html')
  else:
     msg = "user dont exists"
     return render_template("error.html",  msg = msg)



######################################################################### 

@app.route('/sow')
def sow():
  rows=dbHandler.sow2()
  return render_template("sows.html",rows=rows)
  
######################################################################### 

@app.route('/play/<id>', methods=['POST', 'GET'])
def play(id):
   if 'username' in session:
        username=session['username']
        print(id)
        rows=dbHandler.playgo(id)
        playlist = dbHandler.fetch_playlist(username)
        return render_template("two.html",username=username,rows=rows, playlist = playlist)
   else:
      return redirect(url_for('login'))


###########################upload #############################

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'GET':
      f = request.files['file']
      img = request.files['img']

      print(request.form.get('cat', ""))
      print(request.form.get('art', ""))
      print(request.form.get('name', ""))
      for key, value in request.form.items():
        print("key: {0}, value: {1}".format(key, value))

      data = {'cat_id': None,'art_id': None ,'s_name': None, 'u_id':None}
      data['cat_id'] = request.form.get('cat', "")
      data['art_id'] = request.form.get('art', "")
      data['s_name'] = request.form.get('name',"")
    
      data['u_name']=session['username']
      s_id = dbHandler.song_upload(data)
      print(s_id)
      
      print("pass1") 
      f.save(os.path.join(app.config['UPLOAD_FOLDER_FILE'],str(s_id)+'.mp3'))
      img.save(os.path.join(app.config['UPLOAD_FOLDER_IMG'],str(s_id)+'.jpg'))
      print("pass2") 
      return jsonify(
        # summary = make_summary(f),
        s_name = data["s_name"],
        status = s_id
        )
      


########################## DOWNLOAD FILE ###################
@app.route('/download_files/<type>/<id>')
def return_files(type ,id):
  try:
    if str(type) == 'img':
      url = './uploads/images/'+str(id)+'.jpg'
      print(url)
      return send_file(url, attachment_filename='abc.jpg')
    elif str(type) == 'mp3':
      dbHandler.update_songcount(id)
      url = './uploads/songs/' + str(id)+'.mp3'
      return  send_file(url, attachment_filename='abc.mp3')
    return "not a valid file format"
  except Exception as e:
    return str(e)



@app.route('/add_to_playlist/<id>/<songname>/<p_name>')
def add_to_list(id, songname, p_name):
  try:
    if 'username' in session:
      username = session['username']
      result = dbHandler.playlist(username, id, songname, p_name)
      return jsonify(msg = result)
  except Exception as e:
    return str(e)


@app.route('/fetch_playlist/<name>')
def fetch_list(name):
  try:
    if 'username' in session:
      username = session['username']
      result = dbHandler.fetch_playlist(username, name)
      return render_template('playlist_songs.html',rows = result)
  except Exception as e:
    return str(e)




@app.route('/genre/<id>')
def get_genre(id):
  try:
    rows = dbHandler.fetch_genre(id)
    print(rows)
    return render_template("song_temp.html" , rows = rows)
  except Exception as e:
    return str(e)



@app.route('/artist/<id>')
def get_artist(id):
  try:
    rows = dbHandler.fetch_artist(id)
    return render_template("song_temp.html" , rows = rows)
  except Exception as e:
    return str(e)

@app.route('/playlist_names')
def p_names():
  try : 
    if 'username' in session:
      username = session['username']
      result = dbHandler.playlist_names(username)  

      return render_template('playlist_names.html' , rows = result)  
    else:
      return str("error")
  except Exception as e :
    return str(e)

@app.route('/playlist_names1')
def p_names1():
  try : 
    if 'username' in session:
      username = session['username']
      result = dbHandler.playlist_names(username)  

      return render_template('playlist_names1.html' , playlist = result)  
    else:
      return str("error")
  except Exception as e :
    return str(e)


@app.route('/trending_songs')
def tr():
  try:
    result = dbHandler.fetch_trending()
    return render_template('song_temp.html', rows = result)
  except Exception as e:
    return str(e)


@app.route('/devotional_songs')
def trtr():
  try:
    result = dbHandler.fetch_devotional()
    return render_template('song_temp.html', rows = result)
  except Exception as e:
    return str(e)


@app.route('/hiphop_songs')
def trtrtr():
  try:
    result = dbHandler.fetch_hiphop()
    return render_template('song_temp.html', rows = result)
  except Exception as e:
    return str(e)


######################## logout #################################################





if __name__ == '__main__':
    app.run(host='127.0.0.1')

