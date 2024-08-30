import {defineConfig} from 'vitepress'
import {generateSidebar} from 'vitepress-sidebar';
import {zh} from "./zh";
import {en} from "./en";
import {ja} from "./ja";
import {zht} from "./zht";

let defaultLocale = 'zh';
const commonSidebarOptions = {
    collapsed: true,
    convertSameNameSubFileToGroupIndexPage: true,
    useTitleFromFrontmatter: true,
    useTitleFromFileHeading: true,
    useFolderTitleFromIndexFile: true,
    useFolderLinkFromIndexFile: true,
    includeFolderIndexFile: true,
    rootGroupText: 'MBCP',
}

/**
 * Generate sidebar config
 * multiple languages and sections
 * @returns {any[]}
 */
function generateSidebarConfig(): any[] {
    let sections = ["api", "refer", "guide"]
    let languages = ['zh', 'en', 'ja', 'zht']
    let ret = []
    for (let language of languages) {
        for (let section of sections) {
            if (language === defaultLocale) {
                ret.push({
                    basePath: `/${section}/`,
                    scanStartPath: `${language}/${section}`,
                    resolvePath: `/${section}/`,
                    ...commonSidebarOptions
                })
            } else {
                ret.push({
                    basePath: `/${language}/${section}/`,
                    scanStartPath: `${language}/${section}`,
                    resolvePath: `/${language}/${section}/`,
                    ...commonSidebarOptions
                })
            }
        }
    }
    return ret
}

console.log(generateSidebarConfig())

export const common = defineConfig({
    title: "MBCP docs",
    description: "MBCP library docs",
    markdown: {
        math: true
    },
    rewrites: {
        [`${defaultLocale}/:rest*`]: ":rest*",
    },
    themeConfig: {
        sidebar: generateSidebar(
            [
                ...generateSidebarConfig()
            ]
        ),
        socialLinks: [
            {icon: 'github', link: 'https://github.com/snowykami/mbcp'}
        ],
        editLink: {
            pattern: 'https://github.com/snowykami/mbcp/tree/main/docs/:path'
        },
        outline: [2, 6]
    },
    sitemap: {
        hostname: 'https://mbcp.sfkm.me'
    },
    locales: {
        root: {label: "简体中文", ...zh},
        en: {label: "English", ...en},
        ja: {label: "日本語", ...ja},
        zht: {label: "繁體中文", ...zht},
    },
})