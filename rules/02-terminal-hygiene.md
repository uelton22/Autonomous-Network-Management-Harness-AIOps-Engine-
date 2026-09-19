# Diretrizes de Higiene de Terminal SSH (Terminal Hygiene)

Esta regra define as práticas obrigatórias para gerenciamento de sessões CLI em equipamentos de rede multi-vendor, prevenindo travamentos de paginação (`--More--`) e estouros de buffer.

---

## 1. Desativação Obrigatória de Paginação (Pagers)
Antes de enviar qualquer comando de coleta que possa gerar saídas longas, a sessão SSH deve desativar a paginação interativa:

| Fabricante / SO | Comando de Desativação | Escopo |
| :--- | :--- | :--- |
| **Huawei VRP** | `screen-length 0 temporary` | Sessão atual apenas (não altera running-config) |
| **Datacom DmOS** | `terminal length 0` | Sessão atual apenas |
| **Cisco IOS / IOS-XE** | `terminal length 0` | Sessão atual apenas |
| **Juniper JunOS** | `set cli screen-length 0` | Sessão atual apenas |

> [!WARNING]
> Nunca execute comandos que gravem a remoção de paginação de forma persistente no running-config do equipamento de produção.

---

## 2. Detecção de Prompts e Encerramento Limpo
1. **Timeouts**: Comandos de leitura devem ter timeout máximo de 15 segundos. Se o prompt de retorno não for detectado nesse período, a conexão deve ser encerrada para não deixar processos orfãos no plano de controle do switch.
2. **Tratamento de Caracteres Especiais**: O runner deve tratar retornos de carro (`\r\n`), sequências de escape ANSI e caracteres de controle antes de gravar o arquivo `.raw`.
