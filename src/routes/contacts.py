from flask import Blueprint, render_template

contacts_bp = Blueprint("contacts", __name__)

@contacts_bp.route("/")
def index():
    return render_template("index.html")
    
@contacts_bp.route("/new")
def new_contact():
    return render_template("new.contact.html")

@contacts_bp.route("/update")
def update_contact():
    return render_template("update.contact.html")

@contacts_bp.route("/delete")
def delete_contact():
    return render_template("delete.contact.html")

@contacts_bp.route("/about")
def about():
    return render_template("about.html")