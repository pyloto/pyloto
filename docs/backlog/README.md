# Backlog & Roadmap Pyloto

**Este é um documento vivo e deve ser SEMPRE ATUALIZADO"**

Este documento consolida o backlog operacional que estava no README principal.

## 📌 Sumário
- [Visão Geral](#visão-geral)
- [Prioridade 0 - Site Público (Homepage MVP)](#prioridade-0---site-público-homepage-mvp)
- [Backend - FSM & Pedidos](#backend---fsm--pedidos)
- [Assistant O.T.T.O - Funções e Contexto](#assistant-otto---funções-e-contexto)
- [Painel Administrativo](#painel-administrativo)
- [Validador DRAFT & Fluxo Conversacional](#validador-draft--fluxo-conversacional)
- [Testes & Qualidade](#testes--qualidade)
- [Futuras Fases (7 a 11)](#futuras-fases-7-a-11)
- [Riscos e Mitigações](#riscos-e-mitigações)
- [Métricas de Sucesso](#métricas-de-sucesso)
- [Próximos Passos Imediatos (Semanas 1–4)](#próximos-passos-imediatos-semanas-1–4)

## Visão Geral
Backlog estruturado para evolução incremental do ecossistema Pyloto. Foco inicial: presença digital (SEO), fluxo conversacional robusto e pedido fim-a-fim.

---
## Prioridade 0 - Site Público (Homepage MVP)
Objetivo: Indexação inicial e captura de leads.

### Componentes da Homepage
- [ ] Hero (titulo + subtítulo + CTA WhatsApp)
- [ ] Features (benefícios principais)
- [ ] HowItWorks (4 passos)
- [ ] Testimonials (placeholders)
- [ ] CTA Final (reforço de conversão)
- [ ] Header / Footer (layout consistente)

### Conteúdo & SEO
- [ ] Copy marketing para cada seção
- [ ] Metadados refinados (`layout.tsx`)
- [ ] Botão CTA abrindo WhatsApp com mensagem pré-definida
- [ ] Responsividade mobile / tablet / desktop

---
## Backend - FSM & Pedidos
Implementar máquina de estados e endpoints principais de pedidos.

### FSM (Order Lifecycle)
Estados pretendidos: `DRAFT → PENDING_QUOTE → QUOTED → PENDING_PAYMENT → PAID → ASSIGNED → PICKUP_PENDING → PICKED_UP → IN_TRANSIT → DELIVERED` (+ CANCELLED)

Tarefas:
- [ ] `src/services/fsm_service.py` com classe `OrderFSMService`
- [ ] Métodos de transição validando pré-condições
- [ ] Logs estruturados por transição (sucesso/falha)
- [ ] Integração com webhook de pagamento (muda QUOTED/PENDING_PAYMENT → PAID)

### Endpoints `/orders`
- [ ] Arquivo `src/api/v1/endpoints/orders.py`
- [ ] GET /orders (lista paginada filtrada por usuário/role)
- [ ] POST /orders (criação inicial em DRAFT)
- [ ] GET /orders/{id} (autorização por owner ou admin)
- [ ] Schemas Pydantic (CreateOrder, OrderOut, Pagination)

---
## Assistant O.T.T.O - Funções e Contexto
Melhorar a inteligência conversacional e ferramentas.

- [ ] Substituir stubs por integrações reais (GoogleMapsClient, PagSeguroClient)
- [ ] `_compute_delivery_quote`: usar `get_route_info`
- [ ] `_generate_pix_payment`: usar `create_pix_payment`
- [ ] `_search_faq`: leitura com indexação simples (arquivo `docs/user-guides/informacoes_gerais_e_duvidas.md` a criar)
- [ ] Tratamento robusto de exceções em cada função (timeout, 4xx, 5xx)
- [ ] Melhoria de mensagens de fallback para usuário

### Contexto de Pedidos
- [ ] Função `_get_user_order_context` em `services/otto.py` listando pedidos ativos (PAID+)
- [ ] Limitar quantidade (ex: últimos 3 ativos)
- [ ] Formatar JSON compacto usado como metadata

---
## Painel Administrativo
Fluxos para lojistas gerirem pedidos.

### Dashboard
- [ ] Página `apps/admin-panel/src/app/merchant/dashboard/page.tsx`
- [ ] Hook `useQuery` → GET /orders
- [ ] Tabela (react-table) com colunas: ID, Status, Criado, Coleta, Entrega, Valor
- [ ] Estado de loading / empty state

### Novo Pedido
- [ ] Página `merchant/orders/new/page.tsx`
- [ ] Form `react-hook-form` + `zod`
- [ ] POST /orders
- [ ] Toast sucesso + redirect

---
## Validador DRAFT & Fluxo Conversacional
Reduzir chamadas desnecessárias à IA.

- [ ] `src/services/draft_validator.py`
- [ ] Ordem de coleta de campos essenciais (origem, destino, remetente, destinatário, descrição)
- [ ] Retorna primeira pergunta faltante
- [ ] Integrar antes de chamar O.T.T.O no webhook

---
## Testes & Qualidade
Camada mínima de confiança.

### Auth Service
- [ ] `tests/services/test_auth_service.py`
- [ ] Teste login válido
- [ ] Teste login inválido
- [ ] Teste create_user (hash bcrypt)
- [ ] Mocks de banco (session fixture + in-memory)

### Futuro
- [ ] Tests para FSM
- [ ] Tests para endpoints orders
- [ ] Tests para funções do assistant

---
## Futuras Fases (7 a 11)
(Resumo – detalhes no documento de roadmap principal: performance, segurança avançada, observabilidade profunda, documentação viva, estratégias de deploy avançadas.)

---
## Riscos e Mitigações
Referência principal mantida no README para stakeholders; duplicação evitada aqui.

---
## Métricas de Sucesso
Manter centralizadas no README corporativo.

---
## Próximos Passos Imediatos (Semanas 1–4)
(Alinhado ao plano original – agora rastreável neste backlog.)
- Semana 1: Estrutura + Homepage MVP
- Semana 2: FSM + Orders API (CRUD básico + transições iniciais)
- Semana 3: Assistant tools reais + validação DRAFT
- Semana 4: Painel admin (dashboard + novo pedido) + testes foundation

---
Última atualização: $(date +'%Y-%m-%d')
