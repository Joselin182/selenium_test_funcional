from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--user-data-dir=/tmp/edge_profile")

driver = webdriver.Edge(options=options)

try:
    driver.get("https://duckduckgo.com/")
    buscador = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    buscador.send_keys("inmuebles en Bogotá")
    buscador.send_keys(Keys.RETURN)

    resultados = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@id="links"]/div[contains(@class, "result")]'))
    )

    assert len(resultados) > 0, "No se encontraron resultados"
    print(f"✅ Prueba funcional completada con éxito. Resultados encontrados: {len(resultados)}")

finally:
    driver.quit()
