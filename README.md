# ***Framework de Automação***

---

## ***Fluxograma de Funcionamento do Framework de Desenvolvimento de Scripts de Automação***  
Este fluxograma representa o workflow de funcionamento do framework de desenvolvimento adotado pelo time. Este é um workflow de estados de máquina, onde cada etapa é bem definida por seus estados nomeados na tag de cada seção.

---

### ***1. Initialize Environment***  
O fluxo se inicia no estado de **Initialize Environment**, com o objetivo de lidar com todo tipo de configuração relacionada ao ambiente de execução do script:  
- Limpeza/criação de pastas a serem utilizadas.  
- Inicialização de variáveis globais.  
- Criação de tabelas para coleta de informações de relatório.

#### ***Descrição de Funções:***  
- **`read_config_file`**  
  - Lê o arquivo JSON de configuração para obter variáveis necessárias.  
  - **Output:** Variáveis globais configuradas para uso em outras etapas do framework.  

- **`create_queue_items`**  
  - Lê o JSON de itens de fila e retorna uma lista com esses itens e suas informações.  
  - **Observação:** Cada item recebe um contador de tentativas para gerenciar o número máximo de reprocessamentos.  

- **`clear_create_temp_folder`**  
  - Limpa ou cria pastas temporárias utilizadas pela automação.  
  - **Recomendação:** Todas as pastas devem estar dentro da estrutura local do projeto.  

- **`create_general_variables`**  
  - Cria variáveis globais, como logs e informações de erros/sucessos, para uso em outros estados.  

---

### ***2. Initialize Applications***  
O estado **Initialize Applications** é responsável por preparar as aplicações utilizadas no processo.  

#### ***Descrição de Funções:***  
- **`kill_all_applications`**  
  - Encerra os processos das aplicações que serão utilizadas na automação.  

- **`initialize_all_applications`**  
  - Inicializa as aplicações necessárias, realiza logins e acessa transações.  
  - **Output:** Variáveis que apontam para as instâncias das aplicações.  

---

### ***3. Get Queue Items***  
Gerencia os itens de fila que serão processados pelo fluxo.  

#### ***Descrição de Funções:***  
- **`get_queue_items`**  
  - Lê os itens de fila do JSON e os organiza em uma lista aguardando processamento.  

- **`replicate_item`**  
  - Verifica se um item falhou durante o processamento e o replica no final da fila.  
  - **Observação:** O contador de tentativas é incrementado, respeitando o limite de reprocessamento.  

---

### ***4. Process***  
Executa o fluxo principal do processo que se deseja automatizar.  

#### ***Possíveis Saídas:***  
1. **Sucesso**  
2. **Exceção de Sistema (SE):** Problemas relacionados a aplicações ou sistemas.  
3. **Exceção de Regra de Negócio (BRE):** Problemas com dados de entrada.  

#### ***Descrição de Funções:***  
- **`process`**  
  - Executa o passo a passo do processo principal.  

- **`consolidate_report`**  
  - Consolida as informações de relatório em um arquivo Excel para envio por e-mail.  
  - **Observação:** Inclui tabelas adicionais criadas pelo desenvolvedor.  

- **`send_mail_to_user`**  
  - Envia o relatório consolidado aos usuários da automação.  

- **`update_queue_item_status_system_exception`**  
  - Atualiza o status de itens com erro de sistema (SE), registrando origem e mensagem do erro.  

---

### ***5. Final State***  
Finaliza o processo, consolidando resultados e notificando as partes envolvidas.  

#### ***Descrição de Funções:***  
- **`send_items_to_data_lake`**  
  - Envia os dados de execução e informações dos itens processados para o data lake.  

- **`update_queue_item_status_success`**  
  - Atualiza o status de itens processados com sucesso.  

- **`update_queue_item_status_business_rule_exception`**  
  - Atualiza o status de itens com exceção de regra de negócio (BRE), registrando origem e mensagem do erro.  

- **`send_mail_to_dev_team`**  
  - Envia um e-mail ao time de desenvolvimento com relatórios e logs detalhados.  

---

## ***Melhorias Futuras***  
- Suporte a múltiplos threads para processamento paralelo.  
- Logs centralizados com integração a ferramentas de monitoramento.  
- Interface gráfica para configuração dinâmica do framework.  

---

**Time de Desenvolvimento**  
*Framework de Automação - Versão Beta 0.0.1*  
