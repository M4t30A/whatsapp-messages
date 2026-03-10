"""
=======================================================
  WhatsApp Mensajes Personalizados - pywhatkit
=======================================================
REQUISITOS:
  pip install pywhatkit

CÓMO USAR:
  1. Edita la lista CONTACTOS con los números y datos
  2. Edita el TEMPLATE del mensaje
  3. Ejecuta: python whatsapp_masivo.py
  4. Mantén WhatsApp Web abierto en el navegador

NOTAS IMPORTANTES:
  - Los números deben incluir código de país (ej: +54 para Argentina)
  - WhatsApp Web debe estar vinculado a tu teléfono
  - El script abrirá el navegador automáticamente por cada mensaje
  - Deja unos segundos entre mensajes para evitar bloqueos
=======================================================
"""

import pywhatkit as kit
import time
from datetime import datetime, timedelta

# ─────────────────────────────────────────────
# 1. LISTA DE CONTACTOS
#    Agrega todos los contactos que necesites
#    Puedes añadir más campos personalizados
# ─────────────────────────────────────────────
CONTACTOS = [
    {
        "nombre": "juan nogales",
        "telefono": "+549351849298",   # Código de país + número
        "producto": "Plan Premium",
        "vencimiento": "15/03/2026",
    },
    {
        "nombre": "María García",
        "telefono": "+5491187654321",
        "producto": "Plan Básico",
        "vencimiento": "20/03/2026",
    },
    {
        "nombre": "Carlos López",
        "telefono": "+5491199887766",
        "producto": "Plan Anual",
        "vencimiento": "01/04/2026",
    },
    # ← Agrega más contactos aquí con el mismo formato
]


# ─────────────────────────────────────────────
# 2. TEMPLATE DEL MENSAJE PERSONALIZADO
#    Usa {nombre}, {producto}, {vencimiento}
#    para insertar datos de cada contacto
# ─────────────────────────────────────────────
def crear_mensaje(contacto: dict) -> str:
    mensaje = f"""Hola {contacto['nombre']} 👋

Te recordamos que tu *{contacto['producto']}* vence el {contacto['vencimiento']}.

Para renovar o consultar, respondé este mensaje.

¡Gracias por tu confianza! 🙌"""
    return mensaje


# ─────────────────────────────────────────────
# 3. CONFIGURACIÓN DE ENVÍO
# ─────────────────────────────────────────────
SEGUNDOS_ENTRE_MENSAJES = 30   # Pausa entre cada envío
SEGUNDOS_ESPERA_WHATSAPP = 25  # Tiempo para que abra WhatsApp Web


# ─────────────────────────────────────────────
# 4. ENVÍO AUTOMÁTICO (no editar)
# ─────────────────────────────────────────────
def enviar_mensajes():
    total = len(CONTACTOS)
    exitosos = []
    fallidos = []

    print("=" * 50)
    print(f"  📲 Iniciando envío de {total} mensajes")
    print("=" * 50)
    print("⚠️  Asegurate de tener WhatsApp Web abierto\n")

    for i, contacto in enumerate(CONTACTOS, start=1):
        nombre = contacto.get("nombre", "Sin nombre")
        telefono = contacto.get("telefono", "")

        print(f"[{i}/{total}] Enviando a {nombre} ({telefono})...")

        if not telefono.startswith("+"):
            print(f"  ❌ Número inválido (debe empezar con +). Saltando...\n")
            fallidos.append(nombre)
            continue

        try:
            mensaje = crear_mensaje(contacto)

            # Calcular hora de envío (ahora + 2 minutos)
            ahora = datetime.now() + timedelta(minutes=2)
            hora = ahora.hour
            minuto = ahora.minute

            kit.sendwhatmsg(
                telefono,
                mensaje,
                hora,
                minuto,
                wait_time=SEGUNDOS_ESPERA_WHATSAPP,
                tab_close=True,        # Cierra la pestaña tras enviar
                close_time=3,
            )

            print(f"  ✅ Enviado correctamente\n")
            exitosos.append(nombre)

            # Pausa entre mensajes
            if i < total:
                print(f"  ⏳ Esperando {SEGUNDOS_ENTRE_MENSAJES} segundos...\n")
                time.sleep(SEGUNDOS_ENTRE_MENSAJES)

        except Exception as e:
            print(f"  ❌ Error: {e}\n")
            fallidos.append(nombre)

    # Resumen final
    print("=" * 50)
    print("  📊 RESUMEN")
    print("=" * 50)
    print(f"  ✅ Exitosos : {len(exitosos)}")
    print(f"  ❌ Fallidos : {len(fallidos)}")
    if fallidos:
        print(f"  Fallidos   : {', '.join(fallidos)}")
    print("=" * 50)


if __name__ == "__main__":
    enviar_mensajes()
