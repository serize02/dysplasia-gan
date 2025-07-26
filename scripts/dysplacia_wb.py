import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from manager.wb import Manager

manager = Manager()
manager.create_artifact(artifact_name='dysplacia-images', type_='dataset', files=[str(p) for p in Path('data/raw').iterdir() if p.is_file()])