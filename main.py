from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import unittest
import time
import datetime
from decimal import Decimal

var_teste =	{
  "email": "teste" +  datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "@teste.com",
  "nome": "Teste",
  "sobrenome": "Da Silva",
  "senha": "hahaha123",
  "endereco": "Rua dos testes, 1234",
  "cidade": "Teste City",
  "cep": "00000",
  "celular": "+5541999999999",
  "url": 'http://automationpractice.com/'
}

# Creating a class as a pattern in unittest
class TestAuto(unittest.TestCase):
    #special methods
    def setUp(self): #setup initializate geckoWebdriver with Firefox
        self.browser = webdriver.Firefox()
    def teststart(self):
        #01. Acessar o site: www.automationpractice.com.
        self.browser.get(var_teste['url'])

        #02. Escolha um produto qualquer na loja.
        self.browser.find_element_by_css_selector('img.replace-2x.img-responsive').click()

        #03. Adicione o produto escolhido ao carrinho.
        self.browser.find_element_by_css_selector('button[name="Submit"] > span').click()

        #04. Prossiga para o checkout.
        time.sleep(3)
        self.browser.find_element_by_xpath('//div[@id=\'layer_cart\']/div/div[2]/div[4]/a/span').click()

        #05. Valide se o produto foi corretamente adicionado ao carrinho e prossiga caso esteja tudo certo.
        self.assertEqual(self.browser.find_element_by_id('summary_products_quantity').text, "1 Product")
        self.browser.find_element_by_xpath('//div[@id=\'center_column\']/p[2]/a/span').click()

        #06. Realize o cadastro do cliente preenchendo todos os campos obrigatórios dos formulários.
        self.browser.find_element_by_id('email_create').send_keys(var_teste['email'])
        self.browser.find_element_by_xpath('//button[@id=\'SubmitCreate\']/span').click()

        time.sleep(3)

        self.browser.find_element_by_id('customer_firstname').send_keys(var_teste['nome'])
        self.browser.find_element_by_id('customer_lastname').send_keys(var_teste['sobrenome'])
        self.browser.find_element_by_id('passwd').send_keys(var_teste['senha'])
        self.browser.find_element_by_id('address1').send_keys(var_teste['endereco'])
        self.browser.find_element_by_id('city').send_keys(var_teste['cidade'])

        s1 = Select(self.browser.find_element_by_id('id_state'))
        s1.select_by_visible_text('New York')

        self.browser.find_element_by_id('postcode').send_keys(var_teste['cep'])
        self.browser.find_element_by_id('phone_mobile').send_keys(var_teste['celular'])

        self.browser.find_element_by_xpath('//button[@id=\'submitAccount\']/span').click()

        #07. Valide se o endereço está correto e prossiga.
        self.assertEqual(self.browser.find_element_by_xpath('//ul[@id=\'address_delivery\']/li[3]').text, var_teste['endereco'])        
        self.browser.find_element_by_xpath('//div[@id=\'center_column\']/form/p/button/span').click()

        #08. Aceite os termos de serviço e prossiga.
        time.sleep(3)
        self.browser.find_element_by_xpath('//input[@id=\'cgv\']').click()
        self.browser.find_element_by_xpath('//form[@id=\'form\']/p/button/span').click()

        #09. Valide o valor total da compra.
        time.sleep(3)
        valorcompra = self.browser.find_element_by_id('total_price').text
        valorcompra_dec = Decimal(valorcompra.replace('$', ''))
        self.assertGreater(valorcompra_dec, 0)
                    
        #10. Selecione um método de pagamento e prossiga.
        self.browser.find_element_by_xpath('//div[@id=\'HOOK_PAYMENT\']/div/div/p/a').click()

        #11. Confirme a compra e valide se foi finalizada com sucesso.
        self.browser.find_element_by_xpath('//p[@id=\'cart_navigation\']/button/span').click()

        time.sleep(3)
        self.assertEquals(self.browser.find_element_by_class_name('cheque-indent').text, 'Your order on My Store is complete.')
        
    def tearDown(self):# quit browser
        self.browser.quit()
if __name__ == '__main__':
    unittest.main(warnings='ignore')