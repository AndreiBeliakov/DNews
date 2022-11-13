
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.db.models.signals import post_save
from .models import UsersSubscriptions


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_not_author"] = not self.request.user.groups.filter(name='authors').exists()
        return context


@login_required
def upgrade_me(request):
    user = request.user
    editor_group = Group.objects.get(name='editor')
    if not request.user.groups.filter(name='editor').exists():
        editor_group.user_set.add(user)
    return redirect('/account/')

@login_required
def subscribes(request, i):
    user = User.objects.get(username=request.user)
    if user:
        cat1 = Author.objects.get(pk=i)
        cat1.subscriber.add(user)
    return redirect('/news/')