# CopyMate - Smarter, Faster, Better Copywriting

A Figma plugin that helps designers and writers create, translate, and enhance copy directly within Figma.

## Current Features
- 🌐 **Text Translation**: Convert text to multiple languages while preserving formatting
- ✨ **Text Enhancement**: Improve writing quality and clarity with AI suggestions
- 📝 **Text Shortening**: Create concise versions of your text while maintaining meaning
- 🎯 **Quality Check**: Analyze and score your copy across multiple criteria (Premium)
- 🎨 **Brand Guidelines**: Ensure text aligns with your brand voice (Premium)
- 🖼️ **Frame Support**: Select entire frames to process multiple text layers at once
- 🌙 **Dark Mode**: Full dark mode support with system preference detection
- 🎨 **Style Preservation**: Maintains all Figma text styling during updates

## Planned Enhancements
- 🔄 Batch processing for multiple frames
- 💾 Save and reuse common text transformations
- 📊 Quality check score history and trends
- ⭐ Copy effectiveness score with AI-powered readability and impact score

## Installation

1. Open Figma
2. Go to Menu > Plugins > Browse Plugins...
3. Search for "Copywriting Assistant"
4. Click "Install"

## Usage

1. Select text layer(s) in Figma
2. Run the plugin
3. Choose your desired action (Translate, Improve it, Shorten)
4. Review and apply changes

## Development

### Prerequisites

- Node.js
- npm/yarn
- Figma desktop app

1. Clone the repository
2. Install dependencies:    ```bash
   # Install Node dependencies
   npm install

   # Install Python dependencies
   pip install -r requirements.txt   ```

3. Create a `.env` file based on `.env.example`:   ```bash
   cp .env.example .env
   # Add your OpenAI API key to .env   ```

### Running Locally

1. Start the Flask server:   ```bash
   # In one terminal
   python server.py
   # Server will start at http://localhost:5000   ```

2. Start the Figma plugin:   ```bash
   # In another terminal
   npm run dev   ```

3. In Figma desktop app:
   - Go to Plugins > Development > Import plugin from manifest...
   - Select the `manifest.json` file from this repository
   - The plugin should now appear in your development plugins

## Contributing
Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Thanks to all contributors who have helped shape this plugin
* OpenAI for providing the API that powers our text enhancement features
* Figma for their excellent plugin platform 