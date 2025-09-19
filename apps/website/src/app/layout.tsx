import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import { ThemeProvider } from '@/components/providers/theme-provider'
import { QueryProvider } from '@/components/providers/query-provider'
import '@/styles/tailwind.css'
import '@/styles/theme.css'
import { Toaster } from 'sonner'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: {
    default: 'Pyloto - Plataforma de Entregas Inteligente',
    template: '%s | Pyloto'
  },
  description: 'A plataforma mais inteligente para conectar quem precisa de entregas com entregadores qualificados. Powered by AI.',
  keywords: [
    'entrega',
    'delivery',
    'logística',
    'inteligência artificial',
    'WhatsApp',
    'Brasil'
  ],
  authors: [{ name: 'Pyloto Corp' }],
  creator: 'Pyloto Corp',
  publisher: 'Pyloto Corp',
  robots: {
    index: true,
    follow: true,
  },
  openGraph: {
    type: 'website',
    locale: 'pt_BR',
    url: 'https://pyloto.com.br',
    title: 'Pyloto - Plataforma de Entregas Inteligente',
    description: 'A plataforma mais inteligente para conectar quem precisa de entregas com entregadores qualificados.',
    siteName: 'Pyloto',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Pyloto - Plataforma de Entregas Inteligente',
    description: 'A plataforma mais inteligente para conectar quem precisa de entregas.',
    creator: '@pyloto',
  },
  viewport: 'width=device-width, initial-scale=1',
  themeColor: [
    { media: '(prefers-color-scheme: light)', color: '#ffffff' },
    { media: '(prefers-color-scheme: dark)', color: '#000000' },
  ],
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt-BR" suppressHydrationWarning>
      <body className={inter.className}>
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          <QueryProvider>
            {children}
            <Toaster position="top-right" richColors />
          </QueryProvider>
        </ThemeProvider>
      </body>
    </html>
  )
}