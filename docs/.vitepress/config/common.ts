import {defineConfig, type DefaultTheme} from 'vitepress'

export const common = defineConfig({
    title: "MBCP docs",
    description: "MBCP library docs",
    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        socialLinks: [
            {icon: 'github', link: 'https://github.com/snowykami/mbcp'}
        ]
    },
    srcDir: '.'
})