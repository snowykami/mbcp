import {defineConfig} from 'vitepress'

export const ja = defineConfig({

    lang: "ja-JP",
    description: "Minecraftのパーティクル生成用のライブラリ",
    themeConfig: {
        nav: [
            {text: 'スタート', link: '/guide'},
            {text: 'APIドキュメント', link: '/api/'},
            {text: 'インスタンス', link: '/demo/'},
        ],
    },
})