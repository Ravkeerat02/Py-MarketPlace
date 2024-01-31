from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import NewItemForm


def detail(request,pk):
    item = get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(category=item.category , is_sold=False). exclude(pk=pk)[:4]

    return render(request, 'item/detail.html',{
        'item':item,
        'related_items':related_items,
    })
    

# redirected to login page
@login_required
def new(request):
    # checking if form is submitted
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })
