from appmakr import Client
from appmakr.models import Like

#Authenticate with the appmakr API

client = Client('e6c31c23-c356-4bd4-ad42-9f97cb7fbc26', '4T1DMggVTGFQ1%2FSmCg91a2ifSxY%3D')

#Adding a like within the system

like = Like('www.TestTestTest.com','Anything',32.54,35.74)
client.socialize.add_like(like)
