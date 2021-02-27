from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Sum
# Create your views here.
from app.models import Location, Product, ProductMovement
from django.contrib.auth.decorators import login_required

@login_required
def dashoard(request):
    return render(request,"base.html")
@login_required
def location(request):
    record = Location.objects.all()
    return render(request, 'location.html', {"record": record})
@login_required
def savelacation(request):
    if request.method == "POST":
        check_id = request.POST.get('check')
        location = request.POST.get('location')
        location_id = request.POST.get('location_id')
        if check_id:
            Location(location=location, location_id=location_id, ).save()
            data = {"status": 1}
            return JsonResponse(data)
        else:
            check = Location.objects.filter(location_id=location_id)
            if check:
                data = {"status": 0}
                return JsonResponse(data)
            else:
                Location(location=location,location_id=location_id,).save()
                data = { "status": 1}
                return JsonResponse(data)

@login_required
def editlacation(request):
    id = request.GET.get("id")
    update = Location.objects.get(location_id=id)
    record = Location.objects.all()
    key = {"check":"ok"}
    return render(request, 'location.html', {"record": record,"update":update,"key":key})

@login_required
def deletelacation(request):
    id = request.GET.get("id")
    Location.objects.get(location_id=id).delete()
    return location(request)

@login_required
def products(request):
    loc_list = Location.objects.all()
    data = Product.objects.all()
    return render(request,"product.html",{"loc":loc_list,"record":data})
@login_required
def saveproduct(request):
    if request.method =="POST":
        check_id = request.POST.get('check')
        name = request.POST.get("name")
        product_id = request.POST.get("product_id")
        pro_qty = request.POST.get('pro_qty')
        if check_id:
            Product(name=name, pro_qty=pro_qty, product_id=product_id).save()
            data = {"status": 1}
            return JsonResponse(data)
        else:
            check = Product.objects.filter(product_id=product_id)
            if check:
                data = {"status": 0}
                return JsonResponse(data)
            else:
                Product(name=name,pro_qty=pro_qty,product_id=product_id).save()
                data = {"status": 1}
                return JsonResponse(data)
@login_required
def deleteproduct(request):
    id = request.GET.get("id")
    Product.objects.get(product_id=id).delete()
    return products(request)

@login_required
def productmovement(request):
    loc = Location.objects.all()
    pro = Product.objects.all()
    record = ProductMovement.objects.all()
    return render(request,"productmovement.html",{"loc":loc,"pro":pro,"record":record})

@login_required
def productmovementsave(request):
    if request.method =="POST":
        check_id = request.POST.get('check')
        movement_id = request.POST.get("movement_id")
        from_loc = request.POST.get("from_loc","none")
        to_location = request.POST.get("to_location","none")
        pro_id = request.POST.get("pro_id")
        p_qty = request.POST.get("p_qty")
        if check_id:
            name = 0
            product_list = Product.objects.filter(product_id=pro_id)
            for filed in product_list:
                name = filed.name
                productmovement_qty = ProductMovement.objects.filter(p_id_id=pro_id).aggregate(Sum('quantity'))[
                    'quantity__sum']
                if productmovement_qty:
                    val = productmovement_qty
                else:
                    val = 0
                remaining_qty = filed.pro_qty+int(check_id) - val
                if int(p_qty) <= remaining_qty:
                    if to_location == "0" and from_loc == "0":
                        ProductMovement(movement_id=movement_id, p_id_id=pro_id, quantity=p_qty).save()
                    elif to_location != "0" and from_loc != "0":
                        ProductMovement(movement_id=movement_id, to_location_id=to_location,
                                        p_id_id=pro_id, quantity=p_qty).save()
                    if from_loc == "0":
                        ProductMovement(movement_id=movement_id, to_location_id=to_location, p_id_id=pro_id,
                                        quantity=p_qty).save()
                    if to_location == "0":
                        ProductMovement(movement_id=movement_id, from_location_id=from_loc, p_id_id=pro_id,
                                        quantity=p_qty).save()

                    data = {"status": 1}
                    return JsonResponse(data)
                else:
                    data = {"status": 0}
                    return JsonResponse(data)
        else:
            check = ProductMovement.objects.filter(movement_id=movement_id)
            if check:
                data = {"status": 2}
                return JsonResponse(data)
            else:
                name = 0
                product_list = Product.objects.filter(product_id=pro_id)
                for filed in product_list:
                    name = filed.name
                    productmovement_qty = ProductMovement.objects.filter(p_id_id=pro_id).aggregate(Sum('quantity'))['quantity__sum']
                    if productmovement_qty:
                        val = productmovement_qty
                    else:
                        val = 0
                    remaining_qty = filed.pro_qty -val
                    if int(p_qty) <= remaining_qty:
                        if to_location =="0" and from_loc =="0":
                            ProductMovement(movement_id=movement_id,p_id_id=pro_id,quantity=p_qty).save()
                        elif  to_location !="0" and from_loc!="0":
                            ProductMovement(movement_id=movement_id,to_location_id=to_location,p_id_id=pro_id,quantity=p_qty).save()
                        if from_loc =="0":
                            ProductMovement(movement_id=movement_id,to_location_id=to_location,p_id_id=pro_id,quantity=p_qty).save()
                        if to_location == "0":
                            ProductMovement(movement_id=movement_id,from_location_id=from_loc,p_id_id=pro_id,quantity=p_qty).save()

                        data = {"status":1}
                        return JsonResponse(data)
                    else:
                        data = {"status": 0}
                        return JsonResponse(data)
@login_required
def report(request):
    total_product= Product.objects.all()
    record =[]
    data = ProductMovement.objects.all()
    for x in data:
        context = {}
        context['name'] = x.p_id
        if x.from_location != None and x.to_location != None:
            context['location'] = x.to_location
        elif x.from_location == None and x.to_location == None:
            context['location'] = "Store"
        elif x.from_location == None:
            context['location'] = x.to_location
        elif x.to_location == None:
            context['location'] = x.from_location
        context['qty']=x.quantity
        record.append(context)
    return render(request,"report.html",{"record":record,"total":total_product})

@login_required
def editProduct(request):
    id = request.GET.get("id")
    update = Product.objects.get(product_id=id)
    loc_list = Location.objects.all()
    data = Product.objects.all()
    key = {"check": "ok"}
    return render(request, "product.html", {"loc": loc_list, "record": data,"update":update,"key":key})

@login_required
def deletemovement(request):
    id = request.GET.get("id")
    ProductMovement.objects.get(movement_id=id).delete()
    return productmovement(request)

@login_required
def editmovement(request):
    id = request.GET.get("id")
    update = ProductMovement.objects.get(movement_id=id)
    loc = Location.objects.all()
    pro = Product.objects.all()
    record = ProductMovement.objects.all()
    key = {"check": update.quantity}
    return render(request, "productmovement.html", {"loc": loc, "pro": pro, "record": record,"update":update,"key":key})