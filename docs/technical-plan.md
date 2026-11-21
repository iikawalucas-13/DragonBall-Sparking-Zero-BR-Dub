# Plano técnico

## Fase 1 — Inventário
- Registrar nomes, extensões, tamanhos e caminhos relativos.
- Verificar se os arquivos relacionados formam um conjunto coerente.
- Não inferir o formato interno apenas pela extensão.

## Fase 2 — Catálogo
- Preencher `catalog/entries_template.csv` usando os nomes exibidos pelo launcher.
- Distinguir personagem, transformação, forma alternativa, menu e história.
- Registrar origem/ID apenas quando houver evidência verificável.

## Fase 3 — Pesquisa de áudio
- Identificar o middleware/formato por evidências técnicas.
- Verificar permissões para usar e redistribuir cada gravação.
- Não assumir que áudio de PC funciona no Switch.

## Fase 4 — Compatibilidade Switch
- Confirmar Title ID, versão do jogo e estrutura esperada por fontes legítimas.
- Fazer testes pequenos e reversíveis, offline.
- Não produzir instalador até haver um teste real bem-sucedido.
- Documentar exatamente as versões testadas; não prometer compatibilidade universal.

## Critérios para considerar um pacote pronto
1. Arquivos de áudio autorizados e identificados.
2. Mapeamento de IDs validado em teste.
3. Estrutura reconhecida pelo ambiente-alvo.
4. Testes offline sem corrupção de dados.
5. Instruções de instalação e remoção revisadas.

## Não incluir no repositório
Dumps do jogo, chaves, arquivos PAK/UCAS/UTOC, arquivos de áudio protegidos, executáveis de terceiros, credenciais ou dados pessoais.