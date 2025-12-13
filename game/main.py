import random


def choose_options():  # funcion para escoger una opcion
  options = ('piedra', 'papel', 'tijera') # variable con las opciones
  user_option = input('piedra, papel o tijera => ') # input para que el usuario escoja
  user_option = user_option.lower() # sea cual sea la opcion que escoge el usuario se pone en minusculas

  if not user_option in options: # si la opcion que escogio el usuario no esta en opciones imprime el mensaje y no retorna nada
    print('esa opcion no es valida')
    # continue
    return None, None

  computer_option = random.choice(options) # variable para escoger una opcion random de opciones

  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option # en estas 3 lineas muestran las opciones escogidas

def check_rules(user_option, computer_option, user_wins, computer_wins): # funcion para la funcionalidad del juego
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1

    user_option, computer_option = choose_options() # se hace el llamado de la funcion para escoger opciones
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins) # se llama la funcion para ver quien gano 

    if computer_wins == 2:
      print('El ganador es la computadora')
      break

    if user_wins == 2:
      print('El ganador es el usuario')
      break

run_game()