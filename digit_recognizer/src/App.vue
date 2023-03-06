<template>
 
    <h1 class="TituloPrincipal">Digit Recognizer</h1>
    <!-- Aqui onde será renderizado as páginas -->

    <router-view v-slot="{ Component }">
        <transition name="slide" mode="out-in">
            <component :is="Component" :key="$route.path" ></component>
        </transition>
    </router-view>


    <footer>Desenvolvido por <a href="https://github.com/SobrancelhaDoDragao" target="_blank" >Eudson Durães</a></footer>
   
</template>



<script></script>
