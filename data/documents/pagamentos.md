# Pagamentos no Mercado Pago

## Checkout Transparente

O Checkout Transparente permite processar pagamentos diretamente no site ou aplicativo, sem redirecionar o comprador para uma página externa.

Ele suporta diferentes meios de pagamento, como cartões, Pix e boleto.

## Orders API

A Orders API é a opção recomendada para o processamento de pagamentos no Checkout Transparente.

Para criar uma nova order, deve ser realizada uma requisição POST para:

`/v1/orders`

A order pode utilizar processamento automático ou manual.

## Consultar uma order

Uma order existente pode ser consultada pelo seu identificador utilizando uma requisição GET para:

`/v1/orders/{id}`

A consulta retorna informações da order, incluindo seu status, transações e modo de processamento.

## Idempotência

Na criação de uma order, o header `X-Idempotency-Key` é utilizado para evitar a criação duplicada de orders quando uma mesma solicitação é repetida.

## Fonte

Mercado Pago Developers - Checkout Transparente / Orders API