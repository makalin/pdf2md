# PDF to Markdown Converter

A lightweight Python command-line tool that converts PDF documents to Markdown format while preserving basic document structure and formatting.

## Features

- 📄 Converts PDF files to clean, readable Markdown
- 🔍 Preserves basic document structure
- 🧹 Cleans up common PDF artifacts
- ⚙️ Supports both CLI and programmatic usage
- 📝 Detects and formats headers automatically
- 🎯 Simple and intuitive command-line interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pdf2md.git
cd pdf-to-markdown
```

2. Install dependencies:
```bash
pip install PyPDF2
```

3. Make the script executable:
```bash
chmod +x pdf2md.py
```

## Usage

### Command Line Interface

Basic usage:
```bash
./pdf2md.py input.pdf
```

Specify output file:
```bash
./pdf2md.py input.pdf -o output.md
```

Enable verbose output:
```bash
./pdf2md.py input.pdf -v
```

View help:
```bash
./pdf2md.py --help
```

### Programmatic Usage

You can also use the converter in your Python code:

```python
from pdf2md import PDFToMarkdownConverter

# Basic usage
converter = PDFToMarkdownConverter('input.pdf')
success = converter.convert()

# Specify output file
converter = PDFToMarkdownConverter('input.pdf', 'output.md')
success = converter.convert()
```

## Options

| Option | Short | Description |
|--------|--------|------------|
| `--output` | `-o` | Specify output file path |
| `--verbose` | `-v` | Enable verbose output |
| `--help` | `-h` | Show help message |

## Current Limitations

- Images in PDFs are not converted
- Complex layouts (multiple columns, tables) may not convert perfectly
- Font styles and sizes are not preserved
- Some special characters might not be properly converted

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Improvements

- [ ] Add support for image extraction
- [ ] Improve table detection and conversion
- [ ] Add support for font styles and sizes
- [ ] Implement better header detection
- [ ] Add batch processing for multiple files
- [ ] Support for custom conversion rules
- [ ] Add configuration file support

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [PyPDF2](https://github.com/mstamy2/PyPDF2) for PDF processing capabilities

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.