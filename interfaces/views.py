from django.shortcuts import render,redirect
from io import BytesIO
from django.http import HttpResponse
from .service.logic import dataPdf,printDataInExcel

# Create your views here.

def home(request):
    return render(request,"index.html")

def logic(request):
    if (request.method == "POST"):
        data = dataPdf(request.FILES['file'])
        namePdf = f"{data['nameFile'].split('.')[0]}.xlsx"
        excel = printDataInExcel(data["records"])

        excel_buffer = BytesIO()
        excel.save(excel_buffer)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={namePdf}'
        response.write(excel_buffer.getvalue())
        return response
    else:
        redirect("")