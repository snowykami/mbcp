import {defineConfig} from 'vitepress'
import {ThemeConfig} from "./utils";

export const zht = defineConfig({
    lang: "zh-Hant",
    title: "MBCP 文檔",
    description: "MBCP 粒子計算和生成庫文檔",
    themeConfig: {
        nav: [
            {text: '指引', link: '/zht/guide/'},
            {text: '參考', link: '/zht/refer'},
            {text: 'API引用', link: '/zht/api/'},
            {text: '示範', link: '/zht/demo/'},
        ],
        docFooter: {
            prev: '上一頁',
            next: '下一頁'
        },
        editLink: ThemeConfig.getEditLink(
            '於 GitHub 上編輯這頁',
        ),
        footer: {
            message: '文檔由 <a href="https://vitepress.dev/">VitePress</a> 構建 | API引用由 <a href="https://github.com/LiteyukiStudio/litedoc">litedoc</a> 生成',
            copyright: ThemeConfig.copyright
        },
        outline: ThemeConfig.getOutLine("頁面內容")
    },
})