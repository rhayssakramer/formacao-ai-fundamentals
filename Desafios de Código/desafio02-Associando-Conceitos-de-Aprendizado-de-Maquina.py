#Código Inicial
"""
# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "aprendizado supervisionado":
        return "método de treinamento de modelos com dados rotulados"
        
    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:                                 
    elif conceito == "escreva aqui o conceito correspondente":
        return "sistemas computacionais inspirados no funcionamento do cérebro humano"
        
    elif conceito == "escreva aqui o conceito correspondente":
        return "aprendizado baseado em recompensas e punições"
        
    elif conceito == "escreva aqui o conceito correspondente":
        return "descoberta de padrões em dados não rotulados"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito".  
print(descrever_conceito(entrada))
"""

#Solução
# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "aprendizado supervisionado":
        return "método de treinamento de modelos com dados rotulados"
        
    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:                                 
    elif conceito == "redes neurais":
        return "sistemas computacionais inspirados no funcionamento do cérebro humano"
        
    elif conceito == "aprendizado por reforço":
        return "aprendizado baseado em recompensas e punições"
        
    elif conceito == "aprendizado não supervisionado":
        return "descoberta de padrões em dados não rotulados"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito".  
print(descrever_conceito(entrada))