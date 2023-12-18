import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Создание клиента IAM
    iam_client = boto3.client('iam')
    
    # Получение имени пользователя и ключа доступа из события EventBridge
    user_name = event['detail']['resourceName']
    access_key_id = event['detail']['additionalEventData']['accessKeyId']
    
    try:
        # Деактивация ключа доступа
        iam_client.update_access_key(UserName=user_name, AccessKeyId=access_key_id, Status='Inactive')
        
        # Удаление ключа доступа
        iam_client.delete_access_key(UserName=user_name, AccessKeyId=access_key_id)
        
        print(f"Access key {access_key_id} for user {user_name} has been deactivated and deleted.")
    except ClientError as e:
        # Обработка возможных исключений
        print(f"Error occurred while deleting access key {access_key_id} for user {user_name}: {e}")

# Точка входа в функцию Lambda
if __name__ == "__main__":
    lambda_handler({'detail': {'resourceName': 'имя_пользователя', 'additionalEventData': {'accessKeyId': 'ключ_доступа'}}}, None)
