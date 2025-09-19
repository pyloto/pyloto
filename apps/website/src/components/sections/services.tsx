import { SectionShell } from './section-shell'
import { Bot, Workflow, LayoutDashboard, TrendingUp } from 'lucide-react'
import type { ComponentType, SVGProps } from 'react'

type Service = {
  title: string
  desc: string
  slug: string
  benefit: string
  icon: ComponentType<SVGProps<SVGSVGElement>>
}

const SERVICES: Service[] = [
  {
    title: 'Chatbots com IA',
    slug: 'chatbot-ia',
    desc: 'Assistentes contextuais para suporte, vendas e operação — integrados ao WhatsApp e outros canais.',
    benefit: 'Reduz tempo médio de resposta e escala atendimento sem aumentar equipe.',
    icon: Bot
  },
  {
    title: 'Automação de Sistemas',
    slug: 'automacao-sistemas',
    desc: 'Integração de APIs, orquestração de workflows e eliminação de tarefas manuais repetitivas.',
    benefit: 'Liberando sua equipe para focar em inteligência de negócio.',
    icon: Workflow
  },
  {
    title: 'Desenvolvimento de Websites & Painéis',
    slug: 'websites-paineis',
    desc: 'Portais, painéis administrativos e experiências sob medida com foco em performance e conversão.',
    benefit: 'Arquitetura escalável preparada para novas integrações.',
    icon: LayoutDashboard
  },
  {
    title: 'Marketing Digital & Growth',
    slug: 'marketing-digital',
    desc: 'Planejamento de aquisição, conteúdo, mídia paga e analytics orientado a métricas reais de negócio.',
    benefit: 'Estratégia de crescimento mensurável e previsível.',
    icon: TrendingUp
  }
]

export function Services() {
  return (
    <SectionShell
      id="servicos"
      eyebrow="Serviços"
      title="Soluções da Pyloto Corp"
      subtitle="Além da plataforma de entregas, oferecemos um portfólio integrado para acelerar a transformação digital das empresas."
      borderTop
      bg="bg-muted/30"
    >
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {SERVICES.map(s => (
          <div
            key={s.slug}
            className="group relative flex flex-col rounded-lg border bg-background p-6 shadow-sm hover:shadow-md transition"
          >
            <div className="mb-3">
              <div className="mb-4 inline-flex h-10 w-10 items-center justify-center rounded-md bg-primary/10 text-primary ring-1 ring-primary/20">
                <s.icon className="h-5 w-5" aria-hidden="true" />
                <span className="sr-only">Ícone de {s.title}</span>
              </div>
              <h3 className="font-semibold leading-tight text-base">{s.title}</h3>
              <p className="mt-1 text-sm text-muted-foreground leading-relaxed">{s.desc}</p>
            </div>
            <p className="mt-auto pt-3 border-t text-xs text-muted-foreground/90 italic">{s.benefit}</p>
            <div className="absolute inset-0 rounded-lg ring-0 group-hover:ring-2 ring-primary/30 transition" />
          </div>
        ))}
      </div>
    </SectionShell>
  )
}
