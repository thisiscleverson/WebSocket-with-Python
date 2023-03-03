const webSocket = new WebSocket("ws://localhost:8765/")

const input   = document.querySelector('.input_name')
const display = document.querySelector('.display')
const button  = document.querySelector('#button')
const displayUsers = document.querySelector('.displayUser')

//enviar informações para o server 
const sendMessage = (userName, valueIncrement) => {
   webSocket.send(JSON.stringify({
      user: userName,
      point: valueIncrement
   }))
}

// quando apertar o botão, soma mais 1 ao valor atual
const increment = () => {
   if(input.value.length > 3){
      input.style.borderColor = 'rgb(85, 86, 87)'

      let increment = Number(display.innerHTML) + 1 
      display.innerHTML = increment
      sendMessage(input.value, increment)
   }else{
      input.style.borderColor = 'red'
   }
}

//ler todas as mensagem que chagam para o usuário
webSocket.addEventListener('message', receive => {
   const data = JSON.parse(receive.data)

   let elementHtml = ''
   for(let i=0; i<data.length; i++){
      elementHtml += `
         <div class='box'>
            <h3>${data[i].user}</h3>
            <span>${data[i].point}</span>
         </div>
      `
   }
   displayUsers.innerHTML = elementHtml
})

input.addEventListener('input', () => {if(input.value.length > 3){input.style.borderColor = 'rgb(85, 86, 87)'}})
button.addEventListener('click', increment)