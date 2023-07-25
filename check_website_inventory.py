from bs4 import BeautifulSoup
import time

class CheckWebsiteInventory:
    var = None

    def check_label_on_website(response, label_text):
        soup = BeautifulSoup(response.content, 'html.parser')
        label_element = soup.find(text=label_text)

        if label_element:
            print(f"The label '{label_text}' was found")
            return True
        else:
            print(f"The label '{label_text}' was not found")
            return False
