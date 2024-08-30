// 本模块储存一些工具函数和引用

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
    },

    getOutLine: (label: string): { label: string; level: [number, number]; } => {
        return {
            label: label,
            level: [2, 6]
        };
    },

    copyright: 'Copyright (C) 2020-2024 SnowyKami. All Rights Reserved'
}