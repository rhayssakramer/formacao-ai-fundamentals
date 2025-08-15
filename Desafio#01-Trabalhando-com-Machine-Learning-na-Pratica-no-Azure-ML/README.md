# 🤖 Trabalhando com Machine Learning na Prática no Azure ML

Este repositório corresponde ao Desafio #01 da [Bootcamp Microsoft - Fundamentos de IA](https://www.dio.me/bootcamp/microsoft-fundamentos-de-ia) e da [Formação Microsoft Azure AI Fundamentals (AI-900)](https://web.dio.me/track/2150f9b5-b06f-4a59-ade6-ab163c24f089) para aprender a criar nossa conta no Azure e explorar as capacidades de `Machine Learning` da plataforma para desenvolver nossa primeira automação prática. Ao aplicar implementações e soluções escaláveis de aprendizado de máquina na nuvem da Microsoft, adquiriremos conhecimentos valiosos e experiência na construção de soluções eficientes. 

## 📑 Índice
- [Introdução](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2301-Trabalhando-com-Machine-Learning-na-Pratica-no-Azure-ML#introdu%C3%A7%C3%A3o)
- [Tecnologias Utilizadas]()
- [Desafio de Projeto](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2301-Trabalhando-com-Machine-Learning-na-Pratica-no-Azure-ML#-desafio-de-projeto)
- [Objetivos](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2301-Trabalhando-com-Machine-Learning-na-Pratica-no-Azure-ML#%EF%B8%8F-objetivos)
  - [x] [Pré-requisitos](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2301-Trabalhando-com-Machine-Learning-na-Pratica-no-Azure-ML#-pr%C3%A9-requisitos)
  - [x] [Estrutura do Repositório]()
  - [x] [Ferramentas e Tecnologias]()
  - [x] [O que será feito?](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2301-Trabalhando-com-Machine-Learning-na-Pratica-no-Azure-ML#-o-que-ser%C3%A1-feito)
  - [x] [Passo a Passo](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2301-Trabalhando-com-Machine-Learning-na-Pratica-no-Azure-ML#-passo-a-passo)
- [Modelo de Uso](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2301-Trabalhando-com-Machine-Learning-na-Pratica-no-Azure-ML#-modelo-de-uso)  
  - [x] [Etapa 1: Preparar os dados]()
  - [x] [Etapa 2: Criar a tarefa no Azure AutoML]()
  - [x] [Etapa 3: Configurar o experimento]()
  - [x] [Etapa 4: Executar o AutoML]()
  - [x] [Etapa 5: Publicar o modelo como um endpoint]()
  - [x] [Etapa 6: Fazer previsões com o modelo implantado]()
  - [x] [Casos de Uso](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2301-Trabalhando-com-Machine-Learning-na-Pratica-no-Azure-ML#-casos-de-uso)
- [O que é JSON?](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2301-Trabalhando-com-Machine-Learning-na-Pratica-no-Azure-ML#-o-que-%C3%A9-json) 
  - [x] [Entendendo o JSON:]()
  - [x] [Explicando com analogia]()
- [Casos de Uso](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2301-Trabalhando-com-Machine-Learning-na-Pratica-no-Azure-ML#-casos-de-uso)
- [Dica Extra](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2301-Trabalhando-com-Machine-Learning-na-Pratica-no-Azure-ML#-dica-extra)  
- [Recursos Adicionais](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2301-Trabalhando-com-Machine-Learning-na-Pratica-no-Azure-ML#-dica-extra)
- [Créditos]()
- [Autora]()

### ▶️ Introdução
O `Microsoft Azure` é uma plataforma de nuvem que disponibiliza uma variedade de serviços, distribuídos em várias categorias. Este guia foi elaborado para ajudá-lo a navegar pelo portal do Azure e encontrar facilmente os serviços que você precisa.

### 💻 Tecnologias Utilizadas

| Linguagens de Programação | Ferramentas e Tecnologias |
| :-----------------: | :-----------------------: |
| <img height="40" src="https://skillicons.dev/icons?i=py"> | <img height="40" src="https://skillicons.dev/icons?i=github"> <img height="40" src="https://skillicons.dev/icons?i=git"> <img height="40" src="https://skillicons.dev/icons?i=vscode"> <img height="40" src="https://skillicons.dev/icons?i=azure">

### 🎯 Desafio de Projeto
Este projeto apresenta um guia prático para construção e implantação de modelos de `Machine Learning` (ML) usando a plataforma `Azure Machine Learning Studio`. Ideal para quem quer explorar AutoML, criar pipelines e publicar modelos como API de forma acessível e sem precisar programar tudo do zero.

### 🛠️ Objetivos
O objetivo é aprender a criar nossa conta no Azure e explorar as capacidades de Machine Learning da plataforma para desenvolver nossa primeira automação prática. Ao aplicar implementações e soluções escaláveis de aprendizado de máquina na nuvem da Microsoft, adquiriremos conhecimentos valiosos e experiência na construção de soluções eficientes.

#### 📌 Pré-requisitos
1. Abrir seu navegador e acessar [Portal do Azure](portal.azure.com).
2. Fazer login com suas credenciais da Microsoft.
3. Acesse o [Azure Machine Learning Studio](https://ml.azure.com/)
4. Um dataset disponível para upload (CSV, Excel, ou JSON)

#### 📁 Estrutura do Repositório
```
📂 nome-do-repositorio/
│
├── 📄 README.md                 # Descrição completa do projeto (modelo detalhado que você enviou)
├── 📂 assets/                    # Imagens, ícones e recursos visuais usados no README
│    ├── img1.png
│    ├── img2.png
│    └── rodape.png
├── 📂 datasets/                  # Arquivos de dados (.csv, .xlsx, .json) usados nos exemplos
│    ├── dataset-exemplo.csv
│    └── dataset-teste.json
├── 📂 notebooks/                 # Jupyter Notebooks com scripts e experimentos
│    ├── analise-inicial.ipynb
│    ├── treino-automl.ipynb
│    └── avaliacao-modelo.ipynb
├── 📂 scripts/                   # Códigos Python ou outra linguagem para automação
│    ├── preprocessamento.py
│    ├── previsao_api.py
│    └── utils.py
├── 📂 docs/                      # Documentos extras (PDFs, guias, relatórios)
│    ├── guia_azure_ml.pdf
│    └── passo_a_passo.pdf
├── 📂 models/                    # Modelos treinados exportados
│    ├── modelo-produtos.pkl
│    └── modelo-vendas.pkl
├── 📂 api/                       # Exemplos de integração com API do Azure
│    ├── exemplo_curl.txt
│    ├── exemplo_python.py
│    └── exemplo_postman.json
└── 📄 LICENSE                    # Licença do projeto (MIT, Apache 2.0, etc.)
```

#### 🛠️ Ferramentas e Tecnologias
- Python
- JSON
- Azure Machine Learning Studio
- Azure AutoML
- Azure Portal
- GitHub
- Git
- VS Code
- Jupyter Notebook

#### 🧠 O que será feito?
O `Azure Machine Learning Studio` (ML Studio) é um ambiente de desenvolvimento completo na nuvem que permite:
1. Criar modelos de ML com código ou no estilo "arrastar e soltar"
2. Utilizar AutoML para treinar modelos automaticamente
3. Avaliar e comparar modelos
4. Implantar como serviço web

#### 🚀 Passo a Passo
1. Acesse o `Azure ML Studio`
- Link: https://ml.azure.com
- Faça login com sua conta Microsoft
2. Crie um Workspace
- No portal Azure, vá em `Criar um recurso`
- Procure por `Machine Learning`
- Preencha as informações e crie o Workspace
3. Faça Upload do Dataset
- Acesse o `ML Studio`
- Vá até `Datasets` > + `Create Dataset`
- Escolha From local files
- Dê um nome, defina os tipos de coluna e finalize
>Exemplo de dataset: previsão de churn, previsão de preços, saúde, vendas etc.
4. Use o AutoML (Machine Learning Automático)
- Vá até `Automated ML`
- Clique em + `New automated ML` run
- Selecione o dataset que você enviou
- Escolha:
  - Tipo de experimento (Classificação, Regressão ou Séries Temporais)
  - Variável alvo (coluna que será prevista)
- Configure os parâmetros e execute
5. Avalie os Resultados
- Após a execução, acesse a aba de métricas:
  - Acurácia
  - AUC
  - RMSE (se regressão)
- Compare os modelos e visualize as explicações (interpretabilidade)
6. Implante o Modelo como Web Service
- Selecione o melhor modelo
- Clique em `Deploy`
- Escolha `Real-time Endpoint`
- Após a implantação, você terá:
  - URL do endpoint
  - Chave de acesso para autenticação
  - Documentação com exemplo de uso via API
**Exemplo de Requisição para Previsão via API**
```
curl -X POST https://<seu-endpoint>.azurewebsites.net/score \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <sua-chave>" \
-d '{"data": [{"idade": 25, "salario": 4000, "cidade": "Recife"}]}'
```

### 🔧 Modelo de Uso

#### 📁 Etapa 1: Preparar os dados
Utilize o arquivo .csv, que contém 60 exemplos sintéticos com a seguinte estrutura:
| Categoria   | Peso (kg) | Volume (ml) | Marca    | Preço (R$) |
|-------------|-----------|-------------|----------|------------|
|             |           |             |          |            |
|             |           |             |          |            |
|             |           |        |    |          |            |


#### 🧠 Etapa 2: Criar a tarefa no Azure AutoML
1. Acesse: https://ml.azure.com
2. Entre no seu Workspace de Machine Learning
3. Vá até o menu Automated ML
4. Clique em + New Automated ML run
5. Envie o arquivo .csv
6. Marque a opção de que o arquivo tem cabeçalho

#### ⚙️ Etapa 3: Configurar o experimento
- Nome do experimento: 
- Coluna alvo: 
- Tipo de tarefa: Regressão

**Ajuste de validação cruzada**
Na aba Validation (Validação):
- Validation type → K-Fold cross validation
- Number of cross validations (folds) → 3

Com 60 registros, usar 3 divisões já garante robustez sem perda de dados.

#### ⏳ Etapa 4: Executar o AutoML
- O Azure AutoML testará diversos algoritmos automaticamente
- Ao final da execução, será exibida uma lista com os modelos testados
- Escolha o modelo com menor erro (como RMSE ou MAE)

#### 🌐 Etapa 5: Publicar o modelo como um endpoint
1. Clique no melhor modelo e selecione Deploy
2. Dê um nome ao serviço, como modelo-produtos
3. Clique em Deploy

#### ✅ Etapa 6: Fazer previsões com o modelo implantado
🖱️ Testar diretamente no portal
1. Vá até Endpoints
2. Selecione modelo-produtos
3. Acesse a aba Test
4. Insira o seguinte conteúdo:
```
{
  "data": [
    {
      "Categoria": "",
      "Peso": ,
      "Volume": ,
      "Marca": ""
    }
  ]
}
```
5. Clique em Run inference para ver o resultado da previsão.

### 🧱 O que é JSON?
JSON (JavaScript Object Notation) é uma forma de representar dados estruturados, como se fosse uma ficha de cadastro que o computador entende.

🛍️ Exemplo real: produto para prever o preço
Suponha que você queira prever o preço de:
- Categoria: 
- Peso: 
- Volume: 
- Marca: 

No formato JSON:
```
{
  "data": [
    {
      "Categoria": "",
      "Peso": ,
      "Volume": ,
      "Marca": ""
    }
  ]
}
```

#### 🧩 Entendendo o JSON:
| Parte                     | Significado                         |
|---------------------------|-------------------------------------|
| `{ ... }`                 | Um bloco de dados                   |
| `"data"`                  | Campo principal contendo os dados  |
| `[ ... ]`                 | Lista de um ou mais exemplos        |
| `{ "Categoria": ..., ... }` | Um item com suas características |

#### 👩‍💻 Explicando com analogia
>

### 💡 Casos de Uso
- Previsão de evasão de clientes (Churn)
- Diagnóstico de doenças
- Previsão de vendas
- Análise de risco de crédito

### 🤝 Dica Extra
Você pode usar Jupyter Notebooks integrados ao Azure ML Studio para customizar seus modelos com Python, além de reutilizar o modelo treinado com AutoML em pipelines mais avançados.

## 🗒️ Recursos Adicionais
- [Documentação Oficial do Microsoft Azure](https://docs.microsoft.com/azure)
- [Documentação do Azure ML](https://learn.microsoft.com/pt-br/azure/machine-learning/)
- [Introdução ao AutoML no Azure](https://learn.microsoft.com/pt-br/azure/machine-learning/concept-automated-ml)

## 🔗 Créditos
Este guia serve como repositório de estudos, desafios e projetos da [Bootcamp Microsoft - Fundamentos de IA](https://www.dio.me/bootcamp/microsoft-fundamentos-de-ia) e da [Formação Microsoft Azure AI Fundamentals (AI-900)](https://web.dio.me/track/2150f9b5-b06f-4a59-ade6-ab163c24f089), para avaliar o ensinado sobre criar nossa conta no Azure e explorar as capacidades de `Machine Learning` da plataforma para desenvolver nossa primeira automação prática.

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
