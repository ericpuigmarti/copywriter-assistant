// Show the UI
figma.showUI(__html__, { width: 400, height: 640 });

// Add these font loading functions at the top of the file
async function loadInterFontStyles() {
    try {
        await Promise.all([
            figma.loadFontAsync({ family: "Inter", style: "Regular" }),
            figma.loadFontAsync({ family: "Inter", style: "Medium" }),
            figma.loadFontAsync({ family: "Inter", style: "Semi Bold" }),
            figma.loadFontAsync({ family: "Inter", style: "Bold" })
        ]);
        return true;
    } catch (error) {
        console.error("Error loading Inter font:", error);
        return false;
    }
}

// Initialize plugin settings
async function initializeSettings() {
    try {
        // Load Inter font first
        const fontsLoaded = await loadInterFontStyles();
        if (!fontsLoaded) {
            figma.notify("Failed to load Inter font. Using system font as fallback.");
        }

        // Get saved language - add more logging
        const savedLanguage = await figma.clientStorage.getAsync('targetLanguage');
        console.log('[initializeSettings] Loaded saved language:', savedLanguage);
        
        // Send language to UI with explicit default
        const languageToUse = savedLanguage || 'es';
        console.log('[initializeSettings] Setting language to:', languageToUse);
        figma.ui.postMessage({
            type: 'set-language',
            language: languageToUse
        });

        // Get saved theme
        const savedTheme = await figma.clientStorage.getAsync('theme');
        figma.ui.postMessage({
            type: 'set-theme',
            theme: savedTheme || 'system'
        });

        // Get saved brand guidelines
        const savedGuidelines = await figma.clientStorage.getAsync('brandGuidelines');
        figma.ui.postMessage({
            type: 'set-brand-guidelines',
            guidelines: savedGuidelines || ''
        });

    } catch (error) {
        console.error('[initializeSettings] Error:', error);
        figma.notify('Error loading settings');
    }
}

// Call initialize function right after showing UI
initializeSettings();

// Add a global variable to store text mappings
let selectedTextLayers = new Map();

// Add a variable to store the last used operation and its parameters
let lastOperation = {
    type: null,  // 'translate', 'enhance', or 'shorten'
    params: {}   // Store all parameters used
};

// Add this helper function to recursively find text layers
function findTextLayers(node, textLayers = []) {
    // Check if node is a text layer
    if (node.type === "TEXT") {
        textLayers.push({
            id: node.id,
            text: node.characters,
            node: node  // Store reference to the node for later use
        });
    }
    // If node has children (like a frame or group), traverse them
    else if ("children" in node) {
        for (const child of node.children) {
            findTextLayers(child, textLayers);
        }
    }
    return textLayers;
}

// Function to handle text extraction
function handleSelection() {
    console.log('handleSelection called');
    const selection = figma.currentPage.selection;
    console.log('Current selection:', selection);
    
    if (selection.length > 0) {
        let allTextLayers = [];
        selectedTextLayers.clear();
        
        // Process each selected node
        for (const node of selection) {
            // Find all text layers in this node (or its children)
            const textLayers = findTextLayers(node);
            allTextLayers = allTextLayers.concat(textLayers);
        }
        
        // Send extracted text to UI
        if (allTextLayers.length > 0) {
            console.log('Text layers found:', allTextLayers);
            allTextLayers.forEach(item => {
                selectedTextLayers.set(item.id, {
                    text: item.text,
                    node: item.node
                });
            });
            
            // Send only necessary data to UI
            const textsForUI = allTextLayers.map(({ id, text }) => ({ id, text }));
            figma.ui.postMessage({
                type: 'selected-text',
                texts: textsForUI,
                hasContent: true
            });
        } else {
            console.log('No text layers found in selection');
            figma.ui.postMessage({
                type: 'selected-text',
                texts: [],
                hasContent: false,
                error: 'No text layers in selection'
            });
            figma.notify('⚠️ Please select text layer(s) to work with');
        }
    } else {
        console.log('No selection');
        figma.ui.postMessage({
            type: 'selected-text',
            texts: [],
            hasContent: false,
            error: 'Nothing selected'
        });
        figma.notify('⚠️ Please select text layer(s) to work with');
    }
}

// Run initial selection check
console.log('Running initial selection check');
handleSelection();

// Listen for selection changes
figma.on('selectionchange', () => {
    console.log('Selection changed');
    handleSelection();
});

// Handle messages from UI
figma.ui.onmessage = async (msg) => {
    console.log('[Message] Type:', msg.type);
    console.log('[Message] Full data:', msg);

    switch (msg.type) {
        case 'get-selected-text':
            console.log('Received get-selected-text request');
            handleSelection();
            break;

        case 'update-text':
            console.log('[Process] Starting text update with operation:', msg.operation);
            try {
                // Store the operation details for retry
                lastOperation = {
                    type: msg.operation,
                    params: {
                        targetLanguage: msg.targetLanguage,
                        brandGuidelines: msg.brandGuidelines
                    }
                };
                console.log('[Process] Stored operation:', lastOperation);
                if (!selectedTextLayers.size) {
                    const action = msg.action || 'modify'; // Default fallback
                    const errorMsg = `⚠️ No text selected. Please select text layer(s) to ${action}`;
                    console.error(errorMsg);
                    figma.ui.postMessage({
                        type: 'error',
                        message: errorMsg
                    });
                    figma.notify(errorMsg);
                    return;
                }

                let updatedCount = 0;

                // Process each text update
                for (const { id, text } of msg.processedTexts) {
                    const layerInfo = selectedTextLayers.get(id);
                    if (layerInfo && layerInfo.node) {
                        try {
                            const node = layerInfo.node;
                            // Load Inter font first
                            await loadInterFontStyles();
                            // Then load any other fonts used in the text
                            const fonts = node.getRangeAllFontNames(0, node.characters.length);
                            for (const font of fonts) {
                                await figma.loadFontAsync(font);
                            }
                            // Update text
                            node.characters = text;
                            // Set font to Inter if possible
                            try {
                                node.fontName = { family: "Inter", style: "Regular" };
                            } catch (fontError) {
                                console.warn('Could not apply Inter font:', fontError);
                            }
                            updatedCount++;
                        } catch (error) {
                            console.error(`Error updating layer ${id}:`, error);
                        }
                    }
                }

                figma.notify(`Updated ${updatedCount} text layer${updatedCount > 1 ? 's' : ''}`);
            } catch (error) {
                console.error('[Error] Update text:', error);
                figma.notify('Error: ' + error.message);
            }
            break;

        case 'get-language':
            console.log('[get-language] Getting saved language');
            try {
                const savedLanguage = await figma.clientStorage.getAsync('targetLanguage');
                console.log('[get-language] Retrieved language:', savedLanguage);
                
                // Always send a value, default to 'es' if none saved
                const languageToUse = savedLanguage || 'es';
                console.log('[get-language] Sending language to UI:', languageToUse);
                
                figma.ui.postMessage({
                    type: 'set-language',
                    language: languageToUse
                });
            } catch (error) {
                console.error('[get-language] Error:', error);
                figma.notify('Error loading language setting');
            }
            break;

        case 'save-language':
            console.log('[save-language] Saving language:', msg.language);
            try {
                if (!msg.language) {
                    console.error('[save-language] No language provided');
                    return;
                }
                await figma.clientStorage.setAsync('targetLanguage', msg.language);
                console.log('[save-language] Language saved successfully');
                
                // Confirm back to UI
                figma.ui.postMessage({
                    type: 'set-language',
                    language: msg.language
                });
                figma.notify('Language preference saved');
            } catch (error) {
                console.error('[save-language] Error:', error);
                figma.notify('Error saving language setting');
            }
            break;

        case 'save-brand-guidelines':
            console.log('Saving brand guidelines:', msg.guidelines);
            try {
                await figma.clientStorage.setAsync('brandGuidelines', msg.guidelines);
                figma.notify('Brand guidelines saved');
            } catch (error) {
                console.error('Error saving brand guidelines:', error);
                figma.notify('Error saving brand guidelines');
            }
            break;

        case 'get-brand-guidelines':
            console.log('Getting saved brand guidelines');
            try {
                const savedGuidelines = await figma.clientStorage.getAsync('brandGuidelines');
                console.log('Saved guidelines:', savedGuidelines);
                figma.ui.postMessage({
                    type: 'set-brand-guidelines',
                    guidelines: savedGuidelines || ''
                });
            } catch (error) {
                console.error('Error loading brand guidelines:', error);
                figma.notify('Error loading brand guidelines');
            }
            break;

        case 'save-theme':
            console.log('Saving theme preference:', msg.theme);
            try {
                await figma.clientStorage.setAsync('theme', msg.theme);
                figma.notify('Theme preference saved');
            } catch (error) {
                console.error('Error saving theme:', error);
                figma.notify('Error saving theme preference');
            }
            break;

        case 'get-theme':
            console.log('Getting saved theme');
            // Try to get saved theme
            figma.clientStorage.getAsync('theme').then(savedTheme => {
                // If no theme is saved, use the default theme from the message
                const theme = savedTheme || msg.defaultTheme;
                // Send theme back to UI
                figma.ui.postMessage({
                    type: 'set-theme',
                    theme: theme
                });
            });
            break;

        case 'apply-text':
            console.log('Applying text changes:', msg.texts);
            if (!selectedTextLayers.size) {
                const action = msg.action || 'modify'; // Default fallback
                const errorMsg = `⚠️ No text selected. Please select text layer(s) to ${action}`;
                console.error(errorMsg);
                figma.ui.postMessage({
                    type: 'error',
                    message: errorMsg
                });
                figma.notify(errorMsg);
                return;
            }

            (async () => {
                try {
                    // Process text changes sequentially
                    for (const item of msg.texts) {
                        try {
                            // Get the stored node reference
                            const layerInfo = selectedTextLayers.get(item.id);
                            if (!layerInfo || !layerInfo.node) {
                                console.warn(`Node ${item.id} not found in stored layers`);
                                continue;
                            }
                            
                            const node = layerInfo.node;
                            
                            // Load fonts
                            await Promise.all(
                                node.getRangeAllFontNames(0, node.characters.length)
                                    .map(font => figma.loadFontAsync(font))
                            );
                            
                            // Update text
                            node.characters = item.text;
                            console.log(`Successfully updated node ${item.id}`);
                            
                        } catch (err) {
                            console.error(`Failed to update node ${item.id}:`, err);
                            continue;
                        }
                    }
                    
                    figma.notify('Text updates complete');
                    
                } catch (error) {
                    console.error('Error in apply-text:', error);
                    figma.notify('Failed to update some text layers');
                }
            })();
            break;

        case 'retry-text':
            console.log('[Retry] Starting retry with operation:', msg.operation);
            try {
                if (!selectedTextLayers.size) {
                    const errorMsg = "⚠️ No text selected. Please select text layer(s) to retry";
                    console.error(errorMsg);
                    figma.notify(errorMsg);
                    return;
                }

                console.log('[Retry] Previous operation was:', lastOperation.type);
                console.log('[Retry] Requested operation is:', msg.operation);
                console.log('[Retry] Using parameters:', lastOperation.params);

                // Send back to UI for processing
                figma.ui.postMessage({
                    type: 'process-retry',
                    operation: msg.operation,  // Use the operation from the retry request
                    params: lastOperation.params,
                    texts: Array.from(selectedTextLayers.entries()).map(([id, info]) => ({
                        id,
                        text: info.text
                    }))
                });

            } catch (error) {
                console.error('Error in retry-text handler:', error);
                figma.notify('Error: ' + error.message);
            }
            break;

        case 'process-retry':
            console.log('[Process Retry] Starting:', msg);
            try {
                // Call API with correct operation
                const response = await callAPI(msg.operation, {
                    text: msg.texts[0].text,
                    targetLanguage: msg.params.targetLanguage
                });
                
                // Get the correct response property based on operation
                const processedText = msg.operation === 'translate' ? response.translatedText :
                                    msg.operation === 'shorten' ? response.shortenedText :
                                    response.enhancedText;
                
                // Maintain the original ID from the Figma layer
                const processedTexts = [{
                    id: msg.texts[0].id,  // Keep the original Figma layer ID
                    text: processedText
                }];

                // Show results with correct operation type
                showResults(
                    [msg.texts[0].text], 
                    processedTexts,
                    msg.operation
                );
                
                // Store for apply to Figma - use the same ID structure
                currentProcessedTexts = processedTexts;
                
                // Hide loading, show results
                loadingIndicator.style.display = 'none';
                resultsView.style.display = 'block';
                
            } catch (error) {
                console.error('[Process Retry] Error:', error);
                loadingIndicator.style.display = 'none';
                alert('Failed to process text. Please try again.');
            }
            break;
    }
};

// Handle initial selection
figma.ui.postMessage({
    type: 'selected-text',
    texts: figma.currentPage.selection
        .filter(node => node.type === "TEXT")
        .map(node => ({
            id: node.id,
            text: node.characters
        }))
});