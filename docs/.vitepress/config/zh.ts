import {defineConfig} from 'vitepress'
import {ThemeConfig} from "./utils";

export const zh = defineConfig({
    lang: "zh-Hans",
    title: "MBCP 文档",
    description: "MBCP 粒子计算和生成库文档",
    themeConfig: {
        nav: [
            {text: '快速开始', link: '/guide/'},
            {text: '参考', link: '/refer'},
            {text: 'API引用', link: '/api/'},
            {text: '实例', link: '/demo/'},
        ],
        docFooter: {
            prev: '上一页',
            next: '下一页'
        },
        editLink: ThemeConfig.getEditLink(
            '在 GitHub 上编辑此页',
        ),
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