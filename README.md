# ***TODO - SAMUEL***

---

## ***ITENS DE FILA***  
Os itens de fila virão sem JOB_ID, cada vez que um Queue_item seja selecionado ele será atribuido ao evento(JOB_ID) atual, e esse evento vai se encarregar de processar esse item de fila

- Caso ele seja finalizado com sucesso, o seu log será atualizado no banco de dados

- Caso ele nao seja finalizado com sucesso após todos os retries, ele será finalizado como falha

- Caso ocorra algum problema e alguns Queue_items nao foram processados, o novo evento ira pegar os Queue_items que não possuem JOB_ID e tomara conta deles

---

## ***CRIAÇÃO DE ITENS DE FILA***  
- Criar um modulo apenas para criação de Queue_items

---
**Time de Desenvolvimento**  
*Framework de Automação - Versão Beta 0.0.1*  
