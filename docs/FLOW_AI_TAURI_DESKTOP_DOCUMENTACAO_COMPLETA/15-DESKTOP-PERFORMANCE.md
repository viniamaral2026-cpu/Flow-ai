# Performance Desktop

## Metas
O FLOW deve iniciar rapidamente, consumir recursos de forma previsível e não manter processamento pesado sem necessidade.

## Monitorar
CPU, RAM, I/O, uso de GPU quando relevante, tempo de startup, tempo de primeira interação e reconexões.

## Voz
Wake Word e captura devem evitar consumo elevado contínuo. Suspender recursos quando desativados.

## WebView
Evitar renders desnecessários, listeners duplicados e vazamentos de memória.

## Rede
Cache e retry devem ser limitados para não gerar consumo excessivo.
