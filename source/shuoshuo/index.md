---
title: 说说
type: shuoshuo
date: 2024-09-08 16:58:09
---

## 说说

{% note yellow fa-triangle-exclamation %}
这个页面还在测试中！可能会遇到加载不出来的情况xwx
我以后或许会换成别的应用而不是 Artitalk
{% endnote %}

<style>
    /* .power {
        display: none;
    } */
    #shuoshuo-loading {
        font-size: 2rem;
        width: 100%;
        text-align: center;
        display: none;
    }
</style>
<div id="shuoshuo-loading"><i class="fa-regular fa-spinner fa-spin-pulse" style="--fa-animation-duration: 0.8s;"></i> 加载中...</div>
<script data-swup-reload-script type="text/javascript" src="https://unpkg.com/artitalk"></script>
<!-- 存放说说的容器 -->
<div id="artitalk_main">
</div>
<script data-swup-reload-script type="text/javascript">
new Artitalk({
    appId: 'M5lXnnm5xIqW3u8bILD0LItl-MdYXbMMI', // Your LeanCloud appId
    appKey: 'OpChJqGQEn2Lu6ZT43oRIiiZ', // Your LeanCloud appKey
    lang: 'zh',
    shuoPla: '写点东西吧~',
    color1: '#32336522',
    color2: '#32aac9',
    atEmoji: {
        deon_hug: "https://emoji.179.life/deon-emoji/deon_hug.png",
        deon_expect: "https://emoji.179.life/deon-emoji/deon_expect.png",
        deon_vomiting_blood: "https://emoji.179.life/deon-emoji/deon_vomiting-blood.png",
        deon_p: "https://emoji.179.life/deon-emoji/deon_p.png",
        deon_angry: "https://emoji.179.life/deon-emoji/deon_angry.png",
        deon_eat: "https://emoji.179.life/deon-emoji/deon_eat.png",
        x179_stealing: "https://emoji.179.life/179-emoji/179_stealing.png",
        x179_zhaocai: "https://emoji.179.life/179-emoji/179_zhaocai.png",
        x179_firecracker: "https://emoji.179.life/179-emoji/179_firecracker.png",
        x179_firework: "https://emoji.179.life/179-emoji/179_firework.png",
        x179_call: "https://emoji.179.life/179g-emoji/179g_call.gif",
        x179_play: "https://emoji.179.life/179g-emoji/179g_play.gif",
    },
})
</script>
<!-- <script data-swup-reload-script type="text/javascript">
    const loadingElement = document.getElementById('shuoshuo-loading')
    const observer = new MutationObserver(function(mutationsList, observer) {
        if (document.getElementById('artitalk_main').childElementCount > 0) {
            console.log("stop loading")
            loadingElement.style.display = 'none';
        } else {
            loadingElement.style.display = 'block';
            console.log("continue loading")
        }
    });
    observer.observe(targetElement, { childList: true });
</script> -->

Powered By [Artitalk](https://artitalk.js.org)