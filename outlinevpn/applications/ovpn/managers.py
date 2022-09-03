from .contants import *
from django.db import models

#App de Terceros
from outline_vpn.outline_vpn import OutlineVPN

class OutlineKeyManager(models.Manager):

    def create_key(self,user,server,limit_data):
        client = OutlineVPN(api_url=server.api_url)
        key = client.create_key()
        client.rename_key(key.key_id,user.username)
        client.add_data_limit(key.key_id,limit_data*CONVERT_GB)

        o_key = self.create(
            key_id=int(key.key_id),
            name=str(user.username),
            password=key.password,
            port=int(key.port),
            method=key.method,
            access_url=key.access_url,
            used_bytes=int(key.used_bytes),
            limit_data=limit_data,
            user = user,
            server = server
        )
        if o_key:
            return True
        else:
            return False

    def save_used_bytes(self,id,byte):
        key = self.get(id=id)
        size = byte[1]
        tam = byte[0]
        key.used_bytes = float(tam)
        key.size = size
        key.save()

class OutlineServerManager(models.Manager):

    def create_server(self,api_url,server_name,limit_bytes,user):
        if limit_bytes == None or limit_bytes < 0:
            limit_bytes = DEFAULT_SERVER_DATA_LIMIT
        o_server = self.create(
            api_url=api_url,
            server_name = server_name,
            limit_bytes = limit_bytes,
            transferred_bytes = 0,
            user = user
        )

    def list_servers(self,user):
        return self.filter(
            user = user
        )



