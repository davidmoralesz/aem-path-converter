# AEM Path Converter

AEM Path Converter is a Python tool designed to transform clipboard content —specifically URLs, relative paths, or HTML snippets containing `href` attributes— into a standardized Adobe Experience Manager (AEM) path format.

## Features

- **URL Formatting:** Converts full URLs into a standardized path.
   - from `https://www.domain.com/en/branch/page.html`
   - to `/content/domain-com/en/branch/page`
- **Relative Path Handling:** Processes relative paths to produce complete paths.
   - from `/en/branch/page.html`
   - to `/content/{default_domain}/en/branch/page`
- **HTML `href` Attribute Processing:** Extracts and formats URLs within `href` attributes to the desired path structure.
   - from `href="/en/branch/page.html"`
   - to `/content/{default_domain}/en/branch/page`

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/davidmoralesz/aem-path-converter.git
   cd aem-path-converter
   ```

2. **Set Up a Virtual Environment [Recommended]:**

   Creating a virtual environment ensures that dependencies are isolated from your system-wide packages.

   - **Create the Virtual Environment:**

     ```bash
     python3 -m venv env
     ```

   - **Activate the Virtual Environment:**

     - On macOS/Linux:

       ```bash
       source env/bin/activate
       ```

     - On Windows:

       ```bash
       env\Scripts\activate
       ```

3. **Install the Tool:**

   You can install the package in editable mode, which also installs all required dependencies:

   ```bash
   pip install -e .
   ```

   Alternatively, if you prefer to use `requirements.txt`, install dependencies with:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Copy Content:**

   Highlight and copy the URL, relative path, or HTML snippet with the `href` attribute you want to format.

2. **Format the Clipboard Content:**

   Press the designated hotkey (default is Cmd + Shift + . on macOS) to trigger the formatting. The tool will:
   - Validate the clipboard content.
   - Convert it into the valid AEM path format.
   - Copy the formatted path back to the clipboard.
   - Log the conversion status.

3. **Run the Hotkey Listener:**

   After installing, start the hotkey listener by running:

   ```bash
   aem-path-converter
   ```

   This command launches the global hotkey listener, which will run continuously until you terminate it.

## Configuration

- **Configuration Files (`config.py` & `config_local.py`):**

  The `config.py` file centralizes configuration settings for the tool. Your personal configurations should be stored in `config_local.py`.

  **Creating a Local Configuration (`config_local.py`):**  
  To customize these settings without modifying `config.py`, create a `config_local.py` file in the same directory and override only the necessary values.  

  Example:
  ```py
  # path_converter/config_local.py

  # Custom domain used for relative paths
  DEFAULT_DOMAIN = "custom-domain.com"

  # Custom hotkey assignment
  HOTKEY = "<cmd>+<shift>+."

  # Custom base path
  BASE_PATH = "/custom-content/"
  ```

  **Steps to Set Up:**
  1. Copy `config_local.example.py` as `config_local.py`.
  2. Modify values as needed.
  3. `config_local.py` is ignored by Git, ensuring your personal settings remain local.

## Terminating the Script

If necessary, to stop the AEM Path Converter script running in the background, you can use the `pkill` command:

```bash
pkill -f aem-path-converter
```

## License

This project is licensed under [CC0 1.0 Universal](LICENSE).

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

---

By following these instructions, you'll have a robust setup for transforming clipboard content into an AEM-friendly path format. Enjoy using AEM Path Converter!