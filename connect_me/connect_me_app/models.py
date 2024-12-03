from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    biografia = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    foto = models.CharField(max_length=255, blank=True, null=True)
    localizacao = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome

class Interesse(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    interesse = models.CharField(max_length=255)

    class Meta:
        unique_together = ('usuario', 'interesse')

    def __str__(self):
        return f"{self.usuario.nome} - {self.interesse}"

class Conexao(models.Model):
    usuario1 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="conexoes_envia")
    usuario2 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="conexoes_recebe")

    class Meta:
        unique_together = ('usuario1', 'usuario2')

    def __str__(self):
        return f"Conexão entre {self.usuario1.nome} e {self.usuario2.nome}"

class Grupo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class UsuarioGrupo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    papel = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ('usuario', 'grupo')

    def __str__(self):
        return f"{self.usuario.nome} - {self.grupo.nome} ({self.papel})"

class Postagem(models.Model):
    TIPOS_POSTAGEM = [
        ('Texto', 'Texto'),
        ('Imagem', 'Imagem'),
        ('Vídeo', 'Vídeo'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=10, choices=TIPOS_POSTAGEM)
    conteudo = models.TextField()

    def __str__(self):
        return f"Postagem de {self.usuario.nome} ({self.tipo})"

class Interacao(models.Model):
    TIPOS_INTERACAO = [
        ('Curtir', 'Curtir'),
        ('Comentar', 'Comentar'),
        ('Compartilhar', 'Compartilhar'),
    ]
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name="interacoes")
    tipo = models.CharField(max_length=15, choices=TIPOS_INTERACAO)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} na postagem {self.postagem.id}"

class Mensagem(models.Model):
    usuario_envia = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mensagens_enviadas")
    usuario_recebe = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mensagens_recebidas")
    conteudo = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.usuario_envia.nome} para {self.usuario_recebe.nome}"
