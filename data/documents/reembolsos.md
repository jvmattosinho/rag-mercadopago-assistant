# Reembolsos no Mercado Pago

## Reembolso

Um reembolso permite devolver ao comprador o valor de um pagamento que já foi realizado.

Dependendo da operação, o reembolso pode ser total ou parcial.

## Reembolso total

No reembolso total, todo o valor elegível da operação é devolvido ao comprador.

Na Orders API, o reembolso pode ser solicitado através de:

POST /v1/orders/{id}/refund

## Reembolso parcial

Quando suportado pela operação, é possível devolver apenas parte do valor pago.

O valor informado para o reembolso parcial deve respeitar o valor disponível para devolução.

## Diferença entre cancelamento e reembolso

Cancelamento e reembolso representam situações diferentes.

O cancelamento normalmente ocorre antes da conclusão definitiva do pagamento.

O reembolso ocorre depois que um pagamento já foi realizado e existe um valor a ser devolvido ao comprador.

## Status

Após um reembolso, as informações da order podem refletir o novo estado da operação.

Um reembolso total pode resultar em:

status: refunded

Também podem existir situações de reembolso parcial.

## Idempotência

Solicitações de reembolso devem utilizar o mecanismo de idempotência quando exigido pela API.

O header utilizado é:

X-Idempotency-Key

Isso ajuda a impedir que uma tentativa repetida gere múltiplos reembolsos acidentalmente.

## Autenticação

A solicitação deve ser realizada pelo backend utilizando:

Authorization: Bearer SEU_ACCESS_TOKEN

O Access Token deve permanecer protegido.

## Segurança

Antes de solicitar um reembolso, a aplicação deve identificar corretamente a operação que será afetada.

Também é importante armazenar as informações necessárias para relacionar o reembolso à operação existente no sistema.

## Fonte

Mercado Pago Developers - Orders API / Reembolsos