<template>
   
        <div class="containerQuadro" ref="containerQuadro" >

            <canvas ref="canvas" id="quadro"></canvas>
                    
        </div>
            
        <router-link @click.prevent="salvarCanvas" class='BotaoComum' to="">Pronto</router-link>

        
        <Spinner :start="spin" />
      
</template>


<script>
import Spinner from '@/components/Spinner.vue'

    export default {
        name: 'Quadro',
        components: {
            Spinner        
        },

        data(){
            return{
                spin:false,
            }
        },

        methods:{

            async salvarCanvas() {
            //Ativando o louder
            this.spin = true
            // Obtém o elemento canvas
            const canvas = this.$refs.canvas;
            
            // Obtém o objeto de contexto do canvas
            const ctx = canvas.getContext('2d');
             
            
            let DataUrl = canvas.toDataURL('image/png')

            // Enviar o DataURL(Binário da imagem) para o servidor usando Fetch    
            const reponse = await fetch('https://digitrecognizer.up.railway.app/PredictDigit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({'data_url': DataUrl}),
            });
            //Pegando resposta do modelo de IA
            var dado = await reponse.json();

            //Desativando o louder
            this.spin = false;

            //Quadro não foi desenhado
            if(dado.digit == 'Error'){
               alert("O Quadro não foi desenhado");
            }
            else{
            //Redirect
            this.$router.push(`/PredictDigit/${dado.digit}`);
            }
            
        },

        async GetToken(){

            const response = await fetch('https://digitrecognizer.up.railway.app/get_csrf');
             
            let dado = await response.json();

            let csrfToken = await dado.csrf_token;

            return csrfToken;

        }
    },
        mounted() {

            let penSize = 5
            let isDrawing;
            let x;
            let y;
            
            const canvas = this.$refs.canvas;
            const c = canvas.getContext("2d");
            const container = this.$refs.containerQuadro;

            const sizeCanvas = () => {
                canvas.width = container.clientWidth;
                canvas.height = container.clientHeight;
            }

            sizeCanvas();
            
            window.addEventListener('resize',sizeCanvas);
            
            canvas.addEventListener("mousedown",(e)=>{
                isDrawing = true;
                x = e.offsetX;
                y = e.offsetY;
            });
            
            canvas.addEventListener("mouseup",()=>{
            isDrawing = false;
            x = undefined;
            y = undefined;
            })
            
            canvas.addEventListener("mousemove",(event)=>{
            draw(event.offsetX,event.offsetY)
            })
            
            c.fillStyle = "black"
            c.strokeStyle = c.fillStyle
            
            function draw(x2,y2){
            if(isDrawing){
                c.beginPath();
                c.arc(x2,y2,penSize,0,Math.PI * 2);
                c.closePath();
                c.fill();
            
                //draw line
                drawLine(x,y,x2,y2);
            }
            
            x = x2;
            y = y2;
            }
            
            function drawLine(x1,y1,x2,y2){
            c.beginPath();
            c.moveTo(x1,y1);
            c.lineTo(x2,y2);
            c.strokeStyle = c.fillStyle;
            c.lineWidth = penSize * 2;
            c.stroke();
            }
        },

        beforeUnmount(){
            //Removendo todos os linstener para poupar memoria
            window.removeEventListener('resize', this.sizeCanvas);
            window.removeEventListener('mousedown', this.canvas);
            window.removeEventListener('mouseup', this.canvas);
            window.removeEventListener('mousemove', this.canvas);
        }
        
    }

</script>
