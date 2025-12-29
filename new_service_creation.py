from pathlib import Path

global name
name = ""

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
