"""
This is a sample library that requires an env var at import time
"""

import os

assert "SAMPLE_ENV_VAR" in os.environ
