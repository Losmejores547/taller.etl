import pandas as pd


def extraer_datos(pacientes_hospital_archivo):
    datos = pd.read_csv(
        pacientes_hospital_archivo,
        delimiter=",",
        encoding="utf-8-sig",
        low_memory=False
    )

    return datos