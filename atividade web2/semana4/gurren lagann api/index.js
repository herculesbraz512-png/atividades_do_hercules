const express = require('express');
    
const app = express();
const PORT = 3000;

const personagens = [
    {
        id: 1,
        nome: "Simon",
        categoria: "protagonista",
        habilidade: "Manipulação de energia espiral",
        funcao: "Piloto do Gurren Lagann"
    },
    {
        id: 2,
        nome: "Kamina",
        categoria: "aliado",
        habilidade: "Determinação e liderança",
        funcao: "Fundador da Brigada Gurren"
    },
    {
        id: 3,
        nome: "Yoko Littner",
        categoria: "aliado",
        habilidade: "Precisão com rifles",
        funcao: "Atiradora da equipe"
    },
    {
        id: 4,
        nome: "Nia Teppelin",
        categoria: "aliado",
        habilidade: "Comunicação e liderança",
        funcao: "Aliada de Simon"
    },
    {
        id: 5,
        nome: "Viral",
        categoria: "antagonista",
        habilidade: "Combate e pilotagem",
        funcao: "Guerreiro homem-fera"
    },
    {
        id: 6,
        nome: "Lordgenome",
        categoria: "antagonista",
        habilidade: "Força e experiência em batalha",
        funcao: "Rei Espiral"
    },
    {
        id: 7,
        nome: "Rossiu Adai",
        categoria: "aliado",
        habilidade: "Estratégia e administração",
        funcao: "Líder político"
    },
    {
        id: 8,
        nome: "Kittan Bachika",
        categoria: "aliado",
        habilidade: "Combate e pilotagem",
        funcao: "Líder dos Black Siblings"
    },
    {
        id: 9,
        nome: "Leeron Littner",
        categoria: "aliado",
        habilidade: "Engenharia e tecnologia",
        funcao: "Mecânico e cientista"
    },
    {
        id: 10,
        nome: "Boota",
        categoria: "mascote",
        habilidade: "Lealdade e coragem",
        funcao: "mascote do grupo"
    }
];

app.use((req, res, next) => {
    const horario = new Date().toLocaleString('pt-BR');
    console.log(
        `[${horario}] ${req.method} ${req.url}`
    );
    next();
});

app.get('/', (req, res) => {
    res.status(200).json({
        mensagem: "bem vindo a Gurren Lagann api",
        descricao: "api de personagens do anime Gurren Lagann"
    });
});

app.get('/personagens/total', (req, res) => {
    res.status(200).json({
        total: personagens.length
    });
});

app.get('/personagens', (req, res) => {
    let resultado = [...personagens];
    const categoria = req.query.categoria;
    const limite = req.query.limite;

    if (categoria) {
        resultado = resultado.filter(personagem =>
            personagem.categoria.toLowerCase() === categoria.toLowerCase()
        );
    }

    if (limite !== undefined) {
        const numeroLimite = parseInt(limite);

        if (isNaN(numeroLimite) || numeroLimite < 0) {
            return res.status(400).json({
                erro: "o limite deve ser um numero valido"
            });
        }
        resultado = resultado.slice(0, numeroLimite);
    }
    res.status(200).json(resultado);
});

app.get('/personagens/:id', (req, res) => {
    const id = parseInt(req.params.id);

    if (isNaN(id)) {
        return res.status(400).json({
            erro: "o id precisa ser um numero"
        });
    }

    const personagem = personagens.find(p => p.id === id);

    if (!personagem) {
        return res.status(404).json({
            erro: "personagem não encontrado"
        });
    }
    res.status(200).json(personagem);
});

app.listen(PORT, () => {
    console.log(`servidor rodando em http://localhost:${PORT}`);
});
