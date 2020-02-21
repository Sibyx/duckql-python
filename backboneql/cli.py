import click

from .structures import Query


@click.group()
def cli():
    pass


@cli.command()
def schema():
    print(Query.__pydantic_model__.schema_json(indent=2))
    # query = Query('users')
    # print(query.__pydantic_model__.schema_json(indent=2))


if __name__ == '__main__':
    cli()
