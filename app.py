from flask import Flask, render_template, jsonify

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
  {
    'id': 5,
    'title': 'Why Raeliana Ended Up at the Duke\'s Mansion', 
    'genre': 'Isekai',
    'language': 'English',
    'type': 'Manhwa',
  },
  
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, app_name='Book Shelf')

@app.route("/api/books")
def list_books():
  return jsonify(JOBS)
  
print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)