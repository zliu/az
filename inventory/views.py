from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import invTypes, invTypeMaterials, trnTranslationLanguages, trnTranslationColumns, trnTranslations
import requests
import json
from django.core import serializers
from operator import itemgetter

# Create your views here.
def __get_trans(type_id):
    language = get_object_or_404(trnTranslationLanguages, languageID='zh')
    translation = get_object_or_404(trnTranslations, tcID=8, keyID=type_id, languageID=language.languageID)
    return translation.text

def type_list(request):
    types = invTypes.objects.all()[:100]

    return render(request, 'eve/type_list.html', {'types':[{'tid':t.typeID, 'tname': __get_trans(t.typeID)} for t in types]})

def type_detail(request, type_id):
    item = get_object_or_404(invTypes, pk=type_id)
    #return render(request, 'eve/type_detail.html', serializers.serialize('json', item.get_queryset()))
    item_json = json.loads(serializers.serialize("json", invTypes.objects.filter(pk=type_id)))
    item_json[0]['fields']['typeName'] = __get_trans(type_id)
    material_list = invTypeMaterials.objects.filter(productTypeID=type_id)
    a=[]
    if material_list.count():
        a = [{'material_id':item.materialTypeID.typeID,'material_name':__get_trans(item.materialTypeID.typeID),'quantity':item.quantity} for item in material_list]

    context = {}
    context['item_info_json_string'] = json.dumps(item_json[0]).replace('None','null')
    context['industry'] = json.dumps(a)
    price_list = requests.get('https://esi.evepc.163.com/latest/markets/10000002/orders/?datasource=serenity&order_type=all&page=1&type_id=%s'% type_id).json()
    sell_list = sorted([p for p in price_list if not p['is_buy_order']], key=itemgetter('price'))
    buy_list = sorted([p for p in price_list if p['is_buy_order']], key=itemgetter('price'), reverse=True)
    context['market'] = json.dumps({'buy':buy_list, 'sell': sell_list})
    return render(request, 'eve/type_detail.html', context)

def industry_indices(request):
    result = requests.get('https://esi.evepc.163.com/latest/industry/systems/?datasource=serenity').json()
    # DS-LO3 system id is 30003992
    index = None
    for idx in result:
        if idx['solar_system_id'] == 30003992:
            index = idx['cost_indices']
            break
    context = {}
    context['index'] = json.dumps(index)
    return render(request, 'eve/industry.html', context)

