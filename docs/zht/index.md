---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "MBCP"
  text: "更多基礎變化粒子"
  tagline: 用於幾何運算和 當個創世神 粒子製作的軟體庫
  actions:
    - theme: brand
      text: 跟隨引導
      link: ./guide/
    - theme: alt
      text: API文檔
      link: ./api/
  image:
    src: /mbcp-logo.svg
    alt: MBCP logo

features:
  - title: 高度易用
    details: 通過簡單的接口，實現了大部分幾何運算及粒子製作的需求
  - title: 高度集成
    details: 對<code>numpy</code>、<code>scipy</code>及<code>sympy</code>進行了封裝和集成，使腳本編寫像使用Geogebra一樣easy
  - title: 內置預設
    details: 提供了大量的預設，包括常見的幾何圖形、粒子效果等，便於快速生產
---
<style>
:root {
  --vp-home-hero-name-color: transparent;
  --vp-home-hero-name-background: -webkit-linear-gradient(120deg, #bd34fe 30%, #41d1ff);
}

@media (min-width: 640px) {
  :root {
    --vp-home-hero-image-filter: blur(56px);
  }
}

@media (min-width: 960px) {
  :root {
    --vp-home-hero-image-filter: blur(68px);
  }
}
</style>