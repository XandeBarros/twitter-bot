import datetime

def get_date():
  dt = datetime.datetime.today()
  
  day = dt.day
  month = dt.month
  year = dt.year

  monthArray= ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

  result = f"Hoje é {day} de {monthArray[month-1]} de {year}."

  return result
