import argparse
import venv

parser = argparse.ArgumentParser()
parser.add_argument(
    "--trusted",
    help="Download packages from pypi as a trusted-host",
    action="store_true",
    default=False,
)

args = parser.parse_args()

venv.create(env_dir=".venv")

