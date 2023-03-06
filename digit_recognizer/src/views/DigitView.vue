<template>
     
     <div class="container-digit">

        <p class="text-digit">O digito que foi previsto pela IA:</p>
        <h1 class="Digit-Prediction">{{ $route.params.digit }}</h1>
        <p class="text-digit">Probabilidade de %</p>

     </div>
     <router-link class='VoltaDesenharButton' :to="{ name:'index' }">Desenhar de novo</router-link>

</template>

