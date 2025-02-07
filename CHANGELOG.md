# Changelog

All notable changes to the Copywriting Assistant plugin will be documented in this file.
> Note: When updating this changelog, remember to update the version badge and details in README.md

## [0.3.0] - 2024-01-25

### Added
- Custom styled dropdown menus for language and theme selectors
- Feedback link for users to report issues or provide feedback

### Changed
- Updated Quality Check feature to show "Coming Soon" instead of "Premium" tag
- Disabled Quality Check button until feature is ready
- Improved dropdown menu styling and interaction

### Fixed
- Dropdown menus now match the app's design system
- Better visual consistency across UI elements

## [0.2.9] - 2024-01-25
### Fixed
- Language preference persistence between plugin sessions
- Language selection change handler in UI
- Network access warnings by adding Figma API domain

### Changed
- Updated manifest.json network access configuration
- Improved language selection event handling
- Enhanced language state management and logging

### Technical
- Added event listener for language selection changes
- Updated manifest.json allowedDomains to include Figma API
- Enhanced console logging for language-related operations
- Improved language preference synchronization between UI and plugin

## [0.2.8] - 2024-01-25
### Changed
- Removed background from language and appearance dropdowns
- Removed background from brand guidelines textarea
- Updated settings button visibility to only show in text editor view
- Improved apply-to-figma functionality with better error handling

### Fixed
- Fixed text application to Figma layers using getNodeByIdAsync
- Fixed memory access issues with node handling
- Fixed settings button blocking content in other views
- Fixed background styling consistency in dark mode

### Technical
- Updated node retrieval to use figma.getNodeByIdAsync for dynamic-page access
- Improved async operations handling in text application
- Enhanced error boundaries in text processing
- Optimized settings button visibility management

### Added
- Premium tag indicator for Quality Check and Brand Guidelines features
- Support for selecting frames/groups to find nested text layers
- Inter font family for improved typography
- Consistent back button styling across all views
- Better before/after text comparison layout in results view

### Changed
- Improved button styling with subtle backgrounds
- Updated primary button design with rounded corners
- Enhanced text descriptions and captions
- Refined spacing and padding throughout the interface
- Better handling of multiple text layer selections
- Increased plugin height to 640px for better content display

## [0.2.7] - 2024-01-24
### Fixed
- UI view toggling between edit and results
- Button state management based on text content
- Text selection handling from Figma
- Loading state visibility

### Changed
- Improved view state management
- Enhanced error handling in API calls
- Better user feedback during operations

### Technical
- Refactored API call handling
- Improved view state transitions
- Enhanced error recovery

## [0.2.6] - 2024-01-24
### Fixed
- SVG icon display issues in action buttons
- Icon color inheritance
- Icon sizing and alignment

### Technical
- Updated SVG styling structure
- Enhanced icon containers
- Improved color inheritance for icons

## [0.2.5] - 2024-01-24
### Changed
- Redesigned action buttons to match Figma's native style
- Added "Writing tools" section label
- Enhanced button layout and iconography
- Improved visual hierarchy of actions

### Technical
- Updated button component structure
- Added section title styling
- Enhanced button states and interactions
- Improved accessibility with better button structure

## [0.2.4] - 2024-01-24
### Changed
- Updated dark theme with deeper, more contrasting colors
- Enhanced dark mode visual hierarchy
- Improved dark mode readability

### Technical
- Refined dark theme color palette
- Updated system preference dark theme
- Enhanced color contrast ratios

## [0.2.3] - 2024-01-24
### Changed
- Enhanced "Apply to Figma" button visibility
- Added primary button styling
- Improved action hierarchy

### Technical
- Added primary button color variables
- Enhanced button state management
- Updated button contrast for better accessibility

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