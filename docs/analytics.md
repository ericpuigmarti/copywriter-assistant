# Analytics Documentation

This document outlines the analytics implementation for the CopyMate Figma plugin using Mixpanel.

## Setup
The plugin uses Mixpanel's HTTP API via CDN implementation. Analytics are initialized in `ui.html` with the following configuration:

```javascript
mixpanel.init('PROJECT_TOKEN', {
    debug: true,
    track_pageview: true,
    persistence: 'localStorage'
});
```

## Events Tracked

### Core Events
| Event Name | Description | Properties |
|------------|-------------|------------|
| Plugin Loaded | Triggered when plugin is initialized | `timestamp` |

### Text Operations
| Event Name | Description | Properties |
|------------|-------------|------------|
| Translation Started | User initiates translation | `textLength`, `targetLanguage` |
| Translation Completed | Translation successfully completed | `textLength`, `targetLanguage`, `duration` |
| Translation Failed | Translation operation failed | `textLength`, `targetLanguage`, `duration`, `error` |
| Enhancement Started | User initiates text enhancement | `textLength` |
| Enhancement Completed | Enhancement successfully completed | `textLength`, `duration` |
| Enhancement Failed | Enhancement operation failed | `textLength`, `duration`, `error` |
| Shorten Started | User initiates text shortening | `textLength` |
| Shorten Completed | Shortening successfully completed | `textLength`, `duration` |
| Shorten Failed | Shortening operation failed | `textLength`, `duration`, `error` |

### UI Interactions
| Event Name | Description | Properties |
|------------|-------------|------------|
| Settings Opened | User opens settings modal | - |
| Language Changed | User changes target language | `language` |
| Theme Changed | User changes UI theme | `theme` |
| Brand Guidelines Updated | User modifies brand guidelines | `hasGuidelines`, `guidelinesLength` |
| Apply to Figma | User applies changes to Figma | `textCount`, `totalCharacters` |

## Property Definitions

### Common Properties
- `timestamp`: ISO string of when event occurred
- `textLength`: Number of characters in processed text
- `duration`: Time taken for operation in milliseconds
- `error`: Error message if operation failed

### Specific Properties
- `targetLanguage`: Selected language code (e.g., 'es', 'fr')
- `theme`: Selected theme ('light', 'dark', 'system')
- `hasGuidelines`: Boolean indicating if brand guidelines exist
- `guidelinesLength`: Character count of brand guidelines
- `textCount`: Number of text layers being processed
- `totalCharacters`: Total characters across all processed layers

## Implementation Details

Events are tracked using a helper function:
```javascript
function trackEvent(eventName, properties = {}) {
    try {
        mixpanel.track(eventName, {
            ...properties,
            timestamp: new Date().toISOString()
        });
    } catch (error) {
        console.error('Mixpanel tracking error:', error);
    }
}
```

## Performance Tracking
API operations (translate, enhance, shorten) include duration tracking:
- Start time captured before operation begins
- Duration calculated on completion/failure
- Included in completed/failed event properties

## Error Tracking
Failed operations track:
- Error message
- Operation duration
- Context (text length, language if applicable)
- Timestamp of failure

## Privacy Considerations
- No personally identifiable information (PII) is collected
- Text content is not tracked, only length metrics
- All tracking is anonymous
- No user identification or session tracking implemented

## Debugging
Analytics can be monitored in development:
1. Enable debug mode in Mixpanel initialization
2. Check browser console for tracking events
3. Verify events in Mixpanel dashboard

## Future Enhancements
Potential areas for expanded tracking:
- User session duration
- Feature usage patterns
- Error rate monitoring
- Performance metrics aggregation
- User preference trends

## Maintenance
When adding new features:
1. Add relevant tracking events
2. Include meaningful properties
3. Update this documentation
4. Test tracking in development
5. Verify events appear in Mixpanel dashboard 