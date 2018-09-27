# selenium-python
Selenium Python Unittest using Python 3.4

## Why I made this code?

This code was made as an test and study purpose for DBServer, the original proposal is below:
```
Caso de teste: realizar uma compra com sucesso.
 
1. Acessar o site: www.automationpractice.com.
2. Escolha um produto qualquer na loja.
3. Adicione o produto escolhido ao carrinho.
4. Prossiga para o checkout.
5. Valide se o produto foi corretamente adicionado ao carrinho e prossiga caso esteja tudo certo.
6. Realize o cadastro do cliente preenchendo todos os campos obrigatórios dos formulários.
7. Valide se o endereço está correto e prossiga.
8. Aceite os termos de serviço e prossiga.
9. Valide o valor total da compra.
10. Selecione um método de pagamento e prossiga.
11. Confirme a compra e valide se foi finalizada com sucesso.

```
In english:
```
Test case: make a successful purchase.
 
1. Access the website: www.automationpractice.com.
2. Choose any product in the store.
3. Add the chosen product to the cart.
4. Proceed to checkout.
5. Verify that the product has been correctly added to the cart and proceed if it's all correct.
6. Perform the customer registration by filling out all the mandatory fields of the forms.
7. Verify that the address is correct and proceed.
8. Accept the terms of service and proceed.
9. Validate the total value of the purchase.
10. Select a payment method and proceed.
11. Confirm your purchase and validate if it was successfully completed.

```



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

```
1. Python 3.7 >=
2. Selenium
3. Gecko Webdriver
```

### Installing

To run the code you need to:

```
Install Python
https://www.python.org/downloads/
```

```
Install Selenium
pip install -U selenium
```

```
Download and copy to project folder the GeckoDriver available at: 
https://github.com/mozilla/geckodriver/releases
```

That's enough, just run "python main.py"

## To-do List

* Separate the Selenium code from the test code and organize the files and file names (something like buyproduct.py AND buyproduct_test.py)
* Swap time.sleep () for an implicit wait
* Review the code to remove redundances and unecessary actions


## Built With

* [VisualCode](https://code.visualstudio.com/) - Code editing. Redefined.

## Author
 
* **Allan Sklarow** - [LinkedIn](https://www.linkedin.com/in/sklarow) | [Facebook](https://www.fb.com/sklarow)

## Acknowledgments

* This code was made for study purpose and I'm trying to improve it every day, all tips and suggestions are welcome.
