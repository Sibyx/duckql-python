class DuckQLException(Exception):
    pass


class ParseError(DuckQLException):
    pass


class InvalidQueryException(DuckQLException):
    pass
