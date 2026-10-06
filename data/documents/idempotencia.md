# Idempotência no Mercado Pago

## O que é idempotência

Idempotência é um mecanismo utilizado para evitar que uma mesma operação seja executada mais de uma vez quando uma requisição é repetida.

Isso é especialmente importante em operações financeiras para evitar cobranças ou pagamentos duplicados.

## X-Idempotency-Key

O Mercado Pago utiliza o header:

X-Idempotency-Key

Esse header identifica de forma única uma requisição.

## Exemplo

Uma requisição pode enviar:

X-Idempotency-Key: 123456789

Se a mesma operação precisar ser reenviada por causa de uma falha de comunicação, a mesma chave deve ser utilizada.

## Repetição de requisições

Imagine que uma aplicação envia uma solicitação de pagamento, mas ocorre um timeout antes de receber a resposta.

A aplicação não sabe se o pagamento foi processado.

Ao repetir a requisição utilizando a mesma X-Idempotency-Key, a API consegue identificar que aquela operação já foi enviada anteriormente.

Isso ajuda a impedir que um novo pagamento seja criado acidentalmente.

## Nova operação

Uma nova operação deve utilizar uma nova chave de idempotência.

Não se deve reutilizar a mesma chave para operações diferentes.

## Geração da chave

A aplicação cliente é responsável por gerar o valor utilizado como X-Idempotency-Key.

Uma estratégia comum é utilizar um UUID ou outro identificador único gerado pela aplicação.

## Exemplo de fluxo

Primeira tentativa:

POST /v1/orders

X-Idempotency-Key: 550e8400-e29b-41d4-a716-446655440000

Ocorre um timeout.

A aplicação repete a operação utilizando a mesma chave:

POST /v1/orders

X-Idempotency-Key: 550e8400-e29b-41d4-a716-446655440000

A reutilização da chave permite identificar que as duas requisições correspondem à mesma operação.

## Boas práticas

Utilize uma chave única para cada nova operação.

Em tentativas de repetição da mesma operação, reutilize a chave original.

Armazene a chave associada à operação no sistema quando for necessário realizar novas tentativas.

Não utilize a mesma chave para operações diferentes.

## Fonte

Mercado Pago Developers - Idempotência