# 🛡️ SocketLens

**SocketLens** é uma ferramenta modular de exploração de rede e auditoria de segurança desenvolvida em Python. O objetivo deste projeto é fornecer uma "lente" clara sobre portas abertas, protocolos web e vulnerabilidades de configuração.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

## 🚀 Funcionalidades

O projeto é dividido em módulos especializados:

* **LensPort (Scanner de Portas):** Identifica portas TCP abertas de forma eficiente, tratando timeouts e erros de conexão.
* **LensWeb (Validador HTTPS):** Verifica a presença de certificados SSL/TLS e analisa cabeçalhos de segurança (como `Server` e `X-Frame-Options`).
* **Streaming de Logs:** Processamento de arquivos de IP em tempo real, garantindo baixo consumo de memória RAM (ideal para grandes volumes de dados).

## 📁 Estrutura do Projeto

```text
SocketLens/
├── main.py                # Interface de linha de comando (Menu)
├── modules/
│   ├── Lens_Port.py         # Lógica de escaneamento de portas
│   └── Lens_Web.py   # Lógica de validação de protocolos web
├── ips.txt                # Lista de alvos para processamento em lote
└── relatorio_final.txt    # Saída dos resultados
```