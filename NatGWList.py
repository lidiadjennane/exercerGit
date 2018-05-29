import boto3 
client = boto3.client('ec2')
response = client.describe_nat_gateways()
for ngw in response['NatGateways']:
	print 'NATGW ID is :', ngw['NatGatewayId']
	print 'TAGS :'
	for tag in ngw['Tags']:
		print tag['Key'], ':', tag['Value']
	print '-----------------------------------------'