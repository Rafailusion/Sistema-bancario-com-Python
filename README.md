
# Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python que permite realizar operações básicas como depósito, saque, consulta de saldo e visualização de extrato.

## Funcionalidades

### Depósito

Permite adicionar fundos à conta bancária. O valor depositado é adicionado ao saldo e registrado no extrato.

### Saque

Permite retirar fundos da conta bancária, respeitando as seguintes regras:

- Limite de três saques diários.
- Valor máximo de R\$ 500,00 por saque.
- O saldo deve ser suficiente para a operação.

### Consulta de Saldo

Exibe o saldo atual da conta bancária.

### Visualização de Extrato

Mostra todas as movimentações realizadas (depósitos e saques) e o saldo atual.

---

## Requisitos

- Python 3.x instalado no sistema.

---

## Como Utilizar

1. Clone o repositório ou copie o código fornecido.
2. Execute o arquivo Python em seu terminal ou IDE:

```bash
python nome_do_arquivo.py
```

3. Navegue pelo menu interativo para realizar as operações bancárias.

---

## Exemplo de Uso

### Depósito

- Usuário informa o valor do depósito: `R$ 200,00`.
- Sistema atualiza o saldo e registra no extrato:

```
Depósito realizado: R$ 200.00
```

### Saque

- Usuário solicita um saque de `R$ 100,00`.
- Sistema verifica os limites e realiza a operação:

```
Saque realizado: R$ 100.00
```

### Consulta de Saldo

- Usuário escolhe a opção de mostrar saldo:

```
Saldo atual: R$ 100.00
```

### Visualização de Extrato

- Usuário solicita o extrato:

```
=== Extrato ===
Depósito: R$ 200.00
Saque: R$ 100.00
Saldo atual: R$ 100.00
================
```

---

## Estrutura do Código

### Classe `Banco`

Responsável por gerenciar as operações bancárias e armazenar o estado da conta (saldo, extrato, limite de saques).

### Função `menu`

Interface de interação com o usuário. Permite navegar pelas funcionalidades do sistema através de um menu.

---

## Melhorias Futuras

- Adicionar autenticação de usuários (login e senha).
- Implementar persistência de dados (salvar informações em arquivos ou banco de dados).
- Suporte a múltiplas contas.
- Implementar transferências entre contas.

---

## Licença

Este projeto é de uso livre e aberto para modificação e distribuição.

# Entre em contato: 

[Email](<rafaelcesarprestes\@gmail.com>)\
[Linkedin](<https://www.linkedin.com/in/rafaelcesarprestes>)\
[Github](<https://github.com/Rafailusion>)

