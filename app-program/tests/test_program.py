import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración de capacidades
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    app='/Users/Zalvadora/Downloads/app-debug.apk',
)

cap_options = UiAutomator2Options().load_capabilities(capabilities)

# URL del servidor Appium
appium_server_url = "http://127.0.0.1:4723/wd/hub"

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor=appium_server_url, 
            options=cap_options  
        )

    def tearDown(self) -> None:
        if self.driver:
            try:
                self.driver.quit()
            except Exception as e:
                print(f"Error al cerrar el driver: {e}")

    
    def test_programas(self)-> None:
        wait = WebDriverWait(self.driver, 20)
        correE = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')))
        password = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')))
        correE.send_keys("laura.combariza.grupos@zalvadora.com")
        password.send_keys("123456")
        iniciarSes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Iniciar sesión")')))
        iniciarSes.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SELECCIONA UNA EMPRESA")')))
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("marketing")')))
        emp1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("marketing")')))
        emp1.click()
        #Programas 
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Programas")')))
        prog = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Programas")')))
        prog.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Programa Ingles")')))
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Programa Frances")')))
        progIngles = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Programa Ingles")')))
        progIngles.click()  
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ingles 1")')))
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ingles 2")')))
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ingles 3")')))
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("back")')))
        volver = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("back")')))
        volver.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("MI CATÁLOGO")')))

    def test_sinprogramas(self)-> None:
        wait = WebDriverWait(self.driver, 20)
        correE = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')))
        password = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')))
        correE.send_keys("laura.combariza.app01@zalvadora.com")
        password.send_keys("123456")
        iniciarSes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Iniciar sesión")')))
        iniciarSes.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SELECCIONA UNA EMPRESA")')))
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("marketing")')))
        emp1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("marketing")')))
        emp1.click()
        #Programas 
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Programas")')))
        prog = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Programas")')))
        prog.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Cursos")')))
        progIngles = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Cursos")')))
        progIngles.click()  

    
    


        
if __name__ == '__main__':
    unittest.main()