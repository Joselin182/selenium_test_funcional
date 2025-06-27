from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--user-data-dir=/tmp/edge_profile")  # Evita conflicto de perfil en CI

driver = webdriver.Edge(options=options)

try:
    driver.get("https://duckduckgo.com/")
    buscador = driver.find_element(By.NAME, "q")
    buscador.send_keys("inmuebles en Bogotá")
    buscador.send_keys(Keys.RETURN)
    time.sleep(2)
    resultados = driver.find_elements(By.XPATH, '//div[@id="links"]/div[contains(@class, "result")]')
    assert len(resultados) > 0, "No se encontraron resultados"
    print(f"✅ Prueba funcional completada con éxito. Resultados encontrados: {len(resultados)}")

finally:
    driver.quit()

