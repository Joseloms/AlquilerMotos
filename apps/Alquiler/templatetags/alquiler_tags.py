from django import template
from decimal import Decimal
register = template.Library()

@register.filter(name = 'get_price_by_time')
def get_price_by_time(precio, tiempo):
    try:
        minutos = Decimal(tiempo)
    except:
        minutos = Decimal(60)
    porcentaje = ((minutos * Decimal(100)) / Decimal(60))/Decimal(100)
    precio_calculado = precio * porcentaje
    return "%0.2f"%(round(precio_calculado, 2))
