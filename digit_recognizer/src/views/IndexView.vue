<template>
    <div class="animacaoDiv">
        <p class="explicao">Desenhe um número de <b>0</b> a <b>9</b>, a inteligência artificial tentará reconhecer o numero desenhado.</p>     
        <Quadro/>
    </div>
</template>

<script>
import Quadro from '@/components/Quadro.vue'

    export default {
        name: 'IndexView',
        components: {
            Quadro,            
        }
    }
</script>