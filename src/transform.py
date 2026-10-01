import pandas as pd


def transformar_datos(df):
    df = df.copy()

    # Eliminar espacios innecesarios
    columnas_texto = df.select_dtypes(include="object").columns

    for columna in columnas_texto:
        df[columna] = df[columna].str.strip()

    # Estandarizar categorías
    if "diagnostico" in df.columns:
        df["diagnostico"] = df["diagnostico"].str.title()

    if "departamento" in df.columns:
        df["departamento"] = df["departamento"].str.title()

    if "tipo_seguro" in df.columns:
        df["tipo_seguro"] = df["tipo_seguro"].str.upper()

    if "estado" in df.columns:
        df["estado"] = df["estado"].str.title()

    # Convertir datos numéricos
    df["edad"] = pd.to_numeric(df["edad"], errors="coerce")
    df["costo"] = pd.to_numeric(df["costo"], errors="coerce")

    # Convertir fechas
    df["fecha_ingreso"] = pd.to_datetime(
        df["fecha_ingreso"], errors="coerce"
    )

    df["fecha_alta"] = pd.to_datetime(
        df["fecha_alta"], errors="coerce"
    )

    # Completar edad faltante con la mediana
    df["edad"] = df["edad"].fillna(df["edad"].median())

    # Eliminar registros duplicados
    df = df.drop_duplicates()

    # Evitar pacientes repetidos por su ID
    df = df.drop_duplicates(
        subset=["id_paciente"],
        keep="first"
    )

    # Calcular días de estancia
    df["dias_estancia"] = (
        df["fecha_alta"] - df["fecha_ingreso"]
    ).dt.days

    return df