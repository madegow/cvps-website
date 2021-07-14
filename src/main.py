'''
my first py    
'''
#initialization
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

#Routing and View Functions
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def local_index():
    return render_template('index.html')

@app.route('/our-story.html')
def local_ourstory():
    return render_template('our-story.html')

@app.route('/events.html')
def local_events():
    return render_template('events.html')

@app.route('/sample.html')
def local_sample():
    return render_template('sample.html')

@app.route('/gallery.html')
def local_gallery():
    return render_template('gallery.html')

@app.route('/contact.html')
def local_contact():
    return render_template('contact.html')


@app.route('/sample')
def sample():
    return '<h1> Hello World! cvps-website</h1> <b/> <p> Click <a href="/welcome">here</a> to go welcome.</p>'

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')




#Start the server, the default ip port is 127.0.0.1:5000
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
