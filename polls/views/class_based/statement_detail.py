from django.views.generic import DetailView
from polls.models import Statement


class StatementDetail(DetailView):
    model = Statement
    # slug = None
    template_name = 'polls/class_based/statement_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
