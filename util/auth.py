def is_data_authorized(request, user):
    if(request.user != user):
        messages.add_message(request, constants.ERROR, 'Você não tem autorização com acesso aos dados')
        return True
    else:
        return False