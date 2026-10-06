# Webhooks no Mercado Pago

## O que são Webhooks

Webhooks permitem que o Mercado Pago envie notificações para a aplicação quando determinados eventos acontecem.

Isso evita que a aplicação precise consultar constantemente a API para descobrir se houve alguma mudança.

## URL de notificação

A aplicação deve disponibilizar uma URL pública para receber as notificações.

Essa URL deve utilizar HTTPS e estar preparada para receber requisições enviadas pelo Mercado Pago.

## Eventos

As notificações podem informar alterações relacionadas às operações de pagamento.

Ao receber uma notificação, a aplicação pode identificar o recurso relacionado ao evento e consultar a API para obter informações atualizadas.

## Recebimento da notificação

O endpoint responsável pelo webhook deve responder corretamente ao Mercado Pago para confirmar o recebimento.

O processamento interno da aplicação pode ser realizado separadamente após o recebimento da notificação.

## Validação

A aplicação deve validar a autenticidade das notificações recebidas.

Essa validação ajuda a garantir que a requisição realmente foi enviada pelo Mercado Pago.

## Assinatura secreta

O Mercado Pago disponibiliza uma assinatura secreta que pode ser utilizada para validar a origem das notificações Webhook.

A aplicação deve utilizar as informações recebidas na requisição e a assinatura secreta para realizar essa validação.

## Consulta da operação

Uma notificação não deve ser tratada necessariamente como a única fonte de informações sobre a operação.

Após receber o evento, a aplicação pode consultar a API do Mercado Pago para obter o estado atualizado do recurso.

## Idempotência no processamento

Uma mesma notificação pode ser recebida mais de uma vez.

Por isso, o processamento do webhook deve ser idempotente.

A aplicação deve evitar executar novamente uma ação de negócio que já tenha sido processada anteriormente.

## Exemplo

Um pagamento é criado e permanece aguardando confirmação.

Posteriormente, o Mercado Pago envia uma notificação para o webhook da aplicação.

A aplicação recebe o evento, valida sua autenticidade e consulta a API para verificar o estado atualizado do pagamento.

Com essa informação, o sistema pode atualizar o pedido correspondente.

## Boas práticas

Utilize HTTPS no endpoint.

Valide a autenticidade das notificações.

Esteja preparado para receber eventos repetidos.

Não dependa da ordem de chegada das notificações.

Consulte a API quando for necessário confirmar o estado atual do recurso.

## Fonte

Mercado Pago Developers - Webhooks