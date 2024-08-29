import{_ as s,c as i,o as a,a2 as n}from"./chunks/framework.BV61Qrc0.js";const E=JSON.parse('{"title":"mbcp.mp_math.utils","description":"","frontmatter":{"title":"mbcp.mp_math.utils"},"headers":[],"relativePath":"en/api/mp_math/utils.md","filePath":"en/api/mp_math/utils.md"}'),t={name:"en/api/mp_math/utils.md"},l=n(`<h3 id="func-clamp-float" tabindex="-1"><em>func</em> <code>clamp() -&gt; float</code> <a class="header-anchor" href="#func-clamp-float" aria-label="Permalink to &quot;*func* \`clamp() -&gt; float\`&quot;">​</a></h3><p><strong>Description</strong>: 区间限定函数</p><p><strong>Return</strong>: 限制后的值</p><p><strong>Arguments</strong>:</p><blockquote><ul><li>x: 待限定的值</li><li>min_: 最小值</li><li>max_: 最大值</li></ul></blockquote><details><summary><b>Source code</b></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;"> clamp</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(x: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, min_: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, max_: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">) -&gt; </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    区间限定函数</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    Args:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        x: 待限定的值</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        min_: 最小值</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        max_: 最大值</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    Returns:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        限制后的值</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    return</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> max</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">min</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(x, max_), min_)</span></span></code></pre></div></details><h3 id="func-approx-x-float-0-0-y-float-approx-bool" tabindex="-1"><em>func</em> <code>approx(x: float = 0.0, y: float = APPROX) -&gt; bool</code> <a class="header-anchor" href="#func-approx-x-float-0-0-y-float-approx-bool" aria-label="Permalink to &quot;*func* \`approx(x: float = 0.0, y: float = APPROX) -&gt; bool\`&quot;">​</a></h3><p><strong>Description</strong>: 判断两个数是否近似相等。或包装一个实数，用于判断是否近似于0。</p><p><strong>Return</strong>: 是否近似相等</p><p><strong>Arguments</strong>:</p><blockquote><ul><li>x: 数1</li><li>y: 数2</li><li>epsilon: 误差</li></ul></blockquote><details><summary><b>Source code</b></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;"> approx</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(x: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, y: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">=</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">0.0</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, epsilon: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">=</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">APPROX</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">) -&gt; </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">bool</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    判断两个数是否近似相等。或包装一个实数，用于判断是否近似于0。</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    Args:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        x: 数1</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        y: 数2</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        epsilon: 误差</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    Returns:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        是否近似相等</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    return</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> abs</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(x </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">-</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> y) </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">&lt;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> epsilon</span></span></code></pre></div></details><h3 id="func-sign-x-float-false-str" tabindex="-1"><em>func</em> <code>sign(x: float = False) -&gt; str</code> <a class="header-anchor" href="#func-sign-x-float-false-str" aria-label="Permalink to &quot;*func* \`sign(x: float = False) -&gt; str\`&quot;">​</a></h3><p><strong>Description</strong>: 获取数的符号。</p><p><strong>Return</strong>: 符号 + - &quot;&quot;</p><p><strong>Arguments</strong>:</p><blockquote><ul><li>x: 数</li><li>only_neg: 是否只返回负数的符号</li></ul></blockquote><details><summary><b>Source code</b></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;"> sign</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(x: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, only_neg: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">bool</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">=</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">False</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">) -&gt; </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">str</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    &quot;&quot;&quot;获取数的符号。</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    Args:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        x: 数</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        only_neg: 是否只返回负数的符号</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    Returns:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        符号 + - &quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    if</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> x </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">&gt;</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> 0</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">        return</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> &#39;+&#39;</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;"> if</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;"> not</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> only_neg </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">else</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> &#39;&#39;</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    elif</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> x </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">&lt;</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> 0</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">        return</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> &#39;-&#39;</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    else</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">        return</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> &#39;&#39;</span></span></code></pre></div></details><h3 id="func-sign-format-x-float-false-str" tabindex="-1"><em>func</em> <code>sign_format(x: float = False) -&gt; str</code> <a class="header-anchor" href="#func-sign-format-x-float-false-str" aria-label="Permalink to &quot;*func* \`sign_format(x: float = False) -&gt; str\`&quot;">​</a></h3><p><strong>Description</strong>: 格式化符号数 -1 -&gt; -1 1 -&gt; +1 0 -&gt; &quot;&quot;</p><p><strong>Return</strong>: 符号 + - &quot;&quot;</p><p><strong>Arguments</strong>:</p><blockquote><ul><li>x: 数</li><li>only_neg: 是否只返回负数的符号</li></ul></blockquote><details><summary><b>Source code</b></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;"> sign_format</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(x: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, only_neg: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">bool</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">=</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">False</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">) -&gt; </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">str</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    &quot;&quot;&quot;格式化符号数</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    -1 -&gt; -1</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    1 -&gt; +1</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    0 -&gt; &quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    Args:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        x: 数</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        only_neg: 是否只返回负数的符号</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    Returns:</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">        符号 + - &quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">    &quot;&quot;&quot;</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    if</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> x </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">&gt;</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> 0</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">        return</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;"> f</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;+</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">{</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">x</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">}</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;"> if</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;"> not</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> only_neg </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">else</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;"> f</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">{</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">x</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">}</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    elif</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> x </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">&lt;</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> 0</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">        return</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;"> f</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;-</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">{abs</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(x)</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">}</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    else</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">        return</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> &#39;&#39;</span></span></code></pre></div></details><h3 id="class-approx" tabindex="-1"><strong>class</strong> <code>Approx</code> <a class="header-anchor" href="#class-approx" aria-label="Permalink to &quot;**class** \`Approx\`&quot;">​</a></h3><h3 id="method-init-self-value-realnumber" tabindex="-1"><em>method</em> <code>__init__(self, value: RealNumber)</code> <a class="header-anchor" href="#method-init-self-value-realnumber" aria-label="Permalink to &quot;*method* \`__init__(self, value: RealNumber)\`&quot;">​</a></h3><details><summary><b>Source code</b></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> __init__</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(self, value: RealNumber):</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">    self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.value </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">=</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> value</span></span></code></pre></div></details><h3 id="method-eq-self-other" tabindex="-1"><em>method</em> <code>__eq__(self, other)</code> <a class="header-anchor" href="#method-eq-self-other" aria-label="Permalink to &quot;*method* \`__eq__(self, other)\`&quot;">​</a></h3><details><summary><b>Source code</b></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> __eq__</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(self, other):</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    if</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> isinstance</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.value, (</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">int</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">)):</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">        if</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> isinstance</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(other, (</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">float</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">, </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">int</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">)):</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">            return</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> abs</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.value </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">-</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> other) </span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">&lt;</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> APPROX</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">        else</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">            self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.raise_type_error(other)</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    elif</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> isinstance</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.value, Vector3):</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">        if</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> isinstance</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(other, (Vector3, Point3, Plane3, Line3)):</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">            return</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> all</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">([approx(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.value.x, other.x), approx(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.value.y, other.y), approx(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.value.z, other.z)])</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">        else</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">:</span></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">            self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.raise_type_error(other)</span></span></code></pre></div></details><h3 id="method-raise-type-error-self-other" tabindex="-1"><em>method</em> <code>raise_type_error(self, other)</code> <a class="header-anchor" href="#method-raise-type-error-self-other" aria-label="Permalink to &quot;*method* \`raise_type_error(self, other)\`&quot;">​</a></h3><details><summary><b>Source code</b></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;"> raise_type_error</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(self, other):</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    raise</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> TypeError</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">f</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;Unsupported type: </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">{type</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.value)</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">}</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> and </span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">{type</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(other)</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">}</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&#39;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">)</span></span></code></pre></div></details><h3 id="method-ne-self-other" tabindex="-1"><em>method</em> <code>__ne__(self, other)</code> <a class="header-anchor" href="#method-ne-self-other" aria-label="Permalink to &quot;*method* \`__ne__(self, other)\`&quot;">​</a></h3><details><summary><b>Source code</b></summary><div class="language-python vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">def</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> __ne__</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(self, other):</span></span>
<span class="line"><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">    return</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;"> not</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> self</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">.</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;">__eq__</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">(other)</span></span></code></pre></div></details>`,33),h=[l];function p(e,k,r,d,o,g){return a(),i("div",null,h)}const y=s(t,[["render",p]]);export{E as __pageData,y as default};