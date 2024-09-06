import DefaultTheme from 'vitepress/theme-without-fonts'
import Theme from 'vitepress/theme'
import {createI18n} from 'vue-i18n'
import './fonts.css'

const i18n = createI18n({
    // something vue-i18n options here ..
    messages: {
        en: {
            tip: "TIP",
        },
        ja: {
            tip: "ヒント",
        },
        zh: {
            tip: "提示",
        },
        zht: {
            tip: "提示",
        }
    }
})

export default {
    extends: Theme,
    enhanceApp({app}) {
        app.use(i18n)
    }
}