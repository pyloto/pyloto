# Pyloto Corp - Sistema de Entregas Inteligente 🚀

<div align="center">
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow" alt="Status">
  <img src="https://img.shields.io/badge/Versão-1.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/License-Proprietary-red" alt="License">
</div>

## ⚡ Quick Start

```bash
git clone https://github.com/pyloto/pyloto.git
cd pyloto
./tools/scripts/setup.sh
cp .env.example .env
# Configure suas variáveis de ambiente
npm run dev
```

## 🎯 Sobre o Projeto

A **Pyloto** é uma startup de delivery inteligente que utiliza IA para revolucionar o mercado de entregas. Nosso diferencial é o assistente **O.T.T.O** (Optimized Transport & Tracking Operations), que funciona via WhatsApp e automatiza todo o processo de cotação, pagamento e acompanhamento de entregas.

### 🌟 Principais Funcionalidades

- **WhatsApp Business Integration**: Interface conversacional natural
- **O.T.T.O AI Assistant**: Processamento inteligente de pedidos
- **Cotação Automática**: Cálculo em tempo real via Google Maps
- **Pagamento Instantâneo**: PIX integrado com PagSeguro
- **Tracking em Tempo Real**: Acompanhamento completo da entrega
- **Dashboard Administrativo**: Gestão completa para lojistas
- **Sistema Multi-tenant**: Suporte a múltiplos estabelecimentos

## � Características Principais

- **🤖 IA Integrada**: Assistant O.T.T.O powered by OpenAI para conversas naturais
- **📱 WhatsApp First**: Interface principal via WhatsApp Business API
- **⚡ FastAPI Backend**: Performance e escalabilidade com Python
- **🎨 Next.js Frontend**: Site moderno e painel administrativo
- **🏗️ Arquitetura Monorepo**: Código organizado e reutilizável
- **🐳 Docker Ready**: Containerização completa para desenvolvimento e produção
- **📊 Monitoramento**: Observabilidade com Prometheus e Grafana
- **🔒 Segurança**: JWT auth, rate limiting, e boas práticas

## 🏢 Como Funciona

O **Pyloto** conecta três tipos de usuários através de uma plataforma inteligente:

### 👥 Para Consumidores
- Enviam mensagem no WhatsApp solicitando entrega
- O.T.T.O (IA) coleta informações e calcula preço
- Pagamento via PIX gerado automaticamente
- Acompanhamento em tempo real da entrega

### 🏪 Para Lojistas  
- Painel web para solicitar entregadores para seus produtos
- Integração com sistemas existentes via API
- Visibilidade da marca para consumidores próximos
- Relatórios e analytics de entregas

### 🏍️ Para Entregadores
- App/painel para receber solicitações
- Sistema de matching inteligente por proximidade
- Rastreamento GPS e comunicação em tempo real
- Gestão de ganhos e avaliações

## 🛠️ Stack Tecnológica

### Backend
- **FastAPI** - Framework web moderno e performático
- **PostgreSQL** - Banco de dados principal
- **Redis** - Cache e sessões
- **Celery** - Processamento assíncrono
- **SQLAlchemy** - ORM e migrações
- **Alembic** - Controle de versão do banco

### Frontend  
- **Next.js 14** - Framework React com App Router
- **TypeScript** - Tipagem estática
- **Tailwind CSS** - Estilização utilitária
- **Shadcn/ui** - Componentes reutilizáveis

### Integrações
- **OpenAI GPT-4** - Assistant O.T.T.O
- **WhatsApp Business API** - Interface principal
- **Google Maps API** - Geocoding e rotas
- **PagSeguro API** - Processamento de pagamentos

### DevOps & Infraestrutura
- **Docker & Docker Compose** - Containerização
- **Nginx** - Reverse proxy e load balancer
- **Prometheus & Grafana** - Monitoramento
- **GitHub Actions** - CI/CD

## � Estrutura do Projeto

Este é um monorepo organizado para máxima modularidade e reutilização:

```
pyloto/
├── apps/                          # Aplicações independentes
│   ├── delivery-system/           # Backend FastAPI
│   │   ├── src/
│   │   │   ├── api/               # Endpoints REST
│   │   │   ├── core/              # Config, DB, Cache
│   │   │   ├── models/            # Modelos SQLAlchemy
│   │   │   ├── services/          # Lógica de negócio
│   │   │   ├── integrations/      # APIs externas
│   │   │   └── workers/           # Tarefas Celery
│   │   ├── migrations/            # Alembic migrations
│   │   └── tests/                 # Testes automatizados
│   ├── website/                   # Site Next.js
│   │   ├── src/
│   │   │   ├── app/               # App Router
│   │   │   ├── components/        # Componentes React
│   │   │   ├── hooks/             # Custom hooks
│   │   │   └── services/          # API clients
│   │   └── public/                # Assets estáticos
│   └── admin-panel/               # Painel administrativo
│       ├── src/
│       │   ├── app/               # Páginas Next.js
│       │   ├── components/        # UI components
│       │   └── types/             # TypeScript types
│       └── public/
├── packages/                      # Código compartilhado
│   ├── core/                      # Utilitários compartilhados
│   ├── integrations/              # Clients para APIs
│   │   ├── openai/                # OpenAI + O.T.T.O
│   │   ├── whatsapp/              # WhatsApp Business
│   │   ├── google/                # Google Maps/Places
│   │   └── pagseguro/             # Pagamentos
│   ├── shared-types/              # Types TypeScript
│   └── ui-components/             # Componentes reutilizáveis
├── tools/                         # Ferramentas de desenvolvimento
│   ├── docker/                    # Docker configs
│   ├── scripts/                   # Scripts utilitários
│   └── monitoring/                # Configs Prometheus/Grafana
├── docs/                          # Documentação
│   ├── api/                       # Docs da API
│   ├── architecture/              # Diagramas e ADRs
│   └── user-guides/               # Guias do usuário
└── infrastructure/                # Infraestrutura como código
    ├── kubernetes/                # Manifests K8s
    └── terraform/                 # Provisionamento cloud
```

## 🚀 Começando

### Pré-requisitos

- **Node.js** 18+ e **npm** 9+
- **Python** 3.11+
- **Docker** e **Docker Compose**
- **Git**

### Instalação Rápida

1. **Clone o repositório**
   ```bash
   git clone https://github.com/pyloto/pyloto.git
   cd pyloto
   ```

2. **Configure as variáveis de ambiente**
   ```bash
   cp .env.example .env
   # Edite o arquivo .env com suas configurações
   ```

3. **Inicie com Docker (Recomendado)**
   ```bash
   # Desenvolvimento completo
   npm run docker:dev
   
   # Ou individualmente
   docker-compose -f tools/docker/docker-compose.dev.yml up
   ```

4. **Ou instale localmente**
   ```bash
   # Instalar dependências
   npm run setup
   
   # Iniciar todos os serviços
   npm run dev
   ```

### Acesso aos Serviços

Após inicialização, você terá acesso a:

- **🌐 Website**: http://localhost:3000
- **👨‍💼 Painel Admin**: http://localhost:3001  
- **🔧 API Backend**: http://localhost:8000
- **📚 Docs API**: http://localhost:8000/docs
- **📊 Grafana**: http://localhost:3002 (admin/admin123)
- **🐘 pgAdmin**: http://localhost:5050 (admin@pyloto.com/admin123)
- **📧 MailHog**: http://localhost:8025

## 📝 Etapas para Recriar o Projeto

### Fase 1: Planejamento e Setup Inicial
1. **Criar repositório vazio** no GitHub com a nova estrutura.
2. **Configurar monorepo** com `package.json` raiz e workspaces.
3. **Instalar ferramentas**: Node.js, Python 3.11, Docker.
4. **Configurar CI/CD** com GitHub Actions para testes automatizados.

### Fase 2: Sistema Geral (Backend)
1. **Criar `apps/system/`** com estrutura Python/FastAPI.
2. **Migrar modelos** de SQLAlchemy para o novo local.
3. **Implementar serviços** com injeção de dependência.
4. **Configurar banco** com Alembic e PostgreSQL.
5. **Adicionar autenticação** JWT/OAuth.
6. **Implementar FSM** com melhor abstração.
7. **Integrar cache** Redis e tarefas Celery.

### Fase 3: Site (Frontend)
1. **Criar `apps/site/`** com Next.js/React.
2. **Desenvolver páginas**: Dashboard, login, pedidos, relatórios.
3. **Integrar APIs** do sistema backend.
4. **Implementar autenticação** com tokens.
5. **Adicionar responsividade** e acessibilidade.
6. **Configurar deploy** com Vercel/Netlify.

### Fase 4: Documentação
1. **Criar `apps/docs/`** com Docusaurus.
2. **Estruturar conteúdo**: Guias de API, tutoriais, referência.
3. **Adicionar exemplos** de código e integrações.
4. **Configurar busca** e navegação intuitiva.
5. **Automatizar geração** de docs a partir do código.

### Fase 5: Integrações e Testes
1. **Migrar integrações** (WhatsApp, PagSeguro, etc.) para `packages/integrations/`.
2. **Escrever testes** abrangentes para cada módulo.
3. **Configurar Docker** para desenvolvimento local.
4. **Implementar monitoramento** com Prometheus/Grafana.
5. **Adicionar segurança**: Rate limiting, CORS, validações.

### Fase 6: Deploy e Produção
1. **Configurar Docker Compose** para produção.
2. **Implementar CI/CD** completo.
3. **Adicionar monitoramento** e alertas.
4. **Configurar backups** automáticos.
5. **Testar escalabilidade** e performance.

## 🎯 Conclusão

Esta reestruturação transforma o Pyloto em um sistema mais robusto, escalável e fácil de manter. A separação por domínios e a estrutura monorepo permitem desenvolvimento paralelo e reutilização de código.

**Benefícios Esperados:**
- 🚀 **Performance**: Microserviços e cache otimizado.
- 🔧 **Manutenibilidade**: Código organizado e testável.
- 📈 **Escalabilidade**: Suporte a múltiplos produtos e clientes.
- 👥 **Colaboração**: Desenvolvimento independente por equipes.
- 🔒 **Segurança**: Melhor isolamento e controle de acesso.

Para iniciar, comece criando o repositório com a estrutura proposta e migre os módulos gradualmente. Consulte a documentação de cada ferramenta para detalhes específicos.

**Próximos Passos:** Implemente a Fase 1 e configure o ambiente de desenvolvimento. Em caso de dúvidas, consulte os guias na pasta [`docs`](docs ).

## 🚀 Próximas Fases de Desenvolvimento

### Fase 7: Otimização e Performance
1. **Implementar cache distribuído** com Redis Cluster para alta disponibilidade.
2. **Otimizar consultas de banco** com índices compostos e query optimization.
3. **Configurar load balancing** com Nginx ou Traefik para distribuição de carga.
4. **Implementar compressão** de respostas HTTP (gzip, brotli) e otimização de assets.
5. **Configurar connection pooling** para banco de dados e APIs externas.
6. **Implementar circuit breakers** para proteção contra falhas em cascata.
7. **Otimizar imagens e assets** com CDN (CloudFront, Cloudflare).
8. **Configurar auto-scaling** baseado em métricas de CPU/memória.

### Fase 8: Segurança e Compliance
1. **Implementar OAuth 2.0 / OpenID Connect** para autenticação robusta.
2. **Configurar RBAC (Role-Based Access Control)** com permissões granulares.
3. **Implementar criptografia** de dados sensíveis (AES-256) e TLS 1.3 obrigatório.
4. **Adicionar auditoria completa** com logs imutáveis e compliance LGPD/GDPR.
5. **Configurar WAF (Web Application Firewall)** para proteção contra ataques.
6. **Implementar rate limiting** inteligente por usuário/IP com Redis.
7. **Adicionar validação de entrada** rigorosa e sanitização de dados.
8. **Configurar backup criptografado** e recuperação de desastres.

### Fase 9: Monitoramento e Observabilidade
1. **Implementar APM (Application Performance Monitoring)** com New Relic ou DataDog.
2. **Configurar centralized logging** com ELK Stack (Elasticsearch, Logstash, Kibana).
3. **Implementar distributed tracing** com Jaeger ou Zipkin para microserviços.
4. **Configurar alertas inteligentes** baseados em anomalias e thresholds.
5. **Implementar health checks** abrangentes para todos os serviços.
6. **Adicionar métricas de negócio** (conversão, retenção, satisfação).
7. **Configurar dashboards** em tempo real para monitoramento executivo.
8. **Implementar synthetic monitoring** para testes de disponibilidade externos.

### Fase 10: Documentação e Treinamento
1. **Criar documentação técnica** completa com OpenAPI/Swagger para APIs.
2. **Desenvolver guias de usuário** interativos com screenshots e vídeos.
3. **Criar documentação de arquitetura** com diagramas C4 e ADRs (Architecture Decision Records).
4. **Implementar documentação viva** que se atualiza automaticamente com o código.
5. **Criar programa de treinamento** para desenvolvedores e usuários finais.
6. **Desenvolver knowledge base** com FAQs e troubleshooting guides.
7. **Implementar sistema de feedback** para melhoria contínua da documentação.
8. **Criar documentação de compliance** e auditoria para certificações.

### Fase 11: Migração e Deploy Final
1. **Planejar estratégia de migração** com zero downtime (blue-green deployment).
2. **Implementar feature flags** para controle gradual de funcionalidades.
3. **Configurar canary deployments** para testes em produção controlados.
4. **Implementar rollback automático** em caso de falhas na implantação.
5. **Configurar backup e restore** completo do ambiente de produção.
6. **Implementar smoke tests** pós-deployment para validação.
7. **Configurar monitoring** específico para o processo de migração.
8. **Executar migração gradual** com acompanhamento em tempo real.

## 📊 Timeline e Marcos

### Sprint 1-2: Foundation (Semanas 1-4)
- ✅ Setup do monorepo e estrutura base
- ✅ Configuração de CI/CD básico
- ✅ Implementação do sistema backend (Fase 2)
- ✅ Testes unitários e integração

### Sprint 3-4: Core Features (Semanas 5-8)
- ✅ Implementação do site frontend (Fase 3)
- ✅ Sistema de documentação (Fase 4)
- ✅ Integrações principais (Fase 5)
- ✅ Deploy inicial (Fase 6)

### Sprint 5-6: Optimization (Semanas 9-12)
- ✅ Otimização de performance (Fase 7)
- ✅ Segurança e compliance (Fase 8)
- ✅ Monitoramento básico (Fase 9)
- ✅ Testes de carga e stress

### Sprint 7-8: Production Ready (Semanas 13-16)
- ✅ Monitoramento avançado (Fase 9)
- ✅ Documentação completa (Fase 10)
- ✅ Preparação para migração (Fase 11)
- ✅ Testes de aceitação do usuário

### Sprint 9-10: Go-Live (Semanas 17-20)
- ✅ Migração para produção (Fase 11)
- ✅ Monitoramento pós-lançamento
- ✅ Otimização baseada em dados reais
- ✅ Suporte e manutenção inicial

## ⚠️ Riscos e Mitigações

### Riscos Técnicos
- **Complexidade da migração**: Mitigação - planejamento detalhado e testes extensivos
- **Dependências externas**: Mitigação - circuit breakers e fallbacks robustos
- **Performance em escala**: Mitigação - testes de carga e otimização preemptiva
- **Segurança de dados**: Mitigação - criptografia e auditoria desde o início

### Riscos de Negócio
- **Adoção pelos usuários**: Mitigação - comunicação clara e treinamento
- **Concorrência no mercado**: Mitigação - diferenciação por tecnologia superior
- **Regulamentação**: Mitigação - compliance proativo com LGPD/GDPR
- **Orçamento**: Mitigação - controle rigoroso de custos e ROI tracking

### Riscos Operacionais
- **Disponibilidade do sistema**: Mitigação - arquitetura redundante e failover
- **Equipe técnica**: Mitigação - documentação completa e knowledge sharing
- **Dependências de terceiros**: Mitigação - contratos SLA e planos B
- **Mudanças nos requisitos**: Mitigação - processo ágil e feedback contínuo

## 📈 Métricas de Sucesso

### Métricas Técnicas
- **Performance**: < 500ms para 95% das requisições
- **Disponibilidade**: 99.9% uptime mensal
- **Cobertura de Testes**: > 85% de cobertura de código
- **Tempo de Deploy**: < 15 minutos para mudanças críticas

### Métricas de Negócio
- **Satisfação do Usuário**: > 4.5/5 no NPS
- **Conversão**: > 70% dos usuários ativos mensais
- **Retenção**: > 80% retenção mensal
- **ROI**: Retorno sobre investimento em 12 meses

### Métricas de Qualidade
- **Bugs em Produção**: < 0.1 por usuário/mês
- **Tempo Médio de Resolução**: < 4 horas para issues críticos
- **Documentação**: 100% das funcionalidades documentadas
- **Compliance**: 100% aderência aos requisitos regulatórios

## 🎯 Considerações Finais

### Lições Aprendidas
1. **Planejamento é fundamental**: Dedique tempo adequado ao design da arquitetura
2. **Testes desde o início**: Implemente TDD e testes automatizados
3. **Documentação viva**: Mantenha a documentação atualizada com o código
4. **Monitoramento proativo**: Implemente observabilidade desde o início
5. **Segurança por design**: Considere segurança em todas as decisões

### Recomendações para Escalabilidade
1. **Microserviços progressivos**: Comece monolítico e divida conforme necessário
2. **Event-driven architecture**: Use eventos para comunicação assíncrona
3. **CQRS pattern**: Separe operações de leitura e escrita quando apropriado
4. **Domain-driven design**: Organize código por domínio de negócio
5. **Infrastructure as Code**: Automatize toda a infraestrutura

### Roadmap Futuro
- **IA/ML Integration**: Machine learning para otimização de rotas e previsões
- **IoT Integration**: Conectividade com dispositivos IoT para rastreamento
- **Blockchain**: Transparência e imutabilidade para transações críticas
- **Edge Computing**: Processamento próximo aos usuários para baixa latência
- **Multi-cloud**: Distribuição entre provedores para alta disponibilidade

## 🚀 Próximos Passos Imediatos

### Semana 1
1. **Revisar e aprovar arquitetura** proposta neste documento
2. **Criar repositório** com estrutura monorepo
3. **Configurar ferramentas** de desenvolvimento (GitHub, CI/CD)
4. **Definir equipe** e responsabilidades por módulo

### Semana 2
1. **Implementar Fase 1**: Setup inicial e estrutura base
2. **Configurar ambiente** de desenvolvimento local
3. **Criar templates** e padrões de código
4. **Definir contratos** de API entre módulos

### Semana 3
1. **Iniciar Fase 2**: Desenvolvimento do sistema backend
2. **Implementar autenticação** e autorização básica
3. **Criar modelos** de dados fundamentais
4. **Configurar banco** de dados e migrações

### Semana 4
1. **Continuar Fase 2**: APIs REST principais
2. **Implementar testes** unitários e de integração
3. **Configurar CI/CD** pipeline básico
4. **Revisar progresso** e ajustar plano se necessário

---

**Este documento é vivo e deve ser atualizado conforme o projeto evolui. Use-o como guia principal para o desenvolvimento do Pyloto 2.0.**

**📅 Última atualização**: Setembro 2025
**📊 Status**: ✅ Planejamento Completo - Pronto para Execução