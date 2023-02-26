<template>
    
        <p class="explicao" >Desenhe um numero de apenas um digito e clique em “pronto” e o algoritmo de IA irá dizer qual numero é.</p>     
        <Quadro/>
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