# all the imports
# import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
# DATABASE = '/tmp/flaskr.db'
# DEBUG = True
# SECRET_KEY = 'development key'
# USERNAME = 'admin'
# PASSWORD = 'default'


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# def connect_db():
#     return sqlite3.connect(app.config['DATABASE'])


@app.route('/api/v0/alps', methods=['POST'])
def receive_alps():
    val_No = request.form['No']
    # val_MagX = request.form['MagX']
    # val_MagY = request.form['MagY']
    # val_MagZ = request.form['MagZ']
    # val_AccX = request.form['AccX']
    # val_AccY = request.form['AccY']
    # val_AccZ = request.form['AccZ']
    # val_Uv = request.form['Uv']
    # val_Lx = request.form['Lx']
    # val_Humi = request.form['Humi']
    # val_Temp = request.form['Temp']
    # val_Press = request.form['Press']

    return render_template('index.html',
                           No=val_No)
                           # MagX=val_MagX,
                           # MagY=val_MagY,
                           # MagZ=val_MagX,
                           # AccX=val_AccX,
                           # AccY=val_AccY,
                           # AccZ=val_AccZ,
                           # Uv=val_Uv,
                           # Lx=val_Lx,
                           # Humi=val_Humi,
                           # Temp=val_Temp,
                           # Press=val_Temp)
                

if __name__ == '__main__':
    app.run()
