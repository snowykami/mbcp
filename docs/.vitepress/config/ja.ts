import {defineConfig} from 'vitepress'
import {ThemeConfig} from "./utils";

export const ja = defineConfig({
    lang: "ja-JP",
    title: "MBCP ドキュメント",
    description: "MBCP ライブラリ ドキュメント",
    themeConfig: {
        nav: [
            {text: 'スタート', link: '/ja/guide/'},
            {text: 'リファレンス', link: '/ja/refer'},
            {text: 'APIリファレンス', link: '/ja/api/'},
            {text: 'インスタンス', link: '/ja/demo/'},
        ],
        docFooter: {
            prev: '前のページ',
            next: '次のページ'
        },
        editLink: ThemeConfig.getEditLink(
            'このページをGitHubで編集する',
        ),
        footer: {
            message: '<a href="https://vitepress.dev/">VitePress</a> で構築されたドキュメント | <a href="https://github.com/LiteyukiStudio/litedoc">litedoc</a> によって生成されたAPIリファレンス',
            copyright: ThemeConfig.copyright
        },
        outline: ThemeConfig.getOutLine("ページの内容"),
    },
})