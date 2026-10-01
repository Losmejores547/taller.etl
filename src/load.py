from sqlalchemy import create_engine, text


def cargar_datos(df, pacientes_hospital_archivo_bd):
    engine = create_engine(f"sqlite:///{pacientes_hospital_archivo_bd}")

    # Cargar los datos en la tabla pacientes
    df.to_sql(
        "pacientes",
        engine,
        if_exists="replace",
        index=False
    )

    # Crear un índice para facilitar las búsquedas por paciente
    with engine.begin() as conexion:
        conexion.execute(
            text(
                "CREATE INDEX IF NOT EXISTS "
                "idx_pacientes_id "
                "ON pacientes (id_paciente)"
            )
        )

    print("Datos cargados correctamente en la base de datos.")