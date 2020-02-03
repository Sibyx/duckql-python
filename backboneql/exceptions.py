class BackboneQLException(Exception):
    pass


class ParseError(BackboneQLException):
    pass


class InvalidQueryException(BackboneQLException):
    pass
