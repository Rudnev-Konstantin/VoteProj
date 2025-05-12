from . import bp
from flask import current_app

from flask import render_template, url_for, redirect


@bp.route("/")
@bp.route("/index")
def index():
    return "<h1>Main page<h1>"


# david_version_catalog_data = (
#     "catalog.html",
#     title="Вход",
#     nav={
#         'authorized': True,
#         'name': "Фамилия Имя Отчество",
#         'avatar': None,
#         'is_user': True
#     },
#     main={
#         'section_name': 'Каталог',
#         'buttons': [
#             {
#                 'name': 'Изменить',
#                 'id': 'edit'
#             },
#             {
#                 'name': 'Добавить',
#                 'id': 'add'
#             }
#         ],
#         'contests': [
#             {
#                 'picture': None,
#                 'name': 'Название',
#                 'status': 0,
#                 'address': 'г. Владикавказ, ул. Владикавказская 69Г',
#                 'datetime': datetime.now().strftime('%Y-%m-%d %H:%M'),
#                 'description': 'Описание'
#             }
#         ]
#     }
# )
