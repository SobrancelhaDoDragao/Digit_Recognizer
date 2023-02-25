<template>
     
     <div class="container-digit">

        <p class="text-digit">O digito que foi previsto pela IA:</p>
        <h1 class="Digit-Prediction">{{ $route.params.digit }}</h1>
        <p class="text-digit">Probabilidade de 70%</p>

     </div>

     <router-link class='VoltaDesenharButton' :to="{ name:'index' }">Desenha de novo</router-link>
 
</template>

