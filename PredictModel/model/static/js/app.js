const { createApp } = Vue

createApp({
  data() {
      return {
   
      }
    },
    template: `<a href="" @click.prevent="salvarCanvas" id="btnSalvar" class="BotaoComum">Pronto</a>`,
     
    methods: {

        salvarCanvas() {
            // Obtém o elemento canvas
            const canvas = document.querySelector("canvas");
          
            // Obtém o objeto de contexto do canvas
            const ctx = canvas.getContext('2d');
        
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        
            // Cria um novo objeto FormData e adiciona o valor da imagem 
            const formData = new FormData();
            
            DataUrl = canvas.toDataURL('image/png')
        
             // Enviar o DataURL para o servidor usando Fetch
            fetch('/SalvarImagem', {
                method: 'POST',
                headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({data_url: DataUrl}),
            })
            .then(response => {
                console.log('Sucesso!');
                
                sizeCanvas();
            })
            .catch(error => {
                console.error('Erro:', error);
            });

           
        },

        sizeCanvas(){
    
            container = document.querySelector(".containerQuadro")
        
            canvas.width = container.clientWidth;
            canvas.height = container.clientHeight;
        },

      },
}).mount('#app')

