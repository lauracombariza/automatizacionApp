import unittest
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    app='/Users/Zalvadora/Downloads/app-debug.apk',
)

appium_server_url = 'http://localhost:4723/wd/hub'
cap_options=UiAutomator2Options().load_capabilities(capabilities)
# Configurar logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=cap_options)

    def tearDown(self) -> None:
        if self.driver:
            try:
                self.driver.quit()
            except Exception as e:
                print(f"Error al cerrar el driver: {e}")

    def test_login_negative(self) -> None:
        try:
            wait = WebDriverWait(self.driver, 20)
            correE = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')))
            password = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')))
            correE.send_keys("laura.combariza.app01@zalvadora.com")
            password.send_keys("123456")
            iniciarSes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Iniciar sesión")')))
            iniciarSes.click()
            logger.info("Botón 'Iniciar sesión' clickeado.")
            Catalogo = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("MI CATÁLOGO")')))
            busqueda = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')))
            busqueda.send_keys("autocal")
            autoCal = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@text="App Autocalificable (No modificar) App Autocalificable (No modificar)"]')))
            autoCal.click()
            #Ordenamiento Sin realimentacion
            titulo1 = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ordenamiento (Sin Realimentación)")')))
            btnEnv1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enviar respuesta")')))
            btnEnv1.click()
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Ordenamiento (Con realimentación)")')))
            btnSig1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Ordenamiento (Con realimentación)")')))
            btnSig1.click()
            #Ordenamiento Con realimentacion 
            titulo2=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ordenamiento (Con realimentación)")')))
            logger.info("titulo encontrado")
            btnEnv2=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enviar respuesta")')))
            btnEnv2.click()
            logger.info("rta enviada")
            realimentacion1=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Retroalimentación")')))
            logger.info("feedbck encontrado")
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento F/V (Sin realimentación)")')))
            logger.info("btn encontrado")
            btnSig2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento F/V (Sin realimentación)")')))
            btnSig2.click()  
            #F/V Sin realimentacion
            logger.info("Llego a F/V")
            titulo3=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("F/V (Sin realimentación)")')))
            Opn1=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(20)')))
            Opn1.click()
            btnEnv3=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enviar respuesta")')))
            btnEnv3.click()
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento F/V (Con realimentación)")')))
            btnSig3=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento F/V (Con realimentación)")')))
            btnSig3.click()
            #F/V Con realimentacion
            titulo4=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("F/V (Con realimentación)")')))
            Opn2=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(23)')))
            Opn2.click()
            btnEnv4=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enviar respuesta")')))
            btnEnv4.click()
            realimentacion2=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Retroalimentación")')))
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Numérica (Sin realimentación)")')))
            btnSig4=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Numérica (Sin realimentación)")')))
            btnSig4.click()  
            #Numerica Sin realimentacion
            titulo5=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Numérica (Sin realimentación)")')))
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Numérica (Sin realimentación)")')))
            btnSig5=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Numérica (Sin realimentación)")')))
            btnSig5.click()
            #Numerica Con realimentacion
            titulo6=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Numérica (Con realimentación)")')))
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Numérica (Con realimentación)")')))
            btnSig6=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Numérica (Con realimentación)")')))
            btnSig6.click()

            #Seleccion Multiple Sin realimentacion 
            titulo7=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selección múltiple Única correcta (Sin realimentación)")')))
            Opn3=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(20)')))
            Opn3.click()
            btnEnv7=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enviar respuesta")')))
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Selección múltiple única correcta (Con realimentación)")')))
            btnSig7=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Selección múltiple única correcta (Con realimentación)")')))
            btnSig7.click()
            #Seleccion Multiple Con realimentacion 
            titulo8=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selección múltiple única correcta (Con realimentación)")')))
            Opn4=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(20)')))
            Opn4.click()
            btnEnv8=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enviar respuesta")')))
            btnEnv8.click()
            realimentacion2=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Retroalimentación")')))
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Selección múltiple múltiples correctas (Con realimentación)")')))
            btnSig8=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Selección múltiple múltiples correctas (Con realimentación)")')))
            btnSig8.click()  
            #Seleccion Multiple Con realimentacion Multiples correctas
            titulo9=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selección múltiple múltiples correctas (Con realimentación)")')))
            Opn5=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(20)')))
            Opn5.click()
            btnEnv9=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enviar respuesta")')))
            btnEnv9.click()
            realimentacion3=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Retroalimentación")')))
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Selección múltiple múltiples correctas (Sin realimentación)")')))
            btnSig9=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Selección múltiple múltiples correctas (Sin realimentación)")')))
            btnSig9.click()
            #Seleccion Multiple Sin realimentacion Multiples correctas
            titulo10=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selección múltiple múltiples correctas (Sin realimentación)")')))
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("menu outline")')))
            Menu=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("menu outline")')))
            Menu.click()
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ordenamiento (Sin Realimentación)")')))
            Elm1=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ordenamiento (Sin Realimentación)")')))
            Elm1.click()
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("back")')))
            volver=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("back")')))
            volver.click()     
        except Exception as e:
            pytest.fail(f"Error en el flujo: {e}")


if __name__ == '__main__':
    unittest.main()