# ER cookiecutter

This is a base template for entity resolution projects. The core components are:
- extractors - for gathering and parsing from data sources
- storage - data store interface
- pipeline - async and/or parallel, long-running data processing
- api - REST or search API