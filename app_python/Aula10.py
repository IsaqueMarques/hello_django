from datetime import date, time, datetime, timedelta

def trabalhando_com_datatime():
    data_atual = datetime.now()
    #data atual
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    #DIA DA SEMANA EM NUMERO
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta','Quinta','Sexta','Sabado','Domingo')
    print(tupla[data_atual.weekday()])
    #DIA DA SEMANA EM NOME
    data_criada = datetime(2022, 6, 20, 15, 30, 20)
    #DATA CRIADA
    print(data_criada)
    #DATA CRIADA COM STRING
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minuts=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datatime()

