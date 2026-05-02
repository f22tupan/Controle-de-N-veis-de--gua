# Controle de Níveis de Água 💧

Este projeto é um sistema simples de monitoramento para um reservatório de água, desenvolvido como parte da **Agenda 11 de Desenvolvimento de Sistemas I**. O programa exibe mensagens de alerta coloridas no terminal de acordo com o nível de água atual.

## 🚀 Objetivo
Simular o funcionamento de um ambiente real de monitoramento, utilizando listas, funções e a biblioteca externa `colorama` para melhorar a visualização das situações.

## 🛠️ Tecnologias Utilizadas
* **Python**: Linguagem de programação principal.
* **Colorama**: Biblioteca utilizada para destacar cada situação com uma cor específica.
* **Bibliotecas Padrão**: Uso de estruturas como listas e a função `range()`.

## 📋 Funcionalidades
O sistema trabalha com 5 níveis de alerta:
1.  **Nível 1**: Muito baixo (crítico) - Cor Vermelha
2.  **Nível 2**: Baixo - Cor Amarela
3.  **Nível 3**: Médio - Cor Verde
4.  **Nível 4**: Alto - Cor Ciano
5.  **Nível 5**: Muito alto (alerta) - Cor Azul

## 🔧 Como executar
1. Certifique-se de que o Python está instalado.
2. Instale a biblioteca `colorama` através do terminal:
   ```bash
   pip install colorama
Execute o programa:

Bash
python Carlos_Ag11_DSI.py
📊 Exemplo de saída
O programa percorre os níveis e exibe:

Nível 1: Muito baixo (crítico) (Texto em Vermelho)

Nível 2: Baixo (Texto em Amarelo)

Nível 3: Médio (Texto em Verde)

Nível 4: Alto (Texto em Ciano)

Nível 5: Muito alto (alerta) (Texto em Azul)

🎯 Competências trabalhadas
Uso de listas para organizar dados e mensagens.

Criação e utilização de funções para definir cores.

Importação e aplicação de bibliotecas externas via pip.

Simulação de sistemas aplicando princípios de programação.