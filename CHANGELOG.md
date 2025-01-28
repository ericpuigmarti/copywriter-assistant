# Changelog

All notable changes to the Copywriting Assistant plugin will be documented in this file.
> Note: When updating this changelog, remember to update the version badge and details in README.md

## [0.1.7] - 2024-01-24

### Changed
- Improved results view layout with vertical stacking
- Enhanced readability of original vs processed text
- Updated results divider for vertical orientation
- Optimized spacing in results view

### Technical
- Refactored results container CSS for vertical layout
- Simplified results view structure
- Improved responsive behavior

## [0.1.6] - 2024-01-24

### Added
- Configuration management system
- Environment-specific settings
- Server status endpoint with environment info
- Static assets organization

### Changed
- Improved server configuration structure
- Enhanced error handling and logging
- Updated README with clearer feature descriptions
- Reorganized future features list

### Technical
- Added config.py for configuration management
- Structured static assets directory
- Updated server initialization process
- Enhanced environment handling

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

## [0.1.8] - 2024-01-24

### Changed
- Complete UI redesign to match Figma's dark theme
- Improved button layout and styling
- Moved settings to footer navigation
- Enhanced overall visual hierarchy

### Added
- Dark mode as default theme
- Full-width action buttons
- Footer navigation bar
- Help button in footer

### Technical
- Refactored CSS variables for dark theme
- Updated component structure
- Improved responsive layout
- Enhanced button states and transitions

## [0.1.9] - 2024-01-24

### Fixed
- Brand guidelines persistence across plugin sessions
- Settings synchronization for brand guidelines
- Guidelines loading on plugin startup

### Changed
- Improved brand guidelines save behavior
- Enhanced settings persistence logic

### Technical
- Updated client storage handling for guidelines
- Added debug logging for settings persistence
- Improved settings synchronization

## [0.2.0] - 2024-01-24

### Added
- Save confirmation indicator for brand guidelines
- Visual feedback for settings changes
- Auto-hiding save confirmation

### Changed
- Improved user feedback for settings persistence
- Enhanced visual feedback for user actions

### Technical
- Added save confirmation component
- Implemented auto-hiding confirmation message
- Enhanced UI feedback system

## [0.2.1] - 2024-01-24

### Added
- Dark mode support with system preference detection
- Modern, cleaner UI styling
- Enhanced visual hierarchy

### Changed
- Updated button and input styles
- Improved settings modal layout
- Enhanced color system with new variables
- Refined spacing and typography

### Technical
- Added CSS variables for theme support
- Implemented prefers-color-scheme media query
- Enhanced component styling structure

## [0.2.2] - 2024-01-24

### Added
- Theme toggle in settings (Light/Dark/System)
- Theme persistence across sessions
- System theme detection

### Changed
- Updated theme implementation to support manual selection
- Improved theme switching UX
- Enhanced theme persistence logic

### Technical
- Added theme selection UI
- Implemented theme storage in client preferences
- Enhanced theme switching mechanism

## [0.2.3] - 2024-01-24

### Changed
- Enhanced "Apply to Figma" button visibility
- Added primary button styling
- Improved action hierarchy

### Technical
- Added primary button color variables
- Enhanced button state management
- Updated button contrast for better accessibility