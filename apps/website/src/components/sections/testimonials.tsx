const TESTIMONIALS = [
  // Placeholder para integração futura via Google Places/Business API
  { quote: 'Excelente experiência, suporte rápido e plataforma estável.', author: 'Comércio Local', source: 'Google Reviews' },
  { quote: 'Escalamos nossas entregas mantendo previsibilidade.', author: 'Operador Logístico', source: 'Google Reviews' },
  { quote: 'Automação reduziu tempo operacional em várias etapas.', author: 'Rede Varejista', source: 'Google Reviews' }
]

export function Testimonials() {
  return (
    <section className="py-24 border-t bg-muted/30">
      <div className="mx-auto max-w-7xl px-4">
        <div className="max-w-3xl mb-12 text-center mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold tracking-tight mb-4">Validação dos Clientes</h2>
          <p className="text-muted-foreground">15 avaliações 5★ no Google – integraremos em breve os depoimentos reais extraídos automaticamente.</p>
        </div>
        <div className="grid gap-6 md:grid-cols-3">
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
        <p className="mt-10 text-center text-xs text-muted-foreground">Integração automática com Google Reviews planejada (captura periódica + cache).</p>
      </div>
    </section>
  )
}
