# 🤖 Azure Cognitive Search: Utilizando AI Search para indexação e consulta de Dados

Este repositório corresponde ao Desafio #04 da  [Bootcamp Microsoft - Fundamentos de IA](https://www.dio.me/bootcamp/microsoft-fundamentos-de-ia) e da [Formação Microsoft Azure AI Fundamentals (AI-900)](https://web.dio.me/track/2150f9b5-b06f-4a59-ade6-ab163c24f089) para aplicar técnicas de organização e pesquisa de documentos por meio da ingestão de dados e indexação utilizando ferramentas de inteligência artificial.

## 📑 Índice
- [Introdução](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2304-Azure-Cognitive-%20Search-Utilizando-AI-Search-para-indexa%C3%A7%C3%A3o-e-consulta-de-Dados#%EF%B8%8F-introdu%C3%A7%C3%A3o)
- [Tecnologias Utilizadas]()
- [Desafio do Projeto](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2304-Azure-Cognitive-%20Search-Utilizando-AI-Search-para-indexa%C3%A7%C3%A3o-e-consulta-de-Dados#-desafio-de-projeto)
- [Objetivos](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2304-Azure-Cognitive-%20Search-Utilizando-AI-Search-para-indexa%C3%A7%C3%A3o-e-consulta-de-Dados#%EF%B8%8F-objetivos)  
  - [x] [Pré-requisitos](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2304-Azure-Cognitive-%20Search-Utilizando-AI-Search-para-indexa%C3%A7%C3%A3o-e-consulta-de-Dados#-pr%C3%A9-requisitos)  
  - [x] [Estrutura do Repositório]()
  - [x] [Ferramentas e Tecnologias](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2304-Azure-Cognitive-%20Search-Utilizando-AI-Search-para-indexa%C3%A7%C3%A3o-e-consulta-de-Dados#%EF%B8%8F-ferramentas-e-tecnologias) 
  - [x] [O que será feito?]()
  - [x] [Passo a Passo]()
- [Sobre o Azure Cognitive Search](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2304-Azure-Cognitive-%20Search-Utilizando-AI-Search-para-indexa%C3%A7%C3%A3o-e-consulta-de-Dados#-sobre-o-azure-cognitive-search)  
  - [x] [Etapas Realizadas](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2304-Azure-Cognitive-%20Search-Utilizando-AI-Search-para-indexa%C3%A7%C3%A3o-e-consulta-de-Dados#%EF%B8%8F-etapas-realizadas)   
- [Insights Obtidos](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2304-Azure-Cognitive-%20Search-Utilizando-AI-Search-para-indexa%C3%A7%C3%A3o-e-consulta-de-Dados#-insights-obtidos)   
- [Recursos Adicionais](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2304-Azure-Cognitive-%20Search-Utilizando-AI-Search-para-indexa%C3%A7%C3%A3o-e-consulta-de-Dados#%EF%B8%8F-recursos-adicionais)
- [Créditos]()
- [Autora]()

### ▶️ Introdução
O `Microsoft Azure` é uma plataforma de nuvem que disponibiliza uma variedade de serviços, distribuídos em várias categorias. Este guia foi elaborado para ajudá-lo a navegar pelo portal do Azure e encontrar facilmente os serviços que você precisa.

### 💻 Tecnologias Utilizadas

| Linguagens de Programação | Ferramentas e Tecnologias |
| :-----------------: | :-----------------------: |
| <img height="40" src="https://skillicons.dev/icons?i=py"> | <img height="40" src="https://skillicons.dev/icons?i=github"> <img height="40" src="https://skillicons.dev/icons?i=git"> <img height="40" src="https://skillicons.dev/icons?i=vscode"> <img height="40" src="https://skillicons.dev/icons?i=azure"> |

### 🎯 Desafio de Projeto
Este desafio tem como objetivo aplicar técnicas de organização e pesquisa de documentos por meio da ingestão de dados e indexação utilizando ferramentas de inteligência artificial. Durante as aulas, foram abordados três passos principais: ingestão de conteúdo para IA, criação de índices inteligentes e exploração prática dos dados organizados. O foco está em desenvolver uma compreensão sólida sobre como essas ferramentas podem ser utilizadas para minerar e extrair conhecimento de grandes volumes de informação. Como entregável, espera-se um repositório estruturado contendo registros das etapas realizadas e insights obtidos ao longo da prática.

### 🛠️ Objetivos
Durante a prática, seguimos três etapas principais:
1. **Ingestão de conteúdo para IA**
2. **Criação de índices inteligentes**
3. **Exploração prática dos dados organizados**

O objetivo é compreender como ferramentas cognitivas podem ser aplicadas para **minerar, indexar e extrair conhecimento** de grandes volumes de informação.

#### 📌 Pré-requisitos
1. Abra seu navegador e acesse [Portal do Azure](portal.azure.com).
2. Faça login com suas credenciais da Microsoft.
3. Acesse o [Azure Cognitive Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search)
4. Navegador moderno (recomendado: Edge ou Chrome)

#### 📁 Estrutura do Repositório
```
📂 Desafio#04-Azure-Cognitive-Search-Utilizando-AI-Search-para-indexacao-e-consulta-de-Dados/
│
├── 📄 README.md                  # Documento principal com guia, explicações e etapas do desafio
├── 📂 data/                       # Dados brutos utilizados para ingestão e indexação
│    ├── documentos/
│    │   ├── arquivo1.pdf
│    │   ├── arquivo2.docx
│    │   └── imagem1.jpg
│    └── dataset_exemplo.csv
├── 📂 screenshots/                # Capturas de tela das configurações e resultados no portal
│    ├── criacao_indice.png
│    ├── ingestao_dados.png
│    └── consulta_resultados.png
├── 📂 insights/                    # Relatórios e análises obtidas após indexação
│    ├── relatorio_palavras_chave.txt
│    └── resumo_insights.md
├── 📂 config/                      # Configurações exportadas do Azure Cognitive Search
│    ├── index-config.json
│    └── skillset-config.json
├── 📂 scripts/                     # Scripts para interagir com o serviço via API
│    ├── consulta_indice.py
│    └── criar_indice.py
├── 📂 docs/                        # Documentos e diagramas extras
│    ├── guia_cognitive_search.pdf
│    └── arquitetura_projeto.png
└── 📄 LICENSE                      # Licença do projeto
```

#### ⚙️ Ferramentas e Tecnologias
- Azure Cognitive Search
- Azure Blob Storage
- Cognitive Services (OCR, Text Analytics, Language Detection)
- Azure Portal
- GitHub
- Git
- Python

### 🧠 Sobre o Azure Cognitive Search
O `Azure Cognitive Search` é um serviço da Microsoft que permite:
- Indexar dados estruturados e não estruturados
- Enriquecer documentos com IA (OCR, reconhecimento de entidade, tradução, etc.)
- Criar experiências de busca personalizadas e escaláveis.

#### 🗂️ Etapas Realizadas
1. Ingestão de Dados
- Fonte dos dados: arquivos PDF, DOCX, e imagens (OCR)
- Ferramenta utilizada: `Azure Blob Storage` + `Skillsets do Cognitive Search`
- Técnicas aplicadas:
  - Extração de texto (OCR)
  - Detecção de linguagem
  - Análise de entidade nomeada

2. Criação do Índice
- Criação de um índice no portal do Azure
- Definição de campos pesquisáveis (title, content, metadata)
- Configuração de indexadores e data sources
- Aplicação de **Skillsets cognitivos** para enriquecimento de dados

3. Consulta e Exploração dos Dados
- Execução de consultas no painel do Azure
- Utilização de filtros, facetas e ordenação
- Extração de insights:
  - Palavras-chave mais frequentes
  - Documentos com maior densidade informativa
  - Correlação de entidades

### 💡 Insights Obtidos
- A aplicação de IA na indexação permite acelerar o processo de **descoberta de informação** em arquivos diversos.
- Os **skillsets cognitivos** são essenciais para transformar dados não estruturados em conhecimento consultável.
- A combinação de **OCR, linguagem natural e detecção de entidades** torna o Azure Cognitive Search ideal para automação de análise documental.

## 🗒️ Recursos Adicionais
- [Documentação Oficial do Microsoft Azure](https://docs.microsoft.com/azure)
- [Documentação Azure Cognitive Search](https://learn.microsoft.com/pt-br/azure/search/search-what-is-azure-search)
- [Explore an Azure AI Search index (UI) - Laboratório no Microsoft Learning](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/11-ai-search.html)

## 🔗 Créditos
Este guia serve como repositório de estudos, desafios e projetos da [Bootcamp Microsoft - Fundamentos de IA](https://www.dio.me/bootcamp/microsoft-fundamentos-de-ia) e da [Formação Microsoft Azure AI Fundamentals (AI-900)](https://web.dio.me/track/2150f9b5-b06f-4a59-ade6-ab163c24f089), avaliando o ensinado sobre aplicar técnicas de organização e pesquisa de documentos por meio da ingestão de dados e indexação utilizando ferramentas de inteligência artificial.

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