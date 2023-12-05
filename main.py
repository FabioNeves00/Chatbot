from openai import OpenAI

client = OpenAI(api_key='CHAVE')
ocasioes = ["aniversário", "casual", "junina", "casamento"]
receitas = [
    {
        "nome": "Bolo de chocolate",
        "ingredientes": ["chocolate", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "aniversário"
    },
    {
        "nome": "Bolo de cenoura",
        "ingredientes": ["cenoura", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "qualquer"
    },
    {
        "nome": "Bolo de fubá",
        "ingredientes": ["fubá", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "aniversário"
    },
    {
        "nome": "Bolo de laranja",
        "ingredientes": ["laranja", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "casual"
    },
    {
        "nome": "Bolo de limão",
        "ingredientes": ["limão", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "casual"
    },
    {
        "nome": "Bolo de maracujá",
        "ingredientes": ["maracujá", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "junina"
    },
    {
        "nome": "Bolo de milho",
        "ingredientes": ["milho", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "junina"
    },
    {
        "nome": "Bolo de morango",
        "ingredientes": ["morango", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "casamento"
    },
    {
        "nome": "Bolo de pamonha",
        "ingredientes": ["pamonha", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "aniversário"
    },
    {
        "nome": "Bolo de pão de queijo",
        "ingredientes": ["pão de queijo", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "casamento"
    },
    {
        "nome": "Bolo de tapioca",
        "ingredientes": ["tapioca", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "junina"
    },
    {
        "nome": "Bolo de abacaxi",
        "ingredientes": ["abacaxi", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "casual"
    },
    {
        "nome": "Bolo de abóbora",
        "ingredientes": ["abóbora", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "junina"
    },
    {
        "nome": "Bolo de banana",
        "ingredientes": ["banana", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "casual"
    },
    {
        "nome": "Bolo de batata doce",
        "ingredientes": ["batata doce", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "casual"
    },
    {
        "nome": "Bolo de beterraba",
        "ingredientes": ["beterraba", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "casual"
    },
    {
        "nome": "Bolo de brigadeiro",
        "ingredientes": ["brigadeiro", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "qualquer"
    },
    {
        "nome": "Bolo de café",
        "ingredientes": ["café", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "casamento"
    },
    {
        "nome": "Bolo de canela",
        "ingredientes": ["canela", "farinha", "ovos", "leite", "fermento"],
        "ocasiao": "junina"
    },
]

def imprimir_receita(receita):
    print("Nome:", receita['nome'])
    print("Ingredientes:", receita['ingredientes'])
    print("Ocasião:", receita['ocasiao'])

# Função para sugestões com base na ocasião mencionada pelo usuário
def sugerir_receitas_por_ocasiao(ocasiao):
    receitas_sugeridas = []
    if ocasiao:
        for receita in receitas:
            if receita['ocasiao'] == ocasiao:
                receitas_sugeridas.append(receita)
        for receita in receitas_sugeridas:
            imprimir_receita(receita)
    else:
        for receita in receitas:
            if receita['ocasiao'] == 'qualquer':
                receitas_sugeridas.append(receita)
        for receita in receitas_sugeridas:
            imprimir_receita(receita)


def obter_resposta_chatGPT(contexto, texto):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=[
                                                  {"role": "system",
                                                      "content": contexto},
                                                  {"role": "user", "content": texto}
                                              ],
                                              max_tokens=150)
    return response.choices[0].message.content


# Dentro da função principal
def main():
    print("Olá! Eu sou o Assistente de Receitas Culinárias.")
    contexto = "Você está pedindo uma receita culinária."

    while True:
        user_input = input("Você: ")

        # Enviando a mensagem do usuário para o ChatGPT - "Tradutor" de Linguagem Natural
        resposta_gpt = obter_resposta_chatGPT(contexto, user_input)

        # Atualizando o contexto com a resposta do assistente - Dinamico e proativo
        contexto = resposta_gpt

        # Verificando se o usuário mencionou uma ocasião especial a partir de palavras chaves - SBC
        ocasiao = None
        for palavra_chave, valor in ocasioes:
            if palavra_chave in resposta_gpt:
                ocasiao = valor
                break

        sugerir_receitas_por_ocasiao(ocasiao)

        continuar = input("Deseja fazer outra pergunta? (s/n): ")
        if continuar.lower() != 's':
            break


if __name__ == "__main__":
    main()
