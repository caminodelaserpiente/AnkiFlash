# AnkiFlash

Anki Flashcard Audio Generator
---

## 📦 Installation
```consol
git clone https://github.com/caminodelaserpiente/AnkiFlash
```

```consol
cd AnkiFlash
```

```consol
pip install -r requirements.txt
```


## 🎮 Play
```consol
python ankiflash.py test_decks/russian.csv -l russian
```

    usage: ankiflash.py [-h] [-c {front,back}]
                        [-l {spanish,english,french,deutsche,italian,chinese,portuguese,russian}]
                        path_csv

    Processes a CSV file and generates .csv and .mp3 files based on the specified
    options.

    positional arguments:
    path_csv              Required file path for the CSV data. Columns must be
                            separated using a pipe (|) delimiter.

    optional arguments:
    -h, --help            show this help message and exit
    -c {front,back}, --column {front,back}
                            Selects the column to generate .mp3 files from
                            (default: "front").
    -l {spanish,english,french,deutsche,italian,chinese,portuguese,russian}, --lang {spanish,english,french,deutsche,italian,chinese,portuguese,russian}
                            Selects the language for generating .mp3 files
                            (default: "spanish").



## 💾 Files
- Files are stored in the `out_storage` folder


## 📄 License
This project is licensed under the GNU General Public License v3.0. See the [`LICENSE`](LICENSE) file for more information.


## Contributor
```text
╔═══════════════════════════════════════════════════════╗
║ Copyright (C) 2025 Daniel A.L.                        ║
║ Published on GitHub under Caminodelaserpiente         ║
║ https://github.com/caminodelaserpiente                ║
║                                                       ║
║     caminodelaserpiente.py@gmail.com                  ║
║                                                       ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
```
The project was created by [**Daniel A.L.**](https://www.linkedin.com/in/dna-py) and published under [**Caminodelaserpiente (蛇道)**](https://github.com/caminodelaserpiente) on GitHub.