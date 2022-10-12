async function verlivros(){
    const response = await axios.get('http://127.0.0.1:8000/livros/api/')
    const livros = response.data
    const lista = document.getElementById('lista')

    lista.innerHTML = ''

    livros.forEach(livro =>{
        const item = document.createElement('li')
        const dados = `Titulo: ${livro.titulo} Autor: ${livro.autor}`
        item.innerText = dados
        lista.appendChild(item)
        

    })
}

async function post_to_api() {
    document.addEventListener("DOMContentLoaded", function(event){    
    const form_animal = document.getElementById("formulario")
    const input_titulo = document.getElementById('titulo')
    const input_autor = document.getElementById('autor')

    form_animal.onsubmit = async (event) => {
        event.preventDefault()
        alert(`Criar ${input_titulo.value} ${input_autor.value}`)

        await axios.post('http://127.0.0.1:8000/livros/api',
        {
            titulo: input_titulo.value,
            autor:input_autor.value
        }
        )
    }
})
}

function app(){
    console.log("teste")
    verlivros()
    post_to_api()
}

app()