# Autenticação na API do Mercado Pago

## Credenciais

As credenciais identificam uma aplicação nas integrações com o Mercado Pago.

Existem credenciais de teste e credenciais de produção.

As principais credenciais são:

- Public Key
- Access Token
- Client ID
- Client Secret

## Public Key

A Public Key é uma chave pública utilizada principalmente no frontend.

Ela pode ser utilizada, por exemplo, para acessar informações sobre meios de pagamento e para operações relacionadas aos dados de cartão no frontend.

Por ser uma chave pública, ela pode ser utilizada no lado público da aplicação.

## Access Token

O Access Token é uma credencial privada utilizada para autenticar requisições realizadas pelo backend para as APIs do Mercado Pago.

Ele deve permanecer protegido no servidor e não deve ser exposto no frontend ou armazenado diretamente em código público.

## Header Authorization

O Access Token deve ser enviado no header HTTP `Authorization` utilizando o padrão Bearer.

Exemplo:

Authorization: Bearer SEU_ACCESS_TOKEN

O Access Token não deve ser enviado através de parâmetros da URL.

## Credenciais de teste

Durante o desenvolvimento da integração, podem ser utilizadas credenciais de teste.

Elas permitem realizar configurações e validações sem executar transações reais em produção.

## Credenciais de produção

As credenciais de produção são utilizadas quando a integração estiver pronta para operar no ambiente produtivo.

As credenciais devem ser armazenadas de maneira segura e nunca publicadas em repositórios de código.

## Client ID e Client Secret

Client ID e Client Secret são utilizados principalmente em integrações que utilizam OAuth.

O Client ID identifica a aplicação.

O Client Secret é uma credencial privada e deve permanecer protegida no backend.

## OAuth

OAuth permite que uma aplicação obtenha autorização para acessar recursos do Mercado Pago.

O Mercado Pago disponibiliza diferentes fluxos para obtenção de Access Tokens.

## Authorization Code

O fluxo Authorization Code é utilizado quando uma aplicação precisa acessar recursos em nome de terceiros.

Nesse fluxo, o usuário autoriza explicitamente a aplicação a acessar seus dados.

Após a autorização, a aplicação recebe um código de autorização que pode ser utilizado para obter um Access Token.

## Client Credentials

O fluxo Client Credentials é utilizado quando a aplicação precisa acessar seus próprios recursos.

Nesse fluxo não existe interação com o usuário.

A aplicação utiliza seu Client ID e Client Secret para obter um Access Token.

## Refresh Token

Access Tokens obtidos através do fluxo Authorization Code podem ser renovados utilizando um Refresh Token.

Isso permite obter um novo Access Token sem solicitar novamente a autorização do usuário.

A renovação é realizada através do endpoint:

POST /oauth/token

## Segurança

As credenciais privadas devem ser armazenadas de maneira segura.

Nunca exponha:

- Access Token
- Client Secret
- Refresh Token

em código público, frontend ou repositórios Git.

O Access Token deve ser enviado através do header Authorization e as comunicações com as APIs devem utilizar HTTPS.

## Fonte

Mercado Pago Developers - Credenciais e OAuth