import { Header } from '@/components/layout/header'
import { Footer } from '@/components/layout/footer'
import { SectionShell } from '@/components/sections/section-shell'
import Link from 'next/link'

const DIFFERENTIALS = [
  { title: 'Orquestração Inteligente', desc: 'Distribuição de entregas otimizada por dados de tráfego e janelas de SLA.' },
  { title: 'Rastreamento Transparente', desc: 'Cada etapa com status claro: coleta, rota, hub, destinatário.' },
  { title: 'Integrações Simples', desc: 'APIs e webhooks prontos para e-commerce, ERP e canais conversacionais.' },
  { title: 'Pagamentos Instantâneos', desc: 'PIX e conciliação automática para reduzir fricção financeira.' },
  { title: 'Escalabilidade Multi-Cidade', desc: 'Infra preparada para expansão geográfica sem retrabalho arquitetural.' },
  { title: 'Observabilidade e Segurança', desc: 'Logs estruturados, métricas e controles de acesso granular.' }
]

export default function PylotoEntregaPage() {
  return (
    <div className="min-h-screen bg-background">
      <Header />
      <main>
        <SectionShell
          eyebrow="Pyloto Entrega"
          title="Logística urbana acelerada por IA"
          subtitle="Gerencie, acompanhe e escale operações de entrega com transparência e automação conversacional."
          padded
        >
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {DIFFERENTIALS.map(d => (
              <div key={d.title} className="group relative rounded-lg border bg-background p-6 shadow-sm hover:shadow-md transition">
                <h3 className="font-semibold mb-2 leading-tight">{d.title}</h3>
                <p className="text-sm text-muted-foreground leading-relaxed">{d.desc}</p>
                <div className="absolute inset-0 rounded-lg ring-0 group-hover:ring-2 ring-primary/30 transition" />
              </div>
            ))}
          </div>
          <div className="mt-12 flex flex-wrap items-center gap-4">
            <Link href="/" className="text-sm font-medium text-primary hover:underline">Voltar para Home</Link>
            <Link href="/#contato" className="text-sm font-medium text-muted-foreground hover:text-foreground transition">Falar com time comercial →</Link>
          </div>
        </SectionShell>
      </main>
      <Footer />
    </div>
  )
}
