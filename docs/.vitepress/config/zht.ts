import {defineConfig} from 'vitepress'

export const zht = defineConfig({

    lang: "zh-Hant",
    description: "一個用於Minecraft粒子計算和生成的軟體庫",
    themeConfig: {
        nav: [
            {text: '指引', link: '/guide/'},
            {text: 'API文檔', link: '/api/'},
            {text: '示範', link: '/demo/'},
        ],
    },
})