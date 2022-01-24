from flask import Blueprint
from sources.utils.response import Response
from sources.business.cubo import CuboBusiness
import requests


cubo_api = Blueprint('cubo', __name__)
cubo_business = CuboBusiness()
header = { "Authorization" : "Basic aXRicm9rZXI6cmVrb3JidGkz" }

@cubo_api.route('/getfullcnpj/<int:cnpj>', methods=['GET'], strict_slashes=False)
def find_all(cnpj):
    result = requests.get(f'http://api-es.speedio.com.br:5003/getfullcnpjdata?cnpj={cnpj}',headers=header)
    return result.json()