import requests

def custom_context(request):
    context = {}

    if 'cliente_id' in request.session:
        cliente_id = request.session['cliente_id']
        response = requests.get(f'https://apismsemail-production.up.railway.app/list_users', params={'id': cliente_id})
        print(cliente_id)
        if response.status_code == 200:
            context['is_authenticated'] = True
            print("funciona el autentificador")
            data = response.json()
            context['cliente'] = data
            print(context['cliente'])
            print(data)
        else:
            context['is_authenticated'] = False
            context['cliente'] = None
    else:
        context['is_authenticated'] = False
        context['cliente'] = None

    return context