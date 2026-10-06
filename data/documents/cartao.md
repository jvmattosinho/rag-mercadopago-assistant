# Pagamentos com Cartão no Mercado Pago

## Cartões

O Checkout Transparente permite receber pagamentos com cartão diretamente no site ou aplicativo.

Os dados sensíveis do cartão não devem ser enviados diretamente para o backend da aplicação.

## Tokenização

Os dados do cartão são utilizados para gerar um token.

Esse token representa os dados do cartão e pode ser enviado ao backend para realizar o pagamento sem expor os dados sensíveis do cartão.

## Public Key

No frontend, a integração utiliza a Public Key da aplicação para operações relacionadas à tokenização do cartão.

A Public Key pode ser exposta no frontend.

## Access Token

No backend, as requisições para as APIs do Mercado Pago utilizam o Access Token.

Exemplo:

Authorization: Bearer SEU_ACCESS_TOKEN

O Access Token é privado e não deve ser exposto no frontend.

## Criar pagamento

Na Orders API, uma order com pagamento por cartão pode ser criada através de:

POST /v1/orders

A requisição contém informações da order, do comprador e da transação de pagamento.

## Token do cartão

O token gerado no frontend é enviado na transação para que o Mercado Pago processe o pagamento.

O backend não deve armazenar dados sensíveis do cartão.

## Parcelamento

Pagamentos com cartão podem permitir parcelamento.

A quantidade de parcelas é informada na transação de pagamento de acordo com as opções disponíveis para o comprador.

## Status

Após o processamento, a order e suas transações possuem informações de status.

Essas informações devem ser utilizadas pela aplicação para determinar o resultado do pagamento.

Um pagamento pode ser aprovado, permanecer em processamento ou não ser concluído.

## Segurança

Nunca armazene informações sensíveis do cartão, como código de segurança.

Utilize os mecanismos de tokenização fornecidos pelo Mercado Pago.

Credenciais privadas, como o Access Token, devem permanecer exclusivamente no backend.

## Idempotência

Operações de criação devem utilizar o header X-Idempotency-Key quando exigido pela API.

Isso ajuda a evitar pagamentos duplicados em caso de repetição da requisição.

## Fonte

Mercado Pago Developers - Checkout Transparente / Orders API / Cartões