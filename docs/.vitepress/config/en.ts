import {defineConfig} from 'vitepress'

export const en = defineConfig({

    lang: "en-US",
    description: "A library made for Minecraft particle generation",
    themeConfig: {
        nav: [
            {text: 'Get Start', link: '/guide'},
            {text: 'API Document', link: '/api/'},
            {text: 'Demo', link: '/demo/'},
        ],
    },
})