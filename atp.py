import random

# função que gera introdução da história
def gerar_introdução():
    introduções = ["Era uma vez", "Há muito tempo atrás", "Num reino distante"]
    return random.choice(introduções)

    # Função que gera desenvolvimento da história
    def gerar_desenvolvimento():
        desenvolvimentos = ["um valente cavaleiro", "uma destemida guerreira", "um bravo guerreiro", 
                            "uma poderosa feiticeira", " um sábio mago"]
        return random.choice(desenvolvimentos)
    
    # Função que gera o final da história 
    def gerar_final():
        finais = ["enfrentando dragões ferozes.", "derrotando um terrivel vilão.", 
                "descobrindo um tesouro escondido.", "salvando o reino da escuridão.",
                "encontrando um amor verdadeiro."]
        return random.choice(finais)
    
    # Função principal que gera toda a história
    def gerar_história():
        introdução = gerar_introdução()
        desenvolvimento = gerar_desenvolvimento()
        final = gerar_final()

        história = f"{introdução} {desenvolvimento} {final}"
        return história
    
    # Exibe a história gerada
    if __name__== "___main__":
        print(gerar_história())
        
