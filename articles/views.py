
from django.views.generic import TemplateView, UpdateView, ListView, DeleteView
from django.db.models import ProtectedError

from articles.forms import ItemAdd, SubsectionAdd, QuestionsAdd
from articles.models import Items, Subsections, Questions


class HomeView(TemplateView):
    template_name = 'articles/home.html'


class ItemsView(ListView):
    template_name = 'articles/items.html'
    model = Items


class ItemIdView(UpdateView):
    model = Items
    template_name = 'articles/item_id.html'
    form_class = ItemAdd
    success_url = '/items'

    def get_object(self, queryset=None):
        if 'pk' in self.kwargs:
            return super().get_object(queryset)


class ItemDeleteView(DeleteView):
    error = ''
    model = Items
    success_url = '/items'
    template_name = 'articles/item_del.html'

    def post(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError as error:
            self.object = self.get_object()
            context = self.get_context_data(
                object=self.object,
                error=f'Error: {error.protected_objects}'
            )
            return self.render_to_response(context)


class SubsectionsView(ListView):
    template_name = 'articles/subsections.html'
    model = Subsections


class SubsectionIdView(UpdateView):
    model = Subsections
    template_name = 'articles/subsection_id.html'
    form_class = SubsectionAdd
    success_url = '/subsections'

    def get_object(self, queryset=None):
        if 'pk' in self.kwargs:
            return super().get_object(queryset)


class SubsectionDeleteView(DeleteView):
    error = ''
    model = Subsections
    success_url = '/subsections'
    template_name = 'articles/subsection_del.html'

    def post(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError as error:
            self.object = self.get_object()
            context = self.get_context_data(
                object=self.object,
                error=f'Error: {error.protected_objects}'
            )
            return self.render_to_response(context)


class QuestionsView(ListView):
    template_name = 'articles/questions.html'
    model = Questions


class QuestionIdView(UpdateView):
    model = Questions
    template_name = 'articles/question_id.html'
    form_class = QuestionsAdd
    success_url = '/questions'

    def get_object(self, queryset=None):
        if 'pk' in self.kwargs:
            return super().get_object(queryset)


class QuestionDeleteView(DeleteView):
    error = ''
    model = Questions
    success_url = '/questions'
    template_name = 'articles/question_del.html'

    def post(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError as error:
            self.object = self.get_object()
            context = self.get_context_data(
                object=self.object,
                error=f'Error: {error.protected_objects}'
            )
            return self.render_to_response(context)