while True:
    import datetime as dt

    print(dt.datetime.now())


    agora = dt.datetime.now();
    horaatual = int(agora.strftime("%H"))
    minutoatual = int(agora.strftime("%M"))
    print(horaatual)
    print(minutoatual)

    diferencahora = 21 - horaatual
    diferencaminuto = minutoatual

    print(diferencaminuto)
    print(diferencahora)

    print(f"Faltam {diferencahora} horas e {diferencaminuto} minutos para reinicialização")


