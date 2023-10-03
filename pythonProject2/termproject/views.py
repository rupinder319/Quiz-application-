from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max, Min

from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


from .forms import UserRegistrationForm, UserLoginForm, Quizform

# Create your views here.

from django.http import HttpResponse

from .models import Question, Quiz



def home(request):
    return render(request,'termproject/home.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account created successfully. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'termproject/register.html', context)

@csrf_exempt
def Login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
           user = authenticate(username=form.cleaned_data['username'],
                              password = form.cleaned_data['password']) #it is used to convert data into its appropriate type

           if user is not None:
            login(request, user)
            return redirect('quiz')
           else:
               messages.error(request, 'username or password is incorrect. Try again')
               return redirect('login')

    else:
       form = UserLoginForm()
    context = {'form': form}
    return render(request, 'termproject/login.html', context)



@csrf_exempt
def quiz(request):
    if request.method == 'POST':
        score = 0
        wrong = 0
        correct = 0
        total_questions = 5
        q= Question.objects.all()

        for ques in q:

            print(request.POST.get(ques.question))
            print(ques.ans)
            if ques.ans == request.POST.get(ques.question):
                score += 1
                correct += 1
                print(score)
            else:
                wrong = total_questions-correct
        percent = score / (total_questions) * 100

        context = {
                'score': score,

                'correct': correct,
                'wrong': wrong,
                'percent': percent,
                'total': total_questions
            }

        if score<3:
            messages.error(request, "Please try again!!!")
            return render(request, 'termproject/result.html', context)

        elif score>=3 and score<5:
            messages.error(request, "You are good!!!")
            return render(request, 'termproject/result.html', context)

        else:
            messages.error(request,"You are genius!!!")
            return render(request, 'termproject/result.html', context)

    else:
        questions = Question.objects.order_by('?')[:5]
        context = {
            'q': questions
        }
        return render(request, 'termproject/quiz.html', context)

@csrf_exempt
def quiz_create(request):
    form = Quizform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('score')
    else:
        pass

    return render(request, "termproject/quiz.html", {'form': form})
@csrf_exempt
def submit_result(request):
    allList = Quiz.objects.filter(question_id=request.user.id)
    average = Quiz.objects.filter(question_id=request.user.id).aggregate(Avg('score'))
    highest = Quiz.objects.filter(question_id=request.user.id).aggregate(Max('score'))
    lowest = Quiz.objects.filter(question_id=request.user.id).aggregate(Min('score'))
    form = Quizform()

    context = {
        "allList": allList,
        'form': form,
        'average': average,
        'highest': highest,
        'lowest': lowest
    }
    return render(request, 'termproject/score.html', context)



