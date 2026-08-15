from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "ml_project"

list_of_files = [
    f"src/{project_name}/__init__.py",

    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",

    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",

    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",

    "app.py",
    "Dockerfile",
]

for file in list_of_files:
    filepath = Path(file)

    filepath.parent.mkdir(parents=True, exist_ok=True)

    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Created: {filepath}")
    else:
        logging.info(f"Already exists: {filepath}")