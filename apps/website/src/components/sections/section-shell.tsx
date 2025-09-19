import type { ReactNode } from 'react'

interface SectionShellProps {
  readonly id?: string
  readonly eyebrow?: string
  readonly title: string
  readonly subtitle?: string
  readonly children: ReactNode
  readonly padded?: boolean
  readonly borderTop?: boolean
  readonly bg?: string
}

export function SectionShell({ id, eyebrow, title, subtitle, children, padded = true, borderTop = false, bg }: SectionShellProps) {
  return (
    <section id={id} className={[borderTop ? 'border-t' : '', bg || '', padded ? 'py-24' : ''].join(' ').trim()}>
      <div className="mx-auto max-w-7xl px-4">
        <div className="max-w-2xl">
          {eyebrow && <span className="text-xs uppercase tracking-wider text-primary font-semibold">{eyebrow}</span>}
          <h2 className="text-3xl md:text-4xl font-bold tracking-tight mt-2">{title}</h2>
          {subtitle && <p className="mt-4 text-muted-foreground leading-relaxed">{subtitle}</p>}
        </div>
        <div className="mt-12">
          {children}
        </div>
      </div>
    </section>
  )
}
