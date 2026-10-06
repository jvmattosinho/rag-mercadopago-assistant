# Pagamentos com Boleto no Mercado Pago

## Boleto

O Checkout Transparente permite oferecer boleto como meio de pagamento.

Diferentemente de pagamentos instantâneos, o boleto depende do pagamento pelo comprador e da posterior confirmação.

## Criar pagamento com boleto

O pagamento pode ser criado através da Orders API:

POST /v1/orders

A requisição deve conter os dados necessários da order, do comprador e do meio de pagamento.

## Dados do comprador

Para pagamentos com boleto, podem ser necessários dados de identificação do comprador.

As informações exigidas dependem da configuração e das regras aplicáveis à operação.

## Autenticação

A requisição realizada pelo backend deve utilizar:

Authorization: Bearer SEU_ACCESS_TOKEN

O Access Token deve permanecer protegido no backend.

## Idempotência

Na criação da operação, utilize o header X-Idempotency-Key quando exigido.

Isso ajuda a evitar a criação duplicada de uma operação caso a requisição precise ser repetida.

## Pagamento pendente

Após a criação do boleto, o pagamento pode permanecer aguardando a ação do comprador.

A aplicação não deve considerar o pagamento concluído apenas porque o boleto foi gerado.

É necessário acompanhar o status da operação.

## Vencimento

O boleto possui uma data de vencimento.

Após o vencimento, um boleto não pago pode deixar de estar disponível para pagamento de acordo com as regras da operação.

## Confirmação do pagamento

A confirmação não ocorre necessariamente no momento em que o comprador efetua o pagamento.

A aplicação deve acompanhar as atualizações da operação para identificar quando o pagamento foi efetivamente processado.

## Notificações

Webhooks podem ser utilizados para receber notificações sobre mudanças relacionadas às operações de pagamento.

Dessa forma, a aplicação não precisa depender somente de consultas periódicas à API.

## Segurança

Dados privados e credenciais não devem ser expostos no frontend.

Todas as chamadas autenticadas para as APIs devem ser realizadas de forma segura pelo backend.

## Fonte

Mercado Pago Developers - Checkout Transparente / Orders API / Boleto