import {defineConfig} from 'vitepress'

import AutoSidebarPlugin from 'vitepress-auto-sidebar-plugin'

export const common = defineConfig({
    title: "MBCP docs",
    description: "MBCP library docs",
    vite: {
        plugins: [
            AutoSidebarPlugin({
                // 如果不指定 `srcDir`，则默认使用 `vitepress` 的 `srcDir`
                ignoreList: [
                    'README.md'
                ],
                title: {
                    mode: text => text.toLowerCase()
                }
            }),
        ],
    },
    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        socialLinks: [
            {icon: 'github', link: 'https://github.com/snowykami/mbcp'}
        ]
    },
    srcDir: '.'
})