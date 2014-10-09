from os.path import abspath, join, basename
import sys

ROOT_PATH = abspath(join(basename(__file__), '..'))

if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)
