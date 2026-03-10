WhatsApp Messenger
Script en Python para enviar mensajes personalizados de WhatsApp de forma automatizada usando pywhatkit y WhatsApp Web.
¿Cómo funciona?
El script lee una lista de contactos definida en el código, genera un mensaje personalizado para cada uno usando un template, y los envía automáticamente a través de WhatsApp Web abriendo el navegador en el momento indicado.
Requisitos

Python 3.x
Google Chrome o Firefox
WhatsApp Web vinculado a tu celular
Librería pywhatkit

bashpip install pywhatkit
Uso

Editá la lista CONTACTOS con los números y datos de cada persona
Personalizá el mensaje en la función crear_mensaje()
Abrí WhatsApp Web en el navegador antes de ejecutar
Corré el script:

bashpython whatsapp_masivo.py
Configuración
VariableDescripciónValor por defectoSEGUNDOS_ESPERA_WHATSAPPTiempo para cargar WhatsApp Web25 segSEGUNDOS_ENTRE_MENSAJESPausa entre cada envío30 seg
Consideraciones

Los números deben incluir el código de país (ej: +54 para Argentina)
No minimizar el navegador mientras el script está corriendo
Uso personal solamente — envíos masivos pueden resultar en bloqueo de cuenta

Resultado
Al finalizar, el script muestra un resumen con la cantidad de mensajes enviados exitosamente y los que fallaron.

Estado de prueba - no garantizado en no baneo
