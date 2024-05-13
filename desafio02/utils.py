import pickle
import pandas as pd

def vericar_input(input_string):
    if len(input_string) != 0:
        if input_string[0].isdigit():
            b= input_string.replace(',' , '.')
            c= b.replace('.' , '' , 1).isdigit()
            return c
    return False

def Embarque(input_string):
    lista_embarque = []
    if input_string== 'S':
        lista_embarque = [1,0,0]
    elif input_string == 'C':
        lista_embarque = [0,1,0]
    else:
        lista_embarque = [0,0,1]
    return lista_embarque

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
                if features!='S' and features!='Sexo':
                    resposta_for = input(f"Insira o valor para a coluna {features}: ")
                    if vericar_input(resposta_for) == True and features!='S':
                        lista_resposta.append(resposta_for)
                        break
                    else:
                        print('entrada invalida, por favor digite um numero float/int')
                elif features == 'Sexo':
                    resposta_for = input(f"Insira o valor para a coluna {features}(Mulher=0 Homem=1): ")
                    if vericar_input(resposta_for) == True and features!='S':
                        lista_resposta.append(resposta_for)
                        break
                    else:
                        print('entrada invalida, por favor digite um numero float/int')
                else:
                    resposta_for = input(f"Qual o local de embarque?\nS, C ou Q: ")
                    if features=='S':    #adicionar um condição dupla onde sera vericado se o input é S,C ou Q com a função a ser criada 'verifica_embarque()'
                        lista_embarque = Embarque(resposta_for)
                        lista_resposta+=lista_embarque
                        break
                    else:
                        print('entrada invalida, por favor digite um numero float/int')

    df_variaveis.loc[len(df_variaveis)] = lista_resposta
    previsao_model = IA.predict(df_variaveis)
    dic = { 0:'morto', 1:'vivo'}
    resultado = dic[previsao_model.item()]
    print(f"Previsão: {resultado}")