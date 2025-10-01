import pytest


def test_bake_with_defaults(cookies):
    """Test template generation with default values"""
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.project_path.is_dir()
    assert result.project_path.joinpath('src').exists()


def test_bake_selecting_api(cookies):
    """Test API framework selection"""
    result = cookies.bake(extra_context={'api_framework': 'fastapi'})
    assert result.exit_code == 0
    assert result.project_path.is_dir()
    assert result.project_path.joinpath('src/api_fastapi').exists()


def test_bake_with_nlp(cookies):
    """Test with NLP enabled"""
    result = cookies.bake(extra_context={'include_nlp': 'yes'})
    assert result.exit_code == 0
    project_dir = result.project_path
    assert (project_dir / 'src/matchers').exists()


@pytest.mark.parametrize('api_framework', ['fastapi', 'flask', 'django', 'none'])
def test_api_framework_options(cookies, api_framework):
    """Test all API framework options"""
    result = cookies.bake(extra_context={'api_framework': api_framework})
    assert result.exit_code == 0
    assert result.project_path.is_dir()

    if api_framework != 'none':
        assert (result.project_path / f'src/api_{api_framework}').exists()


@pytest.mark.parametrize('database', ['sqlite', 'postgresql', 'neo4j'])
def test_database_options(cookies, database):
    """Test all database options"""
    result = cookies.bake(extra_context={'database': database})
    assert result.exit_code == 0
    assert result.project_path.is_dir()


def test_docker_compose_created(cookies):
    """Test that docker-compose.yml is created when use_docker is yes"""
    result = cookies.bake(extra_context={'use_docker': 'yes'})
    assert result.exit_code == 0
    assert (result.project_path / 'docker-compose.yml').exists()


def test_project_structure(cookies):
    """Test that generated project has expected structure"""
    result = cookies.bake()
    assert result.exit_code == 0

    project_dir = result.project_path
    assert (project_dir / 'src').exists()
    assert (project_dir / 'src/config').exists()
    assert (project_dir / 'src/config/settings.py').exists()
    assert (project_dir / 'tests').exists()
    assert (project_dir / 'pyproject.toml').exists()
    assert (project_dir / 'README.md').exists()