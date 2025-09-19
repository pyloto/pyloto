"use client"
import Link from 'next/link'
import { useState, useId } from 'react'

const WHATSAPP_NUMBER = process.env.NEXT_PUBLIC_WHATSAPP_NUMBER || '5599999999999'
const WHATSAPP_MESSAGE = encodeURIComponent('Quero fazer uma entrega')

export function Header() {
  const [open, setOpen] = useState(false)
  const menuId = useId()
  return (
    <header className="sticky top-0 z-40 w-full border-b bg-background/80 backdrop-blur" role="banner">
      <div className="mx-auto flex h-16 w-full max-w-7xl items-center justify-between px-4">
        <Link href="/" className="font-semibold text-xl tracking-tight">
          Pyloto
        </Link>
        <nav className="hidden gap-8 text-sm font-medium md:flex" aria-label="Navegação principal">
          <Link href="#como-funciona" className="hover:text-primary transition-colors">Como funciona</Link>
          <Link href="#beneficios" className="hover:text-primary transition-colors">Benefícios</Link>
          <Link href="#servicos" className="hover:text-primary transition-colors">Serviços</Link>
          <Link href="/pyloto-entrega" className="hover:text-primary transition-colors">Pyloto Entrega</Link>
          <Link href="#depoimentos" className="hover:text-primary transition-colors">Depoimentos</Link>
          <Link href="#contato" className="hover:text-primary transition-colors">Contato</Link>
        </nav>
        <div className="flex items-center gap-3">
          <a
            href={`https://wa.me/${WHATSAPP_NUMBER}?text=${WHATSAPP_MESSAGE}`}
            className="rounded-md bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground shadow hover:bg-primary/90 transition"
            rel="noopener noreferrer"
            target="_blank"
          >
            Solicitar Entrega
          </a>
          <button
            className="md:hidden inline-flex h-9 w-9 items-center justify-center rounded-md border focus-visible:outline focus-visible:outline-2"
            onClick={() => setOpen(o => !o)}
            aria-label={open ? 'Fechar menu' : 'Abrir menu'}
            aria-expanded={open}
            aria-controls={menuId}
            type="button"
          >
            <span className="sr-only">{open ? 'Fechar menu' : 'Abrir menu'}</span>
            <span aria-hidden="true">☰</span>
          </button>
        </div>
      </div>
      <nav
        id={menuId}
        hidden={!open}
        className="md:hidden border-t bg-background"
        aria-label="Menu móvel"
      >
        <div className="flex flex-col px-4 py-4 gap-4 text-sm" role="menu">
          <Link role="menuitem" onClick={()=>setOpen(false)} href="#como-funciona">Como funciona</Link>
          <Link role="menuitem" onClick={()=>setOpen(false)} href="#beneficios">Benefícios</Link>
          <Link role="menuitem" onClick={()=>setOpen(false)} href="#servicos">Serviços</Link>
          <Link role="menuitem" onClick={()=>setOpen(false)} href="/pyloto-entrega">Pyloto Entrega</Link>
          <Link role="menuitem" onClick={()=>setOpen(false)} href="#depoimentos">Depoimentos</Link>
          <Link role="menuitem" onClick={()=>setOpen(false)} href="#contato">Contato</Link>
        </div>
  </nav>
    </header>
  )
}
