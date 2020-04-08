# Changelog

## 0.2.0 : 2020-04-09

Project renamed to `duckql`, this is the first public release (development status modifier changed to beta).

- **Change**: Name changed to `duckql`
- **Change**: [Poetry](https://python-poetry.org/) as package manager

## 0.1.8 : 2020-04-07

- **Feature**: Subquery support
- **Note**: Changelog datetimes in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compatible `Y-m-d` format

## 0.1.7 : 2020-03-17

- **Fix**: Adding missing imports in `__init__.py` files inside of submodules
- **Change**: Moved `__version__` from `__init__.py` to `version.py`
- **Note**: Development status change to Alpha

## 0.1.6 : 2020-03-13

- **Feature**: Introduced `functions.StringAgg`
- **Feature**: Introduced `structures.CastOperator`
- **Feature**: CLI for parsing files

## 0.1.5 : 2020-02-05

- **Change**: Allow direct use of `structures.Comparision` in query conditions

## 0.1.4 : 2020-02-05

- **Fix**: Allow aliases in `structures.Query`
- **Change**: Do not escape `%`

## 0.1.3 : 2020-02-03

- **Feature**: Natural join support

## 0.1.2 : 2020-02-03

- **Change**: Completed docs
- **Feature**: Recursive nested properties lookup in `Query` object

## 0.1.1 : 2020-02-26

- **Change**: Default values for optional attributes in `structures.Query`
- **Change**: `custom_parser` now can raise `ParseError` if there is invalid object type passed

## 0.1.0 : 2020-02-26

- Initial release
