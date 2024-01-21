from django.forms.models import model_to_dict
from product.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET", "POST"])
def api_product(request, *args, **kwargs):
    """
    DRF API view.
    """
    data = {}
    products = Product.objects.all()
    data['products'] = []
    if products:
        # if request.GET.id:
        #     for product in products:
        #         if product.id == request.GET.id:
        #             item = {}
        #             item["id"] = product.id
        #             item["name"] = product.name
        #             item["price"] = str(product.price)
        #             item["category"] = product.category.name
        #             data['products'].append(item)
        #     return JsonResponse(data)

        for product in products:
            item = model_to_dict(product)
            item['category'] = product.category.name
            data['products'].append(item)
    # print(json.loads(request.GET))
    return Response(data)
