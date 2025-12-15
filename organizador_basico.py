#!/usr/bin/env python3
"""
ORGANIZADOR BÁSICO - Primer producto de Automatización IA
Versión: 1.0
Autor: Gonuzzz
"""
import os
import shutil
from pathlib import Path

# RUTA A ORGANIZAR (MODIFICA ESTA LÍNEA SI ES NECESARIO)
RUTA_BASE = Path.home() / "Descargas"

def main():
    print("🚀 INICIANDO ORGANIZADOR BÁSICO v1.0")
    print(f"📁 Ruta: {RUTA_BASE}")
    
    if not RUTA_BASE.exists():
        print("❌ ERROR: La ruta no existe. Creándola...")
        RUTA_BASE.mkdir(parents=True, exist_ok=True)
    
    # Categorías básicas
    categorias = {
        'IMAGENES': ['.jpg', '.png', '.gif'],
        'DOCUMENTOS': ['.pdf', '.docx', '.txt'],
        'MUSICA': ['.mp3', '.wav'],
        'VIDEOS': ['.mp4', '.avi']
    }
    
    archivos_movidos = 0
    
    for archivo in RUTA_BASE.iterdir():
        if archivo.is_file():
            extension = archivo.suffix.lower()
            
            for categoria, extensiones in categorias.items():
                if extension in extensiones:
                    destino = RUTA_BASE / categoria
                    destino.mkdir(exist_ok=True)
                    
                    try:
                        shutil.move(str(archivo), str(destino / archivo.name))
                        print(f"✓ {archivo.name[:30]:30} -> {categoria}")
                        archivos_movidos += 1
                        break
                    except Exception as e:
                        print(f"✗ Error moviendo {archivo.name}: {e}")
    
    print(f"\n✅ COMPLETADO: {archivos_movidos} archivos organizados.")
    print("💡 Consejo: Ejecuta diariamente para mantener orden automático.")

if __name__ == "__main__":
    main()
