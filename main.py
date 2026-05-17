
# DATA DE INICIALIZAÇÃO - 24/10/2025
# DATA DE FINALIZAÇÃO - 13/12/2025

# OBS: Meu primeiro projeto

import json
import os

ARQUIVO_TAREFAS = "tarefas.json"

# Função para salvar tarefas


def salvar_tarefas():
    try:
        with open(ARQUIVO_TAREFAS, 'w', encoding='utf-8') as arquivo:
            json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"❌ Erro ao salvar tarefas: {e}")

# Função para carregar tarefas


def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        try:
            with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except:
            print("❌ Erro ao carregar tarefas. Iniciando com lista vazia.")
            return []
    return []


# Carregar tarefas ao iniciar o programa
tarefas = carregar_tarefas()
proximo_id = max([t['id'] for t in tarefas]) + 1 if tarefas else 1

# Função para linhas no terminal


def linhaDeSeparacao(tamanho):
    print(tamanho*'_')


# Função para renumerar IDs

def renumera_IDs():
    global proximo_id
    for posicao, tarefa in enumerate(tarefas):
        tarefa['id'] = posicao + 1
    proximo_id = len(tarefas) + 1
    salvar_tarefas()

# Função para processar duplicatas


def processar_duplicata(descricao, prioridade):
    for tarefa in tarefas:
        if tarefa['descrição'] == descricao:
            print("\n⚠️ TAREFA DUPLICATA ENCONTRADA⚠️")
            if tarefa['conclusao'] == True:
                print(f"\nTAREFA JÁ EXISTE, E ESTÁ CONCLUÍDA!")
                print(f"\nDescrição atual: {tarefa['descrição']}")

                nova_descricao = input("\nNova descrição: ")

                if nova_descricao:
                    tarefa['descrição'] = nova_descricao

                tarefa['prioridade'] = prioridade
                salvar_tarefas()

                print("\nTarefa atualizada (mantida como concluída)")
                print(f"\nID: {tarefa['id']}")
                print(f"Descrição: {tarefa['descrição']}")
                print(f"Prioridade: {tarefa['prioridade']}")
                print(f"Conclusao: {tarefa['conclusao']}")
                return "atualizada"

            else:
                tarefas.remove(tarefa)
                renumera_IDs()
                salvar_tarefas()
                print("\nTarefa pendente removida (será recriada)")
                return "removida"

    return None

# Função para adicionar tarefa


def adicionar_tarefa():
    global proximo_id
    descricao = input("\nDigite a descrição da atividade: ")
    prioridade = input(
        "Digite a prioridade da tarefa (alta/media/baixa): ").lower()

    resultado = processar_duplicata(descricao, prioridade)

    if resultado == "atualizada":
        return

    if resultado == "removida":
        print("Criando nova versão da tarefa...")

    if prioridade not in ['alta', 'media','média', 'baixa']:
        print("\n❌ Prioridade inexistente")
        print("Tarefa não cadastrada")
        return

    nova_tarefa = {
        'id': proximo_id,
        'descrição': descricao,
        'prioridade': prioridade,
        'conclusao': False,
    }

    proximo_id += 1
    tarefas.append(nova_tarefa)
    salvar_tarefas()
    print("\nTarefa cadastrada✅")

# Função para listar todas as tarefas


def listar_tarefas():
    concluidas = []
    pendentes = []

    linhaDeSeparacao(80)
    print(f"\n=== HISTÓRICO DE ATIVIDADES ({len(tarefas)}) ===")
    if tarefas:
        for tarefa in tarefas:
            print(f"\nID: {tarefa['id']}")
            print(f"Descrição: {tarefa['descrição']}")
            print(f"Prioridade: {tarefa['prioridade']}")
            print(f"Conclusao: {tarefa['conclusao']}")
    else:
        print("\nNenhuma tarefa cadastrada")
    linhaDeSeparacao(80)

    print("\nSe quiser ver as terefas concluídas e pendentes.")
    print("Digite (1) para concluídas ou (2) pendentes. Digite (3) para sair")

    mostra_tarefas = input("\nDigite um das opções: ")

    for tarefa in tarefas:
        if tarefa['conclusao'] == True:
            concluidas.append(tarefa)
        else:
            pendentes.append(tarefa)

    if mostra_tarefas == '1':
        print(f"\n=== ATIVIDADE(S) CONCLUÍDA(S) ({len(concluidas)}) ===")

        if concluidas:
            for tarefa in concluidas:
                print(f"\nID: {tarefa['id']}")
                print(f"Descrição: {tarefa['descrição']}")
                print(f"Prioridade: {tarefa['prioridade']}")
                print(f"Conclusao: {tarefa['conclusao']}")
        else:
            print("\nNão contém tarefas concluídas")

    elif mostra_tarefas == '2':
        linhaDeSeparacao(80)
        print(f"\n=== TAREFA(S) PENDENTE(S) ({len(pendentes)})===")
        if pendentes:
            for tarefa in pendentes:
                print(f"\nID: {tarefa['id']}")
                print(f"Descrição: {tarefa['descrição']}")
                print(f"Prioridade: {tarefa['prioridade']}")
                print(f"Conclusao: {tarefa['conclusao']}")
        else:
            print("\nNenhuma pendente.")

    elif mostra_tarefas == '3':
        print("saindo...")
        return

    else:
        print("Opção inválida")
    linhaDeSeparacao(80)

# Função para marcar tarefa como concluída


def marca_tarefa_concluida():
    try:
        marca_id = int(input("\nDigite o ID da tarefa para concluir: "))

        tarefa_concluida = None
        for tarefa in tarefas:
            if tarefa['id'] == marca_id:
                tarefa_concluida = tarefa
                break

        if tarefa_concluida:
            if tarefa_concluida['conclusao'] == True:
                linhaDeSeparacao(80)
                print("TAREFA JÁ ESTÁ CONCLUÍDA")
                print(f"\nID: {tarefa_concluida['id']}")
                print(f"Descrição: {tarefa_concluida['descrição']}")
                print(f"Prioridade: {tarefa_concluida['prioridade']}")
                linhaDeSeparacao(80)
            else:
                linhaDeSeparacao(80)

                tarefa_concluida['conclusao'] = True
                salvar_tarefas()
                print("\nTarefa Concluída✅")
                print(f"\nID: {tarefa_concluida['id']}")
                print(f"Descrição: {tarefa_concluida['descrição']}")
                print(f"Prioridade: {tarefa_concluida['prioridade']}")
                print(f"Conclusao: {tarefa_concluida['conclusao']}")

                linhaDeSeparacao(80)
        else:
            print(f"\n❌ Tarefa com o ID {marca_id} não existe")

    except ValueError:
        print("❌ Erro: Digite um número válido para o ID!")
        return

# Função para remover tarefa


def remover_tarefa():
    try:
        remover_id = int(input("\nDigite o ID da tarefa para remover: "))

        tarefa_pra_remover = None
        for tarefa in tarefas:
            if tarefa['id'] == remover_id:
                tarefa_pra_remover = tarefa
                break

        if tarefa_pra_remover:
            tarefas.remove(tarefa_pra_remover)
            renumera_IDs()
            linhaDeSeparacao(80)
            print("\nRemovendo a tarefa...")
            print(f"\nID: {tarefa_pra_remover['id']}")
            print(f"Descrição: {tarefa_pra_remover['descrição']}")
            print(f"Prioridade: {tarefa_pra_remover['prioridade']}")
            print(f"Conclusao: {tarefa_pra_remover['conclusao']}")
            print("\nTarefa removida com sucesso👌")
            linhaDeSeparacao(80)
        else:
            print(f"\n❌ Tarefa com ID {remover_id} não existe.")
    except ValueError:
        print("❌ Erro: Digite um número válido para o ID!")
        return
# Função de estatísticas


def estatisticas():
    linhaDeSeparacao(80)
    print("\n=== 📊 ESTATÍSTICAS GERAIS 📊 ===")
    print(f"\nTOTAL DE TAREFAS: ({len(tarefas)})")

    lista_tarefas_concluidas = []
    lista_tarefas_pendentes = []
    for tarefa in tarefas:
        if tarefa['conclusao'] == True:
            lista_tarefas_concluidas.append(tarefa)
        else:
            lista_tarefas_pendentes.append(tarefa)

    if lista_tarefas_concluidas:
        porcentagem_concluidas = (
            len(lista_tarefas_concluidas) / len(tarefas)) * 100
        print(
            f"\nPERCENTUAL DE TAREFAS CONCLUÍDAS: {porcentagem_concluidas:.2f}%")
    else:
        print("Sem tarefas concluídas")

    if lista_tarefas_pendentes:
        porcentagem_pendentes = len(lista_tarefas_pendentes) / len(tarefas)*100
        print(
            f"PERCENTUAL DE TAREFAS NÃO FEITAS: {porcentagem_pendentes:.2f}%")
    else:
        print("\nNão tem tarefas pendentes")

    tarefas_altas = []
    tarefas_medias = []
    tarefas_baixas = []

    for tarefa in tarefas:
        if tarefa['prioridade'] == "alta":
            tarefas_altas.append(tarefa)
        elif tarefa['prioridade'] == "media":
            tarefas_medias.append(tarefa)
        elif tarefa['prioridade'] == "baixa":
            tarefas_baixas.append(tarefa)

    linhaDeSeparacao(80)
    print("\n🟢 TAREFA(S) COM PRIORIDADDE ALTA")
    if tarefas_altas:
        for tarefa in tarefas_altas:
            status_alta = f"ID: {tarefa['id']} - Descrição: {tarefa['descrição']}"
            print(f"\n{status_alta}")
    else:
        print("\nVazio")

    linhaDeSeparacao(80)
    print("\n🟡 TAREFA(S) COM PRIORIDADE MEDIA")
    if tarefas_medias:
        for tarefa in tarefas_medias:
            status_media = f"ID: {tarefa['id']} - Descrição: {tarefa['descrição']}"
            print(f"\n{status_media}")
    else:
        print("\nVazio")

    linhaDeSeparacao(80)
    print("\n🔴 TAREFA(S) COM PRIORIDADE BAIXA")
    if tarefas_baixas:
        for tarefa in tarefas_baixas:
            status_baixa = f"ID: {tarefa['id']} - Descrição: {tarefa['descrição']}"
            print(f"\n{status_baixa}")
    else:
        print("\nVazio")
    linhaDeSeparacao(80)

# Função para filtrar por prioridade


def filtro_de_prioridade():
    prioridade_alta = []
    prioridade_media = []
    prioridade_baixa = []

    for tarefa in tarefas:
        if tarefa['prioridade'] == "alta":
            prioridade_alta.append(tarefa)
        elif tarefa['prioridade'] == "media":
            prioridade_media.append(tarefa)
        else:
            prioridade_baixa.append(tarefa)

    usuario_prioridade = input(
        "\nDigite a prioridade que queira listar (alta/media/baixa): ").lower()

    linhaDeSeparacao(80)
    if usuario_prioridade == "alta":
        if prioridade_alta:
            for tarefa in prioridade_alta:
                print(f"\nID: {tarefa['id']}")
                print(f"Descrição: {tarefa['descrição']}")
                print(f"Prioridade: {tarefa['prioridade']}")
                print(f"Conclusao: {tarefa['conclusao']}")
        else:
            print("\nVazio")

    elif usuario_prioridade == "media":
        if prioridade_media:
            for tarefa in prioridade_media:
                print(f"\nID: {tarefa['id']}")
                print(f"Descrição: {tarefa['descrição']}")
                print(f"Prioridade: {tarefa['prioridade']}")
                print(f"Conclusao: {tarefa['conclusao']}")
        else:
            print("\nVazio")

    elif usuario_prioridade == "baixa":
        if prioridade_baixa:
            for tarefa in prioridade_baixa:
                print(f"\nID: {tarefa['id']}")
                print(f"Descrição: {tarefa['descrição']}")
                print(f"Prioridade: {tarefa['prioridade']}")
                print(f"Conclusao: {tarefa['conclusao']}")
        else:
            print("\nVazio")
    else:
        print("\n❌ Prioridade inexistente")
    linhaDeSeparacao(80)
# Remover tarefas concluídas


def remover_concluidas():

    tarefasPraRemover = []
    linhaDeSeparacao(80)
    print("\n=== TODAS AS TAREFAS CONCLUÍDAS ===")

    for tarefa in tarefas:
        if tarefa['conclusao'] == True:
            tarefasPraRemover.append(tarefa)

    if tarefasPraRemover:
        for tarefa in tarefasPraRemover:
            print(f"\nID: {tarefa['id']}")
            print(f"Descrição: {tarefa['descrição']}")
            print(f"Prioridade: {tarefa['prioridade']}")

    else:
        print("Vazio")
    linhaDeSeparacao(80)

    try:
        opcaoDeRemocao = int(input(
            "\nDigite (1) remove todas as tarefas concluídas, (2) remove uma tarefa e (3) pra sair: "))

        if opcaoDeRemocao == 1:
            # Remosão total de tarefas
            print("\nRemovendo tarefas 🗑️...")
            print("todas removidas, com sucesso")
            for tarefa in tarefasPraRemover:
                if tarefasPraRemover:
                    tarefas.remove(tarefa)
                    renumera_IDs()
            else:
                print("\nNão tem tarefas.")

        elif opcaoDeRemocao == 2:

            buscarID = int(
                input("\nSelecione um ID para remover a tarefa específica"))
            tarefa_especifica = None
            for tarefa in tarefasPraRemover:
                if tarefa['id'] == buscarID:
                    tarefa_especifica = tarefa
                    tarefas.remove(tarefa_especifica)
                    renumera_IDs()
                    salvar_tarefas()
                    print("\nTAREFA ENCONTRADA E REMOVIDA")
                    print(f"\nID: {tarefa_especifica['id']}")
                    print(f"Descrição: {tarefa_especifica['descrição']}")
                    print(f"Prioridade: {tarefa_especifica['prioridade']}")
                    print(f"Conclusao: {tarefa_especifica['conclusao']}")
                    break
        elif opcaoDeRemocao == 3:
            print("\nSaiu 😎")
            return

        else:
            print("\nOpção inválida")
            return
    except ValueError:
        print("\nErro de digitação ⚠️")
        return

# Atualizar descrição e prioridade


def atualizar_tarefa():
    try:
        IdPraAtualizar = int(input("Digite o ID  tarefa, para atualiza-la: "))

        tarefaPraAtualizar = None
        for tarefa in tarefas:
            if tarefa['id'] == IdPraAtualizar:
                tarefaPraAtualizar = tarefa
                break

        if tarefaPraAtualizar:
            linhaDeSeparacao(80)
            print("\n=== TAREFA ATUAL ===")

            print(f"\nID: {tarefaPraAtualizar['id']}")
            print(f"Descrição: {tarefaPraAtualizar['descrição']}")
            print(f"Prioridade: {tarefaPraAtualizar['prioridade']}")
            print(f"Conclusao: {tarefaPraAtualizar['conclusao']}")

            print("\nDigite (1) para atualizar a descrição e prioridade, (2) pra somente descrição ou (3) para sair")
            opcao_atualizar = input("\nDigite um das opções: ")

            if opcao_atualizar == '1':
                print(
                    f"\n==> DESCRIÇÃO DA TAREFA: {tarefaPraAtualizar['descrição']}")

                nova_descricao = input("\nDigite a nova descrição: ")

                if nova_descricao:
                    tarefaPraAtualizar['descrição'] = nova_descricao
                    print("\ndescrição atualizada ✅")
                    salvar_tarefas()
                else:
                    print(
                        "\n⚠️  Usuário não digitou nada, tarefa mantida com mesma descrição⚠️")

                print(
                    f"\n==> PRIORIDADE DA TAREFA: {tarefaPraAtualizar['prioridade']}")

                nova_prioridade = input(
                    "\nA nova prioridade (alta/media/baixa): ")

                if nova_prioridade not in ['alta', 'media', 'baixa']:
                    print("Prioridade inválida")
                    print("Tarefa não atualizada!")

                if nova_prioridade:
                    tarefaPraAtualizar['prioridade'] = nova_prioridade
                    print("\nPrioridade atualizada ✅")
                    salvar_tarefas()

                    print("\n=== TAREFA ATUALIZADA ===")
                    print(f"\nID: {tarefaPraAtualizar['id']}")
                    print(f"Descrição: {tarefaPraAtualizar['descrição']}")
                    print(f"Prioridade: {tarefaPraAtualizar['prioridade']}")
                    print(f"Conclusao: {tarefaPraAtualizar['conclusao']}")

                else:
                    print(
                        "\n⚠️  Usuário não digitou nada, tarefa mantida com mesma prioridade⚠️")

                    print("\n=== TAREFA NÃO ATUALIZADA ===")
                    print(f"\nID: {tarefaPraAtualizar['id']}")
                    print(f"Descrição: {tarefaPraAtualizar['descrição']}")
                    print(f"Prioridade: {tarefaPraAtualizar['prioridade']}")
                    print(f"Conclusao: {tarefaPraAtualizar['conclusao']}")

            elif opcao_atualizar == '2':
                print(
                    f"\n==> DESCRIÇÃO DA TAREFA: {tarefaPraAtualizar['descrição']}")

                nova_descricao = input("\nA nova descrição: ")

                if nova_descricao:
                    tarefaPraAtualizar['descrição'] = nova_descricao
                    print("\ndescrição atualizada ✅")
                    salvar_tarefas()

                    print("\n=== TAREFA ATUALIZADA ===")
                    print(f"\nID: {tarefaPraAtualizar['id']}")
                    print(f"Descrição: {tarefaPraAtualizar['descrição']}")
                    print(f"Prioridade: {tarefaPraAtualizar['prioridade']}")
                    print(f"Conclusao: {tarefaPraAtualizar['conclusao']}")

                else:
                    print(
                        "\n⚠️  Usuário não digitou nada, tarefa mantida com mesma descrição⚠️")

                    print("\n=== TAREFA NÃO ATUALIZADA ===")
                    print(f"\nID: {tarefaPraAtualizar['id']}")
                    print(f"Descrição: {tarefaPraAtualizar['descrição']}")
                    print(f"Prioridade: {tarefaPraAtualizar['prioridade']}")
                    print(f"Conclusao: {tarefaPraAtualizar['conclusao']}")

            elif opcao_atualizar == '3':
                print("Saiu 😎")

            else:
                print("\nOpção inválida")
        else:
            print(f"\nTarefa com o {IdPraAtualizar} não existe.")

    except ValueError:
        print("Erro detectado, digite novamente")
        return
    linhaDeSeparacao(80)
# Menu do sistema


def menu():
    print("\n=== SISTEMA DE TAREFAS ===")
    print("1.Adicionar tarefa")
    print("2.Listar tarefas")
    print("3.Marcar como concluída")
    print("4.Remover tarefa")
    print("5.Estatísticas")
    print("6.Filtrar por prioridade")
    print("7.Remover concluídas")
    print("8.Atualizar tarefa")
    print("9.Sair")


# Loop principal
while True:
    menu()

    try:
        opcao_usuario = int(input("\nDigite uma das opções do menu: "))
    except ValueError:
        print("\n❌ Erro detectado")
        continue

    if opcao_usuario == 1:
        adicionar_tarefa()
    elif opcao_usuario == 2:
        listar_tarefas()
    elif opcao_usuario == 3:
        marca_tarefa_concluida()
    elif opcao_usuario == 4:
        remover_tarefa()
    elif opcao_usuario == 5:
        estatisticas()
    elif opcao_usuario == 6:
        filtro_de_prioridade()
    elif opcao_usuario == 7:
        remover_concluidas()
    elif opcao_usuario == 8:
        atualizar_tarefa()
    elif opcao_usuario == 9:
        print("\n👋 Saindo do sistema...")
        break
    else:
        print("\n❌ Opção inválida!")
