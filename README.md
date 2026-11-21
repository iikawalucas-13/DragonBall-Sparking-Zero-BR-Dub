# Dragon Ball: Sparking! ZERO — Projeto de Dublagem BR para Nintendo Switch

Projeto de pesquisa e organização para avaliar a viabilidade de uma dublagem brasileira, com foco em inventário de arquivos, catálogo de falas/personagens, documentação e testes de compatibilidade.

> **Status:** fase inicial de análise. Ainda não existe um pacote funcional para Nintendo Switch.

## Objetivos
- Inventariar arquivos fornecidos pelo usuário e registrar formatos/tamanhos.
- Organizar um catálogo de até 215 entradas, sem presumir que sejam 215 personagens únicos.
- Mapear falas e IDs somente com dados verificáveis e material autorizado.
- Documentar diferenças entre versões do jogo.
- Avaliar compatibilidade com Nintendo Switch antes de preparar qualquer pacote.

## Começar
1. Instale Python 3.10 ou superior.
2. Execute `python tools/analyzer.py "CAMINHO_DA_PASTA"`.
3. Consulte os relatórios JSON e CSV criados na pasta `reports/`.
4. Compartilhe apenas os relatórios de inventário, nunca arquivos de jogo ou áudio protegido.

## Estrutura
- `tools/analyzer.py`: inventário local de arquivos.
- `catalog/entries_template.csv`: modelo para registrar as 215 entradas.
- `docs/technical-plan.md`: plano e critérios de validação.
- `reports/`: destino local dos relatórios (não versionar arquivos pessoais).

## Limites importantes
- O analisador **não extrai, converte, modifica ou instala** arquivos do jogo.
- Arquivos de PC não são automaticamente compatíveis com Switch.
- Não distribuir arquivos do jogo, dumps, chaves, pacotes de áudio ou conteúdo protegido.
- Use somente cópias e materiais que você tem autorização para analisar; obtenha permissão dos responsáveis pela modificação e dos profissionais de voz antes de publicar qualquer áudio.
- Testes de mods devem ser feitos offline e respeitando as regras da plataforma.

## Privacidade e segurança
Este repositório está atualmente público. Não envie dumps, arquivos grandes, áudios, dados pessoais, tokens ou senhas.