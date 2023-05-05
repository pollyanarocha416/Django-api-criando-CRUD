from django.http import JsonResponse


def alunos(request):
    if request.method == 'GET':
        alunos = [{'id':1, 'nome':'Guilherme'},
        {'id': 2, 'nome': 'Polly'}]
        
        return JsonResponse(alunos, safe=False)