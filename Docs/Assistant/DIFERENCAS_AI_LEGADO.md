Diferenças entre "ai (legado)" e novo "ai"

Arquitetura
- Legado: múltiplos assistants por mídia, acoplado ao fluxo; prompts extensos e pouco estruturados.
- Novo: único assistant configurado (gpt-4o) com response format json_schema e function calling; prompts por estado (FSM) e coleta determinística de DRAFT com validação.

Principais mudanças
- Portais de importação simplificados (evita ciclos), constants centralizados em `ai/configuration/constants.py`.
- `validation/draft_validator.py`: regras all_of/one_of/conditional com mensagens amigáveis.
- `fsm_bridge/integrator.py`: injeta system prompt específico por estado e mapeia intenções→eventos.
- `integration/assistant_contract.py`: schema + function specs; `assistant_functions.py`: dispatcher `compute_delivery_quote` e `search_faq`.
- `pricing/quote.py`: engine de regras lendo `regras_precos_entrega.json` (faixas, contexto, zonas).
- `prompts/draft_prompts.py`: perguntas por campo, seleção da próxima pergunta, orientação de resposta.
- `repository/in_memory.py`: memória por dia com deduplicação simples.

Redução de dependência de LLM
- Perguntas do DRAFT são guiadas por lógica local; LLM usado apenas quando necessário (ambiguidade/linguagem).

Configuração
- .env usa `OPENAI_ASSISTANT_ID` único. IDs múltiplos do legado são obsoletos.

Compatibilidade e migração
- Fluxos que consumiam o legado devem apontar para o novo router/integrator.
- Funções equivalentes: interpretação de intenção → via integrator; cotação rápida → via assistant_functions.

Remoções (planejadas)
- Submódulos de assistants especializados (texto/áudio/imagem), gerenciadores e config duplicadas.
