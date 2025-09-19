import { Hero } from '@/components/sections/hero'
import { Features } from '@/components/sections/features'
import { HowItWorks } from '@/components/sections/how-it-works'
import { Testimonials } from '@/components/sections/testimonials'
import { CTA } from '@/components/sections/CTA'
import { Services } from '@/components/sections/services'
import { Header } from '@/components/layout/header'
import { Footer } from '@/components/layout/footer'

export default function HomePage() {
  return (
    <div className="min-h-screen bg-background">
      <Header />
      <main>
        <Hero />
        <Features />
        <HowItWorks />
  <Testimonials />
  <Services />
        <CTA />
      </main>
      <Footer />
    </div>
  )
}