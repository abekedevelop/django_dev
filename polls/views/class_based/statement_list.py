from django.views.generic import ListView
from polls.models import Statement


class StatementList(ListView):
    template_name = 'polls/class_based/statement_list.html' # could be omitted if path to template was 'polls/statement_list'
    model = Statement
    queryset = Statement.objects.all()
    context_object_name = 'stats'
