import requests
import json
import os
import sys
from datetime import datetime

# Definição do teste
TEST_NAME = "Teste de disponibilidade do Frontend"
TEST_OBJECTIVE = "Verificar se o Frontend Angular está online e respondendo corretamente"
PRE_CONDITION = "Servidor frontend Angular deve estar em execução na porta 4200"
TEST_PROCEDURE = "Fazer uma requisição GET para o frontend"
EXPECTED_RESULT = "Frontend deve responder com status 200"
POST_CONDITION = "Nenhuma alteração no sistema é esperada após este teste"

def run_test():
    """
    Executa o teste de disponibilidade do Frontend
    """
    print(f"Executando: {TEST_NAME}")
    print(f"Objetivo: {TEST_OBJECTIVE}")
    print(f"Pré-condição: {PRE_CONDITION}")
    print(f"Procedimento: {TEST_PROCEDURE}")
    
    # URL do frontend
    frontend_url = "http://localhost:4200"
    
    try:
        # Requisição para o frontend
        print(f"\nTestando Frontend na URL: {frontend_url}")
        response = requests.get(frontend_url, timeout=5)
        
        # Verificando o resultado
        if response.status_code == 200:
            result = "PASSOU"
            details = f"Frontend respondeu com status {response.status_code}"
            # O frontend normalmente retorna HTML, então não tentamos interpretar como JSON
            # Apenas pegamos os primeiros 200 caracteres para o relatório
            details += f" e conteúdo HTML (primeiros 200 caracteres): {response.text[:200]}..."
            
        else:
            result = "FALHOU"
            details = f"Frontend respondeu com status {response.status_code} ao invés de 200"
            
    except requests.RequestException as e:
        result = "FALHOU"
        details = f"Erro ao conectar com o Frontend: {str(e)}"
    
    # Registrando resultado
    print(f"Resultado esperado: {EXPECTED_RESULT}")
    print(f"Resultado obtido: {details}")
    print(f"Status do teste: {result}")
    print(f"Pós-condição: {POST_CONDITION}")
    
    # Gerar relatório
    generate_report(result, details)
    
    return result == "PASSOU"

def generate_report(result, details):
    """
    Gera um relatório de teste em Markdown
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report_content = f"""# Relatório de Teste do Frontend

## {TEST_NAME}
- **Data e Hora:** {timestamp}
- **Status:** {result}

## Detalhes do Teste
- **Objetivo:** {TEST_OBJECTIVE}
- **Pré-condição:** {PRE_CONDITION}
- **Procedimento:** {TEST_PROCEDURE}
- **Resultado Esperado:** {EXPECTED_RESULT}
- **Resultado Obtido:** {details}
- **Pós-condição:** {POST_CONDITION}

"""
    
    # Salvar relatório em arquivo
    os.makedirs("testes/resultados", exist_ok=True)
    report_file = f"testes/resultados/resultado_teste_frontend_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    
    with open(report_file, "w") as f:
        f.write(report_content)
    
    print(f"Relatório gerado em: {report_file}")

if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1) 