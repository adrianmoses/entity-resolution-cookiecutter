# hooks/post_gen_project.py
import os
import shutil
from pathlib import Path


def remove_file_or_dir(path):
    """Remove a file or directory"""
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


def main():
    # Get cookiecutter variables
    orchestrator = "{{ cookiecutter.orchestrator }}"
    api_framework = "{{ cookiecutter.api_framework }}"
    include_vector_search = "{{ cookiecutter.include_vector_search }}"
    include_nlp = "{{ cookiecutter.include_nlp }}"

    project_slug = "{{ cookiecutter.project_slug }}"
    base_path = Path(f"{project_slug}")

    # Remove unused pipeline files
    pipeline_path = base_path / "pipeline"
    if orchestrator != "prefect":
        remove_file_or_dir(pipeline_path / "prefect_flows.py")
    if orchestrator != "airflow":
        remove_file_or_dir(pipeline_path / "airflow_dags.py")
    if orchestrator != "simple":
        remove_file_or_dir(pipeline_path / "simple_pipeline.py")

    # Handle API framework - keep one, remove others
    if api_framework == "fastapi":
        # Rename api_fastapi to api
        if (base_path / "api_fastapi").exists():
            if (base_path / "api").exists():
                shutil.rmtree(base_path / "api")
            (base_path / "api_fastapi").rename(base_path / "api")
        remove_file_or_dir(base_path / "api_flask")
        remove_file_or_dir(base_path / "api_django")

    elif api_framework == "flask":
        if (base_path / "api_flask").exists():
            if (base_path / "api").exists():
                shutil.rmtree(base_path / "api")
            (base_path / "api_flask").rename(base_path / "api")
        remove_file_or_dir(base_path / "api_fastapi")
        remove_file_or_dir(base_path / "api_django")

    elif api_framework == "django":
        if (base_path / "api_django").exists():
            if (base_path / "api").exists():
                shutil.rmtree(base_path / "api")
            (base_path / "api_django").rename(base_path / "api")
        remove_file_or_dir(base_path / "api_fastapi")
        remove_file_or_dir(base_path / "api_flask")

    elif api_framework == "none":
        remove_file_or_dir(base_path / "api_fastapi")
        remove_file_or_dir(base_path / "api_flask")
        remove_file_or_dir(base_path / "api_django")
        remove_file_or_dir(base_path / "api")

    # Remove optional features if not selected
    if include_vector_search != "y":
        remove_file_or_dir(base_path / "search" / "vector_store.py")
        remove_file_or_dir(base_path / "embeddings")

    if include_nlp != "y":
        remove_file_or_dir(base_path / "nlp")

    print("✅ Project structure cleaned up based on selections!")


if __name__ == "__main__":
    main()