# Async File Sorter

A Python script for asynchronously reading files from a source folder and sorting them into subfolders in the output directory based on file extensions.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt

## Usage
Run the script with the following command:

python async_file_sorting.py /path/to/source /path/to/output

* Replace /path/to/source with the path to the source folder containing the files you want to sort.
* Replace /path/to/output with the path to the output folder where the sorted files will be placed.

## Features

* Asynchronous file reading and copying.
* Automatic creation of subfolders based on file extensions.
* Efficient handling of large numbers of files.
