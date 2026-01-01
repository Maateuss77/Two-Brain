# Breve apresentação

Um site que simplesmente conecta seus pensamentos! Perfeito para aprender algo novo ou revisão.

# Stack
- fastapi
- sqlalchemy 2.0
- sqlite
- pwdlib[argon]

## Organização
O projeto segue uma organição simples. Você encontrar tudo que precisa sobre banco de dados na pasta "Database", as rotas são em "routes". Na pasta "security", vc encontrar os modelos para token e hash de senhas.

Pensando na segurança tenho 2 schemas para os usuarios, onde toda requisição para ver o usuario não mostrará a sua senha em hipotese alguma.1