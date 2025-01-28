# CopyMate - Smarter, Faster, Better Copywriting Assistant

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Version](https://img.shields.io/badge/version-0.2.7-blue)

A Figma plugin that helps you enhance, translate, and optimize your UX copy directly within Figma.

## Current Features

- **Text Enhancement**: Improve your copy while maintaining brand voice and style
- **Translation**: Translate your text to multiple languages while preserving brand tone
- **Text Shortening**: Create more concise versions of your copy
- **Batch Processing**: Select and process multiple text layers simultaneously
- **Brand Guidelines**: Input your brand guidelines to maintain consistent voice and style
- **Settings Persistence**: Saves your language and brand guidelines preferences
- **Real-time Feedback**: Visual confirmation when settings are saved
- **Theme Support**: Choose between light, dark, or system theme
- **Modern UI**: Clean, intuitive interface with improved visual hierarchy

## Brand Voice Management

The plugin now includes robust brand voice management:
- Input detailed brand guidelines in the settings
- Guidelines are applied to all text operations
- Maintains consistent brand voice across translations
- Preserves tone and style in shortened text
- Enhances text while adhering to brand standards
- Real-time save confirmation for guidelines changes

## How It Works

1. Select one or more text layers in your Figma design
2. Choose your desired action (enhance, translate, or shorten)
3. Review the processed text
4. Apply changes to update your designs

## Future Features
- **Dark Mode Support**: Comfortable viewing in any lighting condition
- **Custom Presets**: Save frequently used text patterns and styles
- **Smart Suggestions**: AI-powered recommendations for better copy
- **Character Count Limits**: Set and enforce text length constraints
- **Accessibility Checker**: Verify text meets accessibility standards
- **Team Collaboration**: Share and review copy changes with team members
- **Context Awareness**: Adapt copy based on component type (button, header, etc.)
- **Bulk Operations**: Process entire pages or components at once
- **Voice Tone Slider**: Adjust copy formality/tone on a scale
- **Component-Specific Rules**: Different guidelines for different UI elements
- **Copy Validation**: Check for common UX writing issues


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