Pyloto AI — visão geral do módulo

Objetivo
- Minimizar chamadas LLM, manter o servidor determinístico, e usar a IA para:
	- completar DRAFT com endereços padronizados;
	- aplicar regras de precificação (no Assistant, via arquivo anexado);
	- gerar resumos amigáveis e respostas curtas.

Arquitetura do módulo
- `configuration/` — Constantes e config da FSM/IA (ex.: `constants.py`, `fsm_config.py`).
- `prompts/` — Prompts por estado; destaque para `draft_prompts.py` (padronização de endereço: Rua, Número, Bairro, Cidade, Estado).
- `validation/` — `draft_validator.py` valida campos e pergunta o que falta.
- `fsm_bridge/` — `integrator.py` injeta o system prompt específico do estado atual.
- `integration/` — Contrato e tools do Assistant:
	- `assistant_contract.py` — `AssistantResponseSchema` e `FUNCTION_SPECS`.
	- `assistant_functions.py` — Tools: `compute_delivery_quote`, `summarize_order`, `search_faq`, `get_driver_eta`, `generate_pix_payment`.
	- `openai_client.py` — Cliente simples (modelo `gpt-4o`, `temperature`, `top_p`).
- `management/` — `order_flow.py` orquestra: prepara insumos (Google Maps + heurísticas) e monta resumo.
- `analysis/` — `preprocess.py` (normalize_*), `inference.py` (heurísticas de categoria/peso/urgência/transporte).
- `openai_integration/` — `response_processor.py` valida/normaliza a resposta do Assistant.
- `pricing/` — `markup.py` (apply_system_markup), `quote.py` (estruturas). Regras vivem no Assistant.
- `repository/` — `base.py` e `in_memory.py` (memória simples).
- Arquivos raiz: `router.py` (orquestra chamadas IA), `types.py`, `logging.py`.

Fluxo de cotação (resumo)
1) DRAFT coleta e padroniza endereços.
2) `geocoding` calcula distância/ETA e demais features (tempo do dia, zona, trânsito) com retries/backoff, cache TTL e timeout configurável; pode injetar `weather_provider` opcional.
3) `ai.integration.assistant_functions.compute_delivery_quote` envia insumos ao Assistant (regras anexadas) e recebe preço base.
4) `ai.integration.assistant_functions.summarize_order` aplica MARKUP_RATE do ambiente (padrão 10%) e gera texto de resumo.
5) Opcional: `generate_pix_payment` cria Pix “Copia e Cola” (stub) e `get_driver_eta` estima ETA do entregador.

Como usar (pontos principais)
- `compute_delivery_quote(args)` — Passe `origin_address`/`dest_address` ou `distance_km`/`eta_min` já calculados.
- `summarize_order(args)` — Forneça `amount` (preço base) e metadados para texto amigável.
- `search_faq(args)` — Consulta rápida em `informacoes_gerais_e_duvidas.md`.
- `AIFSMIntegrator` — Injeta prompts de estado quando a FSM decide chamar a IA.

Configuração
- Variáveis: `OPENAI_MODEL`, `OPENAI_ASSISTANT_ID`, `OPENAI_API_KEY`, `AI_PROVIDER`.
- Anexos do Assistant: `regras_precos_entrega.json` (regras) e `informacoes_gerais_e_duvidas.md` (FAQ).

Notas
- Diferenças vs. legado: ver `ai/DIFERENCAS_AI_LEGADO.md`.
