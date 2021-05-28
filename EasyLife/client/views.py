import client
from django.shortcuts import render,redirect,HttpResponseRedirect
from client.models import Client, Offre
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
import datetime

def homeLogin(request):
    if request.method == 'POST':
        if Client.objects.filter(email=request.POST.get('email'),mdp=request.POST.get('password')).exists():
            client = Client.objects.get(email=request.POST.get('email'),mdp=request.POST.get('password'))
            request.session['email']=client.email
            return redirect("profile_client")
        else:
            message = messages.success(request,"le mot de passe ou l'email incorrecte")
            return render(request,"login_client.html",message)
    else:
        return render(request,"login_client.html")

def registerPage(request):
    if request.method == 'POST':
        client = Client(nom=request.POST.get('nom'),prenom=request.POST.get('prenom'),email=request.POST.get('email'),mdp=request.POST.get('password'),tel=request.POST.get('tel'),ville=request.POST.get('ville'))
        client.save()
        return render(request,'login_client.html')
    
    else:
        return render(request,'register_client.html')
    
def getDetailClient(request):
        client = get_object_or_404(Client,email=request.session['email'])
        context = {'data':client}
        return render(request,'client/profile_client.html',context)

def modifierClient(request):
    client = get_object_or_404(Client,email=request.session['email'])
    context = {
        'data':client,
    }
    if request.method =='POST':
        client = Client.objects.get(email=request.session['email'])
        client.nom = request.POST['nom']
        client.prenom = request.POST['prenom']
        client.tel = request.POST['tel']
        client.ville = request.POST['ville']
        if not request.POST['new']:
            client.mdp = request.POST['new']
        client.save()
        return redirect("profile_client")
    return render(request,'client/modifier_client.html',context)

def GetAllOffre(request):
    if request.method == 'POST':
        client1 = Client.objects.get(email=request.session['email'])
        offre = Offre(date_pub=datetime.datetime.now(),description=request.POST['description'],categorie=request.POST['categorie'],client=client1)
        offre.save()
        return redirect('list_offre')
    offre = Offre.objects.all()
    return render(request,"client/List_offre.html",{'offre':offre})

def GetDetailsOffre(request,idC):
    offre = Offre.objects.get(id=idC)
    return render(request,'client/Details_offre.html',{'offre':offre})

def GetOffreClient(request):
    client1 = Client.objects.get(email=request.session['email'])
    offre = Offre.objects.all().filter(client=client1)
    return render(request,'client/Offre_client.html',{'offre':offre})

def ModifierOffre(request,idO):
    offre = Offre.objects.get(id=idO)
    if request.method == 'POST':
        offre.categorie = request.POST.get('categorie')
        offre.description = request.POST.get('description')
        offre.save()
        return redirect('offre_by_client')
    return render(request,'client/modifier_offre.html',{'offre':offre})