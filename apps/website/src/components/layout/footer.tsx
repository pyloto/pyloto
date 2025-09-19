export function Footer() {
  return (
    <footer id="contato" className="border-t bg-muted/30">
      <div className="mx-auto max-w-7xl px-4 py-10 grid gap-8 md:grid-cols-4 text-sm">
        <div>
          <h4 className="mb-2 font-semibold">Pyloto</h4>
          <p className="text-muted-foreground leading-relaxed">Inteligência em logística urbana e automação via IA.</p>
        </div>
        <div>
          <h4 className="mb-2 font-semibold">Plataforma</h4>
          <ul className="space-y-1 text-muted-foreground">
            <li><a href="#como-funciona" className="hover:text-primary">Como funciona</a></li>
            <li><a href="#beneficios" className="hover:text-primary">Benefícios</a></li>
            <li><a href="#depoimentos" className="hover:text-primary">Depoimentos</a></li>
          </ul>
        </div>
        <div>
          <h4 className="mb-2 font-semibold">Contato</h4>
          <ul className="space-y-1 text-muted-foreground">
            <li><a href="mailto:contato@pyloto.com" className="hover:text-primary">contato@pyloto.com</a></li>
            <li><a href="https://wa.me/5599999999999" className="hover:text-primary">WhatsApp comercial</a></li>
          </ul>
        </div>
        <div>
          <h4 className="mb-2 font-semibold">Acompanhe</h4>
          <div className="flex gap-3 text-muted-foreground">
            <a href="#" aria-label="LinkedIn" className="hover:text-primary">in</a>
            <a href="#" aria-label="Twitter" className="hover:text-primary">X</a>
            <a href="#" aria-label="GitHub" className="hover:text-primary">GH</a>
          </div>
        </div>
      </div>
      <div className="border-t text-center py-4 text-xs text-muted-foreground">© {new Date().getFullYear()} Pyloto Corp. Todos os direitos reservados.</div>
    </footer>
  )
}
