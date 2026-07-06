import time
import requests


API_KEY = "1003bee3593c792a6445d3e8843845e4"
TOKEN = "ATTAe74db5c43e0c6766c678543bec282d4b2e3f8104d67e6f677ab379fea9de9ffc9B24FC8A"
BOARD_ID = "OP7nOuVZ"  

BASE_URL = "https://api.trello.com/1"
AUTH_PARAMS = {"key": API_KEY, "token": TOKEN}


class AgenteTrello:

    def __init__(self, board_id):
        self.board_id = board_id
        self.listas = {}
        self._mapear_colunas()

    def _mapear_colunas(self):
        """O agente varre o quadro para descobrir os IDs internos das colunas"""
        url = f"{BASE_URL}/boards/{self.board_id}/lists"
        response = requests.get(url, params=AUTH_PARAMS)

        if response.status_code == 200:
            for coluna in response.json():
                nome_formatado = (
                    coluna["name"].lower().strip().replace(" ", "")
                )
                self.listas[nome_formatado] = coluna["id"]
            print(f"🤖 Agente: Colunas mapeadas com sucesso!")
        else:
            print(
                f"❌ Erro de conexão (Status {response.status_code}). Verifique se suas chaves e o ID do quadro estão certos."
            )

    def criar_cartao(self, nome_coluna, titulo, descricao):
        """Etapa do Fluxo: Criar e listar tarefas"""
        nome_busca = nome_coluna.lower().strip().replace(" ", "")
        id_lista = self.listas.get(nome_busca)

        if not id_lista:
            print(
                f"❌ Coluna '{nome_coluna}' não foi encontrada no seu Trello."
            )
            return None

        url = f"{BASE_URL}/cards"
        payload = {
            **AUTH_PARAMS,
            "idList": id_lista,
            "name": titulo,
            "desc": descricao,
        }
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            card = response.json()
            print(
                f"✅ Cartão '{titulo}' criado com sucesso na coluna '{nome_coluna}'!"
            )
            return card["id"]
        return None

    def mover_cartao(self, card_id, nova_coluna):
        """Etapa do Fluxo: Movimentação automática de tarefas"""
        nome_busca = nova_coluna.lower().strip().replace(" ", "")
        id_lista_destino = self.listas.get(nome_busca)

        if not id_lista_destino:
            print(f"❌ Coluna de destino '{nova_coluna}' não encontrada.")
            return False

        url = f"{BASE_URL}/cards/{card_id}"
        payload = {**AUTH_PARAMS, "idList": id_lista_destino}
        response = requests.put(url, json=payload)

        if response.status_code == 200:
            print(f"🚀 Agente moveu a tarefa para: '{nova_coluna}'")
            return True
        return False


# --- Executando o Fluxo de Automação ---
if __name__ == "__main__":
    agente = AgenteTrello(BOARD_ID)

    if agente.listas:
        print("\n--- Iniciando Automação de Tarefas ---")

        # 1. Cria a tarefa na coluna "A fazer" (Corrigido!)
        id_da_tarefa = agente.criar_cartao(
            nome_coluna="A fazer",  # 👈 Deixei igualzinho ao seu print
            titulo="Configurar Ambiente de Produção",
            descricao="Tarefa gerada automaticamente pelo Agente Python para estruturação do ambiente.",
        )

        if id_da_tarefa:
            # Aguarda 10 segundos para você conseguir ver a mudança acontecer na tela
            time.sleep(10)

            # 2. Move para "Em andamento"
            agente.mover_cartao(id_da_tarefa, nova_coluna="Em andamento")

            time.sleep(10)

            # 3. Finaliza movendo para "Concluído"
            agente.mover_cartao(id_da_tarefa, nova_coluna="Concluído")

        print("\n🏁 Fluxo concluído! Olhe o seu quadro do Trello.")