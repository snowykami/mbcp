import {defineConfig} from 'vitepress'

export const ja = defineConfig({
    lang: "ja-JP",
    description: "Minecraftのパーティクル生成用のライブラリ",
    themeConfig: {
        nav: [
            {text: 'スタート', link: '/ja/guide/'},
            {text: 'APIドキュメント', link: '/ja/api/'},
            {text: 'インスタンス', link: '/ja/demo/'},
        ],
        footer: {
            message: '<a href="https://vitepress.dev/">VitePress</a> で構築されたドキュメント | <a href="https://github.com/LiteyukiStudio/litedoc">litedoc</a> によって生成されたAPIリファレンス',
            copyright: 'Copyright (C) 2020-2024 SnowyKami. All Rights Reserved'
        }
    },
})