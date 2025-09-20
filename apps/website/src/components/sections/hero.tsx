import { ServicesCarousel } from './services-carousel'

export function Hero() {
  return (
    <section className="relative overflow-hidden">
      <div className="absolute inset-0 -z-10 bg-gradient-to-br from-background via-background to-primary/10" />
      <div className="mx-auto max-w-7xl px-4 pt-28 pb-20 md:pt-36 md:pb-28">
        <div className="flex flex-col lg:flex-row items-start gap-14">
          {/* Left content */}
          <div className="flex-1">
            <span className="inline-block rounded-full border px-3 py-1 text-xs font-medium tracking-wide mb-6">Logística assistida por IA</span>
            <h1 className="text-3xl md:text-4xl font-bold tracking-tight mb-4">
              Soluções da Pyloto Corp
            </h1>
            <p className="text-lg text-muted-foreground max-w-2xl mb-10">
              Além da plataforma de entregas, oferecemos um portfólio integrado para acelerar a transformação digital das empresas.
            </p>
            <ServicesCarousel />
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
