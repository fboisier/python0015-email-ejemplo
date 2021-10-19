import csv

from django.http import HttpResponse
from app.models import User


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response,delimiter=';')
    writer.writerow(['First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list( 'firstname', 'lastname', 'email')
    
    for user in users:
        writer.writerow(user)

    return response
