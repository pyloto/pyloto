const TESTIMONIALS = [
  { quote: 'Cotações instantâneas reduziram em 40% nosso tempo de resposta.', author: 'Rede de Farmácias' },
  { quote: 'A automação via WhatsApp simplificou nossa operação.', author: 'Loja de Suplementos' },
  { quote: 'Integração rápida e tracking confiável para nossos clientes.', author: 'E-commerce Local' }
]

export function Testimonials() {
  return (
    <section id="depoimentos" className="py-24 border-t bg-muted/30">
      <div className="mx-auto max-w-7xl px-4">
        <div className="max-w-2xl">
          <h2 className="text-3xl md:text-4xl font-bold tracking-tight">Depoimentos</h2>
          <p className="mt-4 text-muted-foreground">Validação inicial de parceiros em pilotos controlados.</p>
        </div>
        <div className="mt-12 grid gap-6 md:grid-cols-3">
          {TESTIMONIALS.map(t => (
            <figure key={t.author} className="relative rounded-lg border bg-background p-6 shadow-sm">
              <blockquote className="text-sm leading-relaxed">“{t.quote}”</blockquote>
              <figcaption className="mt-4 text-xs font-medium text-muted-foreground">{t.author}</figcaption>
            </figure>
          ))}
        </div>
      </div>
    </section>
  )
}
