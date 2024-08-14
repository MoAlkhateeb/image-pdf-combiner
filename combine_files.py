#!/usr/bin/env python3
"""
Convert multiple images and PDFs from an input directory to a single PDF file.
Author: Mohammed Alkhateeb (@MoAlkhateeb)
"""

import io
import argparse
from pathlib import Path
from typing import Union
from PIL import Image
import pypdf

PathLike = Union[str, Path]
DEFAULT_OUTPUT_FILENAME = "{}_combined_output.pdf"


def ensure_path(path: PathLike) -> Path:
    """
    Ensure the input is a Path object.
    Args:
        path (PathLike): The input path as either a string or Path object.
    Returns:
        Path: The input converted to a Path object.
    """
    return Path(path) if isinstance(path, str) else path


def get_input_files(directory: PathLike) -> list[Path]:
    """
    Get a sorted list of image and PDF files from the given directory.
    Args:
        directory (PathLike): Path to the directory containing image and PDF files.
    Returns:
        list[Path]: Sorted list of image and PDF file paths.
    """
    directory = ensure_path(directory)
    valid_extensions = (".png", ".jpeg", ".jpg", ".pdf")
    return sorted(
        file for file in directory.iterdir() if file.suffix.lower() in valid_extensions
    )


def convert_image_to_pdf(image_path: PathLike, image_dpi: int = 300) -> io.BytesIO:
    """
    Convert a single image to a PDF with increased resolution.
    Args:
        image_path (PathLike): Path to the image file.
        image_dpi (int): DPI for the image conversion.
    Returns:
        io.BytesIO: BytesIO object containing the PDF data.
    """
    image_path = ensure_path(image_path)
    image = Image.open(image_path)
    pdf_bytes = io.BytesIO()
    image.convert("RGB").save(pdf_bytes, "PDF", resolution=image_dpi)
    pdf_bytes.seek(0)
    return pdf_bytes


def convert_files_to_pdf(
    directory: PathLike, save_path: PathLike, image_dpi: int = 300
) -> Path:
    """
    Convert all images and PDFs in a directory to a single PDF file.
    Args:
        directory (PathLike): Path to the directory containing image and PDF files.
        save_path (PathLike): Path where the resulting PDF will be saved.
        image_dpi (int): DPI for the image conversion.
    Returns:
        Path: Path to the saved PDF file.
    """
    directory = ensure_path(directory)
    save_path = ensure_path(save_path)
    if save_path.is_dir():
        save_path = save_path / DEFAULT_OUTPUT_FILENAME.format(directory.name)

    pdf_writer = pypdf.PdfWriter()
    input_files = get_input_files(directory)
    for file in input_files:
        if file.suffix.lower() == ".pdf":
            pdf_reader = pypdf.PdfReader(str(file))
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
        else:
            pdf_bytes = convert_image_to_pdf(file, image_dpi)
            pdf_reader = pypdf.PdfReader(pdf_bytes)
            pdf_writer.add_page(pdf_reader.pages[0])

    with save_path.open("wb") as output:
        pdf_writer.write(output)
    return save_path


def main() -> None:
    """Main function to handle both command-line arguments and interactive input."""
    parser = argparse.ArgumentParser(
        description="Combine images and PDFs into a single PDF file."
    )
    parser.add_argument("-i", "--input", help="Input directory path")
    parser.add_argument("-o", "--output", help="Output PDF path")
    parser.add_argument(
        "--dpi", type=int, default=300, help="DPI for image conversion (default: 300)"
    )
    args = parser.parse_args()

    try:
        if args.input and args.output:
            input_directory = args.input
            output_pdf = args.output
        else:
            input_directory = input("Input directory Path: ")
            output_pdf = input("Output PDF Path: ")

        save_path = convert_files_to_pdf(input_directory, output_pdf, args.dpi)
        print(f"PDF created successfully: {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
