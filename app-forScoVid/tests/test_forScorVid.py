import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
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

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=cap_options)

    def tearDown(self) -> None:
        if self.driver:
            try:
                self.driver.quit()
            except Exception as e:
                print(f"Error al cerrar el driver: {e}")

    def test_videoconferencia(self)-> None:
        wait = WebDriverWait(self.driver, 20)
        correE = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')))
        password = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')))
        correE.send_keys("laura.combariza.app01@zalvadora.com")
        password.send_keys("123456")
        iniciarSes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Iniciar sesión")')))
        iniciarSes.click()
        Catalogo = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("MI CATÁLOGO")')))
        busqueda = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')))
        busqueda.send_keys("scorm")
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Curso Foro y Scorm (No modificar)")')))
        curso = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Curso Foro y Scorm (No modificar)")')))
        curso.click()
        #Foro
        titulo1 = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Foro")')))
        descripcion = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Este elemento no se puede visualizar")')))
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento SCORM")')))
        btnSig1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento SCORM")')))
        btnSig1.click()
        #Scorm
        titulo2=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SCORM")')))
        descripcion2 = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Este elemento no se puede visualizar")')))
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Ordenamiento")')))
        btnSig2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Siguiente elemento Ordenamiento")')))
        btnSig2.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("menu outline")')))
        Menu=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("menu outline")')))
        Menu.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Foro")')))
        Elm1=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Foro")')))
        Elm1.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("back")')))
        volver=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("back")')))
        volver.click()   
        Catalogo2 = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("MI CATÁLOGO")')))

if __name__ == '__main__':
    unittest.main()