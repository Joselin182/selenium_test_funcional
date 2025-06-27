from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuramos el navegador Edge
options = Options()
# options.add_argument("--headless=new")  # Puedes activar esto para que no abra ventana

driver = webdriver.Edge(options=options)

try:
    # Abrimos DuckDuckGo
    driver.get("https://duckduckgo.com/")

    # Encontramos el campo de búsqueda por el atributo name="q"
    buscador = driver.find_element(By.NAME, "q")

    # Simulamos escribir y presionar Enter
    buscador.send_keys("inmuebles en Bogotá")
    buscador.send_keys(Keys.RETURN)

    # Esperamos 2 segundos para que carguen resultados
    time.sleep(2)

    # Buscamos elementos con la clase ".result" que son los resultados
    resultados = driver.find_elements(By.XPATH, "//a[contains(@class, 'result__a')]")


    # Validamos que haya al menos un resultado
    assert len(resultados) > 0, "No se encontraron resultados"

    print("✅ Prueba funcional completada con éxito")

finally:
    driver.quit()

