from django import template

register = template.Library()

def locale_current(valor):
    import locale
        
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')  
    
    valor_formatado = locale.currency(valor)
    return valor_formatado


register.filter('locale_current', locale_current)