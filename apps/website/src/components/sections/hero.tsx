export function Hero() {
  return (
    <section className="relative overflow-hidden">
      <div className="absolute inset-0 -z-10 bg-gradient-to-br from-background via-background to-primary/10" />
      <div className="mx-auto max-w-7xl px-4 pt-28 pb-20 md:pt-36 md:pb-28 flex flex-col md:flex-row items-center gap-14">
        <div className="flex-1">
          <span className="inline-block rounded-full border px-3 py-1 text-xs font-medium tracking-wide mb-4">Logística assistida por IA</span>
          <h1 className="text-4xl md:text-5xl font-bold leading-tight tracking-tight">
            Entregas urbanas <span className="text-primary">inteligentes</span><br/> com automação em tempo real
          </h1>
          <p className="mt-6 max-w-xl text-base md:text-lg text-muted-foreground leading-relaxed">
            Cotações instantâneas, pagamento PIX e acompanhamento em tempo real via uma experiência conversacional.
          </p>
          <div className="mt-8 flex flex-wrap gap-4">
            <a
              href="https://wa.me/5599999999999?text=Quero%20fazer%20uma%20entrega"
              className="inline-flex items-center justify-center rounded-md bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow hover:bg-primary/90 transition"
            >
              Começar pelo WhatsApp
            </a>
            <a
              href="#como-funciona"
              className="inline-flex items-center justify-center rounded-md border px-6 py-3 text-sm font-medium hover:bg-muted transition"
            >
              Ver como funciona
            </a>
          </div>
          <div className="mt-10 grid grid-cols-3 gap-6 max-w-md text-center">
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
        <div className="flex-1 w-full aspect-[4/5] md:aspect-[4/5] rounded-xl bg-neutral-900/70 border relative flex items-center justify-center text-muted-foreground text-sm">
          <span className="opacity-60 px-6 text-center leading-relaxed">
            Área visual demonstrativa para destaque de identidade / animação futuramente.
          </span>
        </div>
      </div>
    </section>
  )
}
