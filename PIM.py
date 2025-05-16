#projeto Python do PIM (Projeto Integrado Multidisciplinar) 

while True:
    while True:
        nome = input("Digite seu nome: ")
        print(f"Olá {nome}, seja bem-vindo(a)")

        print("Você está ciente de que utilizaremos seus dados?")
        resposta = input("Digite 1 para sim ou 2 para não: ")
        if resposta == "1":
            print("Ótimo, vamos continuar.")
            break
        elif resposta == "2":
            print("Que pena, não podemos continuar.\n")
        else:
            print("Resposta inválida, por favor digite 1 ou 2.\n")

    print("\nO que é Tecnologia da Informação?\n")
    print("Tecnologia da Informação (TI) é o uso de computadores, internet, softwares e outros recursos digitais para armazenar, processar, proteger e transmitir informações. Ela está presente em quase tudo hoje: redes sociais, bancos, escolas, empresas, etc.")

    while True:
        print("\nEscolha uma forma de representação de algoritmos:")
        print("1 - Pseudocódigo")
        print("2 - Fluxograma")
        opcao = input("Digite 1 ou 2:")

        if opcao == "1":
            print("\nPseudocódigo é uma forma de escrever algoritmos de maneira simples, parecida com a linguagem humana, facilitando o entendimento antes da programação real.")
        elif opcao == "2":
            print("\nFluxograma é uma representação gráfica dos passos de um processo, usando símbolos para mostrar o fluxo do algoritmo.")
        else:
            print("\nOpção inválida, tente novamente.\n")
            continue

        print("Você gostaria de sair do sistema ou retornar as opções?")
        resposta = input("Digite 1 para sair ou 2 para retornar:")
        if resposta == "1":
            print("Retornando ao início")
            break
        elif resposta == "2":
            print("Retornando as opções")

