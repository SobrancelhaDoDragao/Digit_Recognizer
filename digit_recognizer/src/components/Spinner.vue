<template>

<transition name="slide" mode="out-in">
    <div class="spin-conteiner" v-if="start">

            <div class="lds-dual-ring"><p class="louderMensagem">Carregando</p></div>
    </div>
</transition>

</template>


<style lang="css" scoped>
    
    .spin-conteiner{
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 20;
        width: 100%;
        height: 150%;
        background-color: rgba(255, 255, 255, .80);
        position: fixed;
    }
    .lds-dual-ring {
    display: inline-block;
    }
    .louderMensagem{
    text-align: center;
    font-size: 1.5rem;
    font-weight: bolder;
    }
    .lds-dual-ring:after {
    content: "";
    display: block;
    width: 100px;
    height: 100px;
    border-radius: 50%;
    border: 20px solid #000000;
    border-color: #080808 transparent #000000 transparent;
    animation: lds-dual-ring 1.2s linear infinite;
    }
    @keyframes lds-dual-ring {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
    }

</style>

<script>
   export default{
    props:["start"]
   };
</script>