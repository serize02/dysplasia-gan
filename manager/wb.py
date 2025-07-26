import wandb
from typing import Optional

class Manager:
    def __init__(self, project='dysplacia-gan'):
        self.project = project

    def create_artifact(self, artifact_name: str, type_: str, files: list[str], metadata: Optional[dict] = None):
        run = wandb.init(project=self.project, job_type=f'log_{type_}', reinit=True)
        artifact = wandb.Artifact(name=artifact_name, type=type_, metadata=metadata or {})
        for file in files:
            artifact.add_file(file)
        wandb.log_artifact(artifact)
        wandb.finish()

    def download_artifact(self, artifact_path: str, type_: str) -> str:
        run = wandb.init(project=self.project, job_type=f'download_{type_}', reinit=True)
        artifact = run.use_artifact(artifact_path, type=type_)
        artifact_dir = artifact.download()
        wandb.finish()
        return artifact_dir
