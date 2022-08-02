# Automação para email e WhatsApp feita completamente em python
## O que me motivou
Estava curioso em como seria possivel fazer uma automação Web então encontrei duas bibliotecas "Selenium - WebDriver" e "win32com.client - win32"

``` python
from selenium import webdriver
import time
import win32com.client as win32
```

## O programa foi dividido em duas class
1- class Email:

2- class WhatsappBot:

## Como usar?

### Email
Você deve mudar o valor que "email.To" recebe para o nome do email que você deseja enviar
```python
 email.To = "email da pessoa que vai receber"
```

Quando executar o programa, no terminal vai pereguntar qual é a mensagem que deseja enviar (essa variavel vai ser reutilizada para enviar mensagem para o Whatsapp)
```python
#imput que recebe a mensagem
input_mensagem = input("escreva a sua mensagem: ")
```

### Whatsapp
Você deve alterar a lista "self.grupos" colocando o nome exato dos contatos salvo no whatsapp

``` python
self.grupos = ["Monique"]
```
