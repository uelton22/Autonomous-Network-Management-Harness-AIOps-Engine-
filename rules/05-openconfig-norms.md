# Diretrizes de Normalização Canônica OpenConfig

Esta regra estabelece as diretrizes para padronização de dados de múltiplos fabricantes sob os esquemas JSON definidos em `registry/schemas/`.

---

## 1. Mapeamento de Status de Interface
Diferentes fabricantes utilizam convenções distintas de status:

| Fabricante / CLI | Admin Status | Oper Status | Normalizado OpenConfig |
| :--- | :--- | :--- | :--- |
| Huawei: `up / up` | `UP` | `UP` | `admin_status: "UP"`, `oper_status: "UP"` |
| Huawei: `*down / down` | `*down` | `down` | `admin_status: "DOWN"`, `oper_status: "DOWN"` |
| Datacom: `UP / DOWN` | `UP` | `DOWN` | `admin_status: "UP"`, `oper_status: "DOWN"` |
| Cisco: `administratively down / down` | `down` | `down` | `admin_status: "DOWN"`, `oper_status: "DOWN"` |

Todos os estados devem ser mapeados estritamente para `UP`, `DOWN` ou `TESTING`.

---

## 2. Unidades e Tipagem Canônica
- **Velocidade (Speed)**: Sempre em bits por segundo (bps). Ex: `1000000000` para 1Gbps, `10000000000` para 10Gbps.
- **Endereço MAC**: Sempre no formato hexadecimal padrão `aa:bb:cc:dd:ee:ff` em minúsculas (convertendo formatos Huawei `aabb-ccdd-eeff` ou Cisco `aabb.ccdd.eeff`).
- **Uptime**: Sempre armazenar tanto o valor numérico em segundos (`uptime_seconds`) quanto a descrição amigável (`uptime_str`).

---

## 3. Neutralidade de Fabricante e Nomenclatura Canônica

Ao definir ou estender schemas em `registry/schemas/`, é expressamente **proibido** utilizar termos proprietários de um único fabricante na raiz do modelo de dados.

### Tabela de Equivalências Canônicas Obrigatórias:

| Termo Proprietário / Viés Local | Padrão Canônico OpenConfig Obrigatório |
| :--- | :--- |
| `lags` (Datacom) ou `eth_trunks` (Huawei) ou `etherchannels` (Cisco) | `link_aggregations` (lista de agregações com `members`) |
| `vlanifs` (Huawei) ou `svis` (Cisco) | `routed_vlan_interfaces` ou `interfaces` |
| `bundle_ether` (Cisco XR) | `link_aggregations` |
| `loopbacks` (Cisco) ou `loops` (Huawei) | `interfaces` (com tipo `LoopBack`) |
| `tunnels` | `interfaces` (com tipo `Tunnel`) |

---

## 4. Estrutura Padrão de Schemas OpenConfig

Todo schema JSON em `registry/schemas/` e modelo Pydantic em `mcp_server/schemas/` DEVE seguir esta anatomia canônica:
1. `device`: String obrigatória com hostname ou IP.
2. `summary`: Objeto opcional contendo contadores agregados pré-calculados determinísticamente em código local (evitando alucinações de contagem pela LLM).
3. Entidade de coleção (plural): Array principal (ex: `link_aggregations`, `interfaces`, `neighbors`, `peers`).
4. `collected_at`: String ISO-8601 UTC.

