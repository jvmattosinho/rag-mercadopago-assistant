# Orders API do Mercado Pago

## O que é uma order

Uma order representa uma operação de pagamento gerenciada pela Orders API.

Ela centraliza informações como valor, comprador, meio de pagamento, transações, modo de processamento e status.

Para novas integrações com Checkout Transparente, a Orders API é a opção recomendada.

## Criar uma order

Uma order é criada através do endpoint:

POST /v1/orders

A API retorna um identificador único da order.

Esse ID pode ser utilizado posteriormente para consultar, processar, cancelar ou reembolsar a operação.

## Modos de processamento

O campo `processing_mode` determina como a order será processada.

Os principais valores são:

- `automatic`
- `manual`

## Processamento automático

No modo:

processing_mode: automatic

a order é criada e o pagamento é processado automaticamente.

Esse modo é indicado quando todas as informações necessárias para concluir a transação já estão disponíveis.

## Processamento manual

No modo:

processing_mode: manual

a order é criada primeiro e o processamento ocorre posteriormente.

Para processar uma order criada no modo manual, utilize:

POST /v1/orders/{order_id}/process

## Consultar uma order

Para consultar uma order pelo seu identificador:

GET /v1/orders/{id}

A resposta contém informações da order, incluindo status, modo de processamento e transações.

## Status da order

Uma order possui um status que representa seu estado atual.

Alguns exemplos são:

- `created`: order criada, ainda sem processamento concluído.
- `processing`: pagamento em processamento.
- `processed`: processamento concluído.
- `action_required`: alguma ação adicional é necessária.
- `canceled`: order cancelada.
- `refunded`: pagamento totalmente reembolsado.
- `failed`: processamento não concluído com sucesso.

## Status detail

Além do status principal, a order pode possuir um `status_detail`.

Exemplos:

- `created`
- `in_process`
- `accredited`
- `waiting_payment`
- `partially_refunded`

O `status_detail` fornece informações mais específicas sobre a situação da order.

## Ciclo de vida

Um fluxo comum de uma order pode ser:

created
↓
processing
↓
processed

Quando o pagamento é aprovado e creditado, a order pode apresentar:

status: processed

status_detail: accredited

Também existem fluxos alternativos, como cancelamento, falha ou reembolso.

## External Reference

O campo `external_reference` permite relacionar a order do Mercado Pago com um identificador existente no sistema da aplicação.

Por exemplo, um e-commerce pode armazenar o número do seu pedido nesse campo.

## Cancelar uma order

Uma order pode ser cancelada através do endpoint:

POST /v1/orders/{id}/cancel

O cancelamento é utilizado em situações permitidas antes da conclusão definitiva do pagamento.

## Reembolsar uma order

Uma order processada pode ser reembolsada através do endpoint:

POST /v1/orders/{id}/refund

O reembolso pode ser total ou parcial, conforme as condições da operação.

## Autenticação

As operações da Orders API devem ser autenticadas utilizando o Access Token no header:

Authorization: Bearer SEU_ACCESS_TOKEN

## Idempotência

Operações que exigem idempotência devem enviar o header:

X-Idempotency-Key

A chave deve possuir um valor exclusivo para a requisição.

Isso ajuda a impedir que uma operação seja executada novamente de forma acidental.

## Fonte

Mercado Pago Developers - Orders API