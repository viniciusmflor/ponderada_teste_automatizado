# Testes do Projeto GestorIN

Este diretório contém os testes automatizados e documentação do projeto GestorIN.

## Caso de Teste: Verificação de Disponibilidade do Frontend

### Objetivo
Verificar se o Frontend Angular está online e respondendo corretamente às requisições.

### Pré-condição
- O servidor frontend Angular deve estar em execução na porta 4200
- Ambiente de desenvolvimento configurado corretamente

### Procedimento de Teste
1. Enviar uma requisição GET para o frontend na porta 4200
2. Analisar o código de status da resposta
3. Verificar o conteúdo da resposta HTML

### Resultado Esperado
- Frontend deve responder com status 200 (OK)
- A resposta deve conter HTML válido da aplicação Angular

### Resultado Obtido
Os resultados serão registrados automaticamente em arquivos Markdown na pasta `resultados/` após a execução do teste.

### Pós-condição
Nenhuma alteração no sistema é esperada após este teste, pois trata-se de uma operação apenas de leitura.

## Como Executar os Testes

### Requisitos
- Python 3.6 ou superior
- Biblioteca `requests` instalada

### Instalação das Dependências
```bash
pip install requests
```

### Executando o Teste
```bash
python testes/test-front/test_front.py
```

Os resultados serão exibidos no console e também salvos em formato Markdown na pasta `testes/resultados/`. 