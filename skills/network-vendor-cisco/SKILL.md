---
name: network-vendor-cisco
description: Base de conhecimento especializada do sistema operacional Cisco IOS e IOS-XE (roteadores ISR/ASR e switches Catalyst).
---

# Vendor Skill: Cisco IOS / IOS-XE

O Cisco IOS e IOS-XE constituem o padrão de referência CLI da indústria, baseado no verbo `show`.

## 1. Padrões de Prompt e Conexão
- **Modo Usuário**: `hostname>`
- **Modo Privilegiado (Enable)**: `hostname#`
- **Desativação de Pager**: `terminal length 0`

## 2. Comandos Canônicos Mapeados
- **Versão e Uptime**: `show version`
- **Hardware**: `show inventory`
- **Interfaces (Resumo)**: `show ip interface brief`
- **Interfaces (Detalhe)**: `show interface {interface_name}`
- **BGP**: `show ip bgp summary`
