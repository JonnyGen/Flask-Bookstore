from flask import Flask, render_template, url_for, redirect, render_template_string, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/download_story')
def download_story():
    #create a path to the file
    file_path = "story1.txt"
    #now we will send the file
    return send_file(file_path, as_attachment=True)

#let's create another route that will display a download link to the client browser for the story
@app.route('/read_story')
def read_story():
    #create an html template to display the link
  
    #now render 
    return send_file


@app.route("/admin/")
def admin():
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug =True)