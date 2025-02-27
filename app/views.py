from app import app
from flask import render_template, request, redirect, url_for, flash
from datetime import datetime  # Import for formatting the date

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Jamila McLymont")

def format_date_joined(date_str):
    """Formats a date string as 'Month, Year' (e.g., 'Feb, 2021')."""
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")  # Convert string to datetime
    return date_obj.strftime("%B, %Y")  # Format as 'Month, Year'

@app.route('/profile/')
def profile():
    """Render the profile page with formatted join date."""
    joined_date = "2025-02-15"
    formatted_date = format_date_joined(joined_date)  # Format the date
    return render_template('profile.html', joined_date=formatted_date)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__=="__main__":
    app.run(debug=True)
