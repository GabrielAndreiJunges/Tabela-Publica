#frameworks usados
import pandas as pd
from pandas import DataFrame



#DATABASE (Onde ficam as informações base da tabela.)
database = DataFrame
database = {'Jogos':[1, 2, 3, 4], 
    'Placar':[12, 24, 10, 24],
    'Mínimo da Temporada':[12, 12, 10, 10],
    'Máximo da Temporada':[12, 24, 24, 24],
    'Quebra recorde mín':[0, 0, 1, 1],
    'Quebra recorde max':[0, 1, 1, 1]}

df = pd.DataFrame(database, columns = ['Jogos', 'Placar', 'Mínimo da Temporada', 'Máximo da Temporada', 'Quebra recorde mín', 'Quebra recorde max'])
Data_Table = df.to_string()

p = 0

def primeiro_input():
    '''
    O input, para o usuario poder adicionar novas informações a tabela.
    Caso seja inserido uma string ou um int acima de 1000 ou abaixo de 0, ele irá requisitar uma nova tentativa
    '''
while True:
    try:
        p = int(input("Qual foi o placar?:"))
        if p == 0 <= p <= 1000:
            j = df['Jogos'].iloc[-1] + 1

            mint = df['Mínimo da Temporada'].iloc[-1]
            if int(p) < df['Mínimo da Temporada'].iloc[-1]:
                mint = p

            maxt = df['Máximo da Temporada'].iloc[-1]
            if int(p) > df['Máximo da Temporada'].iloc[-1]:
                maxt = p

            qrmin = df['Quebra recorde mín'].iloc[-1]
            if int(mint) < df['Mínimo da Temporada'].iloc[-1]:
                qrmin = qrmin + 1

            qrmax = df['Quebra recorde max'].iloc[-1]
            if int(maxt) > df['Máximo da Temporada'].iloc[-1]:
                qrmax = qrmax + 1

            new_row = {'Jogos':j, 'Placar': p, 'Mínimo da Temporada': mint, 'Máximo da Temporada': maxt, 'Quebra recorde mín':qrmin, 'Quebra recorde max': qrmax,}
            df = df.append(new_row, ignore_index=True)

            print(df)


        else:
            raise ValueError()
    except ValueError('Valor inválido'):
        print()


   


'''
Cálcula o mínimo e máximo da temporada.
Define o valor base de mint e maxt como sendo o ultimo 
valor das suas respectivas colunas e verifica, no caso de mint,
se o valor mínimo anterior era maior que o placar atual
Faz a mesma coisa com maxt, apenas invertendo
'''




'''    
Cálcula as quebras de recordes.
Define o valor base de qrmin e qrmax como sendo o ultimo 
valor das suas respectivas colunas e verifica se houve mudança nas
colunas de mínimo e máximo da temporada, para modificar o valor da quebra de recordes.

'''

"""
Adiciona novas linhas com as informações dos cálculos e afins, a tabela.

Define qual variável muda o resultado de cada coluna, depois
assimila a nova linha ao dataframe com o código df.append
"""


#Coloca em prática os códigos e lê o dataframe.


'''
Ocorrem todos os comandos para criar novas linhas e assimila-las ao dataframe novamente, 
além dos cálculos.

O processo funciona igual ao do while anterior, com a diferença que ele já vem integrado
com o "new_row", "df.append" "print(df)"
'''

while True:
    p = int(input("Adicione algum placar:"))

    j = (df)['Jogos'].iloc[-1] + 1

    mint = df['Mínimo da Temporada'].iloc[-1]
    if int(p) < df['Mínimo da Temporada'].iloc[-1]:
        mint = p

    maxt = df['Máximo da Temporada'].iloc[-1]
    if int(p) > df['Máximo da Temporada'].iloc[-1]:
        maxt = p
        
    qrmin = df['Quebra recorde mín'].iloc[-1]
    if int(mint) < df['Mínimo da Temporada'].iloc[-1]:
        qrmin = (qrmin + 1)

    qrmax = df['Quebra recorde max'].iloc[-1]
    if int(maxt) > df['Máximo da Temporada'].iloc[-1]:
        qrmax = (qrmax + 1)


    new_row = {'Jogos':j, 'Placar': p, 'Mínimo da Temporada': mint, 'Máximo da Temporada': maxt, 'Quebra recorde mín':qrmin, 'Quebra recorde max': qrmax,}
    df = df.append(new_row, ignore_index=True) 

    print(df)

              
#Possibilidade de ser inserido novos jogos;Feito
#Calculo de mínimo e maximo da temporada;Feito
#Calculo da quantidade de vezes que o recorde foi quebrado;Feito
#Interface para inserção dos dados;Feito
#Interface para consulta dos dados;Feito
#Testes Unitários;
#Controle de versão Git;
#Documentação do código;Feito