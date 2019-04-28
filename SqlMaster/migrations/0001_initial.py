# Generated by Django 2.2 on 2019-04-27 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='域名')),
                ('city', models.CharField(max_length=10, verbose_name='城市')),
                ('province', models.CharField(max_length=10, null=True, verbose_name='省份')),
                ('country', models.CharField(default='中国', max_length=10, null=True, verbose_name='国家')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='系统名称')),
                ('platform', models.CharField(default='Others', max_length=8, verbose_name='系统平台')),
                ('protocol', models.CharField(default='CoAP', max_length=4, verbose_name='接入协议')),
                ('devicecode', models.CharField(max_length=20, null=True, verbose_name='设备注册码')),
                ('type', models.CharField(max_length=300, verbose_name='数据模板')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=15, verbose_name='用户名')),
                ('password', models.CharField(max_length=40, verbose_name='密码')),
                ('name', models.CharField(max_length=12, verbose_name='昵称')),
                ('phone', models.CharField(max_length=14, unique=True, verbose_name='手机号')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('age', models.PositiveSmallIntegerField(null=True, verbose_name='年龄')),
                ('sex', models.NullBooleanField(verbose_name='性别')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='SqlMaster.Domain', verbose_name='所属域')),
                ('rely', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_user', to='SqlMaster.Users', verbose_name='上级用户')),
                ('system', models.ManyToManyField(related_name='admin', to='SqlMaster.System', verbose_name='子系统')),
            ],
        ),
        migrations.AddField(
            model_name='system',
            name='createuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ownsystem', to='SqlMaster.Users', verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='system',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='system', to='SqlMaster.Domain', verbose_name='所属域'),
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveSmallIntegerField(verbose_name='操作码')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operation', to='SqlMaster.Users', verbose_name='操作用户')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.GenericIPAddressField(verbose_name='IP')),
                ('operation', models.CharField(default='IN', max_length=3, verbose_name='操作')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='login', to='SqlMaster.Users', verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='设备名')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('IMEI', models.CharField(max_length=15, verbose_name='序列号')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device', to='SqlMaster.System', verbose_name='所属系统')),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=600, verbose_name='设备数据')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='接收时间')),
                ('model', models.BooleanField(db_index=True, default=0, verbose_name='订阅/推送')),
                ('waring', models.NullBooleanField(db_index=True, default=None, verbose_name='正常/异常')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='SqlMaster.Device', verbose_name='所属设备')),
            ],
        ),
    ]