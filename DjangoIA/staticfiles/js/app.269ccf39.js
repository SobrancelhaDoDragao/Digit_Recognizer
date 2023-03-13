(function(){"use strict";var e={6097:function(e,n,t){var o=t(9242),i=t(3396);const r=(0,i._)("h1",{class:"TituloPrincipal"},"Digit Recognizer",-1),a=(0,i._)("footer",null,[(0,i.Uk)("Desenvolvido por "),(0,i._)("a",{href:"https://github.com/SobrancelhaDoDragao",target:"_blank"},"Eudson Durães")],-1);function s(e,n){const t=(0,i.up)("router-view");return(0,i.wg)(),(0,i.iD)(i.HY,null,[r,(0,i.Wm)(t,null,{default:(0,i.w5)((({Component:n})=>[(0,i.Wm)(o.uT,{name:"slide",mode:"out-in"},{default:(0,i.w5)((()=>[((0,i.wg)(),(0,i.j4)((0,i.LL)(n),{key:e.$route.path}))])),_:2},1024)])),_:1}),a],64)}var c=t(89);const u={},d=(0,c.Z)(u,[["render",s]]);var l=d,f=t(2483);const v={class:"animacaoDiv"},p=(0,i._)("p",{class:"explicao"},[(0,i.Uk)("Desenhe um número de "),(0,i._)("b",null,"0"),(0,i.Uk)(" a "),(0,i._)("b",null,"9"),(0,i.Uk)(", a inteligência artificial tentará reconhecer o numero desenhado.")],-1);function h(e,n,t,o,r,a){const s=(0,i.up)("Quadro");return(0,i.wg)(),(0,i.iD)("div",v,[p,(0,i.Wm)(s)])}const m={class:"containerQuadro",ref:"containerQuadro"},g={ref:"canvas",id:"quadro"};function w(e,n,t,r,a,s){const c=(0,i.up)("router-link"),u=(0,i.up)("Spinner");return(0,i.wg)(),(0,i.iD)(i.HY,null,[(0,i._)("div",m,[(0,i._)("canvas",g,null,512)],512),(0,i.Wm)(c,{onClick:(0,o.iM)(s.salvarCanvas,["prevent"]),class:"BotaoComum",to:""},{default:(0,i.w5)((()=>[(0,i.Uk)("Pronto")])),_:1},8,["onClick"]),(0,i.Wm)(u,{start:a.spin},null,8,["start"])],64)}t(7658);const _=e=>((0,i.dD)("data-v-861eb574"),e=e(),(0,i.Cn)(),e),b={key:0,class:"spin-conteiner"},k=_((()=>(0,i._)("div",{class:"lds-dual-ring"},[(0,i._)("p",{class:"louderMensagem"},"Carregando")],-1))),D=[k];function y(e,n,t,r,a,s){return(0,i.wg)(),(0,i.j4)(o.uT,{name:"slide",mode:"out-in"},{default:(0,i.w5)((()=>[t.start?((0,i.wg)(),(0,i.iD)("div",b,D)):(0,i.kq)("",!0)])),_:1})}var O={props:["start"]};const P=(0,c.Z)(O,[["render",y],["__scopeId","data-v-861eb574"]]);var C=P,x={name:"Quadro",components:{Spinner:C},data(){return{spin:!1}},methods:{async salvarCanvas(){this.spin=!0;const e=this.$refs.canvas;e.getContext("2d");let n=e.toDataURL("image/png");const t=await fetch("/PredictDigit",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({data_url:n})});var o=await t.json();this.spin=!1,"Error"==o.digit?alert("O Quadro não foi desenhado"):this.$router.push(`/PredictDigit/${o.digit}`)},async GetToken(){const e=await fetch("/get_csrf");let n=await e.json(),t=await n.csrf_token;return t}},mounted(){let e,n,t,o=5;const i=this.$refs.canvas,r=i.getContext("2d"),a=this.$refs.containerQuadro,s=()=>{i.width=a.clientWidth,i.height=a.clientHeight};function c(i,a){e&&(r.beginPath(),r.arc(i,a,o,0,2*Math.PI),r.closePath(),r.fill(),u(n,t,i,a)),n=i,t=a}function u(e,n,t,i){r.beginPath(),r.moveTo(e,n),r.lineTo(t,i),r.strokeStyle=r.fillStyle,r.lineWidth=2*o,r.stroke()}s(),window.addEventListener("resize",s),i.addEventListener("mousedown",(o=>{e=!0,n=o.offsetX,t=o.offsetY})),i.addEventListener("mouseup",(()=>{e=!1,n=void 0,t=void 0})),i.addEventListener("mousemove",(e=>{c(e.offsetX,e.offsetY)})),r.fillStyle="black",r.strokeStyle=r.fillStyle},beforeUnmount(){window.removeEventListener("resize",this.sizeCanvas),window.removeEventListener("mousedown",this.canvas),window.removeEventListener("mouseup",this.canvas),window.removeEventListener("mousemove",this.canvas)}};const j=(0,c.Z)(x,[["render",w]]);var E=j,L={name:"IndexView",components:{Quadro:E}};const S=(0,c.Z)(L,[["render",h]]);var T=S,U=t(7139);const W={class:"animacaoDiv"},z={class:"container-digit"},Q=(0,i._)("p",{class:"text-digit"},"O digito que foi previsto pela IA:",-1),$={class:"Digit-Prediction"},Z=(0,i._)("p",{class:"text-digit"},"Probabilidade de %",-1);function I(e,n){const t=(0,i.up)("router-link");return(0,i.wg)(),(0,i.iD)("div",W,[(0,i._)("div",z,[Q,(0,i._)("h1",$,(0,U.zw)(e.$route.params.digit),1),Z]),(0,i.Wm)(t,{class:"VoltaDesenharButton",to:{name:"index"}},{default:(0,i.w5)((()=>[(0,i.Uk)("Desenhar de novo")])),_:1})])}const M={},Y=(0,c.Z)(M,[["render",I]]);var q=Y;const H=[{path:"/",name:"index",component:T},{path:"/PredictDigit/:digit",name:"PredictDigit",component:q}],B=(0,f.p7)({history:(0,f.PO)("/"),routes:H});var R=B;(0,o.ri)(l).use(R).mount("#app")}},n={};function t(o){var i=n[o];if(void 0!==i)return i.exports;var r=n[o]={exports:{}};return e[o](r,r.exports,t),r.exports}t.m=e,function(){var e=[];t.O=function(n,o,i,r){if(!o){var a=1/0;for(d=0;d<e.length;d++){o=e[d][0],i=e[d][1],r=e[d][2];for(var s=!0,c=0;c<o.length;c++)(!1&r||a>=r)&&Object.keys(t.O).every((function(e){return t.O[e](o[c])}))?o.splice(c--,1):(s=!1,r<a&&(a=r));if(s){e.splice(d--,1);var u=i();void 0!==u&&(n=u)}}return n}r=r||0;for(var d=e.length;d>0&&e[d-1][2]>r;d--)e[d]=e[d-1];e[d]=[o,i,r]}}(),function(){t.n=function(e){var n=e&&e.__esModule?function(){return e["default"]}:function(){return e};return t.d(n,{a:n}),n}}(),function(){t.d=function(e,n){for(var o in n)t.o(n,o)&&!t.o(e,o)&&Object.defineProperty(e,o,{enumerable:!0,get:n[o]})}}(),function(){t.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){t.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)}}(),function(){var e={143:0};t.O.j=function(n){return 0===e[n]};var n=function(n,o){var i,r,a=o[0],s=o[1],c=o[2],u=0;if(a.some((function(n){return 0!==e[n]}))){for(i in s)t.o(s,i)&&(t.m[i]=s[i]);if(c)var d=c(t)}for(n&&n(o);u<a.length;u++)r=a[u],t.o(e,r)&&e[r]&&e[r][0](),e[r]=0;return t.O(d)},o=self["webpackChunkdigit_recognizer"]=self["webpackChunkdigit_recognizer"]||[];o.forEach(n.bind(null,0)),o.push=n.bind(null,o.push.bind(o))}();var o=t.O(void 0,[998],(function(){return t(6097)}));o=t.O(o)})();
//# sourceMappingURL=app.269ccf39.js.map