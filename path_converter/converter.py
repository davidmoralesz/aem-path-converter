from .config import DEFAULT_DOMAIN, BASE_PATH
import logging
import re
from urllib.parse import urlparse
import pyperclip
import validators

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def convert_url(input_text: str) -> str:
    """
    Converts a URL or relative path into an AEM-compatible format.

    Args:
        input_text (str): The input URL or path.

    Returns:
        str: The formatted AEM-compatible path.
    """
    parsed = urlparse(input_text)

    # Determine the domain
    if parsed.netloc:
        domain = parsed.netloc
        domain = domain[4:] if domain.startswith("www.") else domain
        domain = domain.replace(".", "-")
    else:
        domain = DEFAULT_DOMAIN

    # Process the path
    path = parsed.path.rstrip(".html")  # Remove `.html` extension if present
    path = f"/{path.lstrip('/')}"  # Ensure leading `/`

    return f"{BASE_PATH}{domain}{path}"


def extract_href(text: str) -> str | None:
    """
    Extracts the href value from an HTML snippet.

    Args:
        text (str): HTML snippet containing an href attribute.

    Returns:
        str | None: Extracted href value if found, otherwise None.
    """
    match = re.search(r'href="([^"]+)"', text)
    return match.group(1) if match else None


def format_clipboard() -> None:
    """
    Reads the clipboard content, processes it, and replaces it with the formatted version.
    """
    text = pyperclip.paste().strip()

    if 'href="' in text:
        href_value = extract_href(text)
        if href_value:
            formatted = convert_url(href_value)
            pyperclip.copy(formatted)
            logging.info("Formatted & copied: %s", formatted)
        else:
            logging.warning("No valid href found. No action taken.")
        return

    # Determine if input is a valid URL or relative path
    parsed = urlparse(text)
    if validators.url(text) or (
        parsed.scheme == "" and parsed.netloc == "" and parsed.path.startswith("/")
    ):
        formatted = convert_url(text)
        pyperclip.copy(formatted)
        logging.info("Formatted & copied: %s", formatted)
    else:
        logging.warning(
            "Selected text is not a valid URL, path, or href attribute. No action taken."
        )
