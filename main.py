from src.extract import extraer_datos
from src.transform import transformar_datos
from src.load import cargar_datos


RUTA_CSV = "datos/pacientes_hospital.csv"
RUTA_BD = "datos/hospital.db"


def main():
    print("Iniciando proceso ETL...")

    # 1. Extracción
    datos = extraer_datos(RUTA_CSV)
    print(f"Datos extraídos: {len(datos)} registros")

    # 2. Transformación y calidad
    datos_limpios = transformar_datos(datos)
    print(f"Datos después de la limpieza: {len(datos_limpios)} registros")

    # 3. Carga
    cargar_datos(datos_limpios, RUTA_BD)

    print("Proceso ETL completado correctamente.")


if __name__ == "__main__":
    main()