# 🤖 Análise de Sentimentos com Language Studio no Azure AI

Este repositório corresponde ao Desafio #03 da  [Bootcamp Microsoft - Fundamentos de IA](https://www.dio.me/bootcamp/microsoft-fundamentos-de-ia) e da [Formação Microsoft Azure AI Fundamentals (AI-900)](https://web.dio.me/track/2150f9b5-b06f-4a59-ade6-ab163c24f089) para praticar e aprofundar o uso das ferramentas `Azure Speech Studio` e `Language Studio`, focando na análise de fala e linguagem natural. 

## 📑 Índice
- [Introdução](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2303-Analise-de-Sentimentos-com-Language-Studio-no-Azure-AI#introdu%C3%A7%C3%A3o)
- [Tecnologias Utilizadas]()
- [Desafio do Projeto](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2303-Analise-de-Sentimentos-com-Language-Studio-no-Azure-AI#-desafio-de-projeto)
- [Objetivos](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2303-Analise-de-Sentimentos-com-Language-Studio-no-Azure-AI#%EF%B8%8F-objetivos)  
  - [x] [Pré-requisitos](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2303-Analise-de-Sentimentos-com-Language-Studio-no-Azure-AI#-pr%C3%A9-requisitos)  
  - [x] [Estrutura do Repositório]()
  - [x] [Tecnologias e Ferramentas]()
  - [x] [O que será feito?]()
  - [x] [Passo a Passo](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2303-Analise-de-Sentimentos-com-Language-Studio-no-Azure-AI#-passo-a-passo-an%C3%A1lise-de-sentimentos)  
- [O que é o Language Studio?](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2303-Analise-de-Sentimentos-com-Language-Studio-no-Azure-AI#-o-que-%C3%A9-o-language-studio)  
- [Análise de Sentimento]()  
- [Recursos Adicionais](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2303-Analise-de-Sentimentos-com-Language-Studio-no-Azure-AI#%EF%B8%8F-recursos-adicionais)
- [Créditos]()
- [Autora]()

### ▶️ Introdução
O `Microsoft Azure` é uma plataforma de nuvem que disponibiliza uma variedade de serviços, distribuídos em várias categorias. Este guia foi elaborado para ajudá-lo a navegar pelo portal do Azure e encontrar facilmente os serviços que você precisa.

### 💻 Tecnologias Utilizadas

| Linguagens de Programação | Ferramentas e Tecnologias |
| :-----------------: | :-----------------------: |
| <img height="40" src="https://skillicons.dev/icons?i=py"> | <img height="40" src="https://skillicons.dev/icons?i=github"> <img height="40" src="https://skillicons.dev/icons?i=git"> <img height="40" src="https://skillicons.dev/icons?i=vscode"> <img height="40" src="https://skillicons.dev/icons?i=azure">

### 🎯 Desafio de Projeto
Este repositório apresenta um passo a passo completo para realizar uma Análise de Sentimentos utilizando o `Language Studio` e `Azure Speech Studio`, ferramenta da plataforma Azure AI. Ideal para iniciantes em IA Cognitiva e `Processamento de Linguagem Natural (PLN)`. Neste laboratório o objetivo é praticar e aprofundar o uso das ferramentas `Azure Speech Studio` e `Language Studio`, focando na análise de fala e linguagem natural. 

### 🛠️ Objetivos
O objetivo é desenvolver habilidades práticas na criação de soluções baseadas em inteligência artificial voltadas para voz e linguagem. O entregável é um repositório organizado contendo anotações e insights adquiridos durante a prática, servindo como material de apoio para estudos e futuras implementações.

#### 📌 Pré-requisitos
1. Abra seu navegador e acesse [Portal do Azure](portal.azure.com).
2. Faça login com suas credenciais da Microsoft.
3. Acesse o Language Studio: [Language Studio](https://language.azure.com/)
4. Navegador moderno (recomendado: Edge ou Chrome)

#### 📁 Estrutura do Repositório
```
📂 Desafio#03-Analise-de-Sentimentos-com-Language-Studio-no-Azure-AI/
│
├── 📄 README.md                 # Documento principal com explicação e guia passo a passo
├── 📂 assets/                    # Imagens e recursos visuais usados no README
│    ├── exemplos/
│    │   ├── sentiment-positivo.png
│    │   ├── sentiment-negativo.png
│    │   └── sentiment-neutro.png
│    └── rodape.png
├── 📂 datasets/                  # Arquivos de texto ou datasets usados para teste
│    ├── frases_exemplo.txt
│    └── dataset_sentimentos.csv
├── 📂 notebooks/                 # Notebooks Jupyter para experimentos de análise de sentimentos
│    └── analise_sentimentos.ipynb
├── 📂 scripts/                   # Scripts Python para interação com a API de Linguagem do Azure
│    ├── analise_sentimento_api.py
│    ├── preprocessamento_texto.py
│    └── utils.py
├── 📂 api/                       # Exemplos de integração com a API do Azure Language Service
│    ├── exemplo_requisicao_curl.txt
│    ├── exemplo_python.py
│    └── exemplo_postman_collection.json
├── 📂 docs/                      # Documentos extras e guias complementares
│    ├── guia_language_studio.pdf
│    └── arquitetura_projeto.png
└── 📄 LICENSE                    # Licença do projeto
```
### Ferramentas e Tecnologias:
- Pyton
- JSON
- Azure Language Studio
- Azure Speech Studio
- Azure Portal
- GitHub
- Git
- VS Code
- Jupyter Notebook

#### 🧠 O que será feito?
Neste projeto, você irá:
- Explorar o `Azure Language Studio` para analisar textos e entender o processamento de linguagem natural (PLN).
- Configurar e utilizar a Análise de Sentimentos, identificando se o conteúdo textual apresenta sentimentos positivos, negativos ou neutros.
- Testar diferentes entradas de texto para observar como o modelo classifica emoções e opiniões.
- Visualizar e interpretar os resultados, incluindo scores e representações gráficas de sentimento.
- Registrar aprendizados e insights, criando um repositório de referência para futuras aplicações de IA Cognitiva e PLN.

#### 🚀 Passo a Passo
1. Acesse o `Language Studio`
- Vá para https://language.azure.com/
- Faça login com sua conta Microsoft.
2. Escolha a opção `Análise de Texto`
- Clique em `Explorar todas as capacidades`
- Selecione `Análise de Texto`
- Clique em `Experimentar` ou `Criar projeto`
3. Selecione `Análise de Sentimento`
- Escolha o recurso `Análise de Sentimento` (Sentiment Analysis)
- Configure o idioma (ex: pt para português)
- Insira o texto de exemplo (ex: "Estou muito feliz com esse produto!")
4. Visualize os resultados
- O `Language Studio` vai retornar:
- Score geral de sentimento (positivo, negativo ou neutro)
- Classificação por frase
- Visualização com cores e probabilidades

🧪 Exemplos de Entrada 
```
"Hoje o atendimento foi excelente, estou muito satisfeita!"
"Não gostei do produto, chegou com defeito e demorou muito."
```

✅ Resultados esperados
- Primeira frase → Sentimento Positivo (score próximo de 1.0)
- Segunda frase → Sentimento Negativo (score próximo de 0.0)

### 🧠 O que é o Language Studio?
O Language Studio é uma interface gráfica que permite usar os serviços de linguagem do Azure (Cognitive Services) sem precisar programar. Ele fornece recursos como:

Análise de sentimentos
Extração de entidades
Tradução de texto
Classificação personalizada

### 🤖 Análise de Sentimento
A Análise de Sentimento permite que você compreenda as emoções expressas em textos, classificando-os como positivos, negativos ou neutros. É uma das aplicações práticas de `Processamento de Linguagem Natural` (PLN) e Inteligência Artificial Cognitiva no Azure AI.

## 🗒️ Recursos Adicionais
- [Documentação Oficial do Microsoft Azure](https://docs.microsoft.com/azure)
- [Documentação oficial do Azure AI Language](https://learn.microsoft.com/pt-br/azure/ai-services/language-service/overview)
- [Tutorial: Como usar a Análise de Texto no Language Studio](https://learn.microsoft.com/pt-br/azure/ai-services/language-service/sentiment-opinion-mining/overview)
- [Explore Speech Studio - Laboratório no Microsoft Learning](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/09-speech.html)
- [Analyze text with Language Studio - Laboratório no Microsoft Learning](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/06-text-analysis.html)

## 🔗 Créditos
Este guia serve como repositório de estudos, desafios e projetos da [Bootcamp Microsoft - Fundamentos de IA](https://www.dio.me/bootcamp/microsoft-fundamentos-de-ia) e da [Formação Microsoft Azure AI Fundamentals (AI-900)](https://web.dio.me/track/2150f9b5-b06f-4a59-ade6-ab163c24f089), para availar o ensinado sobre pratica e aprofundamento do uso das ferramentas `Azure Speech Studio` e `Language Studio`, focando na análise de fala e linguagem natural.

*Nota: Este projeto é apenas para fins educacionais e não possui nenhuma afiliação oficial com a franquia DIO ou suas empresas associadas.*

## 👩🏼‍💻 Autora:
<table style="border=0">
  <tr>
    <td align="left">
      <a href="https://github.com/rhayssakramer">
        <span><b>Rhayssa Kramer</b></span>
      </a>
      <br>
      <span>Sr. Assoc, Full-Stack Development</span>
    </td>
  </tr>
</table>

<div align="center"><a href="https://github.com/rhayssakramer"><img src="https://github.com/rhayssakramer/rhayssakramer/blob/main/img/rodape.png"></a></div>