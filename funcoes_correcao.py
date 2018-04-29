def operacao():
  pt = 5 ** 2
  mt = 9 * 5
  dv = 15 / 12
  di = 12 / 15
  din = 15 // 12
  dit = 12 // 15
  res = 5%2
  re1 = 9%5
  re2 = 15%12
  re3 = 12%15
  re4 = 6%6
  re5 = 0%7
  return pt, mt, dv, di, din, dit, res, re1, re2, re3, re4, re5 

def horas():
    time = (51 + 14)%24
    print("%i horas" %time)

def hour(x, ha):
  x+=ha
  tim = x%24
  if tim<=12:
    print("%i da manha" %tim)
  else:
    tim-=12
    print("%i da tarde/noite" %tim)

def ferias(dm, ds, df):
  df+=dm
  rt = df%30
  rs = rt%7
  print("Dia do mes = %i\ndia da semana = %i" %(rt, rs))

def parenteses():
  q1 = 6 * (1 - 2)
  return q1

def juros(p, r, n, t):
  a = p*((1+((r/100)/n))**(n*t))
  print("%0.2f" %a)

def area(rc):
  ac = 3.14 * (rc**2)
  print("%0.2f" %ac)

def retangulo(ab, ah):
  at = ab * ah
  print(at)

def consumo(km, gas):
  con = km / gas
  print("%0.3f km/l" %con)

def fahrenheit(fh):
  ce = (fh-32)/1.8
  print("%0.1f celcius" %ce)

def celcius(cel):
  fhr = (cel * 1.8) + 32
  print("%0.1f fahrenheits" %fhr)
