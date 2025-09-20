import { Header } from '@/components/layout/header'
import { Footer } from '@/components/layout/footer'
import { SectionShell } from '@/components/sections/section-shell'
import Link from 'next/link'

const DIFFERENTIALS = [
	{
		title: 'Orquestração Inteligente',
		desc: 'Distribuição de entregas otimizada por dados de tráfego e janelas de SLA.',
	},
	{
		title: 'Rastreamento Transparente',
		desc: 'Cada etapa com status claro: coleta, rota, hub, destinatário.',
	},
	{
		title: 'Integrações Simples',
		desc: 'APIs e webhooks prontos para e-commerce, ERP e canais conversacionais.',
	},
	{
		title: 'Pagamentos Instantâneos',
		desc: 'PIX e conciliação automática para reduzir fricção financeira.',
	},
	{
		title: 'Escalabilidade Multi-Cidade',
		desc: 'Infra preparada para expansão geográfica sem retrabalho arquitetural.',
	},
	{
		title: 'Observabilidade e Segurança',
		desc: 'Logs estruturados, métricas e controles de acesso granular.',
	},
]

const FEATURES = [
	{
		title: 'Cotação Instantânea',
		desc: 'Rotas e preços calculados em segundos com dados de tráfego.',
	},
	{
		title: 'Pagamento PIX',
		desc: 'Confirmação imediata e liberação automática do fluxo.',
	},
	{
		title: 'Acompanhamento Tempo Real',
		desc: 'Transparência total da coleta à entrega final.',
	},
	{
		title: 'Automação Conversacional',
		desc: 'Experiência natural pelo canal mais usado: WhatsApp.',
	},
	{
		title: 'Escalabilidade Urbana',
		desc: 'Infra preparada para múltiplas cidades e alto volume.',
	},
	{
		title: 'Segurança & Observabilidade',
		desc: 'Monitoração contínua, métricas e controles de acesso.',
	},
]

const STEPS = [
	{
		step: '1',
		title: 'Inicie no WhatsApp',
		desc: 'Envie uma mensagem descrevendo sua necessidade.',
	},
	{
		step: '2',
		title: 'Receba a cotação',
		desc: 'IA calcula rota, preço e tempo estimado.',
	},
	{
		step: '3',
		title: 'Pague via PIX',
		desc: 'Confirmação instantânea libera a operação.',
	},
	{
		step: '4',
		title: 'Acompanhe em tempo real',
		desc: 'Transparência total até a confirmação de entrega.',
	},
]

export default function PylotoEntregaPage() {
	return (
		<div className="min-h-screen bg-background">
			<Header />
			<main>
				{/* Novo Hero da página de entregas com informações movidas da home */}
				<section className="pt-32 pb-20 md:pt-40 md:pb-28 border-b">
					<div className="mx-auto max-w-7xl px-4 flex flex-col items-center text-center">
						<span className="inline-block rounded-full border px-3 py-1 text-xs font-medium tracking-wide mb-6">
							Logística assistida por IA
						</span>
						<h1 className="text-4xl md:text-5xl font-bold leading-tight tracking-tight mb-6">
							Entregas urbanas{' '}
							<span className="text-primary">inteligentes</span>
							<br /> com automação em tempo real
						</h1>
						<p className="max-w-2xl text-base md:text-lg text-muted-foreground leading-relaxed mb-10">
							Cotações instantâneas, pagamento PIX e acompanhamento em tempo real via uma experiência conversacional.
						</p>
						<div className="grid grid-cols-3 gap-6 max-w-md mb-12">
							<div>
								<p className="text-2xl font-bold">98%</p>
								<p className="text-xs text-muted-foreground">Satisfação</p>
							</div>
							<div>
								<p className="text-2xl font-bold">
									<span className="tabular-nums">30</span>min
								</p>
								<p className="text-xs text-muted-foreground">Média de entrega</p>
							</div>
							<div>
								<p className="text-2xl font-bold">+12k</p>
								<p className="text-xs text-muted-foreground">Entregas</p>
							</div>
						</div>
						<div className="text-center">
							<h2 className="text-2xl font-semibold mb-4">Pronto para otimizar sua operação?</h2>
							<a
								href="https://wa.me/+5541988991078?text=Quero%20falar%20com%20a%20equipe"
								className="inline-flex items-center justify-center rounded-md bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow hover:bg-primary/90 transition"
							>
								Falar com a equipe
							</a>
						</div>
					</div>
				</section>

				<SectionShell
					eyebrow="Pyloto Entrega"
					title="Logística urbana acelerada por IA"
					subtitle="Gerencie, acompanhe e escale operações de entrega com transparência e automação conversacional."
					padded
				>
					<div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
						{DIFFERENTIALS.map(d => (
							<div
								key={d.title}
								className="group relative rounded-lg border bg-background p-6 shadow-sm hover:shadow-md transition"
							>
								<h3 className="font-semibold mb-2 leading-tight">{d.title}</h3>
								<p className="text-sm text-muted-foreground leading-relaxed">{d.desc}</p>
								<div className="absolute inset-0 rounded-lg ring-0 group-hover:ring-2 ring-primary/30 transition" />
							</div>
						))}
					</div>
				</SectionShell>

				{/* Benefícios Section */}
				<section id="beneficios" className="py-24 border-t bg-muted/30">
					<div className="mx-auto max-w-7xl px-4">
						<div className="max-w-2xl">
							<h2 className="text-3xl md:text-4xl font-bold tracking-tight">Benefícios principais</h2>
							<p className="mt-4 text-muted-foreground">
								Cada componente da plataforma foi desenhado para reduzir atrito operacional e acelerar o ciclo pedido →
								entrega.
							</p>
						</div>
						<div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
							{FEATURES.map(f => (
								<div
									key={f.title}
									className="group relative rounded-lg border bg-background p-6 shadow-sm hover:shadow-md transition"
								>
									<h3 className="font-semibold mb-2">{f.title}</h3>
									<p className="text-sm leading-relaxed text-muted-foreground">{f.desc}</p>
									<div className="absolute inset-0 rounded-lg ring-0 group-hover:ring-2 ring-primary/30 transition" />
								</div>
							))}
						</div>
					</div>
				</section>

				{/* Como Funciona Section */}
				<section id="como-funciona" className="py-24 border-t">
					<div className="mx-auto max-w-7xl px-4">
						<div className="max-w-2xl">
							<h2 className="text-3xl md:text-4xl font-bold tracking-tight">Como funciona</h2>
							<p className="mt-4 text-muted-foreground">
								Fluxo otimizado para reduzir o tempo total de processamento e maximizar conversão.
							</p>
						</div>
						<ol className="mt-12 grid gap-6 md:grid-cols-4">
							{STEPS.map(s => (
								<li
									key={s.step}
									className="relative flex flex-col gap-3 rounded-lg border bg-background p-6"
								>
									<div className="h-10 w-10 flex items-center justify-center rounded-full bg-primary text-primary-foreground font-semibold">
										{s.step}
									</div>
									<h3 className="font-medium">{s.title}</h3>
									<p className="text-sm text-muted-foreground leading-relaxed">{s.desc}</p>
								</li>
							))}
						</ol>
					</div>
				</section>

				<div className="mt-12 flex flex-wrap items-center gap-4 px-4">
					<Link
						href="/"
						className="text-sm font-medium text-primary hover:underline"
					>
						Voltar para Home
					</Link>
					<Link
						href="/#contato"
						className="text-sm font-medium text-muted-foreground hover:text-foreground transition"
					>
						Falar com time comercial →
					</Link>
				</div>
			</main>
			<Footer />
		</div>
	)
}
