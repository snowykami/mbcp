import {defineConfig} from 'vitepress'

export const zht = defineConfig({

    lang: "zh-Hant",
    description: "一個用於Minecraft粒子計算和生成的軟體庫",
    themeConfig: {
        nav: [
            {text: '指引', link: '/zht/guide/'},
            {text: 'API文檔', link: '/zht/api/'},
            {text: '示範', link: '/zht/demo/'},
        ],
        footer: {
            message: '文檔由 <a href="https://vitepress.dev/">VitePress</a> 構建 | API引用由 <a href="https://github.com/LiteyukiStudio/litedoc">litedoc</a> 生成',
            copyright: 'Copyright (C) 2020-2024 SnowyKami. All Rights Reserved'
        },
        outline: {
            label: "頁面內容",
            level: [2, 6]
        }
    },
})