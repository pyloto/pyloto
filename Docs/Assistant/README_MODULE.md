# AI (módulo)

Visão geral do módulo de IA e seus submódulos.

## Objetivo
Reduzir chamadas LLM e manter a lógica determinística no servidor, usando a IA para:
- Preencher DRAFT com endereços padronizados;
- Aplicar regras de precificação (no Assistant, via arquivo anexado);
- Gerar textos amigáveis de resumo/explicação.

## Submódulos
- `analysis/` — Normalização de texto e inferências heurísticas (categoria/urgência/peso/transporte).
- `assistant_management/` — Auxiliares de interpretação/gerência de mensagens da IA.
- `configuration/` — Constantes e config de prompts/FSM para IA.
- `fsm_bridge/` — Injeção de system prompt por estado da FSM.
- `fsm_integration/` — Validação de eventos e mapeamento de intenções.
- `integration/` — Contrato + tools + cliente de IA (OpenAI).
- `management/` — Prepara insumos e constrói resumo de pedido.
- `openai_integration/` — Parser/validador do retorno do Assistant.
- `pricing/` — Markup e engine local (opcional; regras ficam no Assistant).
- `prompts/` — Prompts por estado (DRAFT prio: padronização de endereço).
- `repository/` — Memória simples (in-memory e base para persistir depois).
- `validation/` — Validador DRAFT.

## Entradas/Saídas principais
- Entrada: mensagens do WhatsApp → FSM → IA quando necessário.
- Saída: snippets/quotes/summary conforme `AssistantResponseSchema`.

## Pinos de integração
- Google Maps (`geocoding/`), WhatsApp (`mensageria/`), FSM (`fsm/`).
