# Adicionando usuários de teste
from app.perguntas.models import Tema
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model


User = get_user_model()
# Creater users
# Colaborador
colaborador = User.objects.create(
    username="colaborador",
    name="Colaborador de Teste",
    email="colaborador@jogodabiblia.com.br",
    phone="71992540736",
    is_whatsapp=True,
    is_staff=False
)
colaborador.set_password("passw@rd")
colaborador.save()

# Revisor
revisor = User.objects.create(
    username="revisor",
    name="Revisor de Teste",
    email="revisor@teste.com",
    phone="71992540737",
    is_whatsapp=True,
    is_staff=True,
)
revisor.set_password('passw@rd')
revisor.save()

# Publicador
publicador = User.objects.create(
    username="publicador",
    name="Publicador de Teste",
    email="publicador@teste.com",
    phone="71992540738",
    is_whatsapp=True,
    is_staff=True
)
publicador.set_password("passw@rd")
publicador.save()

# Supervisor
supervisor = User.objects.create(
    username="supervisor",
    name="Supervisor de Teste",
    email="supervisor@teste.com",
    phone="71992540739",
    is_whatsapp=True,
    is_staff=True
)
supervisor.set_password("passw@rd")
supervisor.save()

# Administrador
administrador = User.objects.create(
    username="administrador",
    name="Administrador de Teste",
    email="administrador@teste.com",
    phone="71992540740",
    is_whatsapp=True,
    is_staff=True
)
administrador.set_password("passw@rd")
administrador.save()

# Criando os grupos
g_colaboradores, created = Group.objects.get_or_create(name='colaboradores')
g_revisores, created = Group.objects.get_or_create(name='revisores')
g_publicadores, created = Group.objects.get_or_create(name='publicadores')
g_supervisores, created = Group.objects.get_or_create(name='supervisores')
g_administradores, created = Group.objects.get_or_create(name='administradores')

# Permissions lists
perguntas_perms = [
    Permission.objects.get(codename='add_pergunta'),
    Permission.objects.get(codename='view_pergunta'),
    Permission.objects.get(codename='change_pergunta'),
    Permission.objects.get(codename='delete_pergunta'),
]

comentarios_perms = [
    Permission.objects.get(codename='add_comentario'),
    Permission.objects.get(codename='view_comentario'),
    Permission.objects.get(codename='change_comentario'),
    Permission.objects.get(codename='delete_comentario')
]

alternativas_perms = [
    Permission.objects.get(codename='add_alternativa'),
    Permission.objects.get(codename='view_alternativa'),
    Permission.objects.get(codename='change_alternativa'),
    Permission.objects.get(codename='delete_alternativa')
]

referencias_perms = [
    Permission.objects.get(codename='add_referencia'),
    Permission.objects.get(codename='view_referencia'),
    Permission.objects.get(codename='change_referencia'),
    Permission.objects.get(codename='delete_referencia')
]

all_perms = Permission.objects.all()

# Associando grupos às permissões
# Colaboradores
g_colaboradores.permissions.add(
    *comentarios_perms,
    *perguntas_perms,
    *alternativas_perms,
    *referencias_perms
)

# Revisores
g_revisores.permissions.add(
    *comentarios_perms,
    *perguntas_perms,
    *alternativas_perms,
    *referencias_perms
)

# Publicadores
g_publicadores.permissions.add(
    *comentarios_perms,
    *perguntas_perms,
    *alternativas_perms,
    *referencias_perms
)

# Supervisores
g_supervisores.permissions.add(*all_perms)

# Administradores
g_administradores.permissions.add(*all_perms)

# Associando usuários aos grupos
g_colaboradores.user_set.add(colaborador)
g_revisores.user_set.add(revisor)
g_publicadores.user_set.add(publicador)
g_supervisores.user_set.add(supervisor)
g_administradores.user_set.add(administrador)

# Criando temas/grupos de perguntas
Tema(nome="Doutrina", cor="a163e8").save()
Tema(nome="Referencia", cor="f99e00").save()
Tema(nome="Personagens do Antigo Testamento", cor="5ade3c").save()
Tema(nome="Personagens do Novo Testamento", cor="2cd0de").save()
Tema(nome="Conhecimentos Gerais", cor="de5353").save()
Tema(nome="Especial", cor="ffffff").save()
Tema(nome="Números", cor="9e8e34").save()
Tema(nome="Perguntas Ouro", cor="e7d50f").save()
