// 共有配置项，导入index用

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
    head: [
        ['link', {rel: 'icon', type: 'image/svg+xml', href: '/mbcp-logo.svg'}],
        ['link', {rel: 'stylesheet', href: 'https://fonts.font.im/css?family=Cousine:400,400i,700,700i|Poppins:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i'}],
    ],
    markdown: {
        math: true
    },
    rewrites: {
        [`${defaultLocale}/:rest*`]: ":rest*",
    },
    themeConfig: {
        logo: '/mbcp-logo.svg',
        sidebar: generateSidebar(
            [
                ...generateSidebarConfig()
            ]
        ),
        socialLinks: [
            {icon: 'github', link: 'https://github.com/snowykami/mbcp'}
        ],
        search: {
            provider: 'local',
            options: {
                locales: {
                    root: {
                        translations: {
                            button: {
                                buttonText: '搜索文档',
                                buttonAriaLabel: '打开搜索框',
                            },
                            modal: {
                                noResultsText: '没有找到搜索结果',
                                resetButtonTitle: '清除查询条件',
                                footer: {
                                    selectText: '选择',
                                    navigateText: '切换',
                                }
                            }
                        },
                    },
                    en: {
                        translations: {
                            button: {
                                buttonText: 'Search',
                                buttonAriaLabel: 'Search',
                            },
                            modal: {
                                noResultsText: 'No results found',
                                resetButtonTitle: 'Reset search query',
                                footer: {
                                    selectText: 'Select',
                                    navigateText: 'Navigate',
                                }
                            }
                        }
                    },
                    zht: {
                        translations: {
                            button: {
                                buttonText: '搜索文檔',
                                buttonAriaLabel: '打開搜索框',
                            },
                            modal: {
                                noResultsText: '沒有找到搜索結果',
                                resetButtonTitle: '清除查詢條件',
                                footer: {
                                    selectText: '選擇',
                                    navigateText: '切換',
                                }
                            }
                        }
                    },
                    ja: {
                        translations: {
                            button: {
                                buttonText: '検索',
                                buttonAriaLabel: '検索を開く',
                            },
                            modal: {
                                noResultsText: '検索結果が見つかりません',
                                resetButtonTitle: 'リセット',
                                footer: {
                                    selectText: '選択',
                                    navigateText: '移動',
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    sitemap: {
        hostname: 'https://mbcp.sfkm.me'
    },
    lastUpdated: true,
    locales: {
        root: {label: "简体中文", ...zh},
        en: {label: "English", ...en},
        ja: {label: "日本語", ...ja},
        zht: {label: "繁體中文", ...zht},
    },
})