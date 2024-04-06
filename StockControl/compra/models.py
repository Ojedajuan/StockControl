from django.db import models

class Proveedor(models.Model):
    id=models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_documento= models.CharField(null=not (""), max_length=50)
    dni = models.CharField(max_length=10)
    mail_contacto =models.EmailField(null= not (""), max_length=254)

    class Meta:
        verbose_name= 'Proveedor'
        verbose_name_plural= 'Proveedores'
        ordering= ['nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    categoria= models.CharField(max_length=100, default= 'sin categoria')
    descripcion = models.CharField (max_length=100, blank=True,)
    stock_actual = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural='Productos'
        ordering= ['nombre']


    def __str__(self):
        return self.nombre

