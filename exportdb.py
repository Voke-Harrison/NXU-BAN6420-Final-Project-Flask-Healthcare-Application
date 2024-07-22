# Export Data in Mongo db to data.csv
# Voke Harrison Edafejimue
# Learner ID - 143304

# import necessary libraries
from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import csv

# Flask constructor
app = Flask(__name__)
# Set up MongoDB connection
client = MongoClient("mongodb://localhost:27017")

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


@app.route("/export", methods=('GET', 'POST'))
def export():
    if request.method == 'POST':
        user()
        return redirect(url_for('export'))
    all_users = users.find()
    return render_template('export.html', users=all_users)


if __name__ == '__main__':
    app.run(debug=True)

