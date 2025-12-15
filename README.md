# 🏢 Portafolio de Automatización IA

## Scripts disponibles:

### 1. organizador_basico.py
- Versión simple sin IA
- Organiza archivos por extensión
- Rápido y básico

### 2. organizador_negocio.py (RECOMENDADO)
- **Sistema profesional con IA local**
- Usa Ollama (llama3.2:3b) para clasificación inteligente
- Estructura organizada en ~/IA_NEGOCIO/
- Genera logs y backups automáticos
- Listo para uso comercial

## Uso del organizador_negocio.py:

\`\`\`bash
# 1. Preparar estructura
mkdir -p ~/IA_NEGOCIO/tests/{entrada,salida}

# 2. Colocar archivos en entrada
cp ~/Descargas/* ~/IA_NEGOCIO/tests/entrada/

# 3. Ejecutar organizador
python3 organizador_negocio.py

# 4. Ver resultados organizados
ls ~/IA_NEGOCIO/tests/salida/
\`\`\`

## Servicios disponibles:
- Instalación y configuración: $49 USD
- Personalización para negocio: $99 USD
- Soporte mensual: $29 USD/mes

**Contacto:** [TU_EMAIL]
