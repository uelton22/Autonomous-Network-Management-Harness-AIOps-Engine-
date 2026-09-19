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
