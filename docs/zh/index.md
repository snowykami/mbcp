---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "MBCP"
  text: "更多基础变换粒子"
  tagline: 用于几何运算和Minecraft粒子制作的库
  actions:
    - theme: brand
      text: 快速开始
      link: ./guide/
    - theme: alt
      text: API文档
      link: ./api/
    - theme: alt
      text: 最佳实践
      link: ./demo/best-practice
  image:
    src: /mbcp-logo.svg
    alt: MBCP logo

features:
  - title: 高可用性
    icon: 🛠️
    details: 通过简单的接口，实现了大部分几何运算和粒子制作的需求
  - title: 高集成度
    icon: 📦
    details: 对<code>numpy</code>、<code>scipy</code>及<code>sumpy</code>进行了封装和集成，使脚本编写像使用Geogebra一样简单
  - title: 内置预设
    icon: 🧊
    details: 提供了大量的预设，包括常见的几何图形、粒子效果等，方便快速制作
---
