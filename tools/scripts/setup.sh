#!/bin/bash

# Pyloto Setup Script
# Configura o ambiente de desenvolvimento completo

set -e

echo "🚀 Configurando ambiente Pyloto..."
echo "=================================="

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função de log
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}"
}

warn() {
    echo -e "${YELLOW}[$(date +'%Y-%m-%d %H:%M:%S')] WARNING: $1${NC}"
}

error() {
    echo -e "${RED}[$(date +'%Y-%m-%d %H:%M:%S')] ERROR: $1${NC}"
}

# Verificar pré-requisitos
check_prerequisites() {
    log "Verificando pré-requisitos..."
    
    # Node.js
    if ! command -v node &> /dev/null; then
        error "Node.js não encontrado. Instale Node.js 18+ antes de continuar."
        exit 1
    fi
    
    NODE_VERSION=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
    if [ "$NODE_VERSION" -lt "18" ]; then
        error "Node.js versão 18+ é necessária. Versão atual: $(node --version)"
        exit 1
    fi
    
    # Python
    if ! command -v python3 &> /dev/null; then
        error "Python 3 não encontrado. Instale Python 3.11+ antes de continuar."
        exit 1
    fi
    
    # Docker
    if ! command -v docker &> /dev/null; then
        warn "Docker não encontrado. Algumas funcionalidades não estarão disponíveis."
    fi
    
    # Docker Compose
    if ! command -v docker-compose &> /dev/null; then
        warn "Docker Compose não encontrado. Algumas funcionalidades não estarão disponíveis."
    fi
    
    log "✅ Pré-requisitos verificados"
}

# Configurar variáveis de ambiente
setup_env() {
    log "Configurando variáveis de ambiente..."
    
    if [ ! -f ".env" ]; then
        if [ -f ".env.example" ]; then
            cp .env.example .env
            log "✅ Arquivo .env criado a partir do .env.example"
            warn "⚠️  Edite o arquivo .env com suas configurações antes de continuar"
        else
            error "Arquivo .env.example não encontrado"
            exit 1
        fi
    else
        log "✅ Arquivo .env já existe"
    fi
}

# Instalar dependências do monorepo
install_dependencies() {
    log "Instalando dependências do monorepo..."
    
    # Instalar dependências raiz
    npm install
    log "✅ Dependências raiz instaladas"
    
    # Instalar dependências dos workspaces
    npm run setup:frontend
    log "✅ Dependências frontend instaladas"
}

# Configurar backend Python
setup_backend() {
    log "Configurando backend Python..."
    
    cd apps/delivery-system
    
    # Criar ambiente virtual se não existir
    if [ ! -d "venv" ]; then
        python3 -m venv venv
        log "✅ Ambiente virtual Python criado"
    fi
    
    # Ativar ambiente virtual e instalar dependências
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    log "✅ Dependências Python instaladas"
    
    cd ../..
}

# Configurar banco de dados
setup_database() {
    log "Configurando banco de dados..."
    
    if command -v docker &> /dev/null && command -v docker-compose &> /dev/null; then
        # Usar Docker se disponível
        docker-compose -f tools/docker/docker-compose.dev.yml up -d postgres redis
        log "✅ PostgreSQL e Redis iniciados com Docker"
        
        # Aguardar banco estar pronto
        sleep 10
        
        # Executar migrações
        cd apps/delivery-system
        source venv/bin/activate
        alembic upgrade head
        log "✅ Migrações executadas"
        cd ../..
    else
        warn "Docker não disponível. Configure PostgreSQL e Redis manualmente."
        warn "Consulte a documentação para instruções de instalação local."
    fi
}

# Executar testes
run_tests() {
    log "Executando testes..."
    
    # Testes backend
    cd apps/delivery-system
    source venv/bin/activate
    pytest tests/ -v
    log "✅ Testes backend executados"
    cd ../..
    
    # Testes frontend (se configurados)
    if [ -f "apps/website/package.json" ]; then
        cd apps/website
        npm test -- --passWithNoTests
        log "✅ Testes website executados"
        cd ../..
    fi
    
    if [ -f "apps/admin-panel/package.json" ]; then
        cd apps/admin-panel
        npm test -- --passWithNoTests
        log "✅ Testes admin-panel executados"
        cd ../..
    fi
}

# Função principal
main() {
    echo "🎯 Pyloto Setup Script v1.0"
    echo "==========================="
    echo ""
    
    check_prerequisites
    setup_env
    install_dependencies
    setup_backend
    setup_database
    
    # Perguntar se deve executar testes
    read -p "Executar testes? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        run_tests
    fi
    
    echo ""
    log "🎉 Setup concluído com sucesso!"
    echo ""
    echo "📋 Próximos passos:"
    echo "==================="
    echo "1. Edite o arquivo .env com suas configurações"
    echo "2. Execute 'npm run dev' para iniciar em modo desenvolvimento"
    echo "3. Ou execute 'npm run docker:dev' para usar Docker"
    echo ""
    echo "📚 URLs úteis:"
    echo "=============="
    echo "• Website: http://localhost:3000"
    echo "• Admin Panel: http://localhost:3001"
    echo "• API Backend: http://localhost:8000"
    echo "• API Docs: http://localhost:8000/docs"
    echo "• Grafana: http://localhost:3002"
    echo ""
    echo "🆘 Precisa de ajuda? Consulte a documentação em docs/"
}

# Executar apenas se chamado diretamente
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi