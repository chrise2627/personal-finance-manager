from flask import Blueprint, render_template, url_for, redirect, request, flash, current_app


main = Blueprint('main', __name__, static_folder='static')

@main.route('/')
def index():
  return render_template('index.html')