#fazer um pedra papel tesoura
from random import randint
pc_choice = randint(1, 3)
player = input("qual seu nome? ")
player_choice = int(input(f"Boa sorte na partida, {player}!\n [1] - Pedra\n [2] - Papel\n [3] - Tesoura\nEscolha sua arma: "))
if player_choice == 1:
    if pc_choice == 1:
        print("eita! empataram, e agora?")
    elif pc_choice == 2:
        print("ih fio perdeu em...")
    else:
        print("parabens ganhou do pc ur so smart!")
elif player_choice == 2:
    if pc_choice == 2:
        print("eita! empataram, e agora?")
    elif pc_choice == 3:
        print("ih fio perdeu em...")
    else:
        print("parabens ganhou do pc ur so smart!")
elif player_choice == 3:
    if pc_choice == 3:
        print("eita! empataram, e agora?")
    elif pc_choice == 1:
        print("ih fio perdeu em...")
    else:
        print("parabens ganhou do pc ur so smart!")
else:
    print("ta maluco??? nao pedi nada disso")
print(f"é isso {player}, obrigada por jogar")
