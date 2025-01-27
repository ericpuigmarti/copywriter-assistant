# Changelog

All notable changes to the Copywriting Assistant plugin will be documented in this file.
> Note: When updating this changelog, remember to update the version badge in README.md

## [0.1.5] - 2024-01-24

### Fixed
- Language settings not being properly loaded on plugin start
- Incorrect language being applied in translations
- Language persistence issues

### Changed
- Improved language settings initialization
- Added language loading confirmation
- Enhanced language state management

### Technical
- Added language state verification
- Improved settings synchronization
- Added debug logging for language settings

## [0.1.4] - 2024-01-24

### Fixed
- Translation language not being properly applied
- Language persistence in settings
- Language parameter handling in API requests

### Changed
- Improved language selection logging
- Enhanced translation prompts with explicit language requirements
- Better error handling for missing language parameters

### Technical
- Added debug logging for language selection
- Updated API endpoint to validate language parameters
- Strengthened translation prompt structure

## [0.1.3] - 2024-01-24

### Added
- Individual text processing for multiple selections
- Mapping system for text layer tracking
- Separate processing and updating of each text layer

### Changed
- Updated text processing to handle multiple layers independently
- Modified UI to display multiple text results
- Improved text application to maintain layer correspondence

### Fixed
- Issue with multiple text layers receiving same processed content
- Text layer mapping and updating mechanism
- Multiple selection handling in the UI

## [0.1.2] - 2024-01-24

### Added
- Brand guidelines input in settings modal
- Persistent storage for brand guidelines across sessions
- Integration of brand voice in all text processing operations
- Help text and examples for guidelines input
- System prompt enhancement with brand context

### Changed
- Enhanced OpenAI prompts to maintain brand consistency
- Updated settings modal layout with guidelines section
- Improved text processing to respect brand voice
- Modified all operations (translate/enhance/shorten) to consider brand guidelines

### Technical
- Added client storage for brand guidelines persistence
- Updated API endpoint to handle brand context
- Enhanced system prompts with dynamic brand guidelines
- Improved prompt engineering for brand voice consistency

## [0.1.1] - 2024-01-24

### Added
- Better error handling in server.py
- Detailed logging for debugging
- Test endpoint for server verification

### Changed
- Updated OpenAI client implementation to use latest API version (openai v1.0.0+)
- Improved CORS configuration for development
- Refactored UI code for better error handling
- Enhanced text processing feedback

### Fixed
- CORS issues with local development server
- OpenAI API authentication errors
- Text update issues with multiple fonts
- UI responsiveness during text processing

## [0.1.0] - 2024-01-24

### Added
- Initial plugin implementation
- Basic text processing features:
  - Translation
  - Text enhancement
  - Text shortening
- Settings modal for language selection
- Support for multiple text layers
- Font loading for text updates
- Client storage for language preferences

### Features
- Real-time text selection updates
- Preview before applying changes
- Support for multiple text formats
- Error handling and user feedback
- Loading states during processing

### Technical
- Flask backend server
- OpenAI GPT-3.5 Turbo integration
- CORS configuration for local development
- Environment variable management
- Proper gitignore setup 