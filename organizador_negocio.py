#!/usr/bin/env python3
"""
ORGANIZADOR DE NEGOCIO IA - VERSIÓN UNIFICADA
Versión: 3.1
Autor: Gonuzzz
Estructura: Todo en ~/IA_NEGOCIO/
"""
import os
import shutil
import subprocess
import json
from pathlib import Path
from datetime import datetime
import hashlib

# =============== ESTRUCTURA UNIFICADA ===============
BASE_DIR = Path.home() / "IA_NEGOCIO"
SCRIPTS_DIR = BASE_DIR / "scripts"
CLIENTES_DIR = BASE_DIR / "clientes"
RECURSOS_DIR = BASE_DIR / "recursos"
LOGS_DIR = BASE_DIR / "logs"
BACKUPS_DIR = BASE_DIR / "backups"
TESTS_DIR = BASE_DIR / "tests"

# Subcarpetas para organización
ENTRADA_DIR = TESTS_DIR / "entrada"      # Archivos a organizar
SALIDA_DIR = TESTS_DIR / "salida"        # Archivos organizados

# Modelo de IA
MODELO_IA = "llama3.2:3b"

# Categorías de negocio (personalizables)
CATEGORIAS = {
    'DOCUMENTOS': ['.pdf', '.docx', '.xlsx', '.odt', '.txt'],
    'IMAGENES': ['.jpg', '.png', '.webp', '.gif'],
    'MEDIA': ['.mp4', '.mp3', '.avi'],
    'CODIGO': ['.py', '.js', '.html', '.sh'],
    'DATOS': ['.csv', '.json', '.sql'],
    'COMPRIMIDOS': ['.zip', '.rar', '.7z'],
    'SISTEMAS': ['.iso', '.deb', '.exe'],
    'OTROS': []
}

def crear_estructura_negocio():
    """Crea toda la estructura de negocio"""
    carpetas = [
        BASE_DIR, SCRIPTS_DIR, CLIENTES_DIR, RECURSOS_DIR,
        LOGS_DIR, BACKUPS_DIR, TESTS_DIR, ENTRADA_DIR, SALIDA_DIR
    ]
    
    for carpeta in carpetas:
        carpeta.mkdir(exist_ok=True)
    
    print("✅ Estructura de negocio creada en ~/IA_NEGOCIO/")

def organizar_negocio():
    """Organiza archivos dentro de la estructura de negocio"""
    print("=" * 60)
    print("🏢 ORGANIZADOR DE NEGOCIO IA v3.1")
    print(f"📍 Todo en: {BASE_DIR}")
    print("=" * 60)
    
    # Crear estructura si no existe
    crear_estructura_negocio()
    
    # Verificar archivos en ENTRADA
    archivos = list(ENTRADA_DIR.iterdir())
    if not archivos:
        print(f"\n📭 Coloca archivos en: {ENTRADA_DIR}")
        print("   Ejemplo: cp ~/Descargas/* ~/IA_NEGOCIO/tests/entrada/")
        return
    
    print(f"\n📦 Procesando {len(archivos)} archivos...")
    
    resultados = []
    for archivo in archivos:
        if archivo.is_file():
            print(f"\n📄 {archivo.name}")
            
            # Determinar categoría
            extension = archivo.suffix.lower()
            categoria = "OTROS"
            metodo = "EXTENSION"
            
            # Buscar por extensión
            for cat, exts in CATEGORIAS.items():
                if extension in exts:
                    categoria = cat
                    break
            
            # Si no encontró, consultar IA
            if categoria == "OTROS":
                categoria, metodo = consultar_ia(archivo.name, extension)
            
            # Crear carpeta de destino
            destino = SALIDA_DIR / categoria
            destino.mkdir(exist_ok=True)
            
            # Mover con nombre único
            nombre_final = archivo.name
            contador = 1
            while (destino / nombre_final).exists():
                nombre_base = archivo.stem
                nombre_final = f"{nombre_base}_{contador}{archivo.suffix}"
                contador += 1
            
            shutil.move(str(archivo), str(destino / nombre_final))
            
            resultados.append({
                "archivo": archivo.name,
                "categoria": categoria,
                "metodo": metodo,
                "destino": str(destino / nombre_final)
            })
            
            print(f"   → {categoria} ({metodo})")
    
    # Guardar log
    if resultados:
        log_file = LOGS_DIR / f"organizacion_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump({
                "fecha": datetime.now().isoformat(),
                "total": len(resultados),
                "resultados": resultados
            }, f, indent=2)
        
        # Mostrar resumen
        print("\n" + "=" * 60)
        print("📊 RESUMEN DE ORGANIZACIÓN")
        print("=" * 60)
        
        categorias_count = {}
        for r in resultados:
            cat = r['categoria']
            categorias_count[cat] = categorias_count.get(cat, 0) + 1
        
        for cat, count in categorias_count.items():
            print(f"   {cat}: {count} archivos")
        
        print(f"\n✅ Completado: {len(resultados)} archivos organizados")
        print(f"📁 Salida: {SALIDA_DIR}")
        print(f"📝 Log: {log_file}")

def consultar_ia(nombre_archivo, extension):
    """Consulta a la IA para clasificación"""
    prompt = f"""Clasifica este archivo: {nombre_archivo} (Extensión: {extension})
    
Opciones:
1. DOCUMENTOS  2. IMAGENES  3. MEDIA  4. CODIGO  
5. DATOS       6. COMPRIMIDOS  7. SISTEMAS  8. OTROS

Responde solo con el número (1-8):"""
    
    try:
        resultado = subprocess.run(
            ["ollama", "run", MODELO_IA, prompt],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        for linea in resultado.stdout.split('\n'):
            if linea.strip().isdigit():
                num = int(linea.strip())
                if 1 <= num <= 8:
                    categorias = list(CATEGORIAS.keys())
                    return categorias[num-1], "IA"
    
    except:
        pass
    
    return "OTROS", "IA_NO_DISPONIBLE"

if __name__ == "__main__":
    # Verificar Ollama
    try:
        subprocess.run(["ollama", "--version"], capture_output=True)
        organizar_negocio()
    except:
        print("❌ Ollama no disponible. Usando clasificación básica.")
        # Podemos ejecutar igual sin IA
        organizar_negocio()
