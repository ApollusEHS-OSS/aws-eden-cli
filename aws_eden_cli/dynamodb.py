import logging
import time

import botocore

logger = logging.getLogger()


def describe_remote_state_table(dynamodb, table_name):
    response = dynamodb.describe_table(TableName=table_name)
    table_status = response['Table']['TableStatus']
    return table_status


def create_remote_state_table(dynamodb, table_name):
    try:
        response = dynamodb.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'env_name',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'last_updated',
                    'AttributeType': 'S'
                }
            ],
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'env_name',
                    'KeyType':       'HASH'
                },
            ],
            GlobalSecondaryIndexes=[
                {
                    'IndexName':  'env_name_last_updated_gsi',
                    'KeySchema':  [
                        {
                            'AttributeName': 'env_name',
                            'KeyType':       'HASH',
                        },
                        {
                            'AttributeName': 'last_updated',
                            'KeyType':       'RANGE',
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL',
                    }
                },
            ],
            BillingMode='PAY_PER_REQUEST',
        )
        table_status = response['TableDescription']['TableStatus']
        return table_status

    except Exception as e:
        if hasattr(e, 'response') and 'Error' in e.response:
            logger.error(e.response['Error']['Message'])
            return None
        else:
            logger.error(f"Unknown exception raised: {e}")
            return None


def check_remote_state_table(dynamodb, table_name):
    try:
        table_status = describe_remote_state_table(dynamodb, table_name)
    except botocore.exceptions.NoCredentialsError:
        logger.error("AWS credentials not found!")
        return False
    except Exception as e:
        if hasattr(e, 'response') and 'Error' in e.response:
            code = e.response['Error']['Code']
            if code == 'ResourceNotFoundException':
                table_status = create_remote_state_table(dynamodb, table_name)
                if table_status is None:
                    return False
            else:
                logger.error(e.response['Error']['Message'])
                return False

        else:
            logger.error(f"Unknown exception raised: {e}")
            return False

    if table_status == 'DELETING':
        logger.error("Table deletion is in progress, try again later")
        return False

    elif table_status == 'UPDATING':
        logger.error("Table update is in progress, try again later")
        return False

    elif table_status == 'CREATING':
        logger.info("Waiting for table creation...")
        while table_status != 'ACTIVE':
            time.sleep(0.1)
            table_status = describe_remote_state_table(dynamodb, table_name)

    return True
