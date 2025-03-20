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

    def test_cursos_inscritos(self) -> None:
        wait = WebDriverWait(self.driver, 10)
        logoInicio = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.webkit.WebView")')))
        logoInicio.click()
        correE = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')))
        password = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')))
        correE.send_keys("laura.combariza.app01@zalvadora.com")
        password.send_keys("123456")
        iniciarSes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Iniciar sesión")')))
        iniciarSes.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Curso Foro - 10940 Curso Foro - 10940")')))
        cursoForo=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Curso Foro - 10940 Curso Foro - 10940")')))
        cursoForo.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("back")')))
        volver=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("back")')))
        volver.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("App Autocalificable (No modificar) App Autocalificable (No modificar)")')))
        cursoAut=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("App Autocalificable (No modificar) App Autocalificable (No modificar)")')))
        cursoAut.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("back")')))
        volver=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("back")')))
        volver.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Probar todo en la app 2.0 -10218 Probar todo en la app 2.0 -10218")')))
        cursoTodo=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Probar todo en la app 2.0 -10218 Probar todo en la app 2.0 -10218")')))
        cursoTodo.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("back")')))
        volver.click()


    def test_usuario_sin_cursos(self)-> None:
        wait = WebDriverWait(self.driver, 10)
        logoInicio = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.webkit.WebView")')))
        logoInicio.click()
        correE = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')))
        password = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')))
        correE.send_keys("laura.combariza.admin1@zalvadora.com")
        password.send_keys("123456")
        iniciarSes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Iniciar sesión")')))
        iniciarSes.click()
        mensaje=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("No tienes cursos inscritos")')))

    def test_busqueda_Cursos(self)-> None:
        wait = WebDriverWait(self.driver, 10)
        logoInicio = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.webkit.WebView")')))
        logoInicio.click()
        correE = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')))
        password = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')))
        correE.send_keys("laura.combariza@zalvadora.com")
        password.send_keys("123456")
        iniciarSes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Iniciar sesión")')))
        iniciarSes.click()
        Catalogo = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SELECCIONA UNA EMPRESA")')))
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("marketing")')))
        Empresa1=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("marketing")')))
        Empresa1.click()
        busqueda = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')))
        busqueda.send_keys("autocal")
        autoCal = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@text="App Autocalificable (No modificar) App Autocalificable (No modificar)"]')))
        autoCal.click()

        

if __name__ == '__main__':
    unittest.main()