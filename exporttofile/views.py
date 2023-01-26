from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook

def home_page(request):
    wb = Workbook()
    ws = wb.active
    ws.append(['First Name', 'Last Name'])

    data = [{
        'first_name': 'Nidhi',
        'last_name': 'Rathee'
    },
    {
        'first_name': 'Test',
        'last_name': 'Test name'
    }]

    for record in data:
        ws.append([record['first_name'], record['last_name']])

    response = HttpResponse(content=save_virtual_workbook(wb), content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=exportfile.xlsx'

    return response