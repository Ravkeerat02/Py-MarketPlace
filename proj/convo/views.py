from django.shortcuts import get_object_or_404, redirect, render

from item.models import Item
from proj.convo.models import Conversation, ConversationMessage

# Create your views here.
def new_convo(req , item_pk):
    item = get_object_or_404(Item, pk = item_pk)
    
    if item.created_by == req.user:
        return render('dashboard:index')
    
    convo = Conversation.objects.filter(item).filter(members_in = [req.user.id])

    if convo:
        pass #redirect to convo
    if req.method == 'POST':
        form = ConversationMessage(req.POST)
        
    if form.is_valid():
        convo = Conversation.objects.create(item = item)
        convo.members.add(req.user)
        convo.save()
        
        convo_msg = form.save(commit=False)
        convo_msg.created_by = req.user
        convo_msg.conversation = convo
        convo_msg.save()
        
        return redirect('convo:detail', pk=convo.id)