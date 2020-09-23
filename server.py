from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def default_home():
    return render_template("index.html")


# @app.route('/index.html')
# def default_home_render():
#     return render_template("index.html")
#
#
# @app.route('/about.html')
# def about():
#     return render_template("about.html")
#
#
# @app.route('/components.html')
# def components():
#     return render_template("components.html")
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template("contact.html")
#
#
# @app.route('/work.html')
# def work():
#     return render_template("work.html")
#
#
# @app.route('/works.html')
# def works():
#     return render_template("works.html")

@app.route('/<string:page_name>')
def default_pname(page_name):
    return render_template(page_name)


def store_data(data):
    with open("databases.txt", mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n {email} , {subject} , {message}')


def store_csv(data,):
    with open("databases.csv", mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        # csv_writer = csv.writer(database, dialect='excel', **fmtparams ,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        store_data(data)
        store_csv(data)
        return redirect("/thankyou.html")

    else:
        return "Something went wrong. Try again!"
