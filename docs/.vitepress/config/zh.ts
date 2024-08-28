import {defineConfig} from 'vitepress'

export const zh = defineConfig({
    lang: "zh-Hans",
    description: "一个用于Minecraft粒子计算和生成的库",

    themeConfig: {
        nav: [
            {text: '快速开始', link: '/guide'},
            {text: 'API文档', link: '/api/'},
            {text: '实例', link: '/demo/'},
        ],
        // sidebar: {
        //     '/api/': {
        //         base: '/api/',
        //         items: [
        //         ]
        //     }
        // }
    },
})