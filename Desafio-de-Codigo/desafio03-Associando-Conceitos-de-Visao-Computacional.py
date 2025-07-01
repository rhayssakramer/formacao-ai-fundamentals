#Código Inicial
"""
# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "detecção de objetos":
        return "identificação e localização de objetos em uma imagem"
     
    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:                         
    elif conceito == "escreva aqui o conceito correspondente":
        return "divisão de uma imagem para facilitar a análise de cada região"
        
    elif conceito == "escreva aqui o conceito correspondente":
        return "identificação de indivíduos com base em características faciais"
        
    elif conceito == "escreva aqui o conceito correspondente":
        return "monitoramento do movimento em uma sequência de imagens"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito". 
print(descrever_conceito(entrada))
"""

#Solução
# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "detecção de objetos":
        return "identificação e localização de objetos em uma imagem"
     
    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:                         
    elif conceito == "segmentação de imagem":
        return "divisão de uma imagem para facilitar a análise de cada região"
        
    elif conceito == "reconhecimento facial":
        return "identificação de indivíduos com base em características faciais"
        
    elif conceito == "rastreamento de movimento":
        return "monitoramento do movimento em uma sequência de imagens"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito". 
print(descrever_conceito(entrada))