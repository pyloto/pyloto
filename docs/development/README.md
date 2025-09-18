# Pyloto Development Guide

Este guia contém informações essenciais para desenvolvedores trabalhando no projeto Pyloto.

## 🚀 Quick Start

```bash
# 1. Clone e configure
git clone https://github.com/pyloto/pyloto.git
cd pyloto
./tools/scripts/setup.sh

# 2. Configure variáveis de ambiente
cp .env.example .env
# Edite .env com suas configurações

# 3. Inicie o desenvolvimento
npm run dev
```

## 🏗️ Arquitetura

### Fluxo Principal (WhatsApp → O.T.T.O → Sistema)

1. **Usuário envia mensagem** no WhatsApp
2. **Webhook recebe** a mensagem
3. **O.T.T.O (OpenAI Assistant)** processa a mensagem
4. **Sistema executa** as ações necessárias (cálculo, pagamento, etc.)
5. **Resposta enviada** de volta pelo WhatsApp

### Componentes Principais

- **FastAPI Backend** (`apps/delivery-system/`)
  - API REST para todas as operações
  - Integração com O.T.T.O e WhatsApp
  - Processamento de pagamentos
  - Sistema de notificações

- **Next.js Website** (`apps/website/`)
  - Site institucional público
  - Páginas de marketing e informações

- **Next.js Admin Panel** (`apps/admin-panel/`)
  - Painel para lojistas
  - Dashboard administrativo
  - Gestão de entregas e relatórios

- **Packages Integrations** (`packages/integrations/`)
  - Clients para APIs externas
  - Código reutilizável entre apps

## 🔧 Comandos Úteis

### Desenvolvimento

```bash
# Iniciar todos os serviços
npm run dev

# Iniciar apenas backend
npm run dev:backend

# Iniciar apenas website
npm run dev:website

# Iniciar apenas admin panel
npm run dev:admin

# Docker (recomendado)
npm run docker:dev
```

### Build e Deploy

```bash
# Build para produção
npm run build

# Testes
npm run test

# Linting
npm run lint
```

### Banco de Dados

```bash
# Entrar no diretório do backend
cd apps/delivery-system

# Ativar ambiente virtual
source venv/bin/activate

# Criar nova migração
alembic revision --autogenerate -m "Descrição da mudança"

# Aplicar migrações
alembic upgrade head

# Voltar migração
alembic downgrade -1
```

## 🗄️ Estrutura de Dados

### Principais Entidades

- **User**: Usuários (consumidores, lojistas, entregadores, admins)
- **Order**: Pedidos de entrega
- **Delivery**: Execução da entrega (vinculado ao pedido)
- **Payment**: Pagamentos (PIX, cartão, etc.)
- **Notification**: Notificações (WhatsApp, email, push)

### Estados do Pedido (FSM)

```
DRAFT → PENDING_QUOTE → QUOTED → PENDING_PAYMENT → PAID → 
ASSIGNED → PICKUP_PENDING → PICKED_UP → IN_TRANSIT → DELIVERED
```

## 🤖 O.T.T.O Assistant

### Configuração

O assistant O.T.T.O está configurado no OpenAI com:
- **Assistant ID**: `asst_RGAVvFf5IhLa8tShJ0gZWsYX`
- **Model**: GPT-4
- **Functions**: compute_delivery_quote, search_faq, get_driver_eta, etc.

### Fluxo de Conversação

1. Usuário envia mensagem
2. Sistema cria/recupera thread do OpenAI
3. O.T.T.O processa e responde com JSON estruturado
4. Sistema interpreta resposta e executa ações
5. Resposta enviada ao usuário

### Tipos de Resposta

```json
{
  "kind": "question|quote|fsm_event|chat",
  "text": "Mensagem para o usuário",
  "entities": {...},
  "requires": ["campos_faltantes"],
  "metadata": {...}
}
```

## 🔗 APIs Externas

### WhatsApp Business API

- **Base URL**: `https://graph.facebook.com/v18.0`
- **Webhook**: `/api/v1/webhooks/whatsapp`
- **Funcionalidades**: Envio/recebimento de mensagens, botões interativos

### Google Maps API

- **Geocoding**: Conversão endereço ↔ coordenadas
- **Directions**: Cálculo de rotas e tempo
- **Places**: Busca de estabelecimentos

### PagSeguro

- **PIX**: Geração de pagamentos instantâneos
- **Webhook**: Confirmação de pagamentos
- **Sandbox**: Ambiente de testes

## 📱 Frontend (Next.js)

### Estrutura de Componentes

```
src/
├── app/                    # App Router (Next.js 14)
├── components/
│   ├── ui/                # Componentes base (Shadcn)
│   ├── forms/             # Formulários
│   ├── layout/            # Layout components
│   └── sections/          # Seções da página
├── hooks/                 # Custom React hooks
├── services/              # API clients
├── types/                 # TypeScript types
└── utils/                 # Utilitários
```

### Estado Global

- **React Query**: Cache de dados da API
- **Context API**: Estado de autenticação
- **Local Storage**: Preferências do usuário

## 🐳 Docker

### Desenvolvimento

```bash
# Iniciar todos os serviços
docker-compose -f tools/docker/docker-compose.dev.yml up

# Apenas banco e cache
docker-compose -f tools/docker/docker-compose.dev.yml up postgres redis

# Logs específicos
docker-compose -f tools/docker/docker-compose.dev.yml logs backend
```

### Produção

```bash
# Build das imagens
docker-compose -f tools/docker/docker-compose.prod.yml build

# Deploy
docker-compose -f tools/docker/docker-compose.prod.yml up -d
```

## 🧪 Testes

### Backend (Python)

```bash
cd apps/delivery-system
source venv/bin/activate
pytest tests/ -v --cov=src
```

### Frontend (Next.js)

```bash
cd apps/website  # ou apps/admin-panel
npm test
npm run test:coverage
```

## 📊 Monitoramento

### Métricas (Prometheus)

- **URL**: http://localhost:9090
- **Métricas**: Request rate, response time, error rate
- **Alertas**: Configurados via Grafana

### Dashboards (Grafana)

- **URL**: http://localhost:3002
- **Login**: admin/admin123
- **Dashboards**: Sistema, API, Banco de dados

### Logs

- **Aplicação**: `apps/delivery-system/logs/`
- **Docker**: `docker-compose logs <service>`
- **Estruturado**: JSON com timestamp, level, message

## 🔒 Segurança

### Autenticação

- **JWT**: Tokens com expiração de 7 dias
- **Refresh**: Renovação automática
- **Roles**: consumer, merchant, driver, admin

### Autorização

- **RBAC**: Role-based access control
- **Endpoints**: Protegidos por middleware
- **Rate Limiting**: 100 req/min por IP

### Dados Sensíveis

- **Passwords**: Hash com bcrypt
- **API Keys**: Variáveis de ambiente
- **PII**: Logs sem dados pessoais

## 🚀 Deploy

### Staging

```bash
# CI/CD via GitHub Actions
git push origin develop
```

### Produção

```bash
# Tag de release
git tag v1.0.0
git push origin v1.0.0
```

### Verificações

- [ ] Variáveis de ambiente configuradas
- [ ] Banco de dados migrado
- [ ] Testes passando
- [ ] Monitoramento ativo
- [ ] Backup configurado

## 🆘 Troubleshooting

### Problemas Comuns

1. **Error: connection refused**
   - Verificar se PostgreSQL/Redis estão rodando
   - Conferir URLs de conexão no .env

2. **OpenAI API errors**
   - Verificar API key válida
   - Conferir Assistant ID
   - Checar rate limits

3. **WhatsApp webhook não recebe**
   - Verificar token de verificação
   - Confirmar URL pública (ngrok em dev)
   - Checar logs do webhook

4. **Frontend não conecta API**
   - Verificar CORS_ORIGINS
   - Conferir NEXT_PUBLIC_API_URL
   - Checar network na dev tools

### Logs Úteis

```bash
# Backend
tail -f apps/delivery-system/logs/app.log

# Docker
docker-compose logs -f backend

# Next.js
cd apps/website && npm run dev
```

## 📚 Recursos Adicionais

- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Next.js Docs](https://nextjs.org/docs)
- [OpenAI API](https://platform.openai.com/docs)
- [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp)
- [Tailwind CSS](https://tailwindcss.com/docs)

---

## 🤝 Contribuindo

1. Fork do repositório
2. Criar branch para feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit das mudanças (`git commit -m 'Add: nova funcionalidade'`)
4. Push para branch (`git push origin feature/nova-funcionalidade`)
5. Abrir Pull Request

### Padrões de Commit

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Documentação
- `style:` Formatação
- `refactor:` Refatoração
- `test:` Testes
- `chore:` Tarefas de build

### Code Review

- [ ] Código segue padrões do projeto
- [ ] Testes cobrem funcionalidade
- [ ] Documentação atualizada
- [ ] Performance considerada
- [ ] Segurança validada