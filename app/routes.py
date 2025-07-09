# routes.py - placeholder content
from flask import Blueprint, render_template
import pandas as pd
from app.models import check_compliance_and_risk

main = Blueprint('main', __name__)


@main.route('/')
def home():
    data = pd.read_csv('data/simulated_data.csv')
    status = check_compliance_and_risk(data)
    return render_template('index.html', data=status)
