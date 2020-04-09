from django.shortcuts import render
from django.http import HttpResponse
import json

def home(request):
    return render(request,'ACTUAL/HTML.html')
# Create your views here.
def result(request):
    symbol=request.GET['symbol']
    allotment=float(request.GET['allotment'])
    final=float(request.GET['final'])
    scommission=float(request.GET['scommission'])
    initial=float(request.GET['intial'])
    bcommission=float(request.GET['bcommission'])
    Gain=float(request.GET['Gain'])
    proceeds = allotment * final
    purchasePrice = (allotment * initial)
    totalExpenditure = purchasePrice + scommission + bcommission
    capitalGain = proceeds - totalExpenditure
    tax = 0
    if capitalGain > 0 :
        tax = capitalGain * (Gain/100)
    cost = totalExpenditure + tax
    #proceeds = allotment*final
    #cost = (allotment*initial)+ scommission + bcommission + ((allotment*initial - initial  - scommission - bcommission) * (Gain/100))
    profit = proceeds - cost
    return_on_investment = (profit/cost)*100
    break_even = ((allotment*initial)-scommission-bcommission)/allotment
    output=['Symbol:', symbol , 'Proceeds:', proceeds , 'Cost:', cost ,'Profit:', profit ,'Return_on_investment:', return_on_investment, 'Break_even:', break_even]
    #names=['symbol','proceeds','cost','return_on_investment','break_even']
    return render(request,'ACTUAL/RESULT.html',{'outputs':output})
