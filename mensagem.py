from selenium import webdriver
import time
import win32com.client as win32

#imput que recebe a mensagem
input_mensagem = input("escreva a sua mensagem: ")

class Email:
    outlook = win32.Dispatch('outlook.application')

    email = outlook.CreateItem(0)

    #email para receber a mensagem
    #titulo/assunto do email
    email.To = "email da pessoa que vai receber"
    email.Subject = "teste"
    email.HTMLbody = f"""
    <p>{input_mensagem}</p>
    """

    email.Send()
    print("email enviado")

class WhatsappBot:
    def __init__(self):
        self.mensagems = f"{input_mensagem}"
        #nome exto dos grupos ou pessoas
        self.grupos = ["Monique"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        #<span dir="auto" title="NOTAS_FELIPE" class="_ccCW FqYAR i0jNr">NOTAS_FELIPE</span>
        #<div tabindex="-1" class="p3_M1">
        #<span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(20)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(1)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(1)
            chat_box.click()
            print("opa")
            time.sleep(1)
            chat_box.send_keys(self.mensagems)

            botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            time.sleep(1)
            botao_enviar.click()
            time.sleep(3)

Email()
bot = WhatsappBot()
bot.EnviarMensagens()
