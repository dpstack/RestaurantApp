# Generated by Django 3.2.8 on 2021-10-07 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cli_id', models.AutoField(primary_key=True, serialize=False)),
                ('cli_nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('cli_apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('cli_celular', models.CharField(max_length=15, verbose_name='Celular')),
                ('cli_direccion', models.CharField(max_length=30, verbose_name='Direccion')),
                ('cli_recomendaciones', models.TextField(verbose_name='Recomendaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('emp_cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('emp_apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('emp_celular', models.CharField(max_length=15, verbose_name='Celular')),
                ('emp_correo', models.CharField(max_length=30, verbose_name='Correo')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('prod_precio', models.IntegerField()),
                ('prod_cantidad', models.IntegerField()),
                ('prod_tipo', models.CharField(max_length=45, verbose_name='Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('prov_nit', models.IntegerField(primary_key=True, serialize=False)),
                ('prov_nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('prov_celular', models.CharField(max_length=15, verbose_name='Celular')),
                ('prov_direccion', models.CharField(max_length=30, verbose_name='Dirección')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('ped_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ped_fecha', models.DateTimeField(auto_now_add=True)),
                ('cliente_cli_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cliente', to='authApp.cliente')),
                ('ped_emp_cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Empleado', to='authApp.empleado')),
                ('producto_prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Producto', to='authApp.producto')),
                ('proveedor_prov_nit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Proveedor', to='authApp.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('admin_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=100, verbose_name='Contraseña')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
