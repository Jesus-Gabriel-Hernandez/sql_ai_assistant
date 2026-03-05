# =========================================
# GENERATE_IMAGES Module
# =========================================
"""
Módulo: generate_images_utils
Generación de imágenes mediante Ollama (solo cuando Windows lo soporte).

Este módulo intentaba generar imágenes usando modelos locales como llava-llama3
o Stable Diffusion XL. Actualmente, esta funcionalidad está desactivada para
evitar dependencias pesadas (torch, diffusers, etc.) y garantizar compatibilidad
total en cualquier entorno.

Cuando Ollama active la generación de imágenes en Windows, este módulo podrá
reactivarse simplemente descomentando el código original.
"""

# =========================================
# CÓDIGO ORIGINAL (DESACTIVADO)
# =========================================
"""
import os
from datetime import datetime

import torch
from diffusers import StableDiffusionXLPipeline

# Pipeline cargado en memoria (lazy loading)
_pipe_sdxl = None


def cargar_modelo():
    '''
    Carga el modelo SDXL en GPU si está disponible.
    Se ejecuta solo una vez (lazy loading).
    '''
    global _pipe_sdxl

    # Si ya está cargado, devolverlo
    if _pipe_sdxl is not None:
        return _pipe_sdxl

    # Verificar GPU
    if not torch.cuda.is_available():
        return None

    try:
        modelo = "stabilityai/stable-diffusion-xl-base-1.0"

        pipe = StableDiffusionXLPipeline.from_pretrained(
            modelo,
            torch_dtype=torch.float16
        ).to("cuda")

        _pipe_sdxl = pipe
        return _pipe_sdxl

    except Exception:
        return None
"""


# =========================================
# FUNCIÓN ACTIVA (VERSIÓN LIGERA)
# =========================================

def generate_image(prompt: str):
    """
    Placeholder de generación de imágenes.
    La funcionalidad está desactivada para evitar dependencias pesadas.

    Args:
        prompt (str): Texto descriptivo para generar la imagen.

    Returns:
        None: Indica que no se generará ninguna imagen.
    """
    return None


"""
# =========================================
# CÓDIGO ORIGINAL DE GENERACIÓN (DESACTIVADO)
# =========================================

def generate_image(prompt: str):
    '''
    Genera una imagen usando Stable Diffusion XL (SDXL).

    Returns:
        str:
            - Ruta del archivo PNG generado.
            - "SDXL_NO_AVAILABLE" si no hay GPU o SDXL no pudo cargarse.
            - "ERROR_SDXL: <detalle>" si ocurre un error inesperado.
    '''

    pipe = cargar_modelo()

    if pipe is None:
        return "SDXL_NO_AVAILABLE"

    try:
        image = pipe(
            prompt,
            num_inference_steps=20,
            guidance_scale=7.5,
            height=768,
            width=768
        ).images[0]

        # Crear carpeta si no existe
        if not os.path.exists("images"):
            os.makedirs("images")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"images/diag_{timestamp}.png"

        image.save(output_path)

        return output_path

    except Exception as error:
        return f"ERROR_SDXL: {str(error)}"
"""
