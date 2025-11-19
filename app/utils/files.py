# ANKIFLASH Daniel A. L.
# Repository: https://github.com/caminodelaserpiente/AnkiFlash

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
import pandas as pd
from gtts import gTTS
from typing import Union


LANGUAGES = {
    'spanish': ['es', 'com.mx'],
    'english': ['en', 'us'],
    'french': ['fr', 'fr'],
    'deutsche': ['de', 'de'],
    'italian': ['it', 'it'],
    'chinese': ['zh', None],
    'portuguese': ['pt', 'com.br'],
    'russian': ['ru', None],
}


def read_csv(path_file: str) -> Union[pd.DataFrame, None]:
    """
    Reads a CSV file and returns a pandas DataFrame, using a pipe (|) as the separator.
    Args:
        path_file (str): Path to the CSV file.

    Returns:
        Union[pd.DataFrame, None]: DataFrame containing data from the CSV file, or None if there was an error.
    """
    try:
        df = pd.read_csv(path_file, sep='|', header=0)
        df.columns = ["front", "back"]
        print(f"[OK] CSV file '{path_file}' read successfully.")
        return df
    except Exception as e:
        print(f"[ERROR] reading CSV file '{path_file}': {e}")
        return None


def generate_files(dataframe: pd.DataFrame, option_column: str = 'front', default_language: str = 'spanish'):
    """
    Generates CSV and MP3 files based on the provided DataFrame.

    Args:
        dataframe (pd.DataFrame): DataFrame containing 'front' and 'back' columns.
        option_column (str, optional): Column name to use for generating files. Defaults to 'front'.
        default_language (str, optional): Default language for generating MP3 files. Defaults to 'spanish'.
    """
    try:
        _generate_csv(dataframe, option_column)
        _generate_mp3(dataframe, option_column, default_language)
    except Exception as e:
        print(f"[ERROR] generating files: {e}")


def _generate_csv(df: pd.DataFrame, option_column: str):
    """
    Generates a CSV file for Anki import.

    Args:
        df (pd.DataFrame): DataFrame containing data to export.
        option_column (str): Column name to use for generating CSV.
    """
    try:
        df_anki = df.copy()
        if not os.path.exists('out_storage'):
            os.makedirs('out_storage')
        name_csv = os.path.join('out_storage', 'import_anki.csv') 
        df_anki[option_column] = df_anki.apply(lambda row: f"{row[option_column]}<br>[sound:{row[option_column]}.mp3]", axis=1)
        df_anki.to_csv(name_csv, index=False, header=False, sep='|')
        print(f"[OK] CSV file '{name_csv}' generated successfully.")
    except Exception as e:
        print(f"[ERROR] generating CSV file: {e}")


def _generate_mp3(dataframe: pd.DataFrame, option_column: str, option_lang: str):
    """
    Generates MP3 files based on text in the specified column.

    Args:
        dataframe (pd.DataFrame): DataFrame containing text data.
        option_column (str): Column name containing text to convert to speech.
        option_lang (str): Language code for speech generation.
    """
    try:
        languages = {
            'spanish': ['es', 'com.mx'],
            'english': ['en', 'us'],
            'french': ['fr', 'fr'],
            'deutsche': ['de', 'de'],
            'italian': ['it', 'it'],
            'chinese': ['zh', None],
            'portuguese': ['pt', 'com.br'],
            'russian': ['ru', None],
        }

        language_info = LANGUAGES.get(option_lang)
        if language_info is None:
            raise ValueError(f"Idioma no soportado: {option_lang}")
        lang_code, tld = language_info

        for index, row in dataframe.iterrows():
            text = row[option_column]

            cleaned_text = text.strip()
            if not cleaned_text:
                print(f"[SKIP] Skipping MP3 generation for empty text in row {index} of column '{option_column}'.")
                continue
            text = cleaned_text

            name_mp3 = f"{text}.mp3"
            temp_file_path = os.path.join('out_storage', name_mp3)
            lang_code = languages[option_lang][0]
            tld_code = languages[option_lang][1]

            if tld_code is None:
                tts = gTTS(text, lang=lang_code)
            else:
                tts = gTTS(text, lang=lang_code, tld=tld_code)

            tts.save(temp_file_path)
            print(f"[OK] MP3 file {temp_file_path} generated successfully.")

    except Exception as e:
        print(f"[ERROR] Not Generating MP3 file for '{text}': {e}")
