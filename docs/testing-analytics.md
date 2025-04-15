# Analytics Testing Guide

## Prerequisites
1. Ensure Mixpanel project token is correctly set in ui.html
2. Have Mixpanel dashboard open in browser
3. Launch plugin in Figma development mode

## Step 1: Plugin Load Event
- [ ] Close and reopen plugin
- [ ] Verify "Plugin Loaded" event appears in Mixpanel
- [ ] Check timestamp property is present

## Step 2: Text Operations
### Translation Testing
1. [x] Select a text layer in Figma
2. [x] Click "Translate" button
   - ✓ "Translation Started" event verified
   - ✓ textLength and targetLanguage properties present
3. [x] Wait for translation to complete
   - ✓ "Translation Completed" event verified
   - ✓ duration property present
4. [ ] Test failure case:
   - Temporarily break API URL
   - Verify "Translation Failed" event
   - Check error message property

### Enhancement Testing
1. [ ] Select a text layer
2. [ ] Click "Improve it" button
   - Verify "Enhancement Started" event
   - Check textLength property
3. [ ] Wait for completion
   - Verify "Enhancement Completed" event
   - Check duration property

### Shorten Testing
1. [ ] Select a text layer
2. [ ] Click "Shorten" button
   - Verify "Shorten Started" event
   - Check textLength property
3. [ ] Wait for completion
   - Verify "Shorten Completed" event
   - Check duration property

## Step 3: Settings Interactions
1. [ ] Click Settings button
   - Verify "Settings Opened" event

2. [ ] Change language
   - Select different language
   - Verify "Language Changed" event
   - Check language property matches selection

3. [ ] Change theme
   - Switch between light/dark/system
   - Verify "Theme Changed" event
   - Check theme property matches selection

4. [ ] Update brand guidelines
   - Type in guidelines field
   - Wait for save timeout
   - Verify "Brand Guidelines Updated" event
   - Check hasGuidelines and guidelinesLength properties

## Step 4: Multi-layer Operations
1. [ ] Select multiple text layers
2. [ ] Perform operation (translate/enhance/shorten)
3. [ ] Click "Apply to Figma"
   - Verify "Apply to Figma" event
   - Check textCount and totalCharacters properties

## Step 5: Performance Verification
For each operation:
1. [ ] Check duration property is present
2. [ ] Verify duration is reasonable (typically < 5000ms)
3. [ ] Compare durations across operations

## Step 6: Error Cases
1. [ ] Test network error:
   - Disable internet connection
   - Attempt operation
   - Verify failure event with error property

2. [ ] Test empty selection:
   - Clear text selection
   - Verify buttons disabled
   - No events should fire

3. [ ] Test invalid input:
   - Select empty text layer
   - Verify appropriate error handling
   - Check error events

## Step 7: Data Verification
In Mixpanel dashboard:
1. [ ] Verify all events are named correctly
2. [ ] Check all properties are present and formatted correctly
3. [ ] Verify no PII or sensitive data is being sent
4. [ ] Check timestamp consistency
5. [ ] Verify event sequence makes logical sense

## Common Issues to Watch For
- Missing properties in events
- Incorrect property types
- Duplicate events
- Missing error tracking
- Inconsistent naming
- Performance timing issues

## Success Criteria
- All events appear in Mixpanel dashboard
- Properties contain expected values
- No errors in console
- Performance metrics are captured
- Error states properly tracked
- No PII or sensitive data transmitted

## Notes
- Keep Mixpanel dashboard open during testing
- Use browser console to monitor tracking calls
- Test each feature multiple times
- Verify both success and failure paths
- Check all property values are sanitized

## Verifying Mixpanel Integration

### Prerequisites
1. Open the Figma plugin in development mode
2. Open browser Developer Tools (F12)
3. Select the Network tab
4. Filter network requests for "api.mixpanel.com"

### Test Cases

1. **Plugin Load Event**
   - Action: Open the plugin
   - Expected: Should see a "Plugin Loaded" event in console
   - Verify: Check Mixpanel dashboard for the event

2. **Settings Event**
   - Action: Click the Settings button
   - Expected: Should see "Settings Opened" event in console
   - Verify: Check Mixpanel dashboard for the event

3. **Translation Events**
   - Action: Select text and click Translate
   - Expected: Should see "Translation Started" event with text length property
   - Verify: Check Mixpanel dashboard for the event

4. **Enhancement Events**
   - Action: Select text and click Enhance
   - Expected: Should see "Enhancement Started" event with text length property
   - Verify: Check Mixpanel dashboard for the event

### Verification Steps
1. Execute each test case
2. For each event, verify:
   - Console shows successful tracking message
   - Network tab shows request to api.mixpanel.com
   - Mixpanel dashboard shows the event (may have slight delay)

### Troubleshooting
- If no network requests visible:
  - Verify manifest.json has correct domain permissions
  - Check console for CORS errors
  - Ensure tracking code is executing (via console logs)
- If events not showing in Mixpanel:
  - Allow 5-10 minutes for events to appear in dashboard
  - Verify correct project token is being used
  - Check network response for any error messages

## Mixpanel Dashboard Verification ✓

### Event Tracking Verified
1. [x] Events appear in Mixpanel dashboard
2. [x] Correct event names displayed:
   - Translation Started
   - Translation Completed
3. [x] Events show correct timing and sequence
4. [x] User identification working (`plugin_user`)

### Next Steps for Testing
1. Test Settings button click event
2. Test Plugin Load event
3. Test Enhancement feature events
4. Add more user properties (optional):
   - Operating System
   - City/Country (if relevant)
   - Figma plugin version

## Future Enhancements

### User Identification
Currently using default `plugin_user` as distinct_id. When implementing user accounts:

1. **User Properties to Add**
   - User email/account ID
   - Subscription tier (free/premium)
   - Account creation date
   - Usage frequency

2. **Additional Events to Track**
   - Account creation
   - Subscription changes
   - User preferences
   - Usage limits/quotas

3. **Enhanced Analytics**
   - User retention metrics
   - Feature usage per user
   - Subscription conversion rates
   - User engagement patterns 