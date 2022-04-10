from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from app1.models import Medicine
from django.http import JsonResponse

# Create your views here.


def home(request):
    return render(request,'home.html')

def addmedicine(request):
    if request.method=='POST':
        medicinename=request.POST['name']
        purchasecost=request.POST['purchasecost']
        quantity=request.POST['quantity']
        sellingcost=request.POST['sellingprice']
        add=Medicine(medicine_name=medicinename,purchase_price=purchasecost,quantity=quantity,selling_price=sellingcost)
        add.save()
        return redirect('/home/')
    return render(request,'addmedicine.html')

def billing(request):
    if request.method=='POST':
        name=request.POST['medicine']
        qty=request.POST['price']
        med=Medicine.objects.get(id=name)
        current_qty=med.quantity
        updated_qty=int(current_qty)-int(qty)
        med.quantity=str(updated_qty)
        med.save()

    else: 
        med=Medicine.objects.all()
        return render(request,'billing.html',{"medicine":med})

@csrf_exempt
def medbilling(request):
    medname=request.POST['medicine']
    qty=request.POST['qty']
    print(qty)
    med=Medicine.objects.get(id=medname)
    current_qty=med.quantity
    updated_qty=int(current_qty)-int(qty)
    med.quantity=str(updated_qty)
    med.save()
    view = Medicine.objects.get(id=medname)
    price = view.selling_price
    cgst=int(price)*(5/100)
    total=int(qty)*int(price)+cgst
    returnObj = {
        'medicine_name': view.medicine_name,
        'selling_price': view.selling_price
    }
    return JsonResponse({'med': returnObj,'qty':qty,'total':total,'cgst':cgst})
    
def stock(request):
    view=Medicine.objects.all()
    return render(request,'stock.html',{'medicine':view})

def update(request,id):
    if request.method=='POST':
        medicinename=request.POST['name']
        purchasecost=request.POST['purchasecost']
        quantity=request.POST['quantity']
        sellingcost=request.POST['sellingprice']
        upd=Medicine.objects.filter(id=id).update(medicine_name=medicinename,purchase_price=purchasecost,quantity=quantity,selling_price=sellingcost)
        return redirect('/stock/')
    else:
        show=Medicine.objects.filter(id=id).get()
        return render(request,'update.html',{'show':show})