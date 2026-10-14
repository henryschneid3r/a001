from pathlib import Path

# define the base directory "backend/src/"
BASE_DIR = Path(__file__).resolve().parent.parent

# define the root dir "a001/"
ROOT_DIR = BASE_DIR.parent.parent

print(BASE_DIR, ROOT_DIR)
