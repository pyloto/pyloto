const FEATURES = [
  {
    title: 'Cotação Instantânea',
    desc: 'Rotas e preços calculados em segundos com dados de tráfego.'
  },
  {
    title: 'Pagamento PIX',
    desc: 'Confirmação imediata e liberação automática do fluxo.'
  },
  {
    title: 'Acompanhamento Tempo Real',
    desc: 'Transparência total da coleta à entrega final.'
  },
  {
    title: 'Automação Conversacional',
    desc: 'Experiência natural pelo canal mais usado: WhatsApp.'
  },
  {
    title: 'Escalabilidade Urbana',
    desc: 'Infra preparada para múltiplas cidades e alto volume.'
  },
  {
    title: 'Segurança & Observabilidade',
    desc: 'Monitoração contínua, métricas e controles de acesso.'
  }
]

export function Features() {
  return (
    <section id="beneficios" className="py-24 border-t bg-muted/30">
      <div className="mx-auto max-w-7xl px-4">
        <div className="max-w-2xl">
          <h2 className="text-3xl md:text-4xl font-bold tracking-tight">Benefícios principais</h2>
          <p className="mt-4 text-muted-foreground">Cada componente da plataforma foi desenhado para reduzir atrito operacional e acelerar o ciclo pedido → entrega.</p>
        </div>
        <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {FEATURES.map(f => (
            <div key={f.title} className="group relative rounded-lg border bg-background p-6 shadow-sm hover:shadow-md transition">
              <h3 className="font-semibold mb-2">{f.title}</h3>
              <p className="text-sm leading-relaxed text-muted-foreground">{f.desc}</p>
              <div className="absolute inset-0 rounded-lg ring-0 group-hover:ring-2 ring-primary/30 transition" />
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
