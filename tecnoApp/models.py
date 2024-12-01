from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=10)  # Formato: 00000-000
    numero = models.CharField(max_length=10)  # Exemplo: "123A"
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)  # Exemplo: "SP"

    def __str__(self):
        return f"{self.numero}, {self.cep}, {self.cidade}-{self.estado}"

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    nome = models.CharField(max_length=255)
    tipo = models.CharField(
        max_length=2,
        choices=TIPO_USUARIO_CHOICES,
        default='PF',
    )
    cpf = models.CharField(
        max_length=14,  # Formato: 000.000.000-00
        blank=True,
        null=True,
        unique=True,
    )
    cnpj = models.CharField(
        max_length=18,  # Formato: 00.000.000/0000-00
        blank=True,
        null=True,
        unique=True,
    )
    endereco = models.OneToOneField(
        Endereco,
        on_delete=models.CASCADE,
        related_name="usuario"
    )

    def save(self, *args, **kwargs):
        # Validações de consistência de tipo e documentos
        if self.tipo == 'PF' and not self.cpf:
            raise ValueError("Usuários do tipo PF devem ter um CPF.")
        if self.tipo == 'PJ' and not self.cnpj:
            raise ValueError("Usuários do tipo PJ devem ter um CNPJ.")
        if self.tipo == 'PF' and self.cnpj:
            raise ValueError("Usuários do tipo PF não devem ter um CNPJ.")
        if self.tipo == 'PJ' and self.cpf:
            raise ValueError("Usuários do tipo PJ não devem ter um CPF.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} ({'PF' if self.tipo == 'PF' else 'PJ'})"
