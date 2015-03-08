# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify
import random
from contextlib import closing
import base64
import cStringIO


# configuration
DATABASE = 'mydb'
DEBUG = True

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


def delete_old():
    max_size = 1000
    cur = g.db.execute('select count(*) from entries')
    count = cur.fetchone()[0]
    if count > max_size:
        cur = g.db.execute('select id from entries order by id desc')
        max_id = cur.fetchone()[0]
        g.db.execute('delete from entries where id <= {0}'.format(
            max_id - max_size))

    
@app.route('/')
def show_entries():
    delete_old()

    cur = g.db.execute('select N, MagX, MagY, MagZ, AccX, AccY, AccZ, Uv, Lx, Humi, Temp, Press from entries order by id desc')
    entries = [dict(No=row[0],
                    MagX=row[1],
                    MagY=row[2],
                    MagZ=row[3],
                    AccX=row[4],
                    AccY=row[5],
                    AccZ=row[6],
                    Uv=row[7],
                    Lx=row[8],
                    Humi=row[9],
                    Temp=row[10],
                    Press=row[11]) for row in cur.fetchall()]
    return render_template('index.html', entries=entries)


@app.route('/api/v0/alps', methods=['POST'])
def receive_alps():
    # get post values
    val_No = request.form['No']
    val_MagX = request.form['MagX']
    val_MagY = request.form['MagY']
    val_MagZ = request.form['MagZ']
    val_AccX = request.form['AccX']
    val_AccY = request.form['AccY']
    val_AccZ = request.form['AccZ']
    val_Uv = request.form['Uv']
    val_Lx = request.form['Lx']
    val_Humi = request.form['Humi']
    val_Temp = request.form['Temp']
    val_Press = request.form['Press']

    # clear db
    if val_No == "0":
        g.db.execute('delete from entries')
    else:
        delete_old()

    # store value in sqlite3
    g.db.execute('insert into entries (N, MagX, MagY, MagZ, AccX, AccY, AccZ, Uv, Lx, Humi, Temp, Press) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 [val_No, val_MagX, val_MagY, val_MagZ, val_AccX, val_AccY, val_AccZ, val_Uv, val_Lx, val_Humi, val_Temp, val_Press])
    g.db.commit()


    return render_template('index.html',
                           entries=[dict(
                               No=val_No,
                               MagX=val_MagX,
                               MagY=val_MagY,
                               MagZ=val_MagX,
                               AccX=val_AccX,
                               AccY=val_AccY,
                               AccZ=val_AccZ,
                               Uv=val_Uv,
                               Lx=val_Lx,
                               Humi=val_Humi,
                               Temp=val_Temp,
                               Press=val_Temp)])

BACK = -1
STOP = 0
GO = 1

@app.route('/api/v0/getdata')
def get_data():
	fields = ['N', 'MagX', 'MagY', 'MagZ', 'AccX', 'AccY', 'AccZ', 'Uv', 'Lx', 'Humi', 'Temp', 'Press']
	ret = {}
	c = request.args.get('c', '20')
	cur = g.db.execute('select ' + ','.join(fields) + ' from entries order by id desc limit ' + c)
	for row in cur:
		for k, v in enumerate(fields):
			ret.setdefault(v, [])
			ret[v].append(row[k])

	return jsonify(**ret)
	

def calc_angle_akarui():
    cur = g.db.execute('select Lx from entries order by id desc')
    entries = [float(row[0]) for row in cur.fetchall()]
    latest = entries[:30] # 100ms * 30 = 3s

    if len(latest) == 0:
        return STOP

    avg = sum(latest) / float(len(latest))

    if avg >= 200:
        return STOP
    elif avg >= 100:
        return GO
    else:
        return BACK


def calc_angle_random():
    return random.choice([BACK, STOP, GO])


def calc_angle_flat():
    return STOP


@app.route('/api/v0/bantoL')
def send_angleL():
    angle = calc_angle_akarui()
    ret = {"angle": angle}
    return jsonify(**ret)


@app.route('/api/v0/bantoR')
def send_angleR():
    angle = calc_angle_flat()
    ret = {"angle": angle}
    return jsonify(**ret)


@app.route('/api/v0/theta', methods=['POST'])
def receive_image():
    data = request.form['base64']
    # with open("base64.dat") as f:
    #     data = f.read()
    image_string = base64.b64decode(data)
    # print image_string
    with open("theta.png", "wb") as f:
        f.write(image_string)
    return jsonify(**dict(status="SUCCESS"))


if __name__ == '__main__':
    app.run()
    # receive_image()
