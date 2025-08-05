from datetime import datetime,timedelta
from calendar import monthrange

hoy = datetime.today()
año_actual = hoy.year
mes_actual = hoy.month
ventas_mensuales = []
nombres_meses = []

def ultimo_dia_mes(año, mes):
        return str(monthrange(año, mes)[1])
    
meses = {
        'Enero': ('2025-01-01', f'2025-01-{ultimo_dia_mes(2025, 1)}'),
        'Febrero': ('2025-02-01', f'2025-02-{ultimo_dia_mes(2025, 2)}'),
        'Marzo': ('2025-03-01', f'2025-03-{ultimo_dia_mes(2025, 3)}'),
        'Abril': ('2025-04-01', f'2025-04-{ultimo_dia_mes(2025, 4)}'),
        'Mayo': ('2025-05-01', f'2025-05-{ultimo_dia_mes(2025, 5)}'),
        'Junio': ('2025-06-01', f'2025-06-{ultimo_dia_mes(2025, 6)}'),
        'Julio': ('2025-07-01', f'2025-07-{ultimo_dia_mes(2025, 7)}'),
        'Agosto': ('2025-08-01', f'2025-08-{ultimo_dia_mes(2025, 8)}'),
        'Septiembre': ('2025-09-01', f'2025-09-{ultimo_dia_mes(2025, 9)}'),
        'Octubre': ('2025-10-01', f'2025-10-{ultimo_dia_mes(2025, 10)}'),
        'Noviembre': ('2025-11-01', f'2025-11-{ultimo_dia_mes(2025, 11)}'),
        'Diciembre': ('2025-12-01', f'2025-12-{ultimo_dia_mes(2025, 12)}')
    }