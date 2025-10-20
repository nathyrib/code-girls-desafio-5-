import json

def lambda_handler(event, context):
    # Extrai informações do evento S3
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(f"Arquivo recebido: {key} no bucket: {bucket}")
    
    # Simulação de processamento
    response = {
        'statusCode': 200,
        'body': json.dumps(f"Processamento do arquivo {key} concluído com sucesso.")
    }
    
    return response
