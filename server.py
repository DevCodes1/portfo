# lonked to the text file database CSV File

from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def home():
    return render_template('/index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# writing to file method = CSV File


def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
# database.write(f'\n{email},\t\t{subject}, \t\t{message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_Form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        # print(data)
        return redirect('/thankyou.html')
    else:
        return 'Somthing went wrong'
