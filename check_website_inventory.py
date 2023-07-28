from bs4 import BeautifulSoup
import time

class CheckWebsiteInventory:
    var = None

    def check_label_on_website(response, label_text):
        soup = BeautifulSoup(response.content, 'html.parser')
        label_element = soup.find(text=label_text)
        # print(soup.prettify())

        if label_element:
            print(f"The label '{label_text}' was found")
            return True
        else:
            print(f"The label '{label_text}' was not found")
            return False

    @classmethod
    def check_product_availability_on_website(cls, response, product_name):
        soup = BeautifulSoup(response.content, 'html.parser')
        div_elements = soup.find_all("div", class_="product-details")

        # Search product details div tag for the product name
        for div_element in div_elements:
            if div_element.find("a", string=product_name):
                product_availability = div_element.find("div", class_="product-availability").text
                break

        return product_availability
