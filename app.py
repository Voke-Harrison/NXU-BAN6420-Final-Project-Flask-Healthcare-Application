# Final Project: Flask Healthcare Application
# Voke Harrison Edafejimue
# Learner ID - 143304


# import necessary libraries
from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import csv



# Flask constructor
app = Flask(__name__)

# Set up MongoDB connection
uri = "mongodb+srv://vokea:vokedara@atlascluster.ggc36je.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Create a database
db = client.flask_db
# Create a collection/table
users = db.users


class user:
    cursor = users.find()
    # Extract the data from the cursor
    data = [doc for doc in cursor]
    # Specify the file path for the CSV file
    file_path = r"./data.csv"
    # Specify the field names for the CSVfile
    field_names = list(data[0].keys())
    # Write the data to the CSV file
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        for doc in data:
            writer.writerow(doc)


@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        income = request.form['income']
        utilities = request.form['utilities']
        entertainment = request.form['entertainment']
        school_fees = request.form['school_fees']
        shopping = request.form['shopping']
        healthcare = request.form['healthcare']
        users.insert_one({'name': name, 'age': age, 'gender': gender, 'income': income, 'utilities': utilities,
                          'entertainment': entertainment, 'school_fees': school_fees, 'shopping': shopping,
                          'healthcare': healthcare})
        return redirect(url_for('index'))
    all_users = users.find()
    return render_template('index.html', users=all_users)


@app.route("/export", methods=('GET', 'POST'))
def export():
    if request.method == 'POST':
        user()
        return redirect(url_for('export'))
    all_users = users.find()
    return render_template('export.html', users=all_users)


if __name__ == '__main__':
    app.run(debug=True)
