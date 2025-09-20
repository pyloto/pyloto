import { ServicesCarousel } from './services-carousel'

export function Hero() {
  return (
    <section className="relative overflow-hidden">
      <div className="absolute inset-0 -z-10 bg-gradient-to-br from-background via-background to-primary/10" />
      <div className="mx-auto max-w-7xl px-4 pt-28 pb-20 md:pt-36 md:pb-28">
        {/* Header Section */}
        <div className="text-center mb-16">
          <h1 className="text-3xl md:text-4xl font-bold tracking-tight mb-4">
            Soluções da Pyloto Corp
          </h1>
          <p className="text-lg text-muted-foreground max-w-3xl mx-auto">
            Além da plataforma de entregas, oferecemos um portfólio integrado para acelerar a transformação digital das empresas.
          </p>
        </div>

        <div className="flex flex-col lg:flex-row items-start gap-14">
          {/* Services Section */}
          <div className="flex-1">
            <span className="inline-block rounded-full border px-3 py-1 text-xs font-medium tracking-wide mb-4">Logística assistida por IA</span>
            <h2 className="text-4xl md:text-5xl font-bold leading-tight tracking-tight mb-6">
              Entregas urbanas <span className="text-primary">inteligentes</span><br/> com automação em tempo real
            </h2>
            <p className="max-w-xl text-base md:text-lg text-muted-foreground leading-relaxed mb-8">
              Cotações instantâneas, pagamento PIX e acompanhamento em tempo real via uma experiência conversacional.
            </p>

            {/* Services Carousel */}
            <div className="mb-8">
              <ServicesCarousel />
            </div>

            {/* CTA Section */}
            <div className="mb-10">
              <h3 className="text-xl font-semibold mb-4">Pronto para otimizar sua operação?</h3>
              <a
                href="https://wa.me/+5541988991078?text=Quero%20falar%20com%20a%20equipe"
                className="inline-flex items-center justify-center rounded-md bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow hover:bg-primary/90 transition"
              >
                Falar com a equipe
              </a>
            </div>

            {/* Stats */}
            <div className="grid grid-cols-3 gap-6 max-w-md">
              <div>
                <p className="text-2xl font-bold">98%</p>
                <p className="text-xs text-muted-foreground">Satisfação</p>
              </div>
              <div>
                <p className="text-2xl font-bold"><span className="tabular-nums">30</span>min</p>
                <p className="text-xs text-muted-foreground">Média de entrega</p>
              </div>
              <div>
                <p className="text-2xl font-bold">+12k</p>
                <p className="text-xs text-muted-foreground">Entregas</p>
              </div>
            </div>
          </div>

          {/* Visual Area */}
          <div className="flex-1 w-full aspect-[4/5] md:aspect-[4/5] rounded-xl bg-neutral-900/70 border relative flex items-center justify-center text-muted-foreground text-sm">
            <span className="opacity-60 px-6 text-center leading-relaxed">
              Área visual demonstrativa para destaque de identidade / animação futuramente.
              <br /><br />
              Em breve: O.T.T.O - Assistente de IA com efeitos futuristas
            </span>
          </div>
        </div>
      </div>
    </section>
  )
}
