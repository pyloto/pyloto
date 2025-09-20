import { Hero } from '@/components/sections/hero'
import { Testimonials } from '@/components/sections/testimonials'
import { Header } from '@/components/layout/header'
import { Footer } from '@/components/layout/footer'

export default function HomePage() {
  return (
    <div className="min-h-screen bg-background">
      <Header />
      <main>
        <Hero />
      </main>
      <Testimonials />
      <Footer />
    </div>
  )
}