# google-images-scraper

## ⚒️ Built With

* Selenium WebDriver
* urllib.request

## ⚠️ Prerequisites

* [Python >3.10](https://www.python.org/downloads/release/python-31013/)

    > Debian GNU/Linux Bash

    ```bash
      sudo apt install python3.10 && apt install python3.10-venv
    ```
    
* [Chrome >115](https://www.google.com/chrome/)

## ⚙️ Installation

1. [Download](https://github.com/yussuf-codes/google-images-scraper/archive/refs/heads/master.zip) or clone the repository

    ```shell
    git clone https://github.com/yussuf-codes/google-images-scraper.git
    ```

    or

    > Debian GNU/Linux Bash

   ```bash
   curl -o google-images-scraper.zip -L https://github.com/yussuf-codes/google-images-scraper/archive/refs/heads/master.zip
   sudo apt install unzip
   unzip google-images-scraper.zip
   ```

2. Navigate to source directory

    ```shell
    cd ./google-images-scraper/src/
    ```

3. Create a virtual environment
    > Debian GNU/Linux Bash

    ```bash
    python3.10 -m venv .venv
    ```

    > Windows PowerShell

    ```powershell
    python -m venv .venv
    ```

4. Activate the virtual environment
    > Debian GNU/Linux Bash

    ```bash
    source ./.venv/bin/activate
    ```

    > Windows PowerShell

    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
    .\.venv\Scripts\Activate.ps1
    ```

5. Install the requirements

    ```shell
    pip install -r ./google-images-scraper/requirements.txt
    ```

## 🚀 Run

> Debian GNU/Linux Bash

```bash
python3.10 main.py -q <SEARCH_QUERY> -n <NUMBER_OF_IMAGES> -d <IMAGES_DIRECTORY>
```

> Windows PowerShell

```powershell
python main.py -q <SEARCH_QUERY> -n <NUMBER_OF_IMAGES> -d <IMAGES_DIRECTORY>
```

## :octocat: Repository Structure

```text
.
├── LICENSE
├── README.md
└── src
    ├── google-images-scraper
    │   ├── __init__.py
    │   ├── implementation.py
    │   └── requirements.txt
    └── main.py
```

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## ❤️ Show your support

Please ⭐️ this repository if this project helped you!
