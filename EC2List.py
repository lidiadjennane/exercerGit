import boto3
ec2 = boto3.resource('ec2') 
instance = ec2.instances.all()
#Ce commentaire a été ajouté ******************************
# Ceci est un commentaire pour github
#List of running instances , their types and state 
for i in instance:
	if (i.state["Code"] == 16): 
		print i.id, i.instance_type, i.state["Name"]
