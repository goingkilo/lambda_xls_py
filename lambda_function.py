import os
import boto3
import xls_processor

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    filename  = event['Records'][0]['s3']['object']['key']

    output_file_name = filename.split('.')[0] + '.json'
    tmp_file = '/tmp/' + output_file_name

    # move vars to environment
    s3 = boto3.resource("s3",aws_access_key_id=os.environ['s3_key'],aws_secret_access_key=os.environ['s3_secret'])

    s3.Bucket( bucket).download_file( filename, '/tmp/'+filename)

    content = xls_processor.handle( '/tmp/' +filename,  "MICs List by CC")
    save_to_disk( tmp_file, content)

    s3.Bucket( 'steel-bucket-out').upload_file( tmp_file, output_file_name)

    return 'Successfully processed file'


def save_to_disk( output_file_name, content):
    f = open( output_file_name, 'w')
    f.write(  content)
    f.close()



