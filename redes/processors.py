from .models import LinkRed
# ctx = contexto (variables que pasar como argumento para tener acceso a ellos), ctx_dict = diccionario de contexto
def ctx_dict(request):
    ctx = {}
    links = LinkRed.objects.all()
    for l in links:
        ctx[l.key] = l.url
    return ctx