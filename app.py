from airports import app, db
from flask import render_template, redirect, request, url_for, flash
from flask_migrate import Migrate
from flask_restful import Api
from resources.objects import Airport

migrate = Migrate(app, db)


@app.route("/", methods=["POST", "GET"])
def hello():
    if request.method == "POST":
        result = request.form
        result_value = result.get("iata_code")
        if result_value:
            return redirect(url_for('airport', iata_code=result_value))
        else:
            flash("Enter a valid IATA code")
            return render_template("index.html")
    return render_template("index.html")


api = Api(app)
api.add_resource(Airport, '/airport', '/airport/<string:iata_code>', endpoint='airport')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
