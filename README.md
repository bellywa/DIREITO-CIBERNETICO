# Sistema de Análise de Dados com Conformidade à LGPD

Este projeto é um sistema de análise de dados desenvolvido para ajudar alunos de cursinhos preparatórios de medicina a identificar suas fraquezas acadêmicas, em conformidade com a Lei Geral de Proteção de Dados (LGPD). O sistema também oferece uma plataforma segura para professores acompanharem o desempenho dos alunos e adaptarem suas aulas de forma personalizada.

## Funcionalidades

1. *Cadastro de Usuários com Consentimento*:
   - Os alunos se cadastram no sistema, com a obrigatoriedade de consentimento para o uso dos seus dados.
   - Utiliza hash de senha com *bcryptjs* e gera tokens JWT para autenticação.

2. *Anonimização de Dados*:
   - Função de anonimização para proteger os dados pessoais dos alunos, mantendo apenas dados relevantes para análise.

3. *Criptografia de Dados Sensíveis*:
   - Criptografia de informações sensíveis usando *AES-256-CTR* para garantir a segurança dos dados armazenados.

4. *Painel de Gerenciamento de Consentimento*:
   - Os usuários podem visualizar e gerenciar as permissões de uso dos seus dados, assegurando transparência e conformidade com a LGPD.

## Tecnologias Utilizadas

- *Node.js*: Plataforma de servidor para o backend.
- *Express*: Framework para criação de APIs RESTful.
- *MongoDB*: Banco de dados NoSQL para armazenar os dados dos alunos.
- *Mongoose*: ODM para facilitar o uso do MongoDB com Node.js.
- *bcryptjs*: Para hash de senhas.
- *jsonwebtoken (JWT)*: Para autenticação segura com tokens.
