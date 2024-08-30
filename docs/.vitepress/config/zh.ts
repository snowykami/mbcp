import {defineConfig} from 'vitepress'

export const zh = defineConfig({
    lang: "zh-Hans",
    description: "一个用于Minecraft粒子计算和生成的库",
    themeConfig: {
        nav: [
            {text: '快速开始', link: '/guide/'},
            {text: 'API文档', link: '/api/'},
            {text: '实例', link: '/demo/'},
        ],
        footer: {
            message: '文档由 <a href="https://vitepress.dev/">VitePress</a> 构建 | API引用由 <a href="https://github.com/LiteyukiStudio/litedoc">litedoc</a> 生成',
            copyright: 'Copyright (C) 2020-2024 SnowyKami. All Rights Reserved'
        },
        outline: {
            label: "页面内容",
            level: [2, 6]
        }
    },
})