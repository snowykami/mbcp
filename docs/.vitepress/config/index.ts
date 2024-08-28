import {defineConfig} from "vitepress";

import {common} from './common'
import {en} from './en'
import {zh} from './zh'
import {ja} from './ja'



export default defineConfig({
    ...common,
    locales:{
        root: { label: "简体中文", ...zh },
        en: { label: "English", ...en },
        ja: { label: "日本語", ...ja },
    }
})