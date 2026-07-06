# Agente de Automação do Trello 🤖🚀

Esse projeto é um agente em Python que criei para automatizar o fluxo de tarefas dentro do Trello, direto pela API oficial deles. 

A ideia aqui foi criar um script inteligente que faz o trabalho duro sozinho: ele entra no quadro Kanban, mapeia as colunas dinamicamente (sem quebrar por causa de maiúsculas ou espaços extras) e faz uma tarefa rodar a esteira inteira de produção em tempo real.

## 🛠️ O que foi usado
* **Python 3.x**
* **Requests** (para conectar e conversar com a API do Trello)
* **Time** (para dar aquele intervalo esperto entre as movimentações)

## 📌 O que o Agente faz?
1. **Mapeamento Automático:** Ele lê o quadro pelo `BOARD_ID` e acha os IDs internos das listas (`A fazer`, `Em andamento` e `Concluído`). Isso evita ter que adivinhar IDs no código.
2. **Criação de Cartão:** Cria uma tarefa do zero com título e descrição direto na primeira coluna.
3. **Movimentação por Tempo:** Simula um fluxo real de trabalho, movendo o cartão entre as colunas a cada 3 segundos usando `time.sleep()`.

## 🚀 Como rodar o projeto na sua máquina

### 1. Preparando o Ambiente Virtual
Clone o repositório, abra o terminal na pasta e ative o ambiente virtual para garantir que as dependências fiquem isoladas:
```bash
# Ativar o ambiente virtual (PowerShell)
.\venv\Scripts\Activate.ps1

# Instalar a biblioteca necessária
pip install requests