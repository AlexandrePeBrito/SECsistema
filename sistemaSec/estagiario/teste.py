erros = [{"Erro": 'cpf', "Valido": False},
          {"Erro": 'rg', "Valido": False}]

err = filter(lambda x: x['Valido'] == False, erros)
ExisteErros = map(lambda x: x['Erro'], err)
print(len(list(ExisteErros)))