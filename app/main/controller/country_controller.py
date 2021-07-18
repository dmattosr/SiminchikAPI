from flask import request
from flask_restx import Resource

from ..util.dto import (
    CountryDto,
)

from ..service.location_service import (
    save_new_country,
    get_an_country,
)


# ########## Country
api = CountryDto.api
_country = CountryDto.country


@api.route('/')
class CountryCreate(Resource):
    @api.expect(_country, validate=True)
    @api.response(201, 'Country successfully created.')
    @api.doc('Create a country')
    def post(self):
        """Create a country"""
        data = request.json
        return save_new_country(data=data)


@api.route('/<country_id>')
@api.param('country_id', 'The country identifier')
@api.response(404, 'Country not found.')
class Country(Resource):
    @api.doc('Get a country')
    @api.marshal_with(_country)
    def get(self, country_id):
        """get Country information given its identifier"""
        country = get_an_country(country_id)
        if not country:
            api.abort(404)
        else:
            return country
