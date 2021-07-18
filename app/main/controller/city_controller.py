from flask import request
from flask_restx import Resource

from ..util.dto import (
    CityDto,
)

from ..service.location_service import (
    save_new_city,
    get_an_city,
)


api = CityDto.api
_city = CityDto.city


@api.route('/')
class CityCreate(Resource):
    @api.expect(_city, validate=True)
    @api.response(201, 'City successfully created.')
    @api.doc('Create a city')
    def post(self):
        """Create a city"""
        data = request.json
        return save_new_city(data=data)


@api.route('/<city_id>')
@api.param('city_id', 'The city identifier')
@api.response(404, 'City not found.')
class City(Resource):
    @api.doc('Get a city')
    @api.marshal_with(_city)
    def get(self, city_id):
        """get City information given its identifier"""
        city = get_an_city(city_id)
        if not city:
            api.abort(404)
        else:
            return city
