from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import platform
import time

class Scraping():
    def __init__(self):
        self.list_causas = []
        
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")

        self.browser = uc.Chrome(executable_path="/usr/local/bin", options=chrome_options)
        self.url = "https://procesosjudiciales.funcionjudicial.gob.ec"

    def getPage(self):
        self.list_causas = []
        self.browser.get(f'{self.url}/busqueda-filtros')
        self.browser.implicitly_wait(10)

    def __getPaginator(self):
        try:
            paginator = self.browser.find_element(By.CSS_SELECTOR,"div.mat-mdc-paginator-range-label").text
            self.pages = int(paginator.split(" ")[len(paginator.split(" ")) -1])
        except:
            self.pages = 1

    def __getDataTable(self, nro_actor):
        page = 1

        while page <= self.pages:
            print(f"pages {page} / {self.pages}")
            table = self.browser.find_elements(By.CSS_SELECTOR, "div.causa-individual")
            
            for child_div in table:
                id = child_div.find_element(By.CSS_SELECTOR, "div.id").text
                fecha = child_div.find_element(By.CSS_SELECTOR, "div.fecha").text
                nro_proceso = child_div.find_element(By.CSS_SELECTOR, "div.numero-proceso").text
                infraccion = child_div.find_element(By.CSS_SELECTOR, "div.accion-infraccion").text
                detail = child_div.find_element(By.TAG_NAME, "a")

                actions = ActionChains(self.browser)
                if platform.system() == "Darwin":  # Mac
                    actions.key_down(Keys.COMMAND)
                else:  # Windows
                    actions.key_down(Keys.CONTROL)

                actions.click(detail)
                actions.perform()

                self.browser.switch_to.window(self.browser.window_handles[-1])
                
                detail = self.__getDetailProcess()

                self.browser.close()
                self.browser.switch_to.window(self.browser.window_handles[0])

                causa = {
                    "id": id,
                    "fecha": fecha,
                    "nro_proceso": nro_proceso,
                    "infraccion": infraccion,
                    "nro_actor": nro_actor,
                    "detail": detail
                }

                print(f'id: {id} proceso: {nro_proceso}')

                self.list_causas.append(causa)
            

            if page != self.pages:
                self.browser.find_element(By.CSS_SELECTOR,"button.mat-mdc-paginator-navigation-next").click()
            
            time.sleep(1)
            page = page + 1

    def __getDetailProcess(self):
        detail_process = []
        detail = {}
        table_detail = self.browser.find_elements(By.CSS_SELECTOR, "div.movimiento-individual.ng-star-inserted")

        for child_div in table_detail:
            element_detail = child_div.find_element(By.TAG_NAME, "a")
            actions = ActionChains(self.browser)

            if platform.system() == "Darwin":  # Mac
                actions.key_down(Keys.COMMAND)
            else:  # Windows
                actions.key_down(Keys.CONTROL)

            actions.click(element_detail)
            actions.perform()        

            self.browser.switch_to.window(self.browser.window_handles[-1])
            time.sleep(1)

            try:
                section_buttons = self.browser.find_element(By.CSS_SELECTOR, "div.panel-expansion-action-buttons")
                button = section_buttons.find_element(By.TAG_NAME, "button")
                if button.is_enabled():
                    button.click()
            except:
                self.browser.refresh()
                time.sleep(2)
                section_buttons = self.browser.find_element(By.CSS_SELECTOR, "div.panel-expansion-action-buttons")
                button = section_buttons.find_element(By.TAG_NAME, "button")
                if button.is_enabled():
                    button.click()

            section_header = self.browser.find_element(By.CSS_SELECTOR, "section.header-movimiento.ng-star-inserted")
            keys = section_header.find_elements(By.TAG_NAME, "strong")
            values = section_header.find_elements(By.TAG_NAME, "span")

            if len(keys) == len(values):
                detail = {f"{keys[i].text}": f"{values[i].text}" for i in range(len(keys))}
                
            list_actuaciones = self.browser.find_elements(By.CSS_SELECTOR, "mat-expansion-panel.mat-expansion-panel")
            actuaciones = []
            for child_actuacion in list_actuaciones:
                section_header_table = child_actuacion.find_element(By.CSS_SELECTOR, "div.cabecera-tabla")
                headers = section_header_table.find_elements(By.TAG_NAME, "span")
                
                fecha_ingreso = headers[0].text
                summary = headers[1].text
                time.sleep(1)

                section_article = child_actuacion.find_element(By.CSS_SELECTOR, "article.actividad")
                documents = section_article.find_elements(By.TAG_NAME, "p")
                description = ''
                for child_docum in documents:
                    description += child_docum.text

                actuaciones.append({
                    "fecha_ingreso": fecha_ingreso,
                    "summary": summary,
                    "description": description
                })

            detail["actuaciones"] = actuaciones

            self.browser.close()
            self.browser.switch_to.window(self.browser.window_handles[-1])

            detail_process.append(detail)

        return detail_process
            

    def serachCausas(self, nro_actor):
        try:
            actor = self.browser.find_element(By.XPATH, "//input[@id='mat-input-1']")
            actor.clear()
            actor.send_keys(nro_actor)

            self.browser.find_element(By.CSS_SELECTOR,"button.boton-buscar").click()
        except:
            self.browser.refresh()
            actor = self.browser.find_element(By.XPATH, "//input[@id='mat-input-1']")
            actor.clear()
            actor.send_keys(nro_actor)

            self.browser.find_element(By.CSS_SELECTOR,"button.boton-buscar").click()

        time.sleep(1)
        print("Strarting Scraping >>>")

        self.__getPaginator()
        self.__getDataTable(nro_actor)

        return self.list_causas


