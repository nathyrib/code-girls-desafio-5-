#  Desafio 5 - Automatizando Tarefas com AWS Lambda e S3

Nesse desafio foi pedido para consolidar conhecimentos em tarefas automatizadas utilizando AWS Lambda e S3 e fazer anotações. O objetivo é simular a automação de processos em nuvem, aplicando conceitos de eventos, funções serverless e integração com serviços de armazenamento.


---

## 🎯 Objetivos

- Aplicar conceitos de automação com Lambda Functions;
- Simular o acionamento de funções por eventos do S3;
- Documentar o processo técnico de forma clara e estruturada;
- Utilizar o GitHub como ferramenta de versionamento e compartilhamento.

---

## 🧰 O que é AWS Lambda?

AWS Lambda é um serviço que executa código automaticamente em resposta a eventos, sem precisar de servidores. É ideal para tarefas rápidas e automatizadas, como processar arquivos enviados ao S3.

---

## 📦 O que é Amazon S3?

Amazon S3 é um serviço de armazenamento de arquivos na nuvem. Ele guarda documentos, imagens e outros dados, e pode gerar eventos quando novos arquivos são enviados — como acionar uma função Lambda.

---

## 📍 Estrutura da Solução

### 🗂 Arquivos

- `lambda_function.py`: contém o código da função Lambda
- `event.json`: simula o evento de upload no S3 que aciona a função

### 🧾 Explicação Técnica

A função Lambda é acionada automaticamente quando um arquivo é enviado ao bucket S3. Ela extrai o nome do bucket e do arquivo e simula um processamento, retornando uma mensagem de sucesso.

---

## ✨️ Simulação do Funcionamento

- O arquivo `event.json` representa um evento de upload no S3.
- A função `lambda_handler` é acionada automaticamente.
- Ela processa o evento e retorna uma resposta simulada.

---

## 📝 Aprendizados

- Compreensão da estrutura de eventos do S3.
- Criação de funções Lambda simples e eficazes.
- Simulação de ambientes serverless sem depender da AWS.
- Organização de documentação técnica para reuso e estudo.
