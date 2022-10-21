
# def company_request_response():
#     # resposta vai ser no formato abaixo
#     resource_fields = {
#         "id": fields.Integer(),
#         "company_name": fields.String(),
#         "email": fields.String(),
#         "city": fields.String(),
#         "state": fields.String(),
#         "photo_profile": fields.String()
#     }
#     # request de validação do formulario api de envio
#     parser = reqparse.RequestParser()
#     parser.add_argument('company_name', location="form")
#     parser.add_argument('email', location="form")
#     parser.add_argument('password', location="form")
#     parser.add_argument('city', location="form")
#     parser.add_argument('state', location="form")
#     parser.add_argument(
#         "photo_profile", type=werkzeug.datastructures.FileStorage, location='files'
#     )

#     return {
#         "parser": parser,
#         "resource": resource_fields
#     }


# resource_field_company = company_request_response()['resource']
# parser_company = company_request_response()['parser']

# # requisição de paginação
# parser_get_pagination = reqparse.RequestParser()
# parser_get_pagination.add_argument("page", type=int, location="args")


# class CompanyResource(Resource):

#     def __init__(self):
#         ...

#     @marshal_with(resource_field_company)
#     def get(self, company_id=None):
#         if company_id == None:
#             args = parser_get_pagination.parse_args(request)
#             requerystr = args.get("page")

#             return Company.getAll(page=requerystr), 200
#         else:
#             return Company.find(company_id=company_id), 200

#     @marshal_with(resource_field_company, "company")
#     def post(self):
#         args = parser_company.parse_args(request)
#         # get values company
#         company_name = args.get("company_name")
#         email = args.get("email")
#         password = args.get("password")
#         city = args.get("city")
#         state = args.get("state")
#         # photo company
#         photo_profile = args.get("photo_profile")

#         filename = photo_profile.filename

#         # salva companye
#         company = Company(company_name, email, password, city,
#                           state, filename)

#         company.save()

#         return company, 200

#     @marshal_with(resource_field_company)
#     def patch(self, company_id):
#         args = parser_company.parse_args(request)

#         company = Company.find(company_id=company_id)
#         # atualiza companye
#         company.update_company(args)

#         return company

#     def delete(self, company_id):

#         company: company = Company.query.filter_by(id=int(company_id))
#         # deleta companye
#         company.delete_object()
#         return company_id
