from flask import Blueprint
from flask import render_template, request
from flask import redirect
from flask import url_for

from .forms import MovieForm, UploadForm

from models import Movie, Genre
from app import db

from werkzeug.utils import secure_filename

movies = Blueprint('movies', __name__, template_folder = 'templates')


@movies.route('/create', methods=['GET', 'POST'])
def create():
    form = MovieForm()
    return render_template('movies/create_movie.html', form = form)


@movies.route('/create_movie', methods = ['POST'])
#@login_required
def create_movie():

    title = request.form['title']
    description = request.form['description']
    tagline = request.form['tagline']
    fees_in_world = request.form['fees_in_world']
    budget = request.form['budget']
    country = request.form['country']
    premiere = request.form['premiere']
    year = request.form['year']
    try:
        movie = Movie(
            title=title, description=description, tagline=tagline, fees_in_world=fees_in_world,
            budget=budget, country=country, premiere=premiere, year=year
            )
        db.session.add(movie)
        db.session.commit()
    except:
        print('Something wrong')
    return redirect(url_for('movies.index'))




@movies.route('/<slug>/edit', methods=['GET', 'POST'])
def edit(slug):
    movie = Movie.query.filter(Movie.slug==slug).first_or_404()
    form = MovieForm(obj=movie)
    return render_template('movies/edit_movie.html', movie=movie, form=form)

@movies.route('/<slug>/edit_movie', methods=['GET', 'POST'])
def edit_movie(slug):
    movie = Movie.query.filter(Movie.slug==slug).first_or_404()
    form = MovieForm(formdata=request.form, obj=movie)
    form.populate_obj(movie)

    db.session.commit()
    return redirect(url_for('movies.index'))
    



@movies.route('/')
def index():
    q = request.args.get('q')

    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    if q:
        movies = Movie.query.filter(Movie.title.contains(q) | Movie.description.contains(q))#.all()
    else:
        movies = Movie.query#.all()
    pages = movies.paginate(page=page, per_page = 5)
    return render_template('movies/index.html', movies = movies, pages = pages)

@movies.route('/<slug>')
def movie_detail(slug):
    movie = Movie.query.filter(Movie.slug == slug).first_or_404()
    genres = movie.genres
    return render_template('movies/movie_detail.html', movie = movie, genres = genres)

@movies.route('/genre/<slug>')
def genre_detail(slug):
    genre = Genre.query.filter(Genre.slug == slug).first_or_404()
    movies = genre.movies.all()
    return render_template('movies/genre_detail.html', genre = genre, movies = movies)


@movies.route('/<slug>/upload', methods=['GET', 'POST'])
#@login_required
def upload(slug):
    form = UploadForm()
    movie = Movie.query.filter(Movie.slug == slug).first_or_404()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('static/img/uploads/' + filename)
        movie.image = "../../../static/img/uploads/" + filename
        db.session.commit()
        return redirect(url_for('movies.movie_detail', slug=slug))

    return render_template('movies/upload.html', form=form)


@movies.route('/<slug>/delete/', methods=["GET", "POST"])

def delete_movie(slug):
    movie = Movie.query.filter(Movie.slug==slug).first_or_404()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('movies.index'))
