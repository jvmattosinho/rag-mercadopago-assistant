# Pagamentos com Pix no Mercado Pago

## Pix

O Pix é um meio de pagamento instantâneo que pode ser oferecido através do Checkout Transparente do Mercado Pago.

O comprador pode realizar o pagamento utilizando um QR Code ou o código Pix Copia e Cola.

## Criar pagamento Pix

Na Orders API, um pagamento Pix pode ser criado através do endpoint:

POST /v1/orders

Na transação, o meio de pagamento deve utilizar:

payment_method.id: pix

payment_method.type: bank_transfer

## Autenticação

A requisição deve enviar o Access Token:

Authorization: Bearer SEU_ACCESS_TOKEN

Também deve enviar uma chave de idempotência:

X-Idempotency-Key: VALOR_UNICO

## QR Code

Após a criação do pagamento Pix, a resposta pode retornar informações para que o comprador realize o pagamento.

Entre elas estão:

- ticket_url
- qr_code
- qr_code_base64

## ticket_url

O campo `ticket_url` contém uma URL que pode ser apresentada ao comprador.

Essa página contém informações para realizar o pagamento, incluindo QR Code, Pix Copia e Cola e instruções.

## qr_code

O campo `qr_code` contém o código utilizado no Pix Copia e Cola.

Ele pode ser apresentado ao comprador para que seja copiado e utilizado no aplicativo do banco.

## qr_code_base64

O campo `qr_code_base64` contém a representação da imagem do QR Code em Base64.

Essa informação pode ser utilizada para renderizar o QR Code diretamente na aplicação.

## Status aguardando pagamento

Enquanto o comprador ainda não realizou o pagamento Pix, a transação pode apresentar:

status: action_required

status_detail: waiting_transfer

Isso indica que uma ação do comprador ainda é necessária para concluir o pagamento.

## Expiração

Por padrão, o pagamento Pix possui prazo de 24 horas.

Esse período pode ser alterado através do campo:

expiration_time

Na Orders API, esse campo utiliza uma duração no formato ISO 8601.

O prazo configurado para Pix deve ficar entre 30 minutos e 30 dias.

## Processamento

O modo de processamento é definido através do campo:

processing_mode

Os valores podem ser:

automatic

ou:

manual

No modo automático, a order é criada e processada automaticamente.

No modo manual, a order precisa ser processada posteriormente.

## Cancelamento

Um pagamento Pix pendente ou em processamento pode ser cancelado enquanto estiver aguardando a conclusão do pagamento.

Pagamentos que ultrapassam o período de validade também podem expirar.

## Fonte

Mercado Pago Developers - Checkout Transparente / Orders API / Pix