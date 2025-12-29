from pathlib import Path

fastapi_project_structure = {
    "backend": {
        "app": {
            "main.py": None,
            "core": {
                "config.py": None,
                "logging.py": None,
                "security.py": None,
                "lifespan.py": None,
            },
            "api": {
                "deps.py": None,
                "v1": {
                    "router.py": None,
                    "endpoints": {
                        "{name}s.py": None,
                    },
                },
            },
            "models": {
                "domain": {
                    "{name}.py": None,
                },
                "db": {
                    "{name}.py": None,
                },
            },
            "schemas": {
                "{name}.py": None,
            },
            "services": {
                "{name}_service.py": None,
            },
            "dal": {
                "{name}_dal.py": None,
            },
            "db": {
                "session.py": None,
                "init.py": None,
            },
        },
        "tests": {
            "unit": {
                "test_{name}_service.py": None,
            },
            "integration": {
                "test_{name}s_api.py": None,
            },
        },
        "Dockerfile": None,
        "pyproject.toml": None,
        "README.md": None,
        ".env": None,
        ".gitignore": None,
    }
}


def project_creation(project_structure: dict, current_path: Path):
    for key, value in project_structure.items():

        # Replace template names
        name = "flash_card"
        key = key.format(name=name)

        if isinstance(value, dict):
            # 1 Create the folder at the CURRENT path
            new_path = current_path / key
            new_path.mkdir(parents=True, exist_ok=True)

            # 2 Recurse INTO the folder
            project_creation(value, new_path)

        else:
            # 3 Create file at CURRENT path
            file_path = current_path / key
            file_path.touch()


def file_creator(folder_path, file_name):
    file_path = folder_path / file_name
    file_path.write_text("#Hello, this file was created using pathlib!")


def folder_creator(folder_name):
    folder_path = Path(f"{folder_name}")
    folder_path.mkdir(parents=True, exist_ok=True)


root = Path.cwd()
root.mkdir(exist_ok=True)

project_creation(fastapi_project_structure, root)
