# AnkiFlash

 ![Python Version](https://img.shields.io/badge/python-3.10%2B-0055f9?labelColor=FFF80C&logo=python) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-A42E2B?labelColor=333333&logo=gnu&logoColor=FCC624)](LICENSE) ![Linux](https://img.shields.io/badge/Kernel-Linux-ffd133?labelColor=333333&logo=linux&logoColor=FCC624)



> **Automated TTS generator for Anki flashcards powered by CSV data.**


* ### License: This project is licensed under the GNU General Public License v3.0. See the [`LICENSE`](LICENSE) file for more information.


* ### Quick start:
    ```sh
    git clone https://github.com/caminodelaserpiente/AnkiFlash.git
    cd AnkiFlash
    pip install -r requirements.txt
    ```


* ## Play
    ```sh
    python ankiflash.py --help
    ```

        usage: ankiflash.py [-h] [-c {front,back}] [-l {spanish,english,french,deutsche,italian,chinese,portuguese,russian}] path_csv

        Processes a CSV file and generates .csv and .mp3 files based on the specified options.

        positional arguments:
        path_csv              Required file path for the CSV data. Columns must be separated using a pipe (|) delimiter.

        options:
        -h, --help            show this help message and exit
        -c {front,back}, --column {front,back}
                                Selects the column to generate .mp3 files from (default: "front").
        -l {spanish,english,french,deutsche,italian,chinese,portuguese,russian}, --lang {spanish,english,french,deutsche,italian,chinese,portuguese,russian}
                                Selects the language for generating .mp3 files (default: "spanish").

        Quick Start: python ankiflash.py test_decks/russian.csv -l russian


* ## NOTE.
    - Files are stored in the `out_storage` folder


```text
╔══════════════════════════════╗
║                      .........                   ║
║                  ............... .               ║
║                ........    ....    .             ║
║              ..........    ....     .            ║
║             ..................       .           ║
║            ................ .         .          ║
║            ........... .              .          ║
║             ........                 .           ║
║              ......    ....         .            ║
║                ....    ....       .              ║
║                  . .           . .               ║
║                      . . . . .                   ║
║ Copyright (C) 2025                               ║
║ Published on GitHub powered by:                  ║
║ Caminodelaserpiente                              ║
║ https://github.com/caminodelaserpiente           ║
║ caminodelaserpiente.py@gmail.com                 ║
╚══════════════════════════════╝
```
