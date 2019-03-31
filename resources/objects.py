# -*- coding: utf-8 -*-
from flask import render_template, Response, redirect, url_for, flash
from flask_restful import Resource, reqparse
from airports import db


class Airport(Resource):
    def get(self, iata_code):
        if iata_code:
            query = db.engine.execute("SELECT * FROM airports WHERE iata_code=?", (iata_code.upper(),))
            first_element = query.first()
            if first_element:
                result = dict((x, y) for x, y in zip(query.keys(), first_element))
                coord = list(map(float, result.get("coordinates", ("0, 0")).split(", ")))
                return Response(render_template('airport.html', result=result, coord=coord[::-1]))
        flash("Not found")
        return redirect(url_for('hello'))

    def post(self, iata_code):
        parser = reqparse.RequestParser()
        parser.add_argument('iata_code', type=str)
        args = parser.parse_args()
        return redirect(url_for('airport', iata_code=args['iata_code']))
