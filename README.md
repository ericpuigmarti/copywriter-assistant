# Copywriting Assistant

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

A Figma plugin that helps you enhance, translate, and optimize your copy directly within Figma.

## Current Features

- **Text Enhancement**: Improve your copy while maintaining brand voice and style
- **Translation**: Translate your text to multiple languages
- **Text Shortening**: Create more concise versions of your copy
- **Brand Guidelines**: Input your brand guidelines to maintain consistent voice and style
- **Dark Mode Support**: Comfortable viewing in any lighting condition
- **Local Backend**: Flask server for secure API handling

## Setup Instructions

### Backend Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Create a requirements.txt file with the following dependencies:
   ```
   flask
   flask-cors
   openai
   python-dotenv
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. Start the Flask server:
   ```bash
   python server.py
   ```
   The server will run on http://localhost:5000

### Plugin Setup
1. Clone this repository
2. Open Figma Desktop app
3. Go to Plugins > Development > Import plugin from manifest
4. Select the manifest.json file from the cloned repository
5. Ensure the Flask backend is running
6. Select text in your Figma design
7. Open the plugin and choose your desired action


## Planned Features

### PDF Brand Guidelines Upload 📄
- Upload brand guidelines directly from PDF documents
- Automatic extraction and processing of guidelines
- Smart parsing of key brand voice and style elements
- Version control for different guideline documents

### Enhanced Multi-Language Support 🌐
- Support for additional languages
- Regional language variants
- Preservation of text formatting during translation
- Contextual translation based on design context
- Batch translation of multiple text layers

### Automated Layer Updates ⚡
- Direct updating of original Figma layers with processed text
- Maintain layer properties and styles
- Smart text fitting for translated content
- Batch processing of multiple layers
- History of changes with undo capability

## Getting Started with Development

To start developing the plugin:

1. Follow the Backend Setup instructions above
2. Follow the Plugin Setup instructions above
3. Make your changes
4. Test thoroughly
5. Submit a pull request following the Contributing guidelines

## Contributing

We welcome contributions! If you have suggestions or want to contribute to the development, please:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Thanks to all contributors who have helped shape this plugin
* OpenAI for providing the API that powers our text enhancement features
* Figma for their excellent plugin platform 