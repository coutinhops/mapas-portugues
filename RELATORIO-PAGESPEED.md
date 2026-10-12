# Relatório de alterações e PageSpeed

Data: 12 de outubro de 2026. Idioma preservado: português de Portugal.

## Entrega e âmbito
A réplica privada foi atualizada: https://mapas-portugues-remix.corallime.chatgpt.site
O endereço https://mapasportugues.vercel.app/ **não foi alterado**: não foi disponibilizado acesso ao projeto Vercel. Este pacote contém o código completo, pronto para publicação nesse projeto.

## PageSpeed mobile — antes/depois

| Indicador | Antes: original público | Depois: landing otimizada |
| --- | ---: | --- |
| Desempenho | 63/100 | Não mensurável: HTTP 401 |
| Acessibilidade | 80/100 | Não mensurável |
| Práticas recomendadas | 100/100 | Não mensurável |
| SEO | 91/100 | Não mensurável |
| First Contentful Paint | 2,7 s | Não mensurável |
| Largest Contentful Paint | 3,9 s | Não mensurável |
| Total Blocking Time | 260 ms | Não mensurável |
| Cumulative Layout Shift | 0,301 | Não mensurável |
| Speed Index | 2,7 s | Não mensurável |

**A meta de LCP < 2,5 s ainda não está comprovada. Não há pontuação posterior válida da landing page.**

Antes: teste real de laboratório em 12/10/2026 às 00:14 BRT; Moto G Power emulado, rede 4G lenta, Lighthouse 13.5.0.
Relatório: https://pagespeed.web.dev/analysis/https-mapasportugues-vercel-app/3l5u30k2gt?form_factor=mobile

Depois: tentativa real às 00:20 BRT. O Google recebeu a página de acesso privado, com HTTP 401. As pontuações dessa página foram excluídas, porque não representam a landing otimizada.
Tentativa: https://pagespeed.web.dev/analysis/https-mapas-portugues-remix-corallime-chatgpt-site/espt15b65l?form_factor=mobile

A API pública também foi tentada: respondeu HTTP 429 / RESOURCE_EXHAUSTED por quota. A interface web permitiu obter o relatório inicial. Os JSON incluídos são transcrições dos valores visíveis, não exports completos do Lighthouse.

O relatório inicial também mostrou dados de campo CrUX dos últimos 28 dias: LCP 1,3 s, CLS 0, FCP 1,3 s e TTFB 0,3 s; INP indisponível. Estes dados históricos não são o teste de laboratório e não demonstram o desempenho da versão nova.

### Principais alertas iniciais
- Imagens: economia estimada pelo Google de 1.453 KiB.
- Recursos que bloqueiam renderização: economia estimada de 1.720 ms.
- Cache: economia estimada de 246 KiB.
- Imagens sem dimensões, imagem sem alt, ausência de main, problemas de contraste e animações não compostas.

## Alterações aplicadas

| Pedido | Implementação |
| --- | --- |
| Checkout Essencial | Botão convertido em ligação direta ao checkout original off=jv77xndx, €7,90. Não depende de JavaScript. |
| Checkout Completo | Mantido off=89aswr9e, €14,90; o mesmo destino é usado no CTA mobile. |
| Âncora de preços | Confirmado section id=comprar, único; todas as âncoras verificadas. |
| CTA mobile | Barra fixa após iniciar scroll, preço anterior riscado €74,90 e atual €14,90; safe area e espaço inferior reservados. |
| 55 Mapas Mentais | Removida a referência +50, incluindo metadados. |
| Title | Mapas Mentais de Português — Gramática, Verbos e Sintaxe (PDF) | 55 Mapas |
| Description | 119 caracteres, preço e CTA em português europeu. |
| JSON-LD | Product com Offer 14.90 EUR e FAQPage com as sete perguntas e respostas da página. |
| Open Graph | Título, descrição, imagem absoluta com dimensões/alt, URL e locale pt_PT; canonical incluído. |
| Sitemap e robots | Ficheiros completos apontando para o domínio Vercel original. |
| Depoimentos | Movidos para imediatamente antes dos preços. |
| FAQ | details/summary nativo, grupo name comum e fallback de exclusividade em JS. |
| Símbolos órfãos | Removidos os fechos ×; modal de upgrade removido. Ampliação das amostras preservada com dialog e botão Fechar. |
| Urgência genérica | Oferta Especial substituída por Escolha o seu pacote; faixa com data automática removida. |
| Avisos de compras | Removidos os avisos gerados com nomes e minutos aleatórios. |
| Indexabilidade | Confirmado HTML estático: conteúdo já indexável sem JS, sem React/Vite e sem necessidade de SSG. |
| Imagens | Dimensões reais em todas as imagens; lazy abaixo da dobra; WebP e srcset responsivo. |
| Imagem principal | Exceção intencional ao lazy: eager, fetchpriority=high e preload responsivo para favorecer LCP. |
| Fontes | Preconnect e display=swap mantidos; pesos 400/500/600/700/800 usados na página; stylesheet não bloqueante com fallback noscript. |
| Cache | vercel.json incluído com cache de um dia para imagens e stale-while-revalidate. |
| Acessibilidade | main, alt, foco visível, botão de fechar sem símbolo órfão, suporte a movimento reduzido e verde mais escuro nos CTAs. |

## Reduções de ficheiros verificadas
Estas são medições locais dos ficheiros, não métricas PageSpeed. A escolha de srcset depende da largura e densidade do ecrã.

| Recurso | Original | Variante otimizada |
| --- | ---: | ---: |
| Mockup principal | 221.474 bytes | 66.700 bytes a 480 px |
| Mockup principal | 221.474 bytes | 125.974 bytes a 720 px |
| Nove amostras, total | 1.323.639 bytes | 252.390 bytes nas variantes de 256 px |
| Nove amostras, total | 1.323.639 bytes | 745.828 bytes nas variantes de 512 px |

As versões de resolução completa foram mantidas para ampliação. O pacote contém também os originais; o peso total do ZIP não corresponde ao que o browser descarrega.

## Verificações executadas
- Idioma, title exato, description, canonical, OG e estrutura de dados válidos.
- Sete entradas FAQ iguais ao conteúdo visível.
- Checkouts, preços, ordem das secções e ausência de IDs duplicados.
- Imagens e variantes existentes, decodificáveis e com dimensões corretas.
- Sintaxe dos sete scripts JavaScript e do JSON-LD.
- Testes com DOM simulado: CTA ao deslocar e regressar ao topo, exclusividade do FAQ, abertura/fecho do dialog, fallback sem dialog e eventos de checkout por plano, inclusive com analytics indisponível.
- Publicação privada concluída e confirmada.

Não houve teste visual interativo da réplica. Os testes de DOM simulado não substituem inspeção em dispositivos reais. Não foi efetuada uma compra.

## Para concluir a comparação válida
1. Publicar o conteúdo deste pacote no projeto Vercel original.
2. Confirmar visualmente em mobile os dois checkouts, o CTA fixo e o FAQ.
3. Repetir PageSpeed mobile no mesmo URL público. Para comparação mais estável, executar três testes e usar a mediana.
4. Avaliar LCP < 2,5 s e CLS ≤ 0,1; se houver regressão, usar o elemento LCP e o waterfall do relatório real para orientar os próximos ajustes.

Referências técnicas: https://web.dev/articles/optimize-lcp e https://developers.google.com/speed/docs/insights/v5/get-started
