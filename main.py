from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/top_score')
def top_score():
  return render_template("top_score.html")

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/manual')
def manual():
  return render_template("manual.html")

@app.route('/tracking_ijazah')
def tracking_ijazah():
  return render_template("tracking_ijazah.html")

@app.route('/kelas_mkdu')
def kelas_mkdu():
  return render_template("kelas_mkdu.html")

@app.route('/katalog_online')
def katalog_online():
  return render_template("katalog_online.html")

@app.route('/pendaftaran_wisuda')
def pendaftaran_wisuda():
  return render_template("pendaftaran_wisuda.html")

@app.route('/daftar_peserta_mata_kuliah')
def daftar_peserta_mata_kuliah():
  return render_template("daftar_peserta_matkul.html")

@app.route('/daftar_peserta_mata_kuliah_mkdu')
def daftar_peserta_mata_kuliah_mkdu():
  return render_template("daftar_peserta_matkul_mkdu.html")

@app.route('/kalender_akademik')
def kalender_akademik():
  return render_template("kalender_akademik.html")

@app.route('/informasi_skripsi')
def informasi_skripsi():
  return render_template("informasi_skripsi.html")

app.run(debug=True)