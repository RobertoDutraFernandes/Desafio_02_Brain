import pickle
import pandas as pd

def verificar_input(input_string):
    if len(input_string) != 0:
        if input_string[0].isdigit():
            b= input_string.replace(',' , '.')
            c= b.replace('.' , '' , 1).isdigit()
            return c
    return False

def verificar_classe(input_string):
    try:
        inteiro = int(input_string)
        if inteiro == 1 or inteiro == 2 or inteiro == 3:
            return True
    except ValueError:
        pass
    return False

def verificar_sexo(input_string):
    if input_string.lower() == 'Mulher' or input_string.lower() == 'mulher' or input_string.lower() == 'MULHER':
        return 0
    elif input_string.lower() == 'Homem' or input_string.lower() == 'homem' or input_string.lower() == 'HOMEM':
        return 1
    return False

def verificar_intervalo(fare, pclass):
    try:
        valor = float(fare)
        if pclass == 1 and 21 <= valor <= 70:
            return True
        elif pclass == 2 and 11 <= valor <= 20:
            return True
        elif pclass == 3 and 0 <= valor <= 10:
            return True
    except ValueError:
        pass
    return False 

def Embarque(input_string):
    lista_embarque = []
    if input_string== 'S':
        lista_embarque = [1,0,0]
        return lista_embarque
    elif input_string == 'C':
        lista_embarque = [0,1,0]
        return lista_embarque
    elif input_string == 'Q':
        lista_embarque = [0,0,1]
        return lista_embarque
    return False

def pedir_parametros():
    # importa biblioteca, carregar modelo e definir variaveis
    with open('./desafio02/modelo_IA_e_variaveis02.pkl', 'rb') as arquivo:
        dados = pickle.load(arquivo)
    IA = dados[0]
    variaveis = dados[1]

    # iniciar novo DataFrame
    df_variaveis = pd.DataFrame(columns = variaveis)
    lista_resposta = []

    # for para receber os parametros do usuario
    for features in variaveis:
        if features!='C' and features!='Q':
            while True:
                if features!='S' and features!='Sexo' and features != 'Pclass' and features != 'Fare':
                    resposta_for = input(f"Insira o valor para a coluna {features}: ")
                    if verificar_input(resposta_for) == True and features!='S':
                        lista_resposta.append(resposta_for)
                        break
                    else:
                        print('Entrada invalida, por favor digite um numero float/int')

                elif features == 'Pclass':
                    resposta_for = input(f"Insira qual a classe de sua passagem: ")
                    if verificar_classe(resposta_for) and verificar_input(resposta_for):
                        lista_resposta.append(resposta_for)
                        classe = int(resposta_for)
                        break
                    else:
                        print('Entrada invalida, por favor digite o numero de sua classe (1 ,2 ou 3)')

                elif features == 'Fare' and (classe == 1 or classe == 2 or classe == 3):
                    resposta_for = input(f"Insira o valor pago em sua passagem: ")
                    if verificar_intervalo(resposta_for, classe):
                        lista_resposta.append(resposta_for)
                        break
                    else:
                        print(f'Entrada inválida, por favor digite um valor condizente para a classe {classe}')


                elif features == 'Sexo':
                    resposta_for = input(f"Insira o seu sexo (Mulher / Homem): ")
                    sexo = verificar_sexo(resposta_for)
                    if sexo is not False:
                        lista_resposta.append(sexo)
                        break
                    else:
                        print('Entrada invalida, por favor digite seu sexo corretamente, Homem / Mulher')

                else:
                    resposta_for = input(f"Qual o local de embarque?\nS, C ou Q: ")
                    lista_embarque = Embarque(resposta_for)
                    if features=='S' and lista_embarque is not False:
                        lista_resposta+=lista_embarque
                        break
                    else:
                        print('Entrada invalida, por favor digite um local vádido de embarque')

    df_variaveis.loc[len(df_variaveis)] = lista_resposta
    previsao_model = IA.predict(df_variaveis)
    dic = { 0:'morto', 1:'vivo'}
    resultado = dic[previsao_model.item()]
    print(f"Previsão: {resultado}")