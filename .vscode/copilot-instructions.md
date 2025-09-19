# Copilot Instructions – Pyloto
- Observação: Esse Codespace esta aberto diretamente no repositório do projeto Pyloto (https://github.com/pyloto/pyloto), ou seja, não temos nenhum arquivo salvo localmente.

- Este arquivo contém instruções específicas para o GitHub Copilot, visando garantir que as sugestões de código estejam alinhadas com as melhores práticas e padrões do projeto Pyloto.
- Utilizar linguagens e frameworks conforme o contexto do projeto.
- Seguir as regras e diretrizes estabelecidas abaixo para manter a consistência e qualidade do código.

# Linguagens e Frameworks
- **Linguagem Principal**: Python 3.x
- **Frameworks**: Django, Flask, FastAPI, Whatsapp Business API, Celery, SQLAlchemy
- **Banco de Dados**: PostgreSQL, MySQL, SQLite
- **Outras Tecnologias**: Docker, Kubernetes, Redis, RabbitMQ
- **Ferramentas de Qualidade**: pylint, flake8, black
Obs 1.: Sempre sugerir soluções que utilizem essas tecnologias quando apropriado.
obs 2.: Evitar sugerir tecnologias ou frameworks não mencionados, a menos que seja absolutamente necessário e justificado.
Obs 3.: Priorizar soluções que sigam as melhores práticas de segurança, desempenho e escalabilidade.
Obs. 5: Sempre buscar soluções que promovam a modularidade e reutilização de código.

# Diretrizes de Código

## Regras Essenciais e Inalteráveis

1. **Padrões de Código**  
   - Sempre seguir **PEP 8**, **PEP 20 (Zen of Python)**, **PEP 257 (docstrings)** e **PEP 484 (type hints)**.  
   - Usar obrigatoriamente ferramentas de qualidade: **pylint**, **flake8** e **black**.  
   - Seguir padrão **MVC**.  

2. **Estrutura de Módulos**  
   - Todos os pacotes devem ter `__init__.py`, funcionando como **portais** que expõem funções e variáveis públicas (Exceto quando gerar import circular).  
   - Sempre sugerir **modularização** quando o arquivo ficar longo ou complexo.  

3. **Fluxo de Alterações**  
   - Se houver **qualquer dúvida sobre impacto ou intenção**, perguntar antes de alterar o código.  
   - Nunca fazer alterações destrutivas ou que quebrem compatibilidade sem validação explícita.  

4. **Organização do Repositório**  
   - A raiz deve conter apenas arquivos necessários para iniciar o serviço: `app/`, `celery/`, `.env`, scripts de inicialização/migração.  
   - **Testes e scripts** devem ficar em pastas próprias (`tests/`, `scripts/`), nunca soltos na raiz.  
    - **Documentação** deve estar em `docs/` ou `README.md`, nunca solta na raiz.
    - **Configurações** devem estar em `config/` ou `settings/`, nunca soltas na raiz.  
    - **Arquivos estáticos** (CSS, JS, imagens) devem estar em `static/` ou `assets/`, nunca soltos na raiz.
    - **Templates HTML** devem estar em `templates/`, nunca soltos na raiz.
    - **Módulos reutilizáveis** devem estar em `libs/` ou `utils/`, nunca soltos na raiz.
    - **Scripts de migração** devem estar em `migrations/`, nunca soltos na raiz.
    - **Scripts de inicialização** devem estar em `scripts/`, nunca soltos na raiz.
    - **Logs** devem ser armazenados em `logs/`, nunca soltos na raiz
    - **Documentação de API** deve estar em `docs/` ou `api_docs/`, nunca solta na raiz.
    - **Testes unitários e de integração** devem estar em `tests/`, nunca soltos na raiz.
    - **Arquivos de configuração de ambiente** (ex: `.env`, `config.yaml`) devem estar em `config/` ou `settings/`, nunca soltos na raiz.
    - **Scripts de build e deploy** devem estar em `scripts/` ou `deploy/`, nunca soltos na raiz.
    - **Arquivos de licença e termos de uso** devem estar em `LICENSE` ou `TERMS/`, nunca soltos na raiz.
    - **Arquivos de dados estáticos** (ex: CSV, JSON) devem estar em `data/`, nunca soltos na raiz.
    - **Arquivos de configuração de CI/CD** (ex: `.github/workflows/`, `.gitlab-ci.yml`) devem estar em `.github/` ou `.gitlab/`, nunca soltos na raiz.
    - **Arquivos de configuração de containerização** (ex: `Dockerfile`, `docker-compose.yml`) devem estar em `docker/` ou `containers/`, nunca soltos na raiz.
    - **Arquivos de configuração de monitoramento** (ex: `prometheus.yml`, `grafana.ini`) devem estar em `monitoring/`, nunca soltos na raiz.
    - **Arquivos de configuração de segurança** (ex: `firewall.rules`, `security_policy.yml`) devem estar em `security/`, nunca soltos na raiz.
    - **Arquivos de configuração de testes** (ex: `pytest.ini`, `tox.ini`) devem estar em `tests/` ou `config/`, nunca soltos na raiz.
    - **Arquivos de configuração de documentação** (ex: `mkdocs.yml`, `sphinx.conf`) devem estar em `docs/` ou `config/`, nunca soltos na raiz.
    - **Arquivos de configuração de dependências** (ex: `requirements.txt`, `Pipfile`) devem estar em `config/` ou `dependencies/`, nunca soltos na raiz.
    - **Arquivos de configuração de versionamento** (ex: `.gitignore`, `.gitattributes`) devem estar em `.git/` ou `config/`, nunca soltos na raiz.
    - **Arquivos de configuração de IDE** (ex: `.vscode/`, `.idea/`) devem estar em `.vscode/` ou `.idea/`, nunca soltos na raiz.
    - **Arquivos de configuração de análise estática** (ex: `.pylintrc`, `.flake8`) devem estar em `config/` ou `settings/`, nunca soltos na raiz.
    - **Arquivos de configuração de formatação de código** (ex: `pyproject.toml`, `.prettierrc`) devem estar em `config/` ou `settings/`, nunca soltos na raiz.
    - **Arquivos de configuração de logging** (ex: `logging.conf`, `logging.ini`) devem estar em `config/` ou `settings/`, nunca soltos na raiz.
    - **Arquivos de configuração de cache** (ex: `cache.conf`, `cache.ini`) devem estar em `config/` ou `settings/`, nunca soltos na raiz.

# TODAS as regras acima são inalteráveis e devem ser seguidas rigorosamente.
# Qualquer sugestão de melhoria deve ser discutida antes de implementação.
# SEMPRE DOCUMENTAR em arquivos apropriados qualquer alteração significativa. (README.md, docs/, etc.)