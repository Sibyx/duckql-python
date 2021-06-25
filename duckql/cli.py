import click

from .structures import Query, Operator


@click.group()
def cli():
    pass


@cli.command()
def schema():
    Query.update_forward_refs()
    Operator.update_forward_refs()
    print(Query.schema_json(indent=2))


@cli.command()
@click.argument('filename')
def file(filename):
    Query.update_forward_refs()
    Operator.update_forward_refs()
    my_query = Query.parse_file(filename)
    print(my_query)


if __name__ == '__main__':
    cli()
