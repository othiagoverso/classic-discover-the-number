import random

numero_secreto = random.randint(1, 100)

tentativas = 0
tentativas = tentativas =+1
while True:
    palpite_str = input("Adivinhe o número entre 1 e 100: ")

    tentativas += 1

    palpite = int(palpite_str)

    if palpite < numero_secreto:
        print("Seu palpite é muito baixo. Tente novamente!")
    elif palpite > numero_secreto:
        print("Seu palpite é muito alto. Tente novamente!")
        print(f"Numero de tentativas ate agora!!!: ", tentativas)
    else:
        
     
        print(f"Parabéns! Você acertou o número {numero_secreto}!")
        print(f"Você levou {tentativas} tentativas para acertar.")


      
        break