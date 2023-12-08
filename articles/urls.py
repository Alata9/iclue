from django.urls import path

from articles.views import (
    ItemsView, ItemIdView, ItemDeleteView,
    SubsectionsView, SubsectionIdView, SubsectionDeleteView,
    QuestionsView, QuestionIdView, QuestionDeleteView,

)

urlpatterns = [
    path('subsections/', SubsectionsView.as_view(), name='subsections'),
    path('subsection/', SubsectionIdView.as_view(), name='subsection_add'),
    path('subsection/<int:pk>', SubsectionIdView.as_view(), name='subsection_id'),
    path('subsection/<int:pk>/delete', SubsectionDeleteView.as_view(), name='subsection_del'),

    path('items/', ItemsView.as_view(), name='items'),
    path('item/', ItemIdView.as_view(), name='item_add'),
    path('item/<int:pk>', ItemIdView.as_view(), name='item_id'),
    path('item/<int:pk>/delete', ItemDeleteView.as_view(), name='item_del'),

    path('questions/', QuestionsView.as_view(), name='questions'),
    path('question/', QuestionIdView.as_view(), name='question_add'),
    path('question/<int:pk>', QuestionIdView.as_view(), name='question_id'),
    path('question/<int:pk>/delete', QuestionDeleteView.as_view(), name='question_del'),

]