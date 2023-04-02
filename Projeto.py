#Neste projeto, iremos adicionar, listar, remover e editar contatos
agenda = [] #Criando uma lista vazia

#Definindo as funções do sistema

#Descrição: Este procedimento cria um novo contato na agenda
#Nome: novo()
#Tipo: procedimento
def novo():
    global agenda #definindo variável como global
    nome =p_nome()
    celular = input ("Celular.......:")
    email = input ("E-mail.......:")
    agenda.append([nome, celular, email]) #Adicionando os dados na agenda
    print("\n--------------------------"
          "\nRegistro gravado com Sucesso!!!\n"
          "----------------------------")
#Descrição: Este procedimento LÊ o nome digitado pelo usuário
#Nome: p_nome()
#Tipo: procedimento
def p_nome():
    return(input("Nome........:"))   

#LISTAR DADOS DA MATRIZ AGENDA

#descirção: Este procedimento lista UM registro
# Nome: listar_dados(nome, celular, email)
# Tipo: procedimento
def listar_dados(nome, celular, email):
    print("Nome: %s\nCelular: %s\nEmail: %s" %(nome, celular, email))
    print("----------------------------")  
    
    
    
#Descrição: Este procedimento lista TODOS os registros da matriz 
#Nome: listar()
#Tipo: procedimento
def listar(): #Função para mostrar lista de contatos
    print("\nCONTATOS DA AGENDA ##############\n")
    for e in agenda:
        listar_dados(e[0], e[1], e[2])     
    print("\n FIM DA AGENDA ####################\n") 
    
 #Tipo: Função
 #Funcão de pesquisar dados dentro da matriz AGENDA[]
def pesquisa(nome):
     name = nome.lower()
     for  d, e in enumerate(agenda): #percorre toda a matriz.
         if e[0].lower() ==name: #procura o nome desejado
             return d #retorna o índice do nome encontrado
     return None #Retorna vazio senao encontrar     
 
 #Desrição: Este procedimento tem como função PESQUISAR

def pesquisar():
    #pesquisa o nome
    p = pesquisa(p_nome()) #entrada de dados.
    if p != None: #se for diferente de NADA(None), ou seja, se nao tiver algo é pq encontrou alguma coisa 
        print("Registro encontrado!")
        # atualiza as variáveis se encontrou
        nome = agenda[p][0]
        celular = agenda[p][1]
        email = agenda[p][2]
        #mostra o registro
        listar_dados(nome, celular, email)
    else:
        #Exibe a mensagem que nao foi encontrado nada no registro
        print("\nNome não encontrado!!!")
        
        

#Descrição: Este procedimento apaga um contato
# Nome: apagar();
#Tipo: procedimento

        
def apagar():
    global agenda
    nome = p_nome()
    #Retorna o indice do nome ou vazio
    p = pesquisa(nome)
    if p != None: #se encontrou o registro
        del agenda[p] #exclui o contato
        print("\n---------------------"
              "\nRegistro Apagado com Sucesso!!!\n"
              "-------------------------------")
       
    else: #Senao encontrou o registro para excluir
        print("Registro não encontrado!")


#Descrição: Este procedimento edita o nome do usuario
def editar():
    p = pesquisa(p_nome()) #entrada dos dados
    #Se encontrar o registro:
    if p != None: #se for diferente de NADA(None), ou seja, se nao tiver algo é pq encontrou alguma coisa 
        #Mostra o nome e pede a edição dos demais
        nome = agenda[p][0]
        print("Nome.......:", nome)
        celular = input("Celular......:")
        email = input("E-mail........:")
        agenda[p] = [nome, celular, email] #Armazenando os novos dados.
        print("\n-----------------"
              "\nRegistro EDITADO com sucesso"
              "---------------------------")
        
    else:
        print("Nome não encontrado na base de dados!")
        
        

#Descrição: Esta funcao valida se o item digitado foi valido
#Nome: validar(pergunta,inicia,fim): int
#Tipo: Função
        
def validar(pergunta, inicio, fim): #Função para validar números inteiros
    while True: #criando um looping infinito
        try: #Criando um acordo/condição
            valor: int(input(pergunta)) #Entrada de dados
            if inicio <= valor <= fim: #Determinando uma condição.
                return  (valor) #executa caso for verdadeira
            else:
                return(0)
        except ValueError: #Executa caso for falsa.
            print("Valor inválido, favor digitar entre %d e %d" %(inicio, fim))

def menu():
    print("""
    1 - Adicionar um novo contato
    2 - Editar um contato 
    3 - Pesquisar um contato
    4 - Listar um contato
    5 - Apagar um contato
    6 - Sair""")

    return validar("Escolha uma opção: ", 1, 6)



#Programa principal
while True: 
    opcao = menu()
    if opcao ==0: 
        print("Opção inválida")
    elif opcao ==6:
        break
    elif opcao ==1:
        novo()
    elif opcao ==2:
        editar()
    elif opcao ==3:
        pesquisar()
    elif opcao ==4:
        listar()
    elif opcao ==5:
        apagar()