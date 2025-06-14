from django.db.models import Func


class Unaccent(Func):
    function = 'unaccent'
    arity = 1
