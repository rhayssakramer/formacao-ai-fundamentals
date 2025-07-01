## 🔍 Reconhecimento Facial e transformação de imagens em Dados no Azure ML

Este repositório corresponde ao Desafio #02 da  [Bootcamp Microsoft - Fundamentos de IA](https://www.dio.me/bootcamp/microsoft-fundamentos-de-ia) e da [Formação Microsoft Azure AI Fundamentals (AI-900)](https://web.dio.me/track/2150f9b5-b06f-4a59-ade6-ab163c24f089) para praticar a criação de reconhecimento facial, identificação de dados em documentos e também o reconhecimento de elementos em imagens. Através desses exercícios, aprimoraremos nossas habilidades na aplicação prática de tecnologias de reconhecimento, proporcionando uma compreensão mais profunda e prática desses conceitos essenciais. 

### Índice
- [Introdução]()
- [Acessando o Portal do Azure]()
- [Localizando Serviços por Categoria]()
- [Recursos Adicionais]()

### Introdução
O Microsoft Azure é uma plataforma de nuvem que disponibiliza uma variedade de serviços, distribuídos em várias categorias. Este guia foi elaborado para ajudá-lo a navegar pelo portal do Azure e encontrar facilmente os serviços que você precisa.

### Acessando o Portal do Azure
1. Abra seu navegador e acesse [Portal do Azure](portal.azure.com).
2. Faça login com suas credenciais da Microsoft.

### Localizando Serviços por Categoria
No Azure, os serviços são classificados em categorias como Computação, Rede, Armazenamento, entre outras. Vamos entender como acessar serviços específicos dentro de cada uma dessas categorias.

### 🎯 Desafio de Projeto
Este projeto demonstra o uso dos serviços da plataforma Azure AI Vision Studio, uma ferramenta poderosa da Microsoft voltada para análise de imagens usando inteligência artificial.

#### 📷 Detecção Facial
Utilizando uma imagem de exemplo, o Azure Vision Studio foi capaz de detectar com precisão os rostos presentes na imagem e identificar atributos associados a cada um deles.

🔍 Resultado da Detecção
A imagem abaixo foi processada com o recurso Detect faces in an image:

![]()

Atributos detectados:
- Face #1:  
    - Uso de : 
- Face #2:
    - Uso de : 

A ferramenta fornece caixas delimitadoras para cada rosto detectado, além de um painel lateral com os atributos reconhecidos, que também podem ser acessados em formato JSON para uso posterior em aplicações ou treinamento de modelos.

#### 🖼️ Geração de Legendas para Imagens
Nesta etapa do projeto, utilizamos o recurso Add captions to images do Azure Vision Studio, que permite gerar descrições automáticas para imagens com base em visão computacional e modelos de linguagem.

🔍 Exemplo de Legenda Gerada
Imagem utilizada:


Legenda detectada automaticamente:
>Legenda

Essa legenda foi gerada de forma autônoma pela IA da Microsoft, sem necessidade de intervenção manual, demonstrando como o modelo consegue interpretar contextos visuais de maneira precisa e eficiente.

#### 🧾 Extração de Texto com OCR
Na terceira etapa, utilizamos o serviço Extract text from images do Azure Vision Studio, que aplica OCR para reconhecer e extrair texto presente em imagens.

🖼️ Exemplo de Imagem


O serviço foi capaz de identificar todos os textos contidos na imagem de um cartão de crédito de exemplo, incluindo número, nome e validade:


#### ✨ Texto Extraído:



### 🗒️ Recursos Adicionais
- [Documentação Oficial do Microsoft Azure](https://docs.microsoft.com/azure)

## 🔗 Créditos
Este guia serve como repositório de estudos, desafios e projetos da [Bootcamp Microsoft - Fundamentos de IA](https://www.dio.me/bootcamp/microsoft-fundamentos-de-ia) e da [Formação Microsoft Azure AI Fundamentals (AI-900)](https://web.dio.me/track/2150f9b5-b06f-4a59-ade6-ab163c24f089). Explore os recursos compartilhados necessários para atender às suas necessidades de nuvem.

*Nota: Este projeto é apenas para fins educacionais e não possui nenhuma afiliação oficial com a franquia DIO ou suas empresas associadas.*

## 👩🏼‍💻 Autoria:
<table style="border=0">
  <tr>
    <td align="left">
      <a href="https://github.com/rhayssakramer">
        <span><b>Rhayssa Kramer</b></span>
      </a>
      <br>
      <span>Assoc, Full-Stack Development</span>
    </td>
  </tr>
</table>

### <div align="center">Feito por <a href="https://github.com/rhayssakramer">@devrhakramer</a></div>