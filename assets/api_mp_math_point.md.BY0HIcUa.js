import{_ as s,c as i,o as a,a2 as t}from"./chunks/framework.C94oF1kp.js";const y=JSON.parse('{"title":"mbcp.mp_math.point","description":"","frontmatter":{"title":"mbcp.mp_math.point","editLink":false},"headers":[],"relativePath":"api/mp_math/point.md","filePath":"zh/api/mp_math/point.md"}'),n={name:"api/mp_math/point.md"},l=t(`<h1 id="mbcp-mp-math-point" tabindex="-1">mbcp.mp_math.point <a class="header-anchor" href="#mbcp-mp-math-point" aria-label="Permalink to &quot;mbcp.mp_math.point&quot;">​</a></h1><p><strong>说明</strong>: 本模块定义了三维空间中点的类。</p><h3 id="class-point3" tabindex="-1"><em><strong>class</strong></em> <code>Point3</code> <a class="header-anchor" href="#class-point3" aria-label="Permalink to &quot;***class*** \`Point3\`&quot;">​</a></h3><h4 id="def-init-self-x-float-y-float-z-float" tabindex="-1"><em><strong>def</strong></em> <code>__init__(self, x: float, y: float, z: float)</code> <a class="header-anchor" href="#def-init-self-x-float-y-float-z-float" aria-label="Permalink to &quot;***def*** \`__init__(self, x: float, y: float, z: float)\`&quot;">​</a></h4><p><strong>说明</strong>: 笛卡尔坐标系中的点。</p><p><strong>参数</strong>:</p><blockquote><ul><li>x: x 坐标</li><li>y: y 坐标</li><li>z: z 坐标</li></ul></blockquote><details><summary><b>源代码</b> 或 <a href="https://github.com/snowykami/mbcp/tree/main/mbcp/mp_math/point.py#L15" target="_blank">在GitHub上查看</a></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> __init__</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(self, x: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, y: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, z: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">):</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        笛卡尔坐标系中的点。</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        Args:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">            x: x 坐标</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">            y: y 坐标</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">            z: z 坐标</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">    self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.x </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> x</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">    self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.y </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> y</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">    self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.z </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> z</span></span></code></pre></div></details><h4 id="def-approx-self-other-point3-epsilon-float-approx-bool" tabindex="-1"><em><strong>def</strong></em> <code>approx(self, other: Point3, epsilon: float = APPROX) -&gt; bool</code> <a class="header-anchor" href="#def-approx-self-other-point3-epsilon-float-approx-bool" aria-label="Permalink to &quot;***def*** \`approx(self, other: Point3, epsilon: float = APPROX) -&gt; bool\`&quot;">​</a></h4><p><strong>说明</strong>: 判断两个点是否近似相等。</p><p><strong>参数</strong>:</p><blockquote><ul><li>other:</li><li>epsilon:</li></ul></blockquote><p><strong>返回</strong>: 是否近似相等</p><details><summary><b>源代码</b> 或 <a href="https://github.com/snowykami/mbcp/tree/main/mbcp/mp_math/point.py#L27" target="_blank">在GitHub上查看</a></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;"> approx</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(self, other: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;Point3&#39;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, epsilon: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">=</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">APPROX</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">) -&gt; </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">bool</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        判断两个点是否近似相等。</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        Args:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">            other:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">            epsilon:</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        Returns:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">            是否近似相等</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    return</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> all</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">([</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">abs</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.x </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">-</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> other.x) </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">&lt;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> epsilon, </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">abs</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.y </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">-</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> other.y) </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">&lt;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> epsilon, </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">abs</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.z </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">-</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> other.z) </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">&lt;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> epsilon])</span></span></code></pre></div></details><p><code>@overload</code></p><h4 id="def-self-other-vector3-point3" tabindex="-1"><em><strong>def</strong></em> <code>self + other: Vector3 =&gt; Point3</code> <a class="header-anchor" href="#def-self-other-vector3-point3" aria-label="Permalink to &quot;***def*** \`self + other: Vector3 =&gt; Point3\`&quot;">​</a></h4><details><summary><b>源代码</b> 或 <a href="https://github.com/snowykami/mbcp/tree/main/mbcp/mp_math/point.py#L43" target="_blank">在GitHub上查看</a></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;">@overload</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> __add__</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(self, other: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;Vector3&#39;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">) -&gt; </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;Point3&#39;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">    ...</span></span></code></pre></div></details><p><code>@overload</code></p><h4 id="def-self-other-point3-point3" tabindex="-1"><em><strong>def</strong></em> <code>self + other: Point3 =&gt; Point3</code> <a class="header-anchor" href="#def-self-other-point3-point3" aria-label="Permalink to &quot;***def*** \`self + other: Point3 =&gt; Point3\`&quot;">​</a></h4><details><summary><b>源代码</b> 或 <a href="https://github.com/snowykami/mbcp/tree/main/mbcp/mp_math/point.py#L47" target="_blank">在GitHub上查看</a></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;">@overload</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> __add__</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(self, other: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;Point3&#39;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">) -&gt; </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;Point3&#39;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">    ...</span></span></code></pre></div></details><h4 id="def-self-other" tabindex="-1"><em><strong>def</strong></em> <code>self + other</code> <a class="header-anchor" href="#def-self-other" aria-label="Permalink to &quot;***def*** \`self + other\`&quot;">​</a></h4><p><strong>说明</strong>: P + V -&gt; P P + P -&gt; P</p><p><strong>参数</strong>:</p><blockquote><ul><li>other:</li></ul></blockquote><details><summary><b>源代码</b> 或 <a href="https://github.com/snowykami/mbcp/tree/main/mbcp/mp_math/point.py#L50" target="_blank">在GitHub上查看</a></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> __add__</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(self, other):</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        P + V -&gt; P</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        P + P -&gt; P</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        Args:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">            other:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        Returns:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    return</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> Point3(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.x </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">+</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> other.x, </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.y </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">+</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> other.y, </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.z </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">+</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> other.z)</span></span></code></pre></div></details><h4 id="def-eq-self-other" tabindex="-1"><em><strong>def</strong></em> <code>__eq__(self, other)</code> <a class="header-anchor" href="#def-eq-self-other" aria-label="Permalink to &quot;***def*** \`__eq__(self, other)\`&quot;">​</a></h4><p><strong>说明</strong>: 判断两个点是否相等。</p><p><strong>参数</strong>:</p><blockquote><ul><li>other:</li></ul></blockquote><details><summary><b>源代码</b> 或 <a href="https://github.com/snowykami/mbcp/tree/main/mbcp/mp_math/point.py#L60" target="_blank">在GitHub上查看</a></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> __eq__</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(self, other):</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        判断两个点是否相等。</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        Args:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">            other:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        Returns:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    return</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> approx(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.x, other.x) </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">and</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> approx(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.y, other.y) </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">and</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> approx(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.z, other.z)</span></span></code></pre></div></details><h4 id="def-self-other-point3-vector3" tabindex="-1"><em><strong>def</strong></em> <code>self - other: Point3 =&gt; Vector3</code> <a class="header-anchor" href="#def-self-other-point3-vector3" aria-label="Permalink to &quot;***def*** \`self - other: Point3 =&gt; Vector3\`&quot;">​</a></h4><p><strong>说明</strong>: P - P -&gt; V</p><p>P - V -&gt; P 已在 :class:<code>Vector3</code> 中实现</p><p><strong>参数</strong>:</p><blockquote><ul><li>other:</li></ul></blockquote><details><summary><b>源代码</b> 或 <a href="https://github.com/snowykami/mbcp/tree/main/mbcp/mp_math/point.py#L69" target="_blank">在GitHub上查看</a></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> __sub__</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(self, other: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;Point3&#39;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">) -&gt; </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;Vector3&#39;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        P - P -&gt; V</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        P - V -&gt; P  已在 :class:\`Vector3\` 中实现</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        Args:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">            other:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        Returns:</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    from</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> .vector </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">import</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> Vector3</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    return</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> Vector3(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.x </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">-</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> other.x, </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.y </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">-</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> other.y, </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.z </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">-</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> other.z)</span></span></code></pre></div></details>`,36),h=[l];function p(e,k,r,o,d,g){return a(),i("div",null,h)}const c=s(n,[["render",p]]);export{y as __pageData,c as default};