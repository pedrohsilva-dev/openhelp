from flask_restful import reqparse
import werkzeug

parser = reqparse.RequestParser()

def get_request_client():
    parser.add_argument('username', type=str, help='O nome reduzido do cliente.', required=True, strict=True)
    parser.add_argument('email', type=str, help='O melhor email do usuário.', required=True, strict=True)
    parser.add_argument('password', type=str, help='Uma senha forte.', required=True, strict=True)
    parser.add_argument('photo', type=werkzeug.datastructures.FileStorage, location='files')
    parser.add_argument('city', type=str, help='Cidade do cliente.', required=True, strict=True)
    parser.add_argument('state', type=str, help='O Estado que o cliente mora.', required=True, strict=True)
    parser.add_argument('country', type=str, help='Pais que o cliente mora.', required=True, strict=True)

    return parser