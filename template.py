import os
from pathlib import Path

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__int__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "Experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = filepath.parent, filepath.name
    # print(f"Dir is {filedir}\nFile name is {filename}")
    if not filedir.is_dir():
        filedir.mkdir(parents=True, exist_ok=True)

    if not filepath.exists():
        filepath.touch()
    # filedir, filename = os.path.split(filepath)
    # if filedir != "":
    #     os.makedirs(filedir, exist_ok=True)
    #     # logging.info(f"Creating directory: {filedir} for file {filename}")

    # if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
    #     with open(filepath, "w") as f:
    #         pass # Creating en empty file