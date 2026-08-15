import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"


def load_env():
    """Load environment variables from the project's .env file."""
    return load_dotenv(ENV_PATH)


def get_key(name, default=None):
    """Return an environment variable or a default value."""
    return os.getenv(name, default)
