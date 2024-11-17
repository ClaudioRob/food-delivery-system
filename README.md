## Case de um Sistema Básico para entrega de comida

Para criar um sistema de entrega de comida básico, podemos estruturar o sistema em classes e funções em Python. Vamos organizar da seguinte maneira:

Classe Pedido: Representa um pedido de comida, com detalhes como o ID do pedido, nome do cliente, itens pedidos, e status.
Classe SistemaEntrega: Controla os pedidos, permitindo adicionar novos pedidos e listar o histórico de pedidos.

- Código: 

Explicação do Código:

Pedido: Cada instância representa um pedido, com atributos como id_pedido, cliente, itens, status (inicialmente como "Pendente"), e data_hora (data e hora do pedido).
SistemaEntrega: Controla a lista de pedidos. A função adicionar_pedido cria um novo pedido e o adiciona ao registro, enquanto a função listar_pedidos exibe todos os pedidos.

Porque devo usar as class?

Usar classes em um sistema como o de entrega de comida oferece várias vantagens, especialmente quando se trata de organização, reutilização de código e facilidade de manutenção. Vou destacar algumas razões importantes para usar classes nesse contexto:

### 1. Organização e Estrutura
Encapsulamento: As classes permitem agrupar dados e métodos que têm uma relação lógica entre si, criando estruturas mais organizadas. Em vez de ter um monte de variáveis e funções soltas, você pode agrupar tudo relacionado a um pedido dentro da classe Pedido, e tudo relacionado ao gerenciamento de pedidos dentro da classe SistemaEntrega. Isso torna o código mais fácil de entender e acompanhar, especialmente em sistemas maiores.

### 2. Reutilização de Código
Com classes, você pode criar objetos (Pedido, SistemaEntrega) e reutilizá-los facilmente. Por exemplo, se você quiser criar várias instâncias de pedidos, basta instanciar a classe Pedido com os dados apropriados, sem ter que reescrever o código para cada pedido.
A reutilização de classes facilita a expansão do sistema. Se, futuramente, você quiser adicionar uma funcionalidade específica a cada pedido (como o cálculo de um tempo estimado de entrega), basta modificar a classe Pedido e todos os pedidos já criados herdarão a nova funcionalidade automaticamente.

### 3. Facilidade de Expansão e Manutenção
Classes ajudam a manter o código mais modular e, consequentemente, mais fácil de modificar e expandir. Se for necessário alterar a lógica de um pedido ou adicionar novos recursos (como um método para cancelar um pedido), você pode fazer isso diretamente na classe Pedido, sem impactar o restante do sistema. Além disso, quando o código está organizado em classes, é mais fácil para outros desenvolvedores entenderem e darem manutenção. Isso é essencial em equipes de desenvolvimento.

### 4. Conceitos de Programação Orientada a Objetos (POO)
Herança: Com classes, é possível criar subclasses que herdam características da classe principal. Por exemplo, se você quiser criar um tipo especial de pedido com características únicas (como pedido prioritário), você pode criar uma subclasse de Pedido chamada PedidoPrioritario. Polimorfismo e Abstração: Esses conceitos facilitam o desenvolvimento de sistemas complexos, pois permitem que diferentes tipos de objetos (por exemplo, diferentes tipos de pedidos) compartilhem a mesma interface e se comportem de maneira adequada às suas particularidades.

### 5. Segurança e Controle sobre os Dados
Classes permitem controlar melhor o acesso e a modificação dos dados. Por exemplo, ao definir os dados como atributos internos de uma classe (self.cliente, self.status, etc.), você pode garantir que esses atributos sejam manipulados apenas por métodos específicos, reduzindo a chance de erros ou alterações não autorizadas nos dados.

Exemplo Simplificado (Comparação)
Veja a diferença entre usar classes e não usá-las para representar pedidos

Sem classes:
pedidos = []

def adicionar_pedido(id_pedido, cliente, itens):
    pedido = {
        "id_pedido": id_pedido,
        "cliente": cliente,
        "itens": itens,
        "status": "Pendente"
    }
    pedidos.append(pedido)

def listar_pedidos():
    for pedido in pedidos:
        print(pedido)

# Exemplo de uso
adicionar_pedido(1, "João", ["Pizza"])
listar_pedidos()

Com classes:
class Pedido:
    def __init__(self, id_pedido, cliente, itens):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.itens = itens
        self.status = "Pendente"
    
    def __str__(self):
        return f"Pedido ID: {self.id_pedido} - Cliente: {self.cliente}, Itens: {self.itens}, Status: {self.status}"

class SistemaEntrega:
    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, id_pedido, cliente, itens):
        pedido = Pedido(id_pedido, cliente, itens)
        self.pedidos.append(pedido)
        print(f"Pedido {id_pedido} adicionado.")

    def listar_pedidos(self):
        for pedido in self.pedidos:
            print(pedido)

# Exemplo de uso
sistema = SistemaEntrega()
sistema.adicionar_pedido(1, "João", ["Pizza"])
sistema.listar_pedidos()

Com classes, o código fica mais organizado e fácil de entender. Além disso, o uso de classes torna o sistema mais expansível para atender necessidades futuras.

### Novas Funcionalidades:
2. atualizar status de retirada e entrega do pedido
3. modifique os itens do pedido somente se o pedido nao for retirado
4. cancele o pedido se ele não for retirado
5. gere uma fatura total, da seguinte forma:
   \(se(valor\_da\_conta > 1000); valor\_total\_da\_conta = valor\_da\_conta + 10\% imposto\) ou \(se(valor\_da\_conta < 1000); valor\_total\_da\_conta = valor\_da\_conta + 5\% imposto\)

### Vamos expandir o sistema com as funcionalidades solicitadas.

Ajustes no Código
Para implementar essas novas funcionalidades, vamos adicionar métodos à classe Pedido para atualizar o status, modificar itens e cancelar o pedido, além de calcular o valor total com o imposto.

- código:

### Explicação das Novas Funcionalidades
#### Atualizar Status do Pedido (atualizar_status):

O método permite alterar o status do pedido para "Pendente", "Retirado", "Entregue" ou "Cancelado".
O status é atualizado apenas se for uma das opções válidas.
Modificar Itens do Pedido (modificar_itens):

O método permite modificar os itens do pedido, mas apenas se o pedido ainda estiver no status "Pendente".
Caso o pedido já tenha sido retirado, uma mensagem informa que os itens não podem ser modificados.
Cancelar Pedido (cancelar_pedido):

Permite cancelar o pedido, mas somente se ele ainda estiver no status "Pendente".
Caso o pedido já tenha sido retirado, o cancelamento não é permitido.
Gerar Fatura Total com Imposto (gerar_fatura):

Calcula o valor total com imposto baseado no valor da conta:
Se o valor da conta for maior que 1000, aplica um imposto de 10%.
Se o valor da conta for menor ou igual a 1000, aplica um imposto de 5%.
O valor total é exibido e retornado pelo método.
Essas funcionalidades tornam o sistema mais robusto, permitindo gerenciar o ciclo completo de um pedido de forma eficiente e controlada.

### Implementação de Tetes Unitários

Implementar e testar o código em partes permite garantir que cada funcionalidade funciona corretamente antes de avançar para a próxima. Vamos dividir o restante do sistema em pequenas etapas e criar testes específicos para cada uma delas.

Aqui está um plano para continuar o desenvolvimento e os testes do sistema de forma modular:

Estrutura das Próximas Partes do Código
Parte 1: Criar o Pedido

Método para criar um pedido, que adiciona itens e seus preços a um dicionário de pedidos.
Parte 2: Atualizar Status do Pedido

Método para atualizar o status de um pedido (ex.: "Aguardando retirada", "Retirado", "Entregue").
Parte 3: Modificar Itens do Pedido

Método para modificar itens de um pedido apenas se ele ainda não foi retirado.
Parte 4: Cancelar Pedido

Método para cancelar o pedido se ele ainda não foi retirado.
Parte 5: Gerar Fatura Total com Imposto

Método para calcular o valor total com base em impostos.
Vamos implementar a Parte 1 e criar o teste correspondente.

Parte 1: Criar Pedido
Atualize food_delivery_system.py
Adicione um método para criar um pedido:

Esse método create_order cria um pedido com um order_id e uma lista de itens e suas quantidades, calcula o total e armazena o pedido no dicionário orders.

Teste para a Parte 1: create_order
Agora, vamos criar um teste para o método create_order no arquivo test_food_delivery_system.py.

Explicação dos Testes
test_display_menu: Confirma que o menu exibido é o esperado.
test_create_order: Verifica se o pedido é criado corretamente com o total calculado e o status inicial.
test_create_order_invalid_item: Testa o caso em que um item que não está no menu é solicitado, gerando um erro.
Executar o Teste
Para testar a criação de pedidos, rode o comando pytest:

Se os testes passarem, significa que a criação de pedidos está funcionando corretamente.

Parte 2: Atualizar Status do Pedido
Nesta parte, vamos adicionar um método para atualizar o status do pedido.

Atualize food_delivery_system.py
Adicione o método update_order_status na classe FoodDeliverySystem:

Este método update_order_status permite atualizar o status de um pedido específico, desde que ele exista. Se o pedido não existir, lança um erro KeyError.

Teste para a Parte 2: update_order_status
Vamos adicionar testes para o método update_order_status no arquivo test_food_delivery_system.py:

Explicação dos Testes
test_update_order_status: Verifica se o status do pedido é atualizado corretamente.
test_update_order_status_invalid_order: Testa o caso em que se tenta atualizar o status de um pedido inexistente, o que deve gerar um erro KeyError.
Parte 3: Modificar Itens do Pedido
Vamos adicionar um método para modificar os itens do pedido, mas somente se o pedido ainda não foi retirado.

Atualize food_delivery_system.py
Adicione o método modify_order_items:

Este método permite modificar os itens do pedido se o status ainda for "Aguardando retirada". Caso contrário, lança um erro.

Teste para a Parte 3: modify_order_items
No arquivo test_food_delivery_system.py, adicione os testes para modify_order_items:

Explicação dos Testes
test_modify_order_items: Verifica se os itens do pedido podem ser modificados corretamente.
test_modify_order_items_after_pickup: Tenta modificar os itens após o pedido ser retirado, o que deve gerar um erro.
Parte 4: Cancelar Pedido
Agora, vamos adicionar um método para cancelar o pedido se ele ainda não foi retirado.

Atualize food_delivery_system.py
Adicione o método cancel_order:

Teste para a Parte 4: cancel_order
No arquivo test_food_delivery_system.py, adicione os testes para cancel_order:

Explicação dos Testes
test_cancel_order: Verifica se o pedido é cancelado corretamente antes de ser retirado.
test_cancel_order_after_pickup: Tenta cancelar o pedido após a retirada, o que deve gerar um erro.
Execute os testes com o comando:

Essa estrutura modular permite que você vá testando cada funcionalidade separadamente. Quando estiver pronto, podemos avançar para a Parte 5: Gerar Fatura Total com Imposto.

Vamos prosseguir com a Parte 5: Gerar Fatura Total com Imposto.

Nessa etapa, vamos adicionar um método que calcula o total do pedido, incluindo impostos, de acordo com as condições descritas.

Parte 5: Gerar Fatura Total com Imposto
Se o valor do pedido for superior a 1000, aplica-se um imposto de 10%.
Se o valor do pedido for inferior a 1000, aplica-se um imposto de 5%.
Atualize food_delivery_system.py
Adicione o método generate_invoice na classe FoodDeliverySystem:

Este método generate_invoice calcula o total do pedido com o imposto apropriado e retorna um dicionário com o valor base, o imposto aplicado e o total final com imposto.

Teste para a Parte 5: generate_invoice
No arquivo test_food_delivery_system.py, adicione os testes para generate_invoice:

Explicação dos Testes
test_generate_invoice_low_total: Testa a geração de fatura com um pedido cujo total é menor que 1000, aplicando o imposto de 5%.
test_generate_invoice_high_total: Testa a geração de fatura com um pedido cujo total é maior que 1000, aplicando o imposto de 10%.
test_generate_invoice_invalid_order: Tenta gerar uma fatura para um pedido inexistente, o que deve gerar um erro KeyError.
Executando os Testes
Para executar todos os testes, use o comando:

Essa última etapa conclui as funcionalidades principais do sistema de entrega de comida.

Podemos criar uma aplicação simples para esse sistema de entrega de comida usando um framework web em Python, como o Flask ou o FastAPI. Isso nos permitirá expor a funcionalidade do sistema como uma API, onde usuários podem criar pedidos, atualizar o status, modificar itens e gerar faturas por meio de endpoints HTTP.

Vou sugerir uma estrutura usando o Flask, pois é leve e fácil de configurar para uma aplicação simples.

Estrutura do Projeto
Organize o projeto da seguinte forma:

food_delivery_app/
├── app.py               # Arquivo principal da aplicação Flask
├── food_delivery/
│   ├── __init__.py      # Inicialização do módulo
│   ├── food_delivery_system.py  # Classe principal do sistema de entrega
├── tests/
│   ├── test_food_delivery_system.py  # Testes para a classe
└── requirements.txt     # Dependências do projeto

Passo a Passo
1. Instale o Flask
No terminal, dentro do diretório do projeto, instale o Flask:

pip install flask

Adicione a dependência ao requirements.txt:

flask

2. Crie o Arquivo app.py
Este arquivo será o ponto de entrada da aplicação e conterá a lógica dos endpoints da API.

Explicação dos Endpoints
1. /menu (GET): Retorna o menu de itens disponíveis.
2. /order (POST): Cria um novo pedido com os itens especificados. Recebe um JSON com order_id e items.
3. /order/<order_id>/status (PUT): Atualiza o status de um pedido específico. Recebe um JSON com status.
4. /order/<order_id>/modify (PUT): Modifica os itens de um pedido, desde que ele ainda não tenha sido retirado.
5. /order/<order_id>/cancel (DELETE): Cancela um pedido, se ele ainda não tiver sido retirado.
6. /order/<order_id>/invoice (GET): Gera e retorna a fatura do pedido, aplicando o imposto conforme as condições.

3. Testando a Aplicação
Para executar a aplicação, rode o comando no terminal:

4. Exemplos de Testes de Endpoints com curl

1. Criar Pedido:
curl -X POST -H "Content-Type: application/json" -d '{"order_id": 1, "items": {"Burger": 2}}' http://127.0.0.1:5000/order

2. Obter Menu:
curl http://127.0.0.1:5000/menu

3. Atualizar Status do Pedido:
curl -X PUT -H "Content-Type: application/json" -d '{"items": {"Pizza": 1}}' http://127.0.0.1:5000/order/1/modify

4. Modificar Itens do Pedido:
curl -X PUT -H "Content-Type: application/json" -d '{"items": {"Pizza": 1}}' http://127.0.0.1:5000/order/1/modify

5. Cancelar Pedido:
curl -X DELETE http://127.0.0.1:5000/order/1/cancel

6. Gerar Fatura:
curl http://127.0.0.1:5000/order/1/invoice


Essa aplicação básica permite que você gerencie pedidos de comida com operações CRUD e obtenha uma fatura total com imposto. Caso tenha interesse em expandir, podemos explorar funcionalidades adicionais, como autenticação, interface de usuário, ou uma base de dados para persistir os pedidos.



