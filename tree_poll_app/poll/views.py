from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Test, Question, Choice


class HomeViewSet(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'
    
    # Список опросов.
    def list(self, request):
        tests = Test.objects.all()
        context = {
            'tests': tests,
        }
        return render(request, "home.html", context)
    
    # Страница опроса, на которой отображаются все вопросы с dsiplay=True, с формой ответа.
    def retrieve(self, request, pk=None):
        tests = Test.objects.all()
        test = get_object_or_404(tests, pk=pk)
        context = {
            'test': test,
        }
        return render(request, "test.html", context)
    
    # Принимаем результат формы, отображаем что ответ на вопрос получен, и отображаем зависимые вопросы если они есть.
    def post(self, request, pk):
        data = (request.POST.get('number_choice')).split()
        
        test = Test.objects.get(id=data[0])
        quest = test.questions.get(id=data[1])
        vote = quest.choices.get(number_choice=data[2])
        vote.votes += 1
        vote.save()
        
        child_quests = quest.children.filter(choice_trigger__icontains=data[2])
        event_go = True
        context = {
                'child_quests': child_quests,
                'test': test,
                'question': quest,
                'answer': vote,
            }
        return render(request, "add_remove.html", context)
    
    #Страница результатов опроса.
    def statistic(self, request, pk=None):
        # Общее количество ответов на каждый вопрос.
        total_question = Question.objects.raw(
            "WITH total_question AS\
                (SELECT poll_choice.question_id as id, poll_question.test_id,\
                    SUM(poll_choice.votes) as question_sum_votes\
                FROM poll_choice\
                LEFT JOIN poll_question ON poll_choice.question_id = poll_question.id\
                WHERE poll_question.test_id = %s\
                GROUP BY poll_choice.question_id, poll_question.test_id)\
            SELECT id, RANK() OVER(ORDER BY question_sum_votes DESC) as rank,\
            test_id, question_sum_votes, (question_sum_votes * 100 / \
                (SELECT MAX(question_sum_votes) FROM total_question)\
                ) as percent\
            FROM total_question\
            GROUP BY id, test_id, question_sum_votes\
            ORDER BY question_sum_votes DESC", [pk]
            )
        # Общее количество ответов и их долях.
        total_choice = Choice.objects.raw(
            "WITH total_question AS\
                (SELECT poll_choice.question_id as id, poll_question.test_id,\
                    SUM(poll_choice.votes) as question_sum_votes\
                FROM poll_choice\
                LEFT JOIN poll_question ON poll_choice.question_id = poll_question.id\
                WHERE poll_question.test_id = %s\
                GROUP BY poll_choice.question_id, poll_question.test_id)\
            SELECT poll_choice.id, poll_choice.question_id,\
                (poll_choice.votes * 100 / \
                    (SELECT question_sum_votes FROM total_question WHERE total_question.id = poll_choice.question_id)\
                ) as percent\
            FROM poll_choice\
            LEFT JOIN poll_question ON poll_choice.question_id = poll_question.id\
            WHERE poll_question.test_id = %s\
            GROUP BY poll_choice.id, poll_choice.question_id",[pk, pk]
        )
        context = {
            "total_question": total_question,
            "total_choice": total_choice,
        }
        return render(request, "statistic.html", context)