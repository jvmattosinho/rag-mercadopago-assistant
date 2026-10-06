# Erros na API do Mercado Pago

## Erros HTTP

As APIs do Mercado Pago utilizam códigos HTTP para indicar o resultado de uma requisição.

## 400 - Bad Request

Indica que a requisição possui dados inválidos ou não atende aos requisitos esperados pela API.

A aplicação deve verificar os parâmetros enviados e os detalhes retornados na resposta.

## 401 - Unauthorized

Indica um problema relacionado à autenticação.

A aplicação deve verificar se o Access Token foi enviado corretamente no header:

Authorization: Bearer SEU_ACCESS_TOKEN

Também deve verificar se a credencial é válida.

## 403 - Forbidden

Indica que a requisição foi entendida, mas a aplicação não possui permissão para executar a operação solicitada.

## 404 - Not Found

Indica que o recurso solicitado não foi encontrado.

A aplicação deve verificar identificadores como o ID da order ou de outros recursos consultados.

## 409 - Conflict

Pode indicar um conflito relacionado ao estado atual do recurso ou da operação solicitada.

A aplicação deve analisar os detalhes retornados pela API antes de tentar novamente.

## 429 - Too Many Requests

Indica que foram realizadas requisições em excesso.

A aplicação deve evitar novas tentativas imediatamente e aplicar uma estratégia de retry apropriada.

## 500 - Internal Server Error

Indica um erro interno durante o processamento da requisição.

A aplicação deve tratar esse tipo de erro e evitar repetir operações financeiras de maneira insegura.

## Retry

Alguns erros podem justificar uma nova tentativa.

Antes de repetir uma operação de criação ou processamento, a aplicação deve considerar o mecanismo de idempotência.

Utilizar a mesma X-Idempotency-Key para repetir a mesma operação ajuda a evitar duplicidade.

## Timeout

Um timeout não significa necessariamente que a operação falhou.

A requisição pode ter sido processada mesmo que a aplicação não tenha recebido a resposta.

Por isso, operações financeiras não devem ser simplesmente repetidas utilizando uma nova chave de idempotência.

A aplicação deve reutilizar a chave da operação original ou consultar o estado da operação quando apropriado.

## Tratamento de erros

A aplicação deve registrar informações suficientes para investigar falhas, sem registrar credenciais ou dados sensíveis.

Também deve analisar o código HTTP e os detalhes retornados pela API antes de decidir se uma operação deve ser repetida.

## Fonte

Mercado Pago Developers - API Reference / Tratamento de erros