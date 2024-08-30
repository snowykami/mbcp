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
}
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
                ...[defaultLocale, 'en', 'ja', 'zht'].map((locale) => {
                    if (locale === defaultLocale) {
                        return {
                            basePath: '/api/',
                            scanStartPath: `${locale}/api`,
                            resolvePath: '/api/',
                            ...commonSidebarOptions
                        }
                    } else {
                        return {
                            basePath: `/${locale}/api/`,
                            scanStartPath: `${locale}/api`,
                            resolvePath: `/${locale}/api/`,
                            ...commonSidebarOptions
                        }
                    }
                })
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