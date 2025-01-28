// Show the UI
figma.showUI(__html__, { width: 400, height: 600 });

// Add a global variable to store text mappings
let selectedTextLayers = new Map();

// Function to handle text extraction
function handleSelection() {
    console.log('handleSelection called');
    const selection = figma.currentPage.selection;
    console.log('Current selection:', selection);
    
    if (selection.length > 0) {
        let allTextNodes = [];
        selectedTextLayers.clear();
        
        // Process each selected node
        for (const node of selection) {
            if (node.type === 'TEXT') {
                allTextNodes.push({
                    id: node.id,
                    text: node.characters,
                    node: node
                });
            }
        }
        
        // Send extracted text to UI
        const textsForUI = allTextNodes.map(item => {
            if (item.text.trim().length > 0) {
                selectedTextLayers.set(item.id, {
                    text: item.text,
                    node: item.node
                });
                return {
                    id: item.id,
                    text: item.text
                };
            }
        }).filter(Boolean);

        if (textsForUI.length > 0) {
            console.log('Texts extracted:', textsForUI);
            figma.ui.postMessage({
                type: 'selected-text',
                texts: textsForUI
            });
        }
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
    console.log('Message received from UI:', msg);

    switch (msg.type) {
        case 'get-selected-text':
            console.log('Received get-selected-text request');
            handleSelection();
            break;

        case 'update-text':
            console.log('Received update-text request:', msg.processedTexts);
            try {
                let updatedCount = 0;

                // Process each text update
                for (const { id, text } of msg.processedTexts) {
                    const layerInfo = selectedTextLayers.get(id);
                    if (layerInfo && layerInfo.node) {
                        try {
                            const node = layerInfo.node;
                            // Load fonts
                            const fonts = node.getRangeAllFontNames(0, node.characters.length);
                            for (const font of fonts) {
                                await figma.loadFontAsync(font);
                            }
                            // Update text
                            node.characters = text;
                            updatedCount++;
                        } catch (error) {
                            console.error(`Error updating layer ${id}:`, error);
                        }
                    }
                }

                figma.notify(`Updated ${updatedCount} text layer${updatedCount > 1 ? 's' : ''}`);
            } catch (error) {
                console.error('Error in update-text handler:', error);
                figma.notify('Error: ' + error.message);
            }
            break;

        case 'get-language':
            console.log('Getting saved language');
            const savedLanguage = await figma.clientStorage.getAsync('targetLanguage');
            console.log('Saved language:', savedLanguage);
            figma.ui.postMessage({
                type: 'set-language',
                language: savedLanguage || 'es' // Default to Spanish if no language is set
            });
            break;

        case 'save-language':
            console.log('Saving language:', msg.language);
            await figma.clientStorage.setAsync('targetLanguage', msg.language);
            // Send confirmation back to UI
            figma.ui.postMessage({
                type: 'set-language',
                language: msg.language
            });
            break;

        case 'save-brand-guidelines':
            console.log('Saving brand guidelines:', msg.guidelines);
            await figma.clientStorage.setAsync('brandGuidelines', msg.guidelines);
            break;

        case 'get-brand-guidelines':
            console.log('Getting saved brand guidelines');
            const savedGuidelines = await figma.clientStorage.getAsync('brandGuidelines');
            console.log('Saved guidelines:', savedGuidelines);
            figma.ui.postMessage({
                type: 'set-brand-guidelines',
                guidelines: savedGuidelines || ''
            });
            break;

        case 'save-theme':
            console.log('Saving theme preference:', msg.theme);
            await figma.clientStorage.setAsync('theme', msg.theme);
            break;

        case 'get-theme':
            console.log('Getting saved theme');
            const savedTheme = await figma.clientStorage.getAsync('theme');
            figma.ui.postMessage({
                type: 'set-theme',
                theme: savedTheme || 'system'
            });
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