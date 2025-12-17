#!/usr/bin/env python3
"""
Generador de Facturas - Gonúcleo Automatización
"""
import datetime
import json
import os

def generar_factura(cliente, servicio, monto, numero_factura):
    fecha = datetime.datetime.now().strftime("%d/%m/%Y")
    
    factura = f"""
    FACTURA #{numero_factura}
    GONÚCLEO AUTOMATIZACIÓN
    Patricio Castillo Hidalgo
    RUT: 14174467-4
    Dirección: Santiago, Chile
    Email: contacto@gonucleo.cl
    Teléfono: +56 9 6264 6145
    
    -------------------------------
    
    CLIENTE: {cliente}
    FECHA: {fecha}
    
    SERVICIO: {servicio}
    MONTO: ${monto:,} CLP
    
    -------------------------------
    
    FIRMA: _______________________
    (Cliente)
    
    FIRMA: _______________________
    (Gonúcleo Automatización)
    """
    
    # Guardar factura
    nombre_archivo = f"factura_{numero_factura}_{cliente.replace(' ', '_')}.txt"
    with open(nombre_archivo, 'w') as f:
        f.write(factura)
    
    # Actualizar contador
    with open('contador_facturas.json', 'w') as f:
        json.dump({'ultima_factura': numero_factura}, f)
    
    return nombre_archivo

if __name__ == "__main__":
    # Ejemplo de uso
    factura = generar_factura(
        cliente="Juan Pérez",
        servicio="Instalación Sistema Básico",
        monto=35000,
        numero_factura=1
    )
    print(f"Factura generada: {factura}")
