const STEPS = [
  { step: '1', title: 'Inicie no WhatsApp', desc: 'Envie uma mensagem descrevendo sua necessidade.' },
  { step: '2', title: 'Receba a cotação', desc: 'IA calcula rota, preço e tempo estimado.' },
  { step: '3', title: 'Pague via PIX', desc: 'Confirmação instantânea libera a operação.' },
  { step: '4', title: 'Acompanhe em tempo real', desc: 'Transparência total até a confirmação de entrega.' },
]

export function HowItWorks() {
  return (
    <section id="como-funciona" className="py-24 border-t">
      <div className="mx-auto max-w-7xl px-4">
        <div className="max-w-2xl">
          <h2 className="text-3xl md:text-4xl font-bold tracking-tight">Como funciona</h2>
          <p className="mt-4 text-muted-foreground">Fluxo otimizado para reduzir o tempo total de processamento e maximizar conversão.</p>
        </div>
        <ol className="mt-12 grid gap-6 md:grid-cols-4">
          {STEPS.map(s => (
            <li key={s.step} className="relative flex flex-col gap-3 rounded-lg border bg-background p-6">
              <div className="h-10 w-10 flex items-center justify-center rounded-full bg-primary text-primary-foreground font-semibold">{s.step}</div>
              <h3 className="font-medium">{s.title}</h3>
              <p className="text-sm text-muted-foreground leading-relaxed">{s.desc}</p>
            </li>
          ))}
        </ol>
      </div>
    </section>
  )
}
