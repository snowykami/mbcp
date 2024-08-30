/**
 * GetEditLink Options
 * @param text Edit link text
 */
export const ThemeConfig = {
    getEditLink: (editPageText: string): { pattern: (params: { filePath: string; }) => string; text: string; } => {
        return {
            pattern: ({filePath}: { filePath: string; }): string => {
                const regex = /^[^\/]+\/api/;
                if (regex.test(filePath)) {
                    // remove {lang}/api prefix
                    filePath = filePath.replace(regex, '')
                        .replace('index.md', '__init__.py')
                        .replace('.md', '.py');
                    return `https://github.com/snowykami/mbcp/tree/main/mbcp/${filePath}`;
                } else {
                    return `https://github.com/snowykami/mbcp/tree/main/docs/${filePath}`;
                }
            },
            text: editPageText
        };
    }
}