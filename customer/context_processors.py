from account.models import Cart

def cartcount(request):
    if request.user.is_authenticated:
        ccount=Cart.objects.filter(user=request.user,status='cart').count()
        return {"count":ccount}
    else:
        return {"count":0}