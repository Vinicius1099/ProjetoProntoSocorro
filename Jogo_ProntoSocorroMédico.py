import heapq
import random


class Paciente:
    def __init__(self, nome, idade, gravidade):
        self.nome = nome
        self.idade = idade
        self.gravidade = gravidade

    def __lt__(self, other):
        return self.gravidade < other.gravidade
    

class ProntoSocorro:
    def __init__(self):
        self.fila_prioridades = []
        self.pacientes_atendidos = [] 

    def chegada_paciente(self, nome, idade, gravidade):
        paciente = Paciente(nome, idade, gravidade)
        heapq.heappush(self.fila_prioridades, paciente)

    def listar_fila(self):
        print("Fila de Pacientes:")
        for paciente in self.fila_prioridades:
            print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, Gravidade: {paciente.gravidade}")

    def proximo_paciente(self):
        if not self.fila_prioridades:
            print("Não há pacientes na fila.")
            return

        proximo = max(self.fila_prioridades, key=lambda paciente: paciente.gravidade)
        print(f"Próximo paciente a ser chamado - Nome: {proximo.nome}, Idade: {proximo.idade}, Gravidade: {proximo.gravidade}")

    def listar_ultimos_chamados(self, n=5):
        if self.pacientes_atendidos:
            ultimos_chamados = self.pacientes_atendidos[-n:]
            print(f"Últimos {n} pacientes chamados:")
            for paciente in reversed(ultimos_chamados):
                print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, Gravidade: {paciente.gravidade}")
        else:
            print("Não há pacientes chamados recentemente.")

    def simulacao_aleatoria(self, num_pacientes):
        nomes = [
            "João", "Carlos", "Pedro", "Antônio", "Luís", "Rodrigo", "Miguel", "Rafael", "Fernando", "Eduardo", "Paulo",
            "André", "Leonardo", "Daniel", "Gustavo", "Ricardo", "Alexandre", "Gabriel", "Sérgio", "Felipe", "Maria",
            "Ana", "Carolina", "Laura", "Isabela", "Luísa", "Sofia", "Marta", "Beatriz", "Gabriela", "Patrícia",
            "Alice", "Juliana", "Renata", "Fernanda", "Mariana", "Camila", "Clara", "Raquel", "Isabel"            
        ]
        for _ in range(num_pacientes):
            nome = random.choice(nomes)
            idade = random.randint(1, 100)
            gravidade = random.randint(0, 10)
            self.chegada_paciente(nome, idade, gravidade)

    def atendimento_paciente(self):
        if not self.fila_prioridades:
            print("Não há pacientes na fila.")
            return

        print("Lista de Pacientes:")
        for i, paciente in enumerate(self.fila_prioridades):
            print(f"{i+1}. Nome: {paciente.nome}, Idade: {paciente.idade}, Gravidade: {paciente.gravidade}")

        try:
            escolha = int(input("Escolha o número do paciente de maior gravidade: ")) - 1

            if escolha < 0 or escolha >= len(self.fila_prioridades):
                print("Escolha inválida.")
                return

            paciente_escolhido = self.fila_prioridades[escolha]
            
            if paciente_escolhido.gravidade == max(p.gravidade for p in self.fila_prioridades):
                print("Escolha correta")
                self.fila_prioridades.pop(escolha)  # Remove o paciente apenas se a escolha for correta
                self.pacientes_atendidos.append(paciente_escolhido)
                print(f"Atendendo paciente {paciente_escolhido.nome} - Gravidade: {paciente_escolhido.gravidade}")
            else:
                print("Você escolheu atender o paciente errado!!!")

        except ValueError:
            print("Entrada inválida. Insira um número válido.")
            return

            
def main():
    pronto_socorro = ProntoSocorro()
    
    while True:
        print("\nOpções:")
        print("1. Adicionar Paciente")                              
        print("2. Visualizar Fila de Pacientes")                        
        print("3. Visualizar Próximo Paciente")                  
        print("4. Atendendimento ao Paciente")                   
        print("5. Listar os 5 Últimos Pacientes Chamados")                
        print("6. Gerar Simulação Aleatória")                       
        print("7. Sair")                                             
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            nome = input("Nome do paciente: ")
            idade = int(input("Idade do paciente: "))
            gravidade = int(input("Gravidade do paciente:"))
            pronto_socorro.chegada_paciente(nome, idade, gravidade)
        elif escolha == "2":
            pronto_socorro.listar_fila()
        elif escolha == "3":
            pronto_socorro.proximo_paciente()
        elif escolha == "4":
            pronto_socorro.atendimento_paciente()
        elif escolha == "5":
            pronto_socorro.listar_ultimos_chamados()
        elif escolha == "6":
            num_pacientes = int(input("Número de pacientes na simulação: "))
            pronto_socorro.simulacao_aleatoria(num_pacientes)
        elif escolha == "7":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
