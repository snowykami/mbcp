import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "MBCP docs",
  description: "MBCP library docs",
  locales: {
    root: {
      label: '简体中文',
      lang: 'zh-CN'
    },
    en: {
        label: 'English',
        lang: 'en-US'
    }
  },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: 'Examples',
        items: [
          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/snowykami/mbcp' }
    ]
  },
  srcDir: '.'
})
