from flask import Blueprint, render_template
import json

pets = json.load(open('pets.json'))
show_page_bp = Blueprint("show", __name__, template_folder="templates", url_prefix="/pets")


# @show_page_bp.route("/")
# def hello():
#     return "Show Page!"

@show_page_bp.route('/<int:pet_id>')
def show_page(pet_id, pets=pets):
    for i in pets:
        if i["pet_id"] == pet_id:
            return i
            


@show_page_bp.route("/<name>")
def index(name):
    return f"This is {name} in show_page"
