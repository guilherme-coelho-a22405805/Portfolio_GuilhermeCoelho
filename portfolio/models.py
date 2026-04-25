from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

## Classe Tecnologia -> Guarda tecnologias que sei usar -------------------------------------------------------------
class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.FileField(upload_to='tecnologias/', blank=True, null=True)
    link = models.URLField(blank=True)
    rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    descricao = models.TextField()
    aspetos_relevantes = models.TextField()
    
    ## Relações ------------------
    competencias = models.ManyToManyField('Competencia', related_name='tecnologias', blank=True)
    unidades_curriculares = models.ManyToManyField('UnidadeCurricular', related_name='tecnologias', blank=True)

    def __str__(self):
        return f"{self.nome} ({self.rating}/5)"

## Classe Competencias -> Guarda as minhas competências que considero Importantes ----------------------------------
class Competencia(models.Model):
    TIPO_CHOICES = [
        ('soft_skill', 'Soft Skill'),
        ('tecnologia', 'Tecnologia'),
        ('hard_skill', 'Hard Skill'),
    ]
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField()

    ## Não precisa de relações
    def __str__(self):
        return self.nome

## Classe Licenciatura -> Usada para guardar a minha Licenciatura em Engenharia Informática
class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200, default="Universidade Lusófona")
    grau = models.CharField(max_length=100, default="Licenciatura") 
    ano_inicio = models.IntegerField()
    ano_fim = models.IntegerField(blank=True, null=True) 
    diretor = models.CharField(max_length=100)
    objetivos = models.TextField()
    descricao = models.TextField()
    logotipo = models.FileField(upload_to='logos_licenciatura/', blank=True, null=True) 

    ## Sem Relações
    def __str__(self):
        return f"{self.grau} em {self.nome}"


## Classe Unidade Curricular -> Guarda as UCS que tive durante a Licenciatura -------------------------
class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    programa = models.TextField()
    imagem = models.FileField(upload_to='uc_images/', blank=True, null=True)
    docentes = models.TextField(help_text="Link para a página pessoal da Lusófona")
    descricao = models.TextField()

    # Relações ---------
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='unidades_curriculares')

    def __str__(self):
        return self.nome


## Class Projeto -> Usada para guardar projetos que tenha feito na universidade
class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.FileField(upload_to='projetos_img/', blank=True, null=True)
    descricao = models.TextField()
    link_github = models.URLField(blank=True)

    # Relações ----
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='projetos')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')
    competencias = models.ManyToManyField(Competencia, related_name='projetos')

    def __str__(self):
        return self.nome

## Class TFC -> Classe à parte que deve guardar TFCS de 2025
class TFC(models.Model):
    nome = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    orientador = models.CharField(max_length=100)
    link_pdf = models.URLField()
    descricao = models.TextField()
    rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    # Relação ---
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='tfcs')

    def __str__(self):
        return f"{self.nome} ({self.rating}/5)"
    

class Formacao(models.Model):
    nome = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_conclusao = models.DateField()
    link_certificado = models.URLField(blank=True)
    descricao = models.TextField()

    # Relações -----
    licenciaturas = models.ManyToManyField(Licenciatura, related_name='formacoes')
    competencias = models.ManyToManyField(Competencia, related_name='formacoes')

    def __str__(self):
        return self.nome


class Voluntariado(models.Model):
    nome = models.CharField(max_length=200)
    data_inicio = models.DateField(null=True, blank=True)
    data_conclusao = models.DateField(null=True, blank=True)
    descricao = models.TextField()
    certificado = models.FileField(upload_to='certificados/', blank=True, null=True)

    # Relações
    competencias = models.ManyToManyField(Competencia, related_name='voluntariados')

    def __str__(self):
        return self.nome






class MakingOf(models.Model):
    nome = models.CharField(max_length=200, blank=True, default="")
    imagem = models.FileField(upload_to='making_of/')
    decisoes = models.TextField()
    erros_correcoes = models.TextField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome