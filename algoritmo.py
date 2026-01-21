def agrupar_turmas(df, meta=45, tolerancia=5):
    resultado = []

    for curso in df["Curso"].unique():
        dados = df[df["Curso"] == curso]
        dados = dados.sort_values("Alunos", ascending=False)

        turmas = []

        for _, row in dados.iterrows():
            colocado = False

            for turma in turmas:
                if turma["total"] + row["Alunos"] <= meta + tolerancia:
                    turma["ufs"].append(row["UF"])
                    turma["total"] += row["Alunos"]
                    colocado = True
                    break

            if not colocado:
                turmas.append({
                    "ufs": [row["UF"]],
                    "total": row["Alunos"]
                })

        for i, turma in enumerate(turmas, start=1):
            resultado.append({
                "Curso": curso,
                "Turma": f"Turma {i}",
                "UFs": ", ".join(turma["ufs"]),
                "Total Alunos": turma["total"]
            })

    return resultado
