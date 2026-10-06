# Autenticação na API do Mercado Pago

## Access Token

As requisições para a API do Mercado Pago devem ser autenticadas utilizando um Access Token.

O Access Token é uma credencial privada e deve ser utilizado no backend da aplicação.

## Header de autorização

O Access Token deve ser enviado no header HTTP `Authorization`, utilizando o padrão Bearer.

Exemplo:

Authorization: Bearer SEU_ACCESS_TOKEN

## Segurança

O Access Token não deve ser exposto no frontend da aplicação ou armazenado diretamente em código público.

As requisições para a API devem utilizar HTTPS.

## Fonte

Mercado Pago Developers - API Reference