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


import argparse
from app.utils import files
from app.utils.files import LANGUAGES


def main(path_csv, option_column='front', default_language='spanish'):
    """
    Processes a CSV file and generates .mp3 files based on the specified options.

    Args:
        path_csv (str): Path to the CSV file to process.
        option_column (str, optional): Selects the column to generate .mp3 files from (default: "front"). Valid options are 'front' and 'back'.
        default_language (str, optional): Selects the language for generating .mp3 files (default: "spanish"). Valid options are 'spanish', 'chinese', 'italian', 'russian', 'english', 'deutsche', 'portuguese', 'french'.

    Returns:
        None
    """
    try:
        df = files.read_csv(path_csv)
        files.generate_files(df, option_column, default_language)
        print(f"[OK] Files generated successfully for '{option_column}' column in '{default_language}' language.")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")


if __name__ == "__main__":
    available_languages = list(LANGUAGES.keys())

    parser = argparse.ArgumentParser(description='Processes a CSV file and generates .csv and .mp3 files based on the specified options.')
    parser.add_argument('path_csv', type=str, help='Required file path for the CSV data. Columns must be separated using a pipe (|) delimiter.')
    parser.add_argument('-c', '--column', type=str, choices=['front', 'back'], default='front', help='Selects the column to generate .mp3 files from (default: "front").')
    parser.add_argument('-l', '--lang', type=str, choices=available_languages, default='spanish', help='Selects the language for generating .mp3 files (default: "spanish").')

    args = parser.parse_args()
    main(args.path_csv, args.column, args.lang)
