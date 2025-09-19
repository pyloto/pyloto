"use client"
import Link from 'next/link'
import { useState } from 'react'

export function Header() {
  const [open, setOpen] = useState(false)
  return (
    <header className="sticky top-0 z-40 w-full border-b bg-background/80 backdrop-blur">
      <div className="mx-auto flex h-16 w-full max-w-7xl items-center justify-between px-4">
        <Link href="/" className="font-semibold text-xl tracking-tight">
          Pyloto
        </Link>
        <nav className="hidden gap-8 text-sm font-medium md:flex">
          <Link href="#como-funciona" className="hover:text-primary transition-colors">Como funciona</Link>
          <Link href="#beneficios" className="hover:text-primary transition-colors">Benefícios</Link>
          <Link href="#depoimentos" className="hover:text-primary transition-colors">Depoimentos</Link>
          <Link href="#contato" className="hover:text-primary transition-colors">Contato</Link>
        </nav>
        <div className="flex items-center gap-3">
          <a
            href="https://wa.me/5599999999999?text=Quero%20fazer%20uma%20entrega"
            className="rounded-md bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground shadow hover:bg-primary/90 transition"
          >
            Solicitar Entrega
          </a>
          <button
            className="md:hidden inline-flex h-9 w-9 items-center justify-center rounded-md border"
            onClick={() => setOpen(o => !o)}
            aria-label="Abrir menu"
          >
            <span className="i-lucide-menu" />
          </button>
        </div>
      </div>
      {open && (
        <div className="md:hidden border-t bg-background">
          <div className="flex flex-col px-4 py-4 gap-4 text-sm">
            <Link onClick={()=>setOpen(false)} href="#como-funciona">Como funciona</Link>
            <Link onClick={()=>setOpen(false)} href="#beneficios">Benefícios</Link>
            <Link onClick={()=>setOpen(false)} href="#depoimentos">Depoimentos</Link>
            <Link onClick={()=>setOpen(false)} href="#contato">Contato</Link>
          </div>
        </div>
      )}
    </header>
  )
}
