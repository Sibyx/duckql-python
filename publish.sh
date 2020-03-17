#!/bin/bash

# Publish package
python setup.py sdist bdist_wheel
twine upload --repository-url https://pypi.backbone.sk dist/*
rm -rf build dist backboneql.egg-info

# Build docs
mkdocs build
cd site ; zip -r ../backboneQL-v0.0.0-Docs.zip * ; cd ..
rm -rf site
