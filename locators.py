from selenium.webdriver.common.by import By

LOCATORS  = {
    "BUTTON":{
        "ENTRAR_COM_GOV": (By.CSS_SELECTOR,"#botao_gov_br > span"),
        "LOGIN_CERT_DIGITAl": (By.CSS_SELECTOR,"#cert-digital > button"),
        "LUPA":(By.CSS_SELECTOR,"#botao_busca"),
        "LOCALIZAR": (By.CSS_SELECTOR,"#btt_localizar"),
        "CAIXA_DE_ENTRADA":(By.CSS_SELECTOR,"#bt_consultar_caixas_mensagens"),
        "CLIQUE_PARA_PROSSEGUIR": (By.CSS_SELECTOR,"#btt_prosseguir"),
        "HOME":(By.CSS_SELECTOR,"#a_botao_home")
    },
    "PAINEL":{
    
    },
    "LOGO":{
      "LOGO_EFISCO":(By.ID, "efisco_logo")
    },
    "INPUT":{
      "BUSCA_EXTERNO": (By.CSS_SELECTOR,"#input_busca_geral"), 
      "BUSCA_INTERNO": (By.CSS_SELECTOR,"#input_busca_geral_interno"),
      "CNPJ_FORMULARIO": (By.CSS_SELECTOR,"#nuRadicalCNPJ")
    },
    "SELECT":{
    },
    "LINK":{
      "DOM_ELETRONICO":(By.CSS_SELECTOR,"#busca_carrossel_itens > div > ul > li > a")
    },
    "TEXTS":{
      "NAO_LIDA":(By.CSS_SELECTOR,"#table_tabeladados > tbody > tr.tabeladadosodd > td:nth-child(5)"),
      "NAO_HA_REGISTRO": (By.CSS_SELECTOR,"#table_conteiner > tbody > tr:nth-child(40) > td > div > div.quantidade_registro > span"),
      "PEDRO":(By.CSS_SELECTOR,"#a_usuario_span_texto")
    }} 