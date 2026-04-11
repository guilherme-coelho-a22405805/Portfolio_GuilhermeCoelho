from django.db import models

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    link = models.URLField(blank=True)
    rating = models.IntegerField(default=0)
    descricao = models.TextField()
    aspetos_relevantes = models.TextField()
    
    # Relação N <-> N com Competências 
    competencias = models.ManyToManyField('Competencia', related_name='tecnologias', blank=True)

    def __str__(self):
        return self.nome

class Competencia(models.Model):
    TIPO_CHOICES = [
        ('soft_skill', 'Soft Skill'),
        ('tecnologia', 'Tecnologia'),
    ]
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200, default="Universidade Lusófona")
    grau = models.CharField(max_length=100, default="Licenciatura") # Ex: Licenciatura, Mestrado
    ano_inicio = models.IntegerField()
    ano_fim = models.IntegerField(blank=True, null=True) # Pode estar em aberto
    diretor = models.CharField(max_length=100)
    objetivos = models.TextField()
    descricao = models.TextField()
    logotipo = models.ImageField(upload_to='logos/', blank=True, null=True) # Logo da faculdade

    def __str__(self):
        return f"{self.grau} em {self.nome}"

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    # Relação 1 <-> N com Licenciatura
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='unidades_curriculares')
    programa = models.TextField()
    imagem = models.ImageField(upload_to='uc_images/', blank=True, null=True)
    docentes = models.TextField(help_text="Link para a página pessoal da Lusófona")
    descricao = models.TextField()

    def __str__(self):
        return self.nome



class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    # Relação 1 <-> N com Unidade Curricular
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='projetos')
    # Relações N <-> N com Tecnologias e competências 
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')
    competencias = models.ManyToManyField(Competencia, related_name='projetos')
    
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    descricao = models.TextField()
    link_github = models.URLField(blank=True)

    def __str__(self):
        return self.nome

class TFC(models.Model):
    nome = models.CharField(max_length=200)
    # Relação 1 <-> N com Licenciatura
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='tfcs')
    autor = models.CharField(max_length=100)
    orientador = models.CharField(max_length=100)
    link_pdf = models.URLField()
    descricao = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.nome



class Formacao(models.Model):
    nome = models.CharField(max_length=200)
    # Relações N <-> N
    licenciaturas = models.ManyToManyField(Licenciatura, related_name='formacoes')
    competencias = models.ManyToManyField(Competencia, related_name='formacoes')
    
    data_inicio = models.DateField()
    data_conclusao = models.DateField()
    link_certificado = models.URLField(blank=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Voluntariado(models.Model):
    nome = models.CharField(max_length=200)
    # Relação N <-> N com Competências
    competencias = models.ManyToManyField(Competencia, related_name='voluntariados')
    data = models.DateField()
    descricao = models.TextField()
    certificado = models.FileField(upload_to='certificados/', blank=True, null=True)

    def __str__(self):
        return self.nome


class MakingOf(models.Model):
    imagem = models.ImageField(upload_to='making_of/')
    decisoes = models.TextField()
    erros_correcoes = models.TextField()
    descricao = models.TextField()

    def __str__(self):
        return f"Making Of {self.id}"