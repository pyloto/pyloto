const TESTIMONIALS = [
  { quote: 'Cotações instantâneas reduziram em 40% nosso tempo de resposta.', author: 'Rede de Farmácias', source: 'Google Reviews' },
  { quote: 'A automação via WhatsApp simplificou nossa operação.', author: 'Loja de Suplementos', source: 'Google Reviews' },
  { quote: 'Integração rápida e tracking confiável para nossos clientes.', author: 'E-commerce Local', source: 'Google Reviews' },
  { quote: 'Serviço excepcional, entrega sempre no prazo.', author: 'Restaurante Popular', source: 'Google Reviews' },
  { quote: 'Sistema intuitivo e suporte muito eficiente.', author: 'Clínica Veterinária', source: 'Google Reviews' },
  { quote: 'Melhorou significativamente nossa logística.', author: 'Loja de Informática', source: 'Google Reviews' }
]

export function Testimonials() {
  return (
    <section className="py-24 border-t bg-muted/30">
      <div className="mx-auto max-w-7xl px-4">
        <div className="max-w-2xl mb-12">
          <h2 className="text-3xl md:text-4xl font-bold tracking-tight">Depoimentos</h2>
          <p className="mt-4 text-muted-foreground">O que nossos clientes dizem sobre a experiência com a Pyloto.</p>
        </div>
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {TESTIMONIALS.map(t => (
            <figure key={t.author} className="relative rounded-lg border bg-background p-6 shadow-sm">
              <blockquote className="text-sm leading-relaxed mb-4">&ldquo;{t.quote}&rdquo;</blockquote>
              <figcaption className="text-xs font-medium text-muted-foreground">
                {t.author}
                <span className="block text-xs text-muted-foreground/70 mt-1">{t.source}</span>
              </figcaption>
            </figure>
          ))}
        </div>
      </div>
    </section>
  )
}
