# Changelog

## 0.14.0 : 2024-01-12

⚠️ This release is not working with Python 3.13!! ⚠️

Chores, chores and chores. This will be probably the last release based on the Pydantic 1.x.

🌈 Pink fluffy unicorns dancing on rainbows 🌈

- **Changed**: Dropped support for Python 3.7 and 3.8

## 0.13.0 : 2022-06-09

- **Added**: Ability to use casting for `ORDER BY` property

## 0.12.1 : 2022-05-10

- **Fixed**: Corrected cast of JSON fields

## 0.12.0 : 2021-12-21

- **Feature**: `FirstValue` window function introduced
- **Feature**: Positional `ArrayAgg` introduced

## 0.11.1 : 2021-12-14

- **Change**: Ability to cast to UUID

## 0.11.0 : 2021-12-10

- **Feature**: More benevolent type nesting

## 0.10.0 : 2021-11-30

- **Feature**: `Case` introduced (without docs, there was no time, sry, let's call it Easter Egg for a while)

## 0.9.1 : 2021-07-20

- **Fix**: Fixed problem with multiple properties in operations (I had to remove comparison property check)

## 0.9.0 : 2021-06-25

- **Fix**: Fixed nested conditions (`Operator` can contain another `Operator`)
- **Change**: Dropped Python 3.6 support

## 0.8.2 : 2020-10-15

- **Fix**: Use `->` instead of `-->`

## 0.8.1 : 2020-10-15

- **Fix**: Use `-->` operator in JSON lookup chaining in nested objects

## 0.8.0 : 2020-10-14

- **Feature**: Nested JSON fields

## 0.7.2 : 2020-08-28

- **Fix**: Use `->>` operator in JSON lookup instead of `->` (cast result as text)

## 0.7.1 : 2020-08-27

- **Fix**: Use quotes in JSON column type keys in `Property`

## 0.7.0 : 2020-08-27

- **Feature**: Now is possible to pass `Distinct` to `Count` to have `COUNT(DISTINCT property)` syntax in pSQL
- **Tests**: Test for JSON column type in pSQL

## 0.6.1 : 2020-08-04

- **Fix**: Use native `typing.Literal` if possible (Python 3.8 compatibility fix)

## 0.6.0 : 2020-07-23

- **Feature**: `lower` function introduced
- **Feature**: `upper` function introduced
- **Feature**: pSQL `initcap` function introduced

## 0.5.0 : 2020-07-22

- **Feature**: `QueryFactory` supporting `json`, `msgpack` and `bson`
- **Feature**: pSQL `unaccent` function introduced

## 0.4.0 : 2020-06-12

- **Feature**: `Extract.Unit.DAY` introduced
- **Feature**: `CastOperator.DataType.REAL` introduced
- **Feature**: pSQL `to_char` function introduced
- **Feature**: pSQL `to_date` function introduced

## 0.3.0 : 2020-05-20

- **Feature**: `HAVING` support
- **Feature**: `NOW()` support
- **Fix**: `Comparision` allows to have every `BaseType` as `properties`
- **Fix**: Interval value is quoted now

## 0.2.2 : 2020-04-16

- **Change**: Ability to pass `structures.Distinct` into `functions.StringAgg`

## 0.2.1 : 2020-04-09

- **Fix**: Fixed JOIN aliases

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
