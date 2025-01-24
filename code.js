// Show the UI
figma.showUI(__html__, { width: 400, height: 600 });

// Function to extract text from a node and its children
function extractTextFromNode(node) {
    let texts = [];
    
    if (node.type === 'TEXT') {
        texts.push(node.characters);
    } else if ('children' in node) {
        // Recursively get text from child nodes
        for (const child of node.children) {
            texts = texts.concat(extractTextFromNode(child));
        }
    }
    
    return texts;
}

// Function to handle text extraction
function handleSelection() {
    console.log('handleSelection called');
    const selection = figma.currentPage.selection;
    console.log('Current selection:', selection);
    
    if (selection.length > 0) {
        let allTexts = [];
        
        // Process each selected node
        for (const node of selection) {
            allTexts = allTexts.concat(extractTextFromNode(node));
        }
        
        // Filter out empty strings and join with newlines
        const combinedText = allTexts.filter(text => text.trim().length > 0).join('\n\n');
        
        if (combinedText) {
            console.log('Text extracted:', combinedText);
            figma.ui.postMessage({
                type: 'selected-text',
                text: combinedText
            });
            console.log('Sent selected-text message to UI');
        } else {
            console.log('No text found in selection');
            figma.ui.postMessage({
                type: 'selected-text',
                text: ''
            });
        }
    } else {
        console.log('No valid selection found');
        figma.ui.postMessage({
            type: 'selected-text',
            text: ''
        });
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

// Handle messages received from the UI
figma.ui.onmessage = async (msg) => {
    console.log('Message received from UI:', msg);

    switch (msg.type) {
        case 'get-selected-text':
            console.log('Received get-selected-text request');
            handleSelection();
            break;

        case 'update-text':
            console.log('Received update-text request:', msg.text);
            try {
                const selection = figma.currentPage.selection;
                
                // Check if we have a valid selection
                if (selection.length === 0) {
                    figma.notify('Please select a text layer to update');
                    return;
                }

                // Update each selected text layer
                let updatedCount = 0;
                for (const node of selection) {
                    // If node is a frame or group, update all text layers within it
                    if ('children' in node) {
                        const textNodes = node.findAll(n => n.type === 'TEXT');
                        for (const textNode of textNodes) {
                            try {
                                // Get all fonts used in the text node
                                const fonts = textNode.getRangeAllFontNames(0, textNode.characters.length);
                                console.log('Loading fonts:', fonts);
                                
                                // Load each font
                                for (const font of fonts) {
                                    await figma.loadFontAsync(font);
                                }
                                
                                // Update the text
                                textNode.characters = msg.text;
                                updatedCount++;
                                console.log('Successfully updated text layer');
                            } catch (error) {
                                console.error('Error updating text layer:', error);
                                figma.notify('Error updating text layer: ' + error.message);
                            }
                        }
                    } else if (node.type === 'TEXT') {
                        try {
                            // Get all fonts used in the text node
                            const fonts = node.getRangeAllFontNames(0, node.characters.length);
                            console.log('Loading fonts:', fonts);
                            
                            // Load each font
                            for (const font of fonts) {
                                await figma.loadFontAsync(font);
                            }
                            
                            // Update the text
                            node.characters = msg.text;
                            updatedCount++;
                            console.log('Successfully updated text layer');
                        } catch (error) {
                            console.error('Error updating text layer:', error);
                            figma.notify('Error updating text layer: ' + error.message);
                        }
                    }
                }

                // Show success message
                if (updatedCount > 0) {
                    figma.notify(`Updated ${updatedCount} text layer${updatedCount > 1 ? 's' : ''}`);
                } else {
                    figma.notify('No text layers were updated');
                }
            } catch (error) {
                console.error('Error in update-text handler:', error);
                figma.notify('Error: ' + error.message);
            }
            break;

        case 'save-language':
            console.log('Saving language:', msg.language);
            await figma.clientStorage.setAsync('targetLanguage', msg.language);
            break;

        case 'get-language':
            console.log('Getting saved language');
            const savedLanguage = await figma.clientStorage.getAsync('targetLanguage');
            figma.ui.postMessage({
                type: 'set-language',
                language: savedLanguage || 'es' // Default to Spanish if no language is set
            });
            break;
    }
};