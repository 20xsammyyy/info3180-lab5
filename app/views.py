import os
from app import app, db
from flask import render_template, request, jsonify, send_file
from .forms import MovieForm
from .models import Movie
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename

# Routing for your application.
@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

# The functions below should be applicable to all Flask apps.
@app.route('/api/v1/movies', methods=['POST'])
def movies():
    form = MovieForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        poster = form.poster.data

        # Ensure the upload folder exists
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        filename = secure_filename(poster.filename)
        poster.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_movie = Movie(title=title, description=description, poster=filename)
        db.session.add(new_movie)
        db.session.commit()

        return jsonify({
            "message": "Movie successfully added",
            "title": title,
            "poster": filename,
            "description": description
        }), 201
    else:
        return jsonify({"errors": form_errors(form)}), 400

@app.route('/api/v1/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    movie_list = []

    for movie in movies:
        movie_list.append({
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "poster": f"/api/v1/posters/{movie.poster}"
        })

    return jsonify({"movies": movie_list})

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

@app.route('/api/v1/posters/<filename>')
def get_poster(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
