---

# 📂 Gerenciador de Tarefas CLI

Este repositório apresenta um **Gerenciador de Tarefas via Terminal (CLI)** desenvolvido inteiramente em Python. Sendo o meu primeiro projeto focado no desenvolvimento Back-end, ele foi projetado entre outubro e dezembro de 2025 com o objetivo de consolidar conceitos de lógica de programação, manipulação de arquivos com o formato JSON, tratamento de exceções e persistência de dados.

O sistema conta com um menu numérico interativo de 9 opções que oferece um ciclo completo de navegação e uso dinâmico para a organização de atividades diárias.

---

## 🚀 Funcionalidades do Sistema

O algoritmo oferece uma interface interativa com as seguintes opções:

1. **Adicionar tarefa**: Criação de novas atividades com preenchimento de descrição e prioridade (`alta`, `media`, `baixa`). Conta com validação interna contra duplicidade.
2. **Listar tarefas**: Exibe o histórico total de atividades cadastradas. Permite uma navegação interna para filtrar e visualizar especificamente apenas as tarefas `Concluídas` ou `Pendentes`.
3. **Marcar como concluída**: Permite alterar o status de uma tarefa para finalizada através do seu ID identificador.
4. **Remover tarefa**: Exclusão de uma atividade específica baseada em seu ID.
5. **Estatísticas Gerais**: Apresenta métricas em tempo real sobre a lista:
   - Quantidade total de tarefas cadastradas.
   - Percentual (%) exato de tarefas concluídas e pendentes.
   - Agrupamento visual das tarefas separadas por níveis de prioridade (Alta, Média e Baixa).
6. **Filtrar por prioridade**: Exibe de forma isolada apenas as tarefas pertencentes à prioridade selecionada pelo usuário.
7. **Remover concluídas**: Menu de gerenciamento de exclusões que permite limpar todas as tarefas concluídas de uma só vez ou remover uma tarefa concluída pessoalmente por ID.
8. **Atualizar tarefa**: Permite editar tarefas existentes, oferecendo a opção de atualizar a descrição e a prioridade em conjunto ou modificar apenas a descrição.
9. **Sair**: Finaliza o loop de execução do programa de forma segura.

---

## 🛠️ Detalhes Técnicos e Soluções de Lógica

A análise técnica do código-fonte destaca soluções inteligentes aplicadas para resolver problemas comuns de persistência e manipulação de coleções de dados:

### 1. Reorganização Sequencial de IDs (`renumera_IDs`)
* **Desafio**: Ao excluir um registro intermediário em uma lista (por exemplo, remover a tarefa de ID `2` em uma sequência de `1` a `3`), o sistema geraria uma lacuna estrutural, pulando diretamente do `1` para o `3`.
* **Solução**: Foi desenvolvida uma função que utiliza a função nativa `enumerate()` do Python. Toda vez que uma tarefa é removida (seja individualmente ou na limpeza em lote), o algoritmo percorre a lista redefinindo o atributo `id` de cada objeto com base em sua nova posição estrutural (`posicao + 1`). Isso garante integridade visual e sequencial contínua para o usuário.

### 2. Controle Inteligente de Duplicatas (`processar_duplicata`)
* **Desafio**: Evitar que tarefas idênticas poluam o gerenciador de forma redundante.
* **Solução**: Antes de salvar um novo registro, o sistema varre o arquivo em busca de descrições idênticas:
  - Se a tarefa correspondente já estiver **Concluída** (`True`), o sistema avisa o usuário e permite que ele atualize a descrição e prioridade mantendo o status de conclusão.
  - Se a tarefa correspondente estiver **Pendente** (`False`), o sistema remove a versão antiga do arquivo automaticamente, reordena as posições e prepara o ambiente para a criação da nova versão atualizada.

### 3. Resiliência a Falhas (Tratamento de Exceções)
* O código utiliza blocos `try...except ValueError` em todas as entradas numéricas cruciais (como na escolha do menu principal, na remoção e na conclusão por ID). Isso impede o encerramento inesperado do programa (*crash*) caso o usuário digite letras ou caracteres inválidos por engano.

---

## 📁 Estrutura de Dados (`tarefas.json`)

A persistência de dados utiliza codificação em formato UTF-8 e recuo estruturado (`indent=2`), simulando o comportamento de um banco de dados documental (NoSQL):

```json
[
  {
    "id": 1,
    "descrição": "Cortar o cabelo",
    "prioridade": "media",
    "conclusao": false
  },
  {
    "id": 2,
    "descrição": "Estudar estruturas de dados em Python",
    "prioridade": "alta",
    "conclusao": true
  }
]
