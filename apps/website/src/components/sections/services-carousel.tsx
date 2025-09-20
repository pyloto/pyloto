"use client"
import { useState } from 'react'
import { Bot, Workflow, LayoutDashboard, TrendingUp, Package, ChevronLeft, ChevronRight } from 'lucide-react'
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
    title: 'Pyloto Entrega',
    slug: 'pyloto-entrega',
    desc: 'Intermediação e orquestração de entregas urbanas com rastreio e automação conversacional.',
    benefit: 'Eficiência operacional com transparência ponta a ponta.',
    icon: Package
  },
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

export function ServicesCarousel() {
  const [currentIndex, setCurrentIndex] = useState(0)
  const itemsPerView = 2
  const maxIndex = Math.max(0, SERVICES.length - itemsPerView)

  const nextSlide = () => {
    setCurrentIndex((prev) => (prev >= maxIndex ? 0 : prev + 1))
  }

  const prevSlide = () => {
    setCurrentIndex((prev) => (prev <= 0 ? maxIndex : prev - 1))
  }

  const visibleServices = SERVICES.slice(currentIndex, currentIndex + itemsPerView)

  return (
    <div className="relative">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-xl font-semibold">Nossos Serviços</h3>
        <div className="flex gap-2">
          <button
            onClick={prevSlide}
            disabled={currentIndex === 0}
            className="p-2 rounded-md border hover:bg-muted disabled:opacity-50 disabled:cursor-not-allowed transition"
            aria-label="Serviços anteriores"
          >
            <ChevronLeft className="h-4 w-4" />
          </button>
          <button
            onClick={nextSlide}
            disabled={currentIndex >= maxIndex}
            className="p-2 rounded-md border hover:bg-muted disabled:opacity-50 disabled:cursor-not-allowed transition"
            aria-label="Próximos serviços"
          >
            <ChevronRight className="h-4 w-4" />
          </button>
        </div>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        {visibleServices.map(s => (
          <div
            key={s.slug}
            className="group relative flex flex-col rounded-lg border bg-background p-4 shadow-sm hover:shadow-md transition"
          >
            <div className="mb-3">
              <div className="mb-3 inline-flex h-8 w-8 items-center justify-center rounded-md bg-primary/10 text-primary ring-1 ring-primary/20">
                <s.icon className="h-4 w-4" aria-hidden="true" />
                <span className="sr-only">Ícone de {s.title}</span>
              </div>
              <h4 className="font-semibold leading-tight text-sm mb-2">{s.title}</h4>
              <p className="text-xs text-muted-foreground leading-relaxed">{s.desc}</p>
            </div>
            <p className="mt-auto pt-2 border-t text-xs text-muted-foreground/90 italic">{s.benefit}</p>
            <div className="absolute inset-0 rounded-lg ring-0 group-hover:ring-2 ring-primary/30 transition" />
          </div>
        ))}
      </div>

      {/* Indicators */}
      <div className="flex justify-center gap-2 mt-4">
        {Array.from({ length: maxIndex + 1 }, (_, i) => (
          <button
            key={i}
            onClick={() => setCurrentIndex(i)}
            className={`h-2 w-2 rounded-full transition ${
              i === currentIndex ? 'bg-primary' : 'bg-muted-foreground/30'
            }`}
            aria-label={`Ir para slide ${i + 1}`}
          />
        ))}
      </div>
    </div>
  )
}