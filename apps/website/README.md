# Website (Site Público Pyloto)

Este app contém o **site público (marketing/homepage)** da Pyloto. Objetivo principal: presença SEO inicial, explicação de valor e geração de conversões (lead via WhatsApp / futuro formulário).

## 🎯 Objetivos do MVP
- Hero enxuto destacando badge + heading + subtítulo e carrossel de serviços
- Página dedicada /pyloto-entrega concentra copy detalhada (benefícios, como funciona, métricas e CTA)
- Testimonials sintetizados com sumário de reputação (15 avaliações 5★) e plano de integração real
- Navegação minimizada para caminhos de conversão (Produto / Contato / Entrar)
- Layout responsivo mobile-first

## 🗂️ Estrutura
```
apps/website/
├── next.config.js
├── package.json
├── public/                # Imagens, ícones, favicons
├── src/
│   ├── app/               # App Router (layout.tsx, page.tsx, pyloto-entrega/)
│   ├── components/
│   │   ├── layout/        # Header, Footer
│   │   ├── providers/     # Providers globais (theme, react-query)
│   │   └── sections/      # Hero, ServicesCarousel, Testimonials, SectionShell, CTA (uso agora só em /pyloto-entrega)
│   ├── styles/            # Arquivos globais (tailwind.css, theme.css)
│   ├── hooks/             # (futuro) custom hooks
│   ├── services/          # (futuro) clients REST/GraphQL
│   ├── utils/             # Helpers puros
│   └── types/             # Tipos locais
└── tests/                 # (futuro) testes e2e/unit
```

| Tipo | Local | Regra |
|------|-------|-------|
| Seções de página | `components/sections/` | Autônomas, conteúdo estático ou props; sem side-effects |
| Layout global | `components/layout/` | Header / Footer |
| Providers | `components/providers/` | Contextos isolados (tema, query) |
| Carrossel | `components/sections/services-carousel.tsx` | Controle local de estado | 

## 🔄 Ajustes 20-09 Pós-Revisão
- Removidos da home: métricas, CTA de entregas e copy de produto (migraram para /pyloto-entrega)
- Adicionado card "Pyloto Entrega" ao carrossel (primeira posição)
- Testimonials agora: título centralizado + sumário reputacional + nota de futura integração Google Reviews
- CTA final agora exclusivo na página /pyloto-entrega

## 📌 Integração Futuras (Backlog Curto)
| Item | Status | Notas |
|------|--------|-------|
| Google Reviews fetch + cache | Planejado | Usar cron + API Places / scraping aprovado |
| Animação O.T.T.O área visual | Planejado | Canvas/WebGL ou Lottie + toggle | 
| Dark mode | Planejado | theme provider já preparado |

---
Última atualização: 2025-09-20 (refine pós realocação conteúdo /pyloto-entrega)
