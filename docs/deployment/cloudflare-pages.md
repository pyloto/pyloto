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
Definir em Pages → Settings → Environment Variables (Production & Preview) no formato:

| Variable name | Value (exemplo) |
|---------------|-----------------|
| NEXT_PUBLIC_API_URL | https://api.pyloto.com.br/api/v1 |
| NEXT_PUBLIC_SITE_URL | https://pyloto.com.br |
| NEXT_PUBLIC_WHATSAPP_NUMBER | +5542999999999 |
| NEXT_PUBLIC_SITE_ENV | production |
| WHATSAPP_WEBHOOK_TOKEN | (secret) ex: 8a1c7f9c0a2b4e2d... |
| OPENAI_API_KEY | (secret) sk-live-... |
| PAGSEGURO_TOKEN | (secret) APP123456789... |
| MAPS_API_KEY | (secret) AIzaSyXXXXXX... |

Notas:
- Variáveis com prefixo `NEXT_PUBLIC_` são expostas ao bundle.
- Segredos (sem prefixo) não ficam acessíveis no cliente.

### Exemplo de configuração via CLI (Wrangler)
```bash
wrangler pages project create pyloto-website \
   --production-branch=main \
   --compatibility-date=$(date +%Y-%m-%d)

wrangler secret put OPENAI_API_KEY
wrangler secret put PAGSEGURO_TOKEN
wrangler secret put MAPS_API_KEY
wrangler secret put WHATSAPP_WEBHOOK_TOKEN
```

Secrets via CLI:
```bash
wrangler secret put OPENAI_API_KEY
wrangler secret put PAGSEGURO_TOKEN
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
| No wrangler.toml file found | Arquivo só na raiz enquanto Root Directory = apps/website | Mover/duplicar para `apps/website/wrangler.toml` (preferir manter apenas um) |
| internal error após segundo "Found wrangler.toml" | Duplicidade ou relocação recente do `wrangler.toml` gerando caminho `../../.vercel` | Manter arquivo só em `apps/website` e limpar cache do projeto |
| Node version ignorada (usa 22.x) | Cloudflare Pages default mais novo que engines | Adicionar `.node-version` e/ou setar Node no painel Build Settings |
| too many arguments. Expected 0 arguments | Uso antigo: `npx @cloudflare/next-on-pages build` | Remover `build` e usar apenas `npx @cloudflare/next-on-pages@latest` |
| paths como ../../.vercel/output/static no log | Caminho relativo recalculado por conta de múltiplos níveis de wrangler | Garantir apenas um `wrangler.toml` e caminho `.vercel/output/static` |

Notas adicionais:
- Se o erro interno persistir após limpar duplicidades, abrir ticket Cloudflare anexando o log completo.
- Planeje migração para OpenNext conforme aviso de depreciação.

Última atualização: 2025-09-19 (wrangler definitivo em apps/website, ajuste troubleshooting)