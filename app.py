from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Jujutsu Kaisen Vol 1', 
    'genre': 'Supernatural',
    'language': 'English',
    'type': 'Manga',
  },
  {
    'id': 2,
    'title': 'Jujutsu Kaisen Vol 2', 
    'genre': 'Supernatural',
    'language': 'English',
    'type': 'Manga',
  },
  {
    'id': 3,
    'title': 'Kaodake ja Suki ni Narimasen Vol 1', 
    'genre': 'Slice of Life',
    'language': 'Japanese',
    'type': 'Manga',
  },
  {
    'id': 4,
    'title': 'Yubisaki to Renren vol 1', 
    'genre': 'Slice of Life',
    'language': 'Japanese',
    'type': 'Manga',
  },
  
]
@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, app_name='Book Shelf')

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)