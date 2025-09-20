import { ServicesCarousel } from './services-carousel'

export function Hero() {
  return (
    <section className="relative overflow-hidden">
      <div className="absolute inset-0 -z-10 bg-gradient-to-br from-background via-background to-primary/10" />
      <div className="mx-auto max-w-7xl px-4 pt-20 pb-16 md:pt-28 md:pb-24">
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
            {/* Bloco Persuasivo Pós-Carrossel */}
            <div className="mt-12 p-6 rounded-xl border bg-background/60 backdrop-blur supports-[backdrop-filter]:bg-background/40 shadow-sm text-center">
              <h2 className="text-xl md:text-2xl font-semibold tracking-tight mb-3">
                Algo aqui chamou sua atenção? 🚀
              </h2>
              <p className="text-sm md:text-base text-muted-foreground max-w-xl mx-auto mb-6 leading-relaxed">
                Seja automação de WhatsApp, entregas urbanas, chatbots inteligentes ou desenvolvimento sob medida — vamos entender seu contexto e desenhar a próxima evolução digital da sua operação.
              </p>
              <a
                href="https://wa.me/+5541988991078?text=Quero%20falar%20com%20a%20equipe"
                className="inline-flex items-center justify-center rounded-md bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow hover:bg-primary/90 transition"
              >
                Falar com a equipe
              </a>
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
