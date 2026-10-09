from pathlib import Path
from pprint import pprint
import json

class Directories():
    def __init__(self):
        self.main = Path(__file__).resolve().parent.parent
        self.backend = self.main / "backend"

    def __repr__(self):
        directories = {
            "main":str(self.main),
            "backend":str(self.backend)
        }
        return json.dumps(directories)

dirs = Directories()

pprint(dirs, indent=2)
