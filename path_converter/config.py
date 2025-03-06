# Default domain used for relative paths
DEFAULT_DOMAIN = "domain.com"

# Hotkey assignment for triggering the conversion
HOTKEY = "<cmd>+<shift>+."

# Base path used for building the AEM path
BASE_PATH = "/content/"

# Override with local settings
try:
    from . import config_local

    DEFAULT_DOMAIN = getattr(config_local, "DEFAULT_DOMAIN", DEFAULT_DOMAIN)
    HOTKEY = getattr(config_local, "HOTKEY", HOTKEY)
    BASE_PATH = getattr(config_local, "BASE_PATH", BASE_PATH)
except ImportError:
    pass
