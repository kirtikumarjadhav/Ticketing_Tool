from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Ticket, User
from .forms import TicketForm, CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm




def home(request):
    return render(request, 'tickets/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('ticket_list')
    else:
        form = UserCreationForm()
    return render(request, 'tickets/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ticket_list')
    else:
        form = AuthenticationForm()
    return render(request, 'tickets/login.html', {'form': form})





@login_required
def ticket_list(request):
    if request.user.is_engineer:
        tickets = Ticket.objects.filter(assigned_engineer=request.user)
    else:
        tickets = Ticket.objects.filter(creator=request.user)
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.user != ticket.creator and request.user != ticket.assigned_engineer:
        return redirect('ticket_list')

    if request.method == 'POST' and request.user == ticket.assigned_engineer:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.ticket = ticket
            comment.save()
            return redirect('ticket_detail', ticket_id=ticket.id)
    else:
        comment_form = CommentForm()

    return render(request, 'tickets/ticket_detail.html', {
        'ticket': ticket,
        'comment_form': comment_form,
        'comments': ticket.comment_set.all(),
    })

@login_required
def ticket_update(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.user != ticket.assigned_engineer:
        return redirect('ticket_list')

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_detail', ticket_id=ticket.id)
    else:
        form = TicketForm(instance=ticket)

    return render(request, 'tickets/ticket_form.html', {'form': form})

@login_required
def create_ticket(request):
   if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.creator = request.user
            ticket.save()
            return redirect('ticket_list')
   else:
        form = TicketForm()

   return render(request, 'tickets/ticket_form.html', {'form': form})

@login_required
def update_ticket_status(request, ticket_id):
    if not request.user.is_engineer:
        return redirect('ticket_list')
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ticket_detail', args=[ticket_id]))
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/update_ticket_status.html', {'form': form, 'ticket': ticket})


from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('home')

from allauth.account.views import SignupView
from .forms import CustomSignupForm
from django.views import View


class CustomSignupView(SignupView):
    form_class = CustomSignupForm



