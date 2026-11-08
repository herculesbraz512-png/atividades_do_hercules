const formulario = document.getElementById("formBusca");
const campoBusca = document.getElementById("nomePokemon");
const mensagem = document.getElementById("mensagem");
const resultado = document.getElementById("resultado");

async function buscarPokemon(nome) {
    mensagem.textContent = "Carregando...";
    resultado.replaceChildren();
    try {
        const resposta = await fetch(`https://pokeapi.co/api/v2/pokemon/${nome}`);
        if (!resposta.ok) {
            throw new Error("Pokemon não encontrado");
        }
        const pokemon = await resposta.json();
        mostrarPokemon(pokemon);
        mensagem.textContent = "";
    } catch (erro) {
        mensagem.textContent = erro.message.includes("Pokemon não encontrado")
            ? erro.message
            : "Não foi possível carregar. tente novamente.";
    }
}

function criarInformacao(rotulo, valor) {
    const bloco = document.createElement("div");
    bloco.classList.add("informacao");
    const titulo = document.createElement("strong");
    titulo.textContent = rotulo;
    const texto = document.createElement("span");
    texto.textContent = valor;
    bloco.appendChild(titulo);
    bloco.appendChild(texto);
    return bloco;
}

function mostrarPokemon(pokemon) {
    const imagem = document.createElement("img");
    imagem.src = pokemon.sprites.front_default || "";
    imagem.alt = `Imagem de ${pokemon.name}`;
    const numero = document.createElement("p");
    numero.classList.add("numero");
    numero.textContent = `Nº ${pokemon.id}`;
    const nome = document.createElement("h2");
    nome.textContent = pokemon.name;

    const tipos = pokemon.types.map(item => item.type.name).join(", ");
    const altura = (pokemon.height / 10).toFixed(1) + " m";
    const peso = (pokemon.weight / 10).toFixed(1) + " kg";
    const informacoes = document.createElement("div");

    informacoes.classList.add("informacoes");
    informacoes.appendChild(criarInformacao("Tipo", tipos));
    informacoes.appendChild(criarInformacao("Altura", altura));
    informacoes.appendChild(criarInformacao("Peso", peso));

    resultado.appendChild(imagem);
    resultado.appendChild(numero);
    resultado.appendChild(nome);
    resultado.appendChild(informacoes);
}

formulario.addEventListener("submit", function(evento) {
    evento.preventDefault();
    const nome = campoBusca.value.trim().toLowerCase();
    if (nome === "") {
        mensagem.textContent = "Digite o nome do Pokemon.";
        resultado.replaceChildren();
        return;
    }
    buscarPokemon(nome);
});

buscarPokemon("beedrill");
