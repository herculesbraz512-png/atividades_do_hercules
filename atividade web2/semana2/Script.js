const form= document.getElementById("formgasto");
const campoDescricao= document.getElementById("descricao");
const campoValor= document.getElementById("valor");
const campoCategoria= document.getElementById("categorias");
const mensagem= document.getElementById("mensagem");
const totalGeral= document.getElementById("totalgeral");
const vazio= document.getElementById("vazio");
const listaGastos= document.getElementById("listagasto");
const campoCategoria= document.getElementById("orcamento");
const avisoOrcamento= document.getElementById("avisoorcamento");
const filtroCategoria= document.getElementById("filtrocategoria");
const blocoTotal= totalGeral.parentElement;

const botaoLinpar= document.getElementById("limpartudo");


const nomesCategorias= {
alimentacao: "alimentacao",
transporte: "transporte",
lazer: "lazer",
estudos: "estudos",
outros: "outros",
saude: "saude",
}

let gastos = JSON.parse(localStorage.getItem("gastos")) ?? [];
let orcamento = Number(localStorage.getItem("orcamento")) || 0;

function formatar(valor) {
  return valor.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
}

function mostrarMensagem(texto, tipo) {
  mensagem.textContent = texto;
  mensagem.className = "mensagem";
  if (tipo) {
    mensagem.classList.add(tipo);
  }
}

function salvar() {
  localStorage.setItem("gastos", JSON.stringify(gastos));
}

function validar(descricao, textoValor, categoria) {
  if (descricao === "") {
    return "informe a descricao do gasto.";
  }
  if (textoValor === "" || Number.isNaN(Number(textoValor))) {
    return "informe um valor numerico.";
  }
  if (Number(textoValor) <= 0) {
    return "o valor deve ser maior que zero.";
  }
  if (categoria === "") {
    return "selecione uma categoria.";
  }
  return "";
}

function criarLinha(gasto) {
  const tr = document.createElement("tr");
  tr.dataset.id = gasto.id;

  const tdDescricao = document.createElement("td");
  tdDescricao.textContent = gasto.descricao;

  const tdCategoria = document.createElement("td");
  const badge = document.createElement("span");
  badge.classList.add("badge", gasto.categoria);
  badge.textContent = nomesCategorias[gasto.categoria];
  tdCategoria.appendChild(badge);

  const tdValor = document.createElement("td");
  tdValor.classList.add("valor");
  tdValor.textContent = formatar(gasto.valor);

  const tdAcao = document.createElement("td");
  const botao = document.createElement("button");
  botao.type = "button";
  botao.classList.add("remover");
  botao.setAttribute("aria-label", "Remover " + gasto.descricao);
  botao.textContent = "Remover";
  tdAcao.appendChild(botao);

  tr.appendChild(tdDescricao);
  tr.appendChild(tdCategoria);
  tr.appendChild(tdValor);
  tr.appendChild(tdAcao);
  return tr;
}

function atualizarResumo() {
  const totais = {};
  for (const categoria in nomesCategorias) {
    totais[categoria] = 0;
  }

  let geral = 0;
  for (const gasto of gastos) {
    totais[gasto.categoria] += gasto.valor;
    geral += gasto.valor;
  }

  totalGeral.textContent = formatar(geral);
  for (const categoria in totais) {
    document.getElementById("total-" + categoria).textContent = formatar(totais[categoria]);
  }

   if (orcamento > 0 && geral > orcamento) {
    blocoTotal.classList.add("estourou");
    avisoOrcamento.textContent = "atencao: voce ultrapassou o orcamento em " + formatar(geral - orcamento) + ".";
  } else {
    blocoTotal.classList.remove("estourou");
    avisoOrcamento.textContent = "";
  }
}

function renderizar() {
  listaGastos.textContent = "";

  const filtro = filtroCategoria.value;
  for (const gasto of gastos) {
    if (filtro === "" || gasto.categoria === filtro) {
      listaGastos.appendChild(criarLinha(gasto));
    }
  }

  vazio.classList.toggle("oculto", listaGastos.children.length > 0);
  atualizarResumo();
}

form.addEventListener("submit", function (evento) {
  evento.preventDefault();

  const descricao = campoDescricao.value.trim();
  const textoValor = campoValor.value;
  const categoria = campoCategoria.value;

  const problema = validar(descricao, textoValor, categoria);
  if (problema !== "") {
    mostrarMensagem(problema, "erro");
    return;
  }

  gastos.push({
    id: Date.now(),
    descricao: descricao,
    valor: Math.round(Number(textoValor) * 100) / 100,
    categoria: categoria,
  });

  salvar();
  renderizar();
  form.reset();
  campoDescricao.focus();
  mostrarMensagem("gasto adicionado com sucesso!", "sucesso");
});

listaGastos.addEventListener("click", function (evento) {
  const botao = evento.target.closest(".remover");
  if (!botao) {
    return;
  }

  const id = Number(botao.closest("tr").dataset.id);
  gastos = gastos.filter(function (gasto) {
    return gasto.id !== id;
  });

  salvar();
  renderizar();
});

filtroCategoria.addEventListener("change", renderizar);

campoOrcamento.addEventListener("input", function () {
  orcamento = Number(campoOrcamento.value) || 0;
  localStorage.setItem("orcamento", orcamento);
  atualizarResumo();
});
function ordenargastos(){
gastos.sort(function(a, b) {retorn b.valor - a,valor;
})
}

if (orcamento > 0) {
  campoOrcamento.value = orcamento;
}
renderizar();