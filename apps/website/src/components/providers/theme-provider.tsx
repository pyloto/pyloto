"use client"
import * as React from 'react'

interface Props {
  children: React.ReactNode
  attribute?: string
  defaultTheme?: string
  enableSystem?: boolean
  disableTransitionOnChange?: boolean
}

export function ThemeProvider({ children }: Props) {
  // Simplificação: placeholder para futura integração de tema
  return <>{children}</>
}
