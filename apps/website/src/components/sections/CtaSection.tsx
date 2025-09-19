export function CtaSection() {
  return (
    <section className="py-24 border-t">
      <div className="mx-auto max-w-4xl px-4 text-center">
        <h2 className="text-3xl md:text-4xl font-bold tracking-tight">Pronto para otimizar sua operação de entregas?</h2>
        <p className="mt-4 text-muted-foreground max-w-2xl mx-auto">Inicie agora pelo canal mais simples para o seu cliente e elimine atritos no ciclo de logística urbana.</p>
        <div className="mt-8 flex flex-wrap justify-center gap-4">
          <a
            href="https://wa.me/5599999999999?text=Quero%20fazer%20uma%20entrega"
            className="inline-flex items-center justify-center rounded-md bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow hover:bg-primary/90 transition"
          >
            Iniciar no WhatsApp
          </a>
          <a
            href="mailto:contato@pyloto.com"
            className="inline-flex items-center justify-center rounded-md border px-6 py-3 text-sm font-medium hover:bg-muted transition"
          >
            Falar com equipe
          </a>
        </div>
      </div>
    </section>
  )
}

export default CtaSection
