# Pagamentos no Mercado Pago

## Checkout Transparente

O Checkout Transparente permite processar pagamentos diretamente no site ou aplicativo do vendedor, sem redirecionar o comprador para uma página externa.

A integração permite maior controle sobre a experiência de pagamento e suporta diferentes meios de pagamento.

Entre os principais meios disponíveis estão:

- Cartão de crédito
- Cartão de débito
- Pix
- Boleto

## Orders API

Para novas integrações com Checkout Transparente, a Orders API é a opção recomendada.

A Orders API centraliza o gerenciamento do pagamento através do recurso chamado order.

Uma order representa uma operação de pagamento e pode conter informações sobre:

- Valor da compra
- Comprador
- Meio de pagamento
- Transações
- Status do processamento
- Referência externa

## Criar uma order

Uma nova order pode ser criada através do endpoint:

POST /v1/orders

A requisição deve ser autenticada utilizando um Access Token.

Também deve ser utilizada uma chave de idempotência através do header:

X-Idempotency-Key

A chave de idempotência ajuda a impedir que uma mesma operação seja processada mais de uma vez acidentalmente.

## Processamento automático

Uma order pode utilizar o modo de processamento automático.

Nesse modo, a order é criada e o pagamento é processado automaticamente.

O modo é definido utilizando:

processing_mode: automatic

## Processamento manual

Também é possível utilizar processamento manual.

Nesse modo, a order é criada primeiro e processada posteriormente.

O modo é definido utilizando:

processing_mode: manual

Uma order criada para processamento manual pode posteriormente ser processada através do endpoint:

POST /v1/orders/{order_id}/process

## Consultar uma order

Uma order pode ser consultada através do seu identificador.

Endpoint:

GET /v1/orders/{id}

A consulta permite recuperar informações da order, incluindo seu estado e informações relacionadas ao processamento.

## Buscar orders

Também é possível pesquisar múltiplas orders utilizando filtros.

Endpoint:

GET /v1/orders

A busca pode utilizar informações como período e referência externa.

## Identificador da order

Quando uma order é criada, o Mercado Pago gera um identificador único.

Esse identificador pode ser utilizado posteriormente para consultar e gerenciar a operação.

## External Reference

Uma order pode possuir uma referência externa definida pela aplicação.

A external_reference permite relacionar a order do Mercado Pago com uma entidade existente no sistema do vendedor, como um pedido de um e-commerce.

## Autenticação

As requisições realizadas pelo backend devem utilizar o Access Token no header Authorization.

Exemplo:

Authorization: Bearer SEU_ACCESS_TOKEN

O Access Token é uma credencial privada e não deve ser exposto no frontend.

## Idempotência

Operações de criação e processamento devem utilizar o header X-Idempotency-Key quando exigido pela API.

A idempotência permite repetir uma requisição com segurança sem executar a mesma operação novamente de forma acidental.

Isso é especialmente importante em operações financeiras, pois ajuda a evitar pagamentos duplicados.

## Payments API

Integrações existentes também podem utilizar a Payments API.

Para novas integrações com Checkout Transparente, a recomendação atual é utilizar a Orders API.

Integrações existentes com Payments API continuam funcionando, mas essa API é considerada legado nesse fluxo.

## Fonte

Mercado Pago Developers - Checkout Transparente e Orders API