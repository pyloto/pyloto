# Deploy do Website (Next.js) no Cloudflare Pages

Este guia descreve o processo para build e deploy do app `apps/website` usando **Cloudflare Pages** com suporte a runtime edge via `@cloudflare/next-on-pages`.

## ✅ Abordagens
| Abordagem | Quando usar | Observação |
|-----------|-------------|------------|
| Build nativo `next build` (auto-detect) | Site estático simples | Menos controle sobre edge features |
| `@cloudflare/next-on-pages` (recomendada) | Necessidade futura de bindings (KV/R2/AI) | Usa saída `.vercel/output` |

## 📦 Scripts (root `package.json`)
| Script | Ação |
|--------|------|
| `npm run cf:build:website` | Gera build edge do site |
| `npm run cf:preview:website` | Previsualiza local com Pages dev |
| `npm run cf:deploy:website` | Faz deploy na Cloudflare (branch main) |

## 🗂 Estrutura de Build
- Output gerado: `.vercel/output/static`
- Configuração Cloudflare: `apps/website/wrangler.toml` (não duplicar na raiz — evita resolução irregular)

## ⚙ Configuração Cloudflare Pages
No dashboard:
1. Create Project → Conectar repositório GitHub
2. Branch: `main`
3. Root directory: `apps/website` (ou root + script com `cd`)
4. Build command:
   ```bash
   npx @cloudflare/next-on-pages@latest
   ```
5. Output directory: `.vercel/output/static`
6. Node version: 20
7. **Compatibility Flags:**
   - Adicione o flag `nodejs_compat` em **Settings → Compatibility Flags** (Production e Preview).
   - Declarado também em `wrangler.toml` via `compatibility_flags = ["nodejs_compat"]`.
   - Garante APIs Node (fs, path, buffer) necessárias ao adaptador.

### Campos (Resumo Direto)
| Campo UI Cloudflare | Valor a Informar | Observações |
|---------------------|------------------|-------------|
| Framework preset | None (ou Detect automaticamente) | Usamos `next-on-pages`; não selecionar outro preset (evita conflito) |
| Build command | `npx @cloudflare/next-on-pages@latest` | Removido arg `build` (CLI espera zero args) |
| Build output directory | `.vercel/output/static` | Gerado após o build next-on-pages |
| Root directory (Project settings → Builds) | `apps/website` | Caso deixe root vazio use script com `cd apps/website && ...` |
| Node version | `20` | Garantir consistência com local |
| Environment variables | Ver tabela abaixo | Definir Production e Preview se necessário |

Se optar por não usar root directory (deixar em branco), ajuste Build command para:
```bash
cd apps/website && npx @cloudflare/next-on-pages@latest
```

## 🔐 Variáveis de Ambiente
Definir em Pages → Settings → Environment Variables (Production & Preview). Separar variáveis públicas (prefixo `NEXT_PUBLIC_`) de segredos. Nunca expor tokens ou chaves inteiras em documentação pública.

| Variable name | Tipo | Uso | Observações |
|---------------|------|-----|-------------|
| NEXT_PUBLIC_API_URL | pública | URL base da API | Diferente entre preview e produção |
| NEXT_PUBLIC_SITE_URL | pública | URL canônica do site | Usada em metatags e links absolutos |
| NEXT_PUBLIC_WHATSAPP_NUMBER | pública | Exibição de contato | Formato internacional +55 |
| NEXT_PUBLIC_SITE_ENV | pública | Flag de ambiente | Ex: production / preview |
| WHATSAPP_ACCESS_TOKEN | secret | Chamadas API WhatsApp | Rotacionar periodicamente |
| WHATSAPP_PHONE_NUMBER_ID | secret | ID do número Business | Necessário para endpoints de mensagens |
| WHATSAPP_BUSINESS_ACCOUNT_ID | secret | ID da conta Business | Para correlacionar webhooks |
| WHATSAPP_API_VERSION | secret | Versão Graph API | Alinhar com changelog Meta |
| WHATSAPP_WEBHOOK_VERIFY_TOKEN | secret | Validação de webhook | Usado no handshake GET (hub.verify_token) |
| OPENAI_API_KEY | secret | Assistant O.T.T.O | Limitar via usage policies |
| OPENAI_MODEL | secret | Modelo principal | Atualizado para gpt-4o |
| OPENAI_ASSISTANT_ID | secret | ID do Assistant | Referência interna |
| OPENAI_MAX_TOKENS | secret | Limite resposta | Controla custo/previsibilidade |
| OPENAI_TEMPERATURE | secret | Controle de criatividade | Manter baixo para respostas consistentes |
| PAGSEGURO_EMAIL | secret | Autenticação PagSeguro | Ambiente sandbox inicialmente |
| PAGSEGURO_TOKEN | secret | Token PagSeguro | Rotacionar se suspeita de vazamento |
| PAGSEGURO_SANDBOX | secret | Flag sandbox | true/false |
| GOOGLE_MAPS_API_KEY | secret | Geocoding/Rotas | Restringir por domínio/IP |
| GOOGLE_PLACES_API_KEY | secret | Autocomplete/Lugares | Pode ser mesma chave se unificada |
| WHATSAPP_WEBHOOK_TOKEN | deprecated/legacy | Token antigo exemplo | Manter até remover referências antigas |

Notas:
- Prefixo `NEXT_PUBLIC_` expõe a variável ao bundle; tudo sem prefixo fica só no runtime edge/server.
- Consolidado token de verificação: usar `WHATSAPP_WEBHOOK_VERIFY_TOKEN` (novo nome) — manter o antigo apenas durante transição.
- Sempre habilitar rotação e registrar data da última alteração em um cofre seguro (ex: 1Password, Vault).

### Exemplo de configuração via CLI (Wrangler)
```bash
wrangler pages project create pyloto-website \
   --production-branch=main \
   --compatibility-date=$(date +%Y-%m-%d)

wrangler secret put OPENAI_API_KEY
wrangler secret put PAGSEGURO_TOKEN
wrangler secret put GOOGLE_MAPS_API_KEY
wrangler secret put GOOGLE_PLACES_API_KEY
wrangler secret put WHATSAPP_ACCESS_TOKEN
wrangler secret put WHATSAPP_WEBHOOK_VERIFY_TOKEN
```

Secrets via CLI:
```bash
wrangler secret put OPENAI_API_KEY
wrangler secret put PAGSEGURO_TOKEN
wrangler secret put WHATSAPP_ACCESS_TOKEN
wrangler secret put WHATSAPP_WEBHOOK_VERIFY_TOKEN
```

## 🚀 Deploy via CLI
Pré-requisitos: `wrangler` instalado (global ou via npx). O adaptador roda via npx; para fixar versão adicione em devDependencies depois.

```bash
npm run cf:deploy:website
```

Preview local (Pages dev):
```bash
npm run cf:preview:website
```

## 🛡 Cabeçalhos de Segurança
Definidos em `next.config.js` (X-Frame-Options, X-Content-Type-Options, Referrer-Policy). Próximos:
- `Content-Security-Policy`
- `Permissions-Policy`
- `Strict-Transport-Security` (via Cloudflare SSL/TLS settings)

## 📊 Observabilidade & Analytics
- Adicionar Cloudflare Web Analytics (token) no `layout.tsx` quando disponível.
- Futuro: Worker cron monitorando disponibilidade do backend.

## ♻ Rollback
No dashboard → Deployments → selecionar build anterior → Promote.
Ou CLI com commit hash:
```bash
wrangler pages deploy .vercel/output/static --commit-hash <hash>
```

## 🧪 Pipeline CI (Futuro)
Workflow (resumido):
1. Install & lint
2. Type check
3. Build website (`cf:build:website`)
4. Deploy automático (main) com wrangler API token (secret: `CLOUDFLARE_API_TOKEN`).

## 📝 Changelog
Ver `docs/changelogs/` para registro diário.

---
## 🔧 Troubleshooting (erros comuns)
| Sintoma | Causa provável | Ação |
|---------|----------------|------|
| No wrangler.toml file found | Arquivo só na raiz enquanto Root Directory = apps/website | Mover para `apps/website/wrangler.toml` (manter apenas um) |
| internal error após segundo "Found wrangler.toml" | Duplicidade ou relocação recente do `wrangler.toml` gerando caminho `../../.vercel` | Manter arquivo só em `apps/website` e limpar cache do projeto |
| Node.JS Compatibility Error (no nodejs_compat) | Flag não aplicada (UI) ou ausente no wrangler | Adicionar em Settings e em `compatibility_flags` |
| Node version ignorada (usa 22.x) | Cloudflare Pages default mais novo que engines | Adicionar `.node-version` e/ou setar Node no painel Build Settings |
| too many arguments. Expected 0 arguments | Uso antigo: `npx @cloudflare/next-on-pages build` | Remover `build` e usar apenas `npx @cloudflare/next-on-pages@latest` |
| paths como ../../.vercel/output/static no log | Caminho relativo recalculado por conta de múltiplos níveis de wrangler | Garantir apenas um `wrangler.toml` e caminho `.vercel/output/static` |

Notas adicionais:
- Se o erro interno persistir após limpar duplicidades, abrir ticket Cloudflare anexando o log completo.
- Planeje migração para OpenNext conforme aviso de depreciação.

Última atualização: 2025-09-19 (adicionado nodejs_compat em wrangler + doc)