# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Cookiecutter template for entity resolution projects. It generates Python projects with a modular architecture designed for data extraction, processing, and storage workflows.

## Architecture

The generated projects follow a 4-layer architecture:

1. **Extractors** (`src/extractors/`) - Data gathering and parsing from various sources (web scraping, APIs, files, databases)
2. **Storage** (`src/storage/`) - Data persistence layer with pluggable backends (SQLite, PostgreSQL, Neo4j)
3. **Pipeline** (`src/pipeline/`) - Async/parallel data processing workflows (Prefect, Airflow orchestration)
4. **API** (`src/api/`) - REST or search API endpoints (FastAPI, Flask)

Core configuration is managed through `src/config/settings.py` using Pydantic settings with environment variable support.

## Template Configuration

The template uses `cookiecutter.json` to configure:
- Data sources: web_scraping, api, files, database
- Storage backends: sqlite, postgresql, neo4j  
- Pipeline orchestrators: prefect, airflow
- Search engines: elasticsearch, opensearch
- API frameworks: fastapi, flask
- NLP requirements and language support

## Development Commands

Generated projects include these standardized commands via `pyproject.yaml`:

**Testing:**
```bash
pytest                    # Run all tests
pytest --cov             # Run with coverage
pytest -m "not slow"     # Skip slow tests
pytest tests/test_specific.py  # Run specific test file
```

**Code Quality:**
```bash
black src/ tests/        # Format code
isort src/ tests/        # Sort imports  
flake8 src/ tests/       # Lint code
mypy src/                # Type checking
```

**Installation:**
```bash
pip install -e .         # Development install
pip install -e ".[dev]"  # With dev dependencies
pip install -e ".[test]" # With test dependencies
```

**Project Scripts:**
```bash
{project_slug}           # Main CLI entry point
{project_slug}-worker    # Pipeline worker (if Prefect selected)
```

## Template Development

When working on the cookiecutter template itself:
- Template files are in `{{ cookiecutter.project_slug }}/`
- Variables use Jinja2 syntax: `{{ cookiecutter.variable_name }}`
- Conditional content uses `{% if cookiecutter.option %}` blocks
- Post-generation cleanup handled by `hooks/post_gen_project.py`
- Test generation with: `cookiecutter .` from repository root

**Testing Template Generation:**
```bash
cookiecutter .                    # Generate project with prompts
cookiecutter . --no-input         # Generate with defaults
cookiecutter . --replay           # Replay last generation
```

**Template Structure:**
- `cookiecutter.json` - Template configuration and variables
- `hooks/pre_gen_project.py` - Pre-generation validation
- `hooks/post_gen_project.py` - Post-generation cleanup (removes unused components)
- `{{ cookiecutter.project_slug }}/` - Main template directory

## Key Template Features

The template conditionally includes components based on cookiecutter.json selections:
- **Database backends**: SQLite, PostgreSQL (with optional pgvector), Neo4j, MongoDB
- **Pipeline orchestrators**: Prefect, Dagster, or simple pipeline
- **API frameworks**: FastAPI, Flask, Django, or none
- **Search engines**: None, vector/hybrid, Elasticsearch
- **Optional features**: Web scraping, API scraping, vector search, NLP, Docker

Generated projects include Docker Compose configurations for selected services.