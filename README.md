# Image and PDF Combiner

This Python script combines multiple images and PDFs from an input directory into a single PDF file.

## Features

- Combines images (PNG, JPEG, JPG) and PDFs into a single PDF
- Maintains original PDF quality
- Allows customization of image DPI for better quality
- Handles both file paths and directory paths as input
- Automatically generates output filename if a directory is provided
- The order of the files in the output PDF is based on the file names
  
## Requirements

- Python 3.8 or higher
- Pillow
- pypdf

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MoAlkhateeb/image-pdf-combiner.git
cd image-pdf-combiner
```

2. Install the required packages: 
   
```bash
pip install pillow pypdf
```

Or if you're using pipenv:
```bash
pipenv install
```

## Usage

You can use this script in two ways:

1. *Interactive Mode*: Run the script without any arguments and follow the prompts.

```bash
python combine_files.py
```

You will be prompted to enter:
1. The input directory path containing your images and PDFs
2. The output PDF path (can be a file path or a directory)

Example:
```
Input directory Path: /path/to/your/files
Output PDF Path: /path/to/output/combined.pdf
```

2. *Command Line Mode*: Pass in the input and output paths as arguments.

```bash
python combine_files.py -i /path/to/input/directory -o /path/to/output.pdf --dpi 600
```

Arguments:
`-i` or `--input`: Input directory path (required)
`-o` or `--output`: Output PDF path (required)
`--dpi`: DPI for image conversion (optional, default is 300)

If you provide a directory as the output path, the script will automatically generate a filename based on the input directory name.

## Customization

You can change the DPI of images by using the `--dpi` argument when running the script with command-line arguments. Higher values will result in better quality but larger file sizes. or you can run the function with a different `image_dpi` value.

```python
combine_files(input_dir, output_path, image_dpi=300)
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/MoAlkhateeb/image-pdf-combiner/issues).

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

**Mohammed Alkhateeb**

- Github: [@MoAlkhateeb](https://github.com/MoAlkhateeb)