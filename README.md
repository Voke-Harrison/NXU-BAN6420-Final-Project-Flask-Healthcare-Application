# NXU-BAN6420-Final-Project-Flask-Healthcare-Application
In the attached Zip file named BAN 6420 Final Project contains;
* app.py - a Python source file with flask -accessible on http://127.0.0.1:5000
* exportdb.py - a Python source file with flask and a class named 'user' for downloading data from Mongodb - accessible on http://127.0.0.1:5000/export
* Template folder containing
  * index.html - a html document for the App python source file
  * export.html - a html document for the exportdb python source file
* Visualization - a Jupyter source file for visualizations and downloading the corresponding visualization images.
* Others -
  * data - a csv file generated from the app python source file
  * GenderbyUtilities.jpg - Visualization image.
  * GenderbyIncome.jpg - Visualization image.
  * GenderbyEntertainment.jpg - Visualization image.
  * GenderbyShopping.jpg - Visualization image.
  * GenderbySchoolFees.jpg - Visualization image.
  * GenderbyHealthcare.jpg - Visualization image.
  * Other system folders and files.

# Steps to Host the Flask application on Vercel
1. Create an account with Vercel.
2. Use npm to install Vercel globally on your computer.
3. Make sure that you have the latest version of Python3 installed and the Flask framework with pip3.
4. Navigate to directory for your Flask app using the command line. then Add the required dependencies to the `requirements.txt` file.
5. Create a new file called `vercel.json` in the root directory of your app. This file will contain the configuration information for Vercel.
6. Deploy your app to Vercel by running the command - vercel --prod
