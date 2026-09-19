# Cenário de Teste 03: Pipeline Híbrido TTP, Sandbox e Cache Hit

## Objetivo
Testar a inteligência do motor TTP em caso de **Cache Miss**, auto-cura via LLM/Sandbox e comprovar que a segunda chamada atinge **Tier 1 (< 5ms)**.

## Etapas do Teste
1. Excluir temporariamente qualquer template existente para `get_system_version` de Datacom.
2. Executar a ação canônica:
   - Constatar **Cache Miss**.
   - O motor executa **Chunk Sampling** (Head 15 + Body 20 + Tail 10 linhas).
   - O sintetizador gera o template TTP.
   - O Sandbox testa o template no `.raw` integral.
   - O schema `DeviceInfoSchema` valida os dados com sucesso.
   - O template é salvo em `storage/templates/get_system_version/datacom_dmos__12_0_2.ttp`.
3. Executar a mesma ação pela segunda vez:
   - Constatar **Cache Hit** instantâneo no **Tier 1 (< 5ms)** com zero gasto de tokens!
