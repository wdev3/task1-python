#classe e defs
class tarefa:
    def __init__(self, nome, tarefa, dificuldade):
        self.nome = nome
        self.tarefa = tarefa
        self.dificuldade = dificuldade
    def mostrar_nome(self):
        print (F"O nome da tarefa e: {self.nome}")
    def mostrar_tarefa(self):
       print (f"A tarefa e: {self.tarefa}")
    def mostrar_dificuldade(self):
       print (f"A dificuldade e: {self.dificuldade}")
   

#pergunta incial de adicionar tarefa     
try:
 pergunta_txt = input("Qual e o nome do .txt que voce quer criar? \n")
 pergunta_nome = input("Qual e o nome da tarefa?: \n")
 pergunta_tarefa = input("Qual e a tarefa?: \n")
 pergunta_dificuldade = int(input("Qual e a dificuldade? (de 1 a 10): \n"))

except ValueError:
   print("Digite apenas numeros de 0 a 10")


#adicionar os valores ao class e copiar as tarefas no .txt e removendo tarefas
nome_classe = tarefa(pergunta_nome, pergunta_tarefa, pergunta_dificuldade)
arquivo = open(pergunta_txt, "a")
nome_classe.mostrar_nome()
nome_classe.mostrar_tarefa()
nome_classe.mostrar_dificuldade()


with open(pergunta_txt, "w"):
   arquivo.write (f"O nome da tarefa e: {pergunta_nome} \n")
   arquivo.write (f"A tarefa e: {pergunta_tarefa} \n")
   arquivo.write (str(f"A dificuldade da tarefa e: {pergunta_dificuldade}"))


#nova pergunta
while True:
 pergunta_nova = input ("Quer adicionar uma tarefa nova? s/n \n")
 if pergunta_nova.lower() == "nao":
    print ("Ok, olhe o .txt que foi criado")
    break
 if pergunta_nova.lower() == "sim":
   print ("Digite os novos detalhes da tarefa")
   pergunta_nome2 = input("Qual e o nome da tarefa?: \n")
   pergunta_tarefa2 = input("Qual e a tarefa?: \n")
   pergunta_dificuldade2 = int(input("Qual e a dificuldade? (de 1 a 10): \n"))

#adicionar as novas perguntas ao .txt
   with open ("tarefas.txt", "w"):
      arquivo.write (f"O nome da tarefa e: {pergunta_nome2} \n")
      arquivo.write (f"A tarefa e: {pergunta_tarefa2} \n")
      arquivo.write (str(f"A dificuldade da tarefa e {pergunta_dificuldade2} \n"))
