# google-images-scraper

## ⚒️ Built using

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

1. [Download](https://github.com/yussuf-codes/google-images-scraper/archive/master.zip) the project
    > Debian GNU/Linux Bash

   ```bash
   wget -O google-images-scraper-master.zip https://github.com/yussuf-codes/google-images-scraper/archive/master.zip
   sudo apt install unzip
   unzip google-images-scraper-master.zip
   ```

2. Navigate to source directory

    ```shell
    cd ./google-images-scraper-master/src/
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
    pip install -r ./google_images_scraper/requirements.txt
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
