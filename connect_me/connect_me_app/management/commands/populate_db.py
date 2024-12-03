from django.core.management.base import BaseCommand
from connect_me_app.models import Usuario, Interesse, Conexao, Grupo, UsuarioGrupo, Postagem, Interacao, Mensagem
import random
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Popula o banco de dados com dados fictícios'

    def handle(self, *args, **kwargs):
        # Adicionando usuários
        nomes = [
            "João Silva", "Maria Oliveira", "Carlos Pereira", "Ana Santos", "Paulo Costa",
            "Fernanda Souza", "Lucas Almeida", "Juliana Mendes", "Ricardo Bastos", "Mariana Farias",
            "Gabriel Rodrigues", "Amanda Lima", "Rafael Martins", "Laura Azevedo", "Pedro Cunha",
            "Isabela Barbosa", "Thiago Castro", "Luiza Ramos", "Felipe Nogueira", "Camila Lopes",
            "Victor Monteiro", "Larissa Teixeira", "Bruno Melo", "Alice Vieira", "Mateus Moraes",
        ]

        usuarios = []
        for nome in nomes:
            usuario_data = {
                "nome": nome,
                "biografia": f"Biografia de {nome}.",
                "data_nascimento": f"{random.randint(1980, 2005)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}",
                "foto": f"foto_{nome.lower().replace(' ', '_')}.jpg",
                "localizacao": f"{random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba'])}, Brasil"
            }
            usuario = Usuario.objects.create(**usuario_data)
            usuarios.append(usuario)

        # Adicionando interesses
        topicos = ["Tecnologia", "Literatura", "Viagens", "Fotografia", "Poesia", "Música", "Cinema", "Esportes", "Gastronomia"]
        for usuario in usuarios:
            interesses_usuario = random.sample(topicos, k=random.randint(1, 3))
            for interesse in interesses_usuario:
                Interesse.objects.create(usuario=usuario, interesse=interesse)

        # Adicionando conexões
        for _ in range(30):
            usuario1, usuario2 = random.sample(usuarios, 2)
            Conexao.objects.get_or_create(usuario1=usuario1, usuario2=usuario2)

        # Adicionando grupos
        grupos = [
            {"nome": "Desenvolvedores", "descricao": "Grupo para discutir sobre tecnologia, programação e IA."},
            {"nome": "Leitores de Poesia", "descricao": "Grupo para os apaixonados por literatura e poesia."},
            {"nome": "Aventureiros", "descricao": "Exploradores do mundo e amantes de aventuras."},
        ]
        for grupo_data in grupos:
            Grupo.objects.create(**grupo_data)

        # Adicionando membros aos grupos
        for usuario in usuarios:
            grupo = random.choice(Grupo.objects.all())
            UsuarioGrupo.objects.create(usuario=usuario, grupo=grupo, papel=random.choice(["Membro", "Administrador"]))

        # Adicionando postagens
        for usuario in usuarios[:15]:  # Apenas alguns usuários farão postagens
            for _ in range(random.randint(1, 3)):
                Postagem.objects.create(
                    usuario=usuario,
                    data_hora=datetime.now() - timedelta(days=random.randint(0, 7)),
                    tipo=random.choice(["Texto", "Imagem", "Vídeo"]),
                    conteudo=f"Conteúdo da postagem de {usuario.nome}.",
                )

        # Adicionando interações
        for _ in range(50):  # Mais interações para enriquecer o banco
            postagem = random.choice(Postagem.objects.all())
            Interacao.objects.create(
                postagem=postagem,
                tipo=random.choice(["Curtir", "Comentar", "Compartilhar"]),
                data_hora=datetime.now() - timedelta(days=random.randint(0, 7), hours=random.randint(0, 23)),
            )

        # Adicionando mensagens
        for _ in range(40):  # Mensagens entre usuários
            usuario_envia, usuario_recebe = random.sample(usuarios, 2)
            Mensagem.objects.create(
                usuario_envia=usuario_envia,
                usuario_recebe=usuario_recebe,
                conteudo=f"Mensagem de {usuario_envia.nome} para {usuario_recebe.nome}.",
                data_hora=datetime.now() - timedelta(days=random.randint(0, 7), hours=random.randint(0, 23)),
            )

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
