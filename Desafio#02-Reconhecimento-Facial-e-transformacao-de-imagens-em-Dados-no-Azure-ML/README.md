## 🤖 Reconhecimento Facial e transformação de imagens em Dados no Azure ML

Este repositório corresponde ao Desafio #02 da  [Bootcamp Microsoft - Fundamentos de IA](https://www.dio.me/bootcamp/microsoft-fundamentos-de-ia) e da [Formação Microsoft Azure AI Fundamentals (AI-900)](https://web.dio.me/track/2150f9b5-b06f-4a59-ade6-ab163c24f089) para praticar a criação de reconhecimento facial, identificação de dados em documentos e também o reconhecimento de elementos em imagens. Através desses exercícios, aprimoraremos nossas habilidades na aplicação prática de tecnologias de reconhecimento, proporcionando uma compreensão mais profunda e prática desses conceitos essenciais. 

### Índice
- [Introdução](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2302-Reconhecimento-Facial-e-transformacao-de-imagens-em-Dados-no-Azure-ML#introdu%C3%A7%C3%A3o)
- [Desafio de Projeto](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2302-Reconhecimento-Facial-e-transformacao-de-imagens-em-Dados-no-Azure-ML#-desafio-de-projeto)
- [Objetivos](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2302-Reconhecimento-Facial-e-transformacao-de-imagens-em-Dados-no-Azure-ML#%EF%B8%8F-objetivos)  
  [x] [Pré-requisitos](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2302-Reconhecimento-Facial-e-transformacao-de-imagens-em-Dados-no-Azure-ML#-pr%C3%A9-requisitos)     
  [x] [O que será feito?](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2302-Reconhecimento-Facial-e-transformacao-de-imagens-em-Dados-no-Azure-ML#-o-que-ser%C3%A1-feito)    
  [x] [Passo a Passo](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2302-Reconhecimento-Facial-e-transformacao-de-imagens-em-Dados-no-Azure-ML#-passo-a-passo)  
  [x] [Geração de Legendas para Imagens](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2302-Reconhecimento-Facial-e-transformacao-de-imagens-em-Dados-no-Azure-ML#%EF%B8%8F-gera%C3%A7%C3%A3o-de-legendas-para-imagens)  
  [x] [Extração de Texto com OCR](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2302-Reconhecimento-Facial-e-transformacao-de-imagens-em-Dados-no-Azure-ML#-extra%C3%A7%C3%A3o-de-texto-com-ocr)  
  [x] [Resultado da Detecção](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2302-Reconhecimento-Facial-e-transformacao-de-imagens-em-Dados-no-Azure-ML#-resultado-da-detec%C3%A7%C3%A3o)  
- [Recursos Adicionais](https://github.com/rhayssakramer/formacao-ai-fundamentals/tree/main/Desafio%2302-Reconhecimento-Facial-e-transformacao-de-imagens-em-Dados-no-Azure-ML#%EF%B8%8F-recursos-adicionais)

### ▶️ Introdução
O `Microsoft Azure` é uma plataforma de nuvem que disponibiliza uma variedade de serviços, distribuídos em várias categorias. Este guia foi elaborado para ajudá-lo a navegar pelo portal do Azure e encontrar facilmente os serviços que você precisa.

### 🎯 Desafio de Projeto
Este projeto apresenta um passo a passo de como realizar reconhecimento facial e transformar imagens em dados tabulares usando o `Azure Machine Learning Studio` e os serviços cognitivos da Microsoft Azure. Ele demonstra o uso dos serviços da plataforma `Azure AI Vision Studio`, uma ferramenta poderosa da Microsoft voltada para análise de imagens usando inteligência artificial.

### 🛠️ Objetivos
O objetivo é praticar a criação de reconhecimento facial, identificação de dados em documentos e também o reconhecimento de elementos em imagens. Através desses exercícios, aprimoraremos nossas habilidades na aplicação prática de tecnologias de reconhecimento, proporcionando uma compreensão mais profunda e prática desses conceitos essenciais. 

#### 📌 Pré-requisitos
1. Abra seu navegador e acesse [Portal do Azure](portal.azure.com).
2. Faça login com suas credenciais da Microsoft.
3. Acesse ao [Azure Machine Learning Studio](https://ml.azure.com/)
4. Assinatura do Azure com permissão para criar recursos de Cognitive Services
5. Imagens faciais para teste (com autorização legal de uso)

#### 🧠 O que será feito?
Utilizando uma imagem de exemplo, o `Azure Vision Studio` foi capaz de detectar com precisão os rostos presentes na imagem e identificar atributos associados a cada um deles.
1. Upload de imagens para o `Azure ML`
2. Utilização da API de Face Recognition `(Azure Cognitive Services)`
3. Extração de dados faciais (posição, emoção, idade estimada etc.)
4. Armazenamento dos dados em formato tabular para uso em modelos de ML

#### 🚀 Passo a Passo
1. Acesse o `Azure Machine Learning Studio`
- Vá para https://ml.azure.com
- Selecione ou crie um workspace

2. Crie um novo pipeline (Designer)
- Vá para `Designer`
- Clique em + `New pipeline`
- Selecione o dataset com as imagens ou faça o upload diretamente

3. Adicione o módulo `Cognitive Services – Face`
- Clique em `Add module`
- Procure por `Cognitive Services - Face`
- Insira o endpoint e chave da API Face que você obteve no portal do Azure  
  Dica: Para criar um recurso de Face API:
- Vá até o portal: https://portal.azure.com
- Crie um novo recurso → `Face`
- Copie o endpoint e a chave de acesso

4. Configure o módulo de Reconhecimento Facial
- Selecione as opções de detecção:
  - Emoções
  - Idade estimada
  - Gênero
  - Posição dos olhos, boca etc.
- Vincule o dataset de imagens ao módulo

5. Execute o pipeline
- Clique em `Run`
- Após a execução, visualize os resultados na saída do módulo

6. Transforme os dados em formato tabular
- Use o módulo `Convert to CSV` ou `Extract Columns`
- Exporte os dados para análise posterior com Excel, Power BI, Python etc.  

#### 🖼️ Geração de Legendas para Imagens
Nesta etapa do projeto, utilizamos o recurso Add captions to images do `Azure Vision Studio`, que permite gerar descrições automáticas para imagens com base em visão computacional e modelos de linguagem.

🔍 **Exemplo de Legenda Gerada**  
Imagem utilizada:

Legenda detectada automaticamente:
>Legenda

Essa legenda foi gerada de forma autônoma pela IA da Microsoft, sem necessidade de intervenção manual, demonstrando como o modelo consegue interpretar contextos visuais de maneira precisa e eficiente.

#### 🧾 Extração de Texto com OCR 
Na terceira etapa, utilizamos o serviço Extract text from images do Azure Vision Studio, que aplica OCR para reconhecer e extrair texto presente em imagens.

🖼️ **Exemplo de Imagem**  
O serviço foi capaz de identificar todos os textos contidos na imagem de um cartão de crédito de exemplo, incluindo número, nome e validade:

✨ **Texto Extraído:**  

#### 🔍 Resultado da Detecção
A ferramenta fornece caixas delimitadoras para cada rosto detectado, além de um painel lateral com os atributos reconhecidos, que também podem ser acessados em formato JSON para uso posterior em aplicações ou treinamento de modelos.

A imagem abaixo foi processada com o recurso Detect faces in an image:

Atributos detectados:
- Face #1:  
    - Uso de : 
- Face #2:
    - Uso de : 

📊 **Exemplo de Saída (Tabela)**

| Nome da Imagem | Emoção Predominante | Idade Estimada | Gênero    | Posição dos Olhos |
|----------------|---------------------|----------------|-----------|-------------------|
| pessoa1.jpg    | Feliz               | 29             | Feminino  | X=112, Y=88       |
| pessoa2.jpg    | Neutro              | 41             | Masculino | X=95, Y=102       |

### 🗒️ Recursos Adicionais
- [Documentação Oficial do Microsoft Azure](https://docs.microsoft.com/azure)
- [Documentação da Face API](https://learn.microsoft.com/pt-br/azure/cognitive-services/face/)
- [Documentação do Azure ML Studio](https://learn.microsoft.com/pt-br/azure/machine-learning/)

## 🔗 Créditos
Este guia serve como repositório de estudos, desafios e projetos da [Bootcamp Microsoft - Fundamentos de IA](https://www.dio.me/bootcamp/microsoft-fundamentos-de-ia) e da [Formação Microsoft Azure AI Fundamentals (AI-900)](https://web.dio.me/track/2150f9b5-b06f-4a59-ade6-ab163c24f089). Explore os recursos compartilhados necessários para atender às suas necessidades de nuvem.

*Nota: Este projeto é apenas para fins educacionais e não possui nenhuma afiliação oficial com a franquia DIO ou suas empresas associadas.*

### 👩🏼‍💻 Autora:
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
