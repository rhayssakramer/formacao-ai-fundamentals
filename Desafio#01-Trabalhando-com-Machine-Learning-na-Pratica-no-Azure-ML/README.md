## 🤖 Trabalhando com Machine Learning na Prática no Azure ML

Este repositório corresponde ao Desafio #01 da  [Bootcamp Microsoft - Fundamentos de IA](https://www.dio.me/bootcamp/microsoft-fundamentos-de-ia) e da [Formação Microsoft Azure AI Fundamentals (AI-900)](https://web.dio.me/track/2150f9b5-b06f-4a59-ade6-ab163c24f089) para aprender a criar nossa conta no Azure e explorar as capacidades de Machine Learning da plataforma para desenvolver nossa primeira automação prática. Ao aplicar implementações e soluções escaláveis de aprendizado de máquina na nuvem da Microsoft, adquiriremos conhecimentos valiosos e experiência na construção de soluções eficientes. 

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

#### 🎯 Desafio de Projeto

#### 📁 Etapa 1: Preparar os dados
Utilize o arquivo .csv, que contém 60 exemplos sintéticos com a seguinte estrutura:
| Categoria   | Peso (kg) | Volume (ml) | Marca    | Preço (R$) |
|-------------|-----------|-------------|----------|------------|
|             |           |             |          |            |
|             |           |             |          |            |
|             |           |        |    |          |            |

🔗 Carreguei o arquivo no repositório para quem quiser utilizar.


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

🔧 Ajuste de validação cruzada
Na aba Validation (Validação):
- Validation type → K-Fold cross validation
- Number of cross validations (folds) → 3

Com 60 registros, usar 3 divisões já garante robustez sem perda de dados.

#### ⏳ Etapa 4: Executar o AutoML
- O Azure AutoML testará diversos algoritmos automaticamente
- Ao final da execução, será exibida uma lista com os modelos testados
- Escolha o modelo com menor erro (como RMSE ou MAE)

##### 🌐 Etapa 5: Publicar o modelo como um endpoint
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

#### 🧱 O que é JSON?
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

### 🗒️ Recursos Adicionais
- [Documentação Oficial do Microsoft Azure](https://docs.microsoft.com/azure)

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

<div align="center"><a href="https://github.com/rhayssakramer"><img src="https://github.com/rhayssakramer/rhayssakramer/blob/main/img/by-devrhakramer.png" width="100"></a></div>
