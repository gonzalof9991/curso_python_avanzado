from filestack import Client
client = Client('ADEJVxigJSpabxfbFBoKrz')

new_filelink = client.upload(filepath='bill.pdf')
print(new_filelink.url)