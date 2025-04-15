export function initializeTheme() {
    // Request saved theme from Figma
    parent.postMessage({ 
        pluginMessage: { 
            type: 'get-theme',
            defaultTheme: 'dark'
        }
    }, '*');
}

export function setTheme(theme: 'light' | 'dark' | 'system') {
    if (theme === 'system') {
        document.documentElement.removeAttribute('data-theme');
    } else {
        document.documentElement.setAttribute('data-theme', theme);
    }
} 