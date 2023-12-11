from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # to protect function views
from .forms import SalesSearchForm
from .models import Sale
from .utils import get_bookname_from_id

import pandas as pd

# Create your views here.


def home(request):
    return render(request, 'sales/home.html')

# define function-based view - records()
# keep protected


@login_required
def records(request):
    # create instance of SalesSearchForm
    form = SalesSearchForm(request.POST or None)
    # initialize dataframe to None
    sales_df = None

    # check if button is clicked
    if request.method == 'POST':
        # read book title and chart type
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')

        # apply filter to extract data
        qs = Sale.objects.filter(book__name=book_title)
        if qs:
            sales_df = pd.DataFrame(qs.values())
            sales_df['book_id'] = sales_df['book_id'].apply(
                get_bookname_from_id)
            sales_df = sales_df.to_html()

    context = {
        'form': form,
        'sales_df': sales_df,
    }

    # send request and context to template
    return render(request, 'sales/records.html', context)
