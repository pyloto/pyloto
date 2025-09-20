"use client"
import Image from 'next/image'
import { useState, useEffect } from 'react'
import { Eye, EyeOff } from 'lucide-react'

/**
 * Componente visual do O.T.T.O com animação de surgimento futurista e toggle.
 */
export function OttoVisual() {
  const [visible, setVisible] = useState(true)
  const [mounted, setMounted] = useState(false)

  useEffect(() => {
    const t = setTimeout(() => setMounted(true), 40)
    return () => clearTimeout(t)
  }, [])

  return (
    <div className="relative w-full h-full flex items-center justify-center overflow-hidden">
      {/* Botão Toggle */}
      <button
        type="button"
        onClick={() => setVisible(v => !v)}
        className="absolute top-3 right-3 z-20 inline-flex items-center justify-center h-9 w-9 rounded-md border bg-background/70 backdrop-blur text-foreground hover:bg-background/90 shadow-sm transition"
        aria-label={visible ? 'Ocultar O.T.T.O' : 'Mostrar O.T.T.O'}
      >
        {visible ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
      </button>

      {/* Efeitos de fundo (brilhos/partículas simples) */}
      <div className="pointer-events-none absolute inset-0">
        <div className="absolute -top-32 left-1/2 h-72 w-72 -translate-x-1/2 rounded-full bg-primary/20 blur-3xl animate-pulse" />
        <div className="absolute bottom-0 left-1/4 h-40 w-40 rounded-full bg-purple-500/20 blur-2xl animate-[ping_6s_linear_infinite]" />
        <div className="absolute top-10 right-10 h-24 w-24 rounded-full bg-blue-500/10 blur-xl animate-[pulse_5s_ease-in-out_infinite]" />
      </div>

      {/* Container da imagem com animações */}
      <div
        className={[
          'relative z-10 transition-all duration-900 ease-[cubic-bezier(.22,.68,.37,1)]',
          mounted && visible ? 'opacity-100 scale-100 rotate-0' : 'opacity-0 scale-75 -rotate-3',
          !visible && mounted ? 'pointer-events-none' : '',
        ].join(' ')}
      >
        <div className="relative">
          <div className="absolute -inset-4 rounded-2xl bg-gradient-to-tr from-primary/30 via-fuchsia-400/20 to-cyan-300/20 blur-2xl opacity-40 animate-[pulse_7s_ease-in-out_infinite]" />
          <Image
            src="/otto.png"
            alt="O.T.T.O Assistente de IA"
            width={520}
            height={520}
            priority
            className="relative rounded-xl shadow-lg ring-1 ring-white/10 select-none pointer-events-none"
          />
          {/* Brilho dinâmico overlay */}
          <div className="pointer-events-none absolute inset-0 rounded-xl mix-blend-screen bg-[radial-gradient(circle_at_30%_20%,rgba(255,255,255,0.25),transparent_60%)]" />
        </div>
      </div>

      {/* Overlay quando oculto (feedback) */}
      {mounted && !visible && (
        <div className="absolute inset-0 flex items-center justify-center text-xs text-muted-foreground/70">
          <span className="tracking-wide">O.T.T.O oculto</span>
        </div>
      )}
    </div>
  )
}
