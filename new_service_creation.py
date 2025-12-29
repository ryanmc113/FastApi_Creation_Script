from pathlib import Path


fastapi_project_structure = {
    "backend": {
        "app": {
            "main.py": None,
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
        },
        "tests": {
            "unit": {
                "test_{name}_service.py": None,
            },
            "integration": {
                "test_{name}s_api.py": None,
            },
        },
    }
}


def creation_additional_services(project_structure: dict, current_path: Path):
    for key, value in project_structure.items():

        # Replace template names
        name = "plan"
        key = key.format(name=name)

        if isinstance(value, dict):
            # 1 Create the folder at the CURRENT path
            new_path = current_path / key

            # 2 Recurse INTO the folder
            creation_additional_services(value, new_path)

        else:
            # 3 Create file at CURRENT path
            file_path = current_path / key
            file_path.touch()


root = Path.cwd()

creation_additional_services(fastapi_project_structure, root)
