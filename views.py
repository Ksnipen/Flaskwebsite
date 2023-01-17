from flask import Blueprint, render_template, request, redirect, url_for, session
from datascraper import webscraper

views = Blueprint(__name__, "/")
ek = 0

@views.route("/", methods = ['POST', 'GET'])
def home():
    return render_template("index.html")

@views.route("/result", methods = ['POST', 'GET'])
def result():
    if request.method == 'POST' and request.form.get('finnkode'):
        if webscraper.check_valid_finncode(request.form.get('finnkode')):
            ek = request.form.get('ek')
            interest = request.form.get('rente').replace(',','.')
            url = f"https://www.finn.no/realestate/homes/ad.html?finnkode={request.form.get('finnkode')}"
            property_data = webscraper.get_essensial_numbers_from_property(webscraper.get_soup(url))
            monthly_municipal_fees = int(int(property_data['municipal_fees'].replace(' ','')) / 12)
            return render_template("result.html", property_data = property_data, monthly_municipal_fees = monthly_municipal_fees, capital = ek, interest = interest)
    return redirect(url_for('views.home'))