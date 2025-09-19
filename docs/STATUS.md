# Status Atual do Projeto (Snapshot)

Esse documento resume o que já foi implementado até a data abaixo e o que está imediatamente pendente.

> Data do snapshot: 2025-09-19

## ✅ Concluído
### Estrutura & Monorepo
- Monorepo organizado (`apps`, `packages`, `tools`, `docs`)
- README raiz enxuto + visão macro
- Backlog operacional movido para `docs/backlog/README.md`

### Backend (delivery-system)
- FastAPI base estruturada
- Modelos iniciais + integrações placeholders (OpenAI, WhatsApp, Google, PagSeguro)
- Autenticação básica (JWT)
- Webhook WhatsApp inicial (token hardcoded – a externalizar)

### Assistente O.T.T.O
- Estrutura inicial de funções e integração com OpenAI (alguns stubs)
- Chamadas de ferramenta planejadas (`_compute_delivery_quote`, `_generate_pix_payment`, `_search_faq`)

### Frontend Website
- Estrutura Next.js criada em `apps/website`
- Componentes de seções: Hero, Features, HowItWorks, Testimonials, CTA
- Layout: Header, Footer
- Providers: Theme, React Query (mínimos)
- Arquivos de estilo base (`tailwind.css`, `theme.css`) – sem pipeline ainda

### Documentação
- Backlog detalhado com prioridades e fases (1–11)
- README do website criado com visão de arquitetura front e convenções

## 🟡 Em Progresso
(Nenhum item parcialmente em execução neste snapshot — próximo foco: dependências frontend)

## ⏳ Pendente (Curto Prazo)
| Área | Pendência | Arquivo/Local Alvo |
|------|-----------|--------------------|
| Frontend | Instalar dependências React/Next/Tailwind | `apps/website/package.json` |
| Frontend | Configurar Tailwind + PostCSS | `apps/website/tailwind.config.js` |
| Frontend | Ajustar links placeholders (a11y) | `header.tsx`, `footer.tsx` |
| Backend | FSM de pedidos | `services/fsm_service.py` |
| Backend | Endpoints /orders CRUD + transições | `api/v1/endpoints/orders.py` |
| Assistente | Função `_search_faq` | `packages/integrations/openai/...` |
| Assistente | FAQ doc base | `docs/user-guides/informacoes_gerais_e_duvidas.md` |
| Segurança | Externalizar token webhook | `.env` + `settings.py` |
| QA | Testes auth + healthcheck | `apps/delivery-system/tests/` |

## 🛰️ Planejado (Médio Prazo)
- Painel admin inicial (dashboard + criação de pedido)
- Enriquecimento das funções do assistente (PIX real, cotação real via Google Maps)
- Testes para FSM e orders
- Observabilidade (Prometheus/Grafana config ativa)

## ⚠️ Riscos / Atenções Imediatas
| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| Token webhook hardcoded | Vazamento / segurança | Mover para env e validar no startup |
| Falta de testes iniciais | Regressões silenciosas | Implementar baseline asap |
| Dependências frontend ausentes | Bloqueia evolução UI | Instalar e configurar já na próxima etapa |
| Stubs assistant sem fallback robusto | UX inconsistente | Adicionar try/except e mensagens controladas |

## 📌 Decisões Recentes (Resumo)
| Decisão | Motivo | Data |
|---------|-------|------|
| Separar backlog do README raiz | Reduz ruído para stakeholders | 2025-09-19 |
| Componentizar homepage desde início | Facilitar iteração futura sem refactor | 2025-09-19 |
| Estrutura providers mínima | Evitar over-engineering precoce | 2025-09-19 |

## 🔮 Próximo Passo Imediato
Instalar e configurar dependências do frontend (React, Next.js, Tailwind, React Query, linting) para desbloquear evolução visual e SEO.

---
Atualize este documento sempre que um bloco relevante avançar (ideal: ao final de cada sprint ou milestone significativo).
