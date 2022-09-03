from django.db import models
#
from .contants import *
from applications.user.models import User
from .managers import OutlineKeyManager,OutlineServerManager

#App de Terceros
from outline_vpn.outline_vpn import OutlineVPN

# Create your models here.


class OutlineServer(models.Model):
    api_url = models.CharField(max_length=256)
    server_name = models.CharField(max_length=50)

    transferred_bytes = models.BigIntegerField(default=0)
    limit_bytes = models.BigIntegerField(default=DEFAULT_SERVER_DATA_LIMIT)

    user = models.ForeignKey(User, related_name='user_server', on_delete=models.CASCADE)

    objects = OutlineServerManager()

    def __str__(self):
        return self.server_name

    class Meta:
        verbose_name = 'Servidor'
        verbose_name_plural = 'Servidores'

class OutlineKey(models.Model):
    #Elementos de la Clave
    key_id = models.IntegerField('Llave ID',null=True,blank=True)
    name = models.CharField('Nombre',null=True, max_length=256,blank=True)
    password = models.CharField('Contraseña',null=True, max_length=15,blank=True)
    port = models.IntegerField(null=True,blank=True)
    method = models.CharField('Metodo',null=True, max_length=256,blank=True)
    access_url = models.CharField('Acceso Url',null=True, max_length=256,blank=True)
    used_bytes = models.BigIntegerField(null=True,blank=True)
    size = models.CharField(max_length=3)
    limit_data = models.BigIntegerField('Limite')

    objects = OutlineKeyManager()

    #Relaciones
    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE)
    server = models.ForeignKey(OutlineServer, related_name='server_fora', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Llave'
        verbose_name_plural = 'Llaves'

    """Metodo Save Para Registrar Usuario en el Servdor y la Base de Datos"""
    def save(self, *args, **kwargs):
        #Creando Conexion al Servidor
        client = OutlineVPN(api_url=self.server.api_url)

        cont = 0
        for cliente in client.get_keys():
            if cliente.name == self.name:
                super(OutlineKey, self).save(*args, **kwargs)
                return
        if cont<1:    
            key = client.create_key()
            client.rename_key(key.key_id,self.user.username)
            client.add_data_limit(key.key_id,self.limit_data*CONVERT_GB)

        self.key_id=int(key.key_id)
        self.name=str(self.user.username)
        self.password=key.password
        self.port=int(key.port)
        self.method=key.method
        self.access_url=key.access_url
        self.used_bytes=int(key.used_bytes)
        self.limit_data=self.limit_data
        self.save()

        super(OutlineKey, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        client = OutlineVPN(api_url=self.server.api_url)
        client.delete_key(self.key_id)

        super(OutlineKey, self).delete(*args, **kwargs)

    def rename_key(self,name):
        self.name = name

    def __str__(self):
        if self.name:
            return self.name
        else:
            return ''

