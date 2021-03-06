from aws_eden_core import validators

DEFAULT_TABLE_NAME = 'eden'
DEFAULT_PROFILE_NAME = 'default'

parameters = [
    {
        'name': 'endpoint_s3_bucket_name',
        'envvar_name': 'ENDPOINT_S3_BUCKET_NAME',
        'validator': validators.is_string,
        'help_string': 'Endpoints file S3 bucket_name',
        'flag': '--endpoint-s3-bucket-name',
    },
    {
        'name': 'endpoint_s3_key',
        'envvar_name': 'ENDPOINT_S3_KEY',
        'validator': validators.is_string,
        'help_string': 'Endpoints file S3 key',
        'flag': '--endpoint-s3-key',
    },
    {
        'name': 'endpoint_name_prefix',
        'envvar_name': 'ENDPOINT_NAME_PREFIX',
        'validator': validators.is_string,
        'help_string': 'Endpoint name prefix',
        'flag': '--endpoint-name-prefix',
    },
    {
        'name': 'endpoint_update_key',
        'envvar_name': 'ENDPOINT_UPDATE_KEY',
        'validator': validators.is_string,
        'help_string': 'Endpoint update key',
        'flag': '--endpoint-update-key',
    },
    {
        'name': 'endpoint_env_type',
        'envvar_name': 'ENDPOINT_ENV_TYPE',
        'validator': validators.is_string,
        'help_string': 'Endpoint env type',
        'flag': '--endpoint-env-type',
    },
    {
        'name': 'domain_name_prefix',
        'envvar_name': 'DOMAIN_NAME_PREFIX',
        'validator': validators.is_string,
        'help_string': 'Endpoint domain name prefix',
        'flag': '--domain-name-prefix',
    },
    {
        'name': 'dynamic_zone_id',
        'envvar_name': 'DYNAMIC_ZONE_ID',
        'validator': validators.is_string,
        'help_string': 'Dynamic Zone ID',
        'flag': '--dynamic-zone-id',
    },
    {
        'name': 'name_prefix',
        'envvar_name': 'NAME_PREFIX',
        'validator': validators.is_string,
        'help_string': 'Resource name prefix',
        'flag': '--name-prefix',
    },
    {
        'name': 'target_cluster',
        'envvar_name': 'TARGET_CLUSTER',
        'validator': validators.is_string,
        'help_string': 'Target cluster for dynamic environments',
        'flag': '--target-cluster',
    },
    {
        'name': 'master_alb_arn',
        'envvar_name': 'MASTER_ALB_ARN',
        'validator': validators.is_string,
        'help_string': 'Master ALB ARN',
        'flag': '--master-alb-arn',
    },
    {
        'name': 'reference_service_arn',
        'envvar_name': 'REFERENCE_SERVICE_ARN',
        'validator': validators.is_string,
        'help_string': 'Reference ECS Service ARN',
        'flag': '--reference-service-arn',
    },
]

parameter_names = set()
for p in parameters:
    parameter_names.add(p['name'])
