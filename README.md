FastAPI Project Scaffold Generator

    A small Python utility for generating a production-ready FastAPI project structure using a nested dictionary and recursion.

    This project was built to explore and reinforce:

        Clean FastAPI architecture patterns

        Recursive directory traversal

        Explicit state passing (no globals)

        Filesystem automation with pathlib

What This Does

    This script programmatically creates a FastAPI backend folder structure, including:

        Versioned API layout

        Core configuration modules

        Service and DAL layers

        Pydantic schemas

        Test directories

        Template-based file naming

        It is not a FastAPI app itself, but a scaffolding tool to speed up starting new FastAPI projects with a clean architecture baseline.

Architecture Philosophy

    The generated structure follows these principles:

        Routes orchestrate, services contain logic

        Database access is isolated in a DAL

        Schemas define API contracts

        No global state

        Explicit dependency boundaries

        The folder structure mirrors how larger FastAPI applications are typically organized in production environments.

Example Output

    Example generated structure (simplified):

    backend/
    ├── app/
    │   ├── main.py
    │   ├── core/
    │   ├── api/
    │   │   └── v1/
    │   │       └── endpoints/
    │   ├── services/
    │   ├── dal/
    │   ├── schemas/
    │   └── db/
    ├── tests/
    │   ├── unit/
    │   └── integration/
    ├── Dockerfile
    ├── pyproject.toml
    └── README.md

How It Works

    A nested Python dictionary defines the project structure

    Folder keys map to directories

    None values represent files

    A recursive function:

        Creates directories

        Passes the current path downward

        Creates files at the correct scope

        There is no global “current directory” — all path context is passed explicitly.

Usage

    Clone the repository

    Update the project name and template variables

    Run the script

    A new FastAPI backend structure will be generated at the specified root path

This script currently focuses on structure creation only.
It does not populate file contents beyond placeholders.
