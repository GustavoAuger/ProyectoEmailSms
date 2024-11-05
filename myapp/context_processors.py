import requests

def custom_context(request):
    context = {}

    if 'cliente_id' in request.session:
        cliente_id = request.session['cliente_id']
        response = requests.get(f'http://localhost:5000/get_cliente_data', params={'cliente_id': cliente_id})
        
        if response.status_code == 200:
            context['is_authenticated'] = True
            print("funciona el autentificador")
            context['cliente'] = response.json()
        else:
            context['is_authenticated'] = False
            context['cliente'] = None
    else:
        context['is_authenticated'] = False
        context['cliente'] = None

    return context