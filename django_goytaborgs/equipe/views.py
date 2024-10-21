from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Robot, Team, Competitor
from .forms import RobotForm

# View para cadastrar um robô
def register_robot(request):
    if request.method == 'POST':
        form = RobotForm(request.POST, request.FILES)
        if form.is_valid():
            robot = form.save(commit=False)
            # Verificar se o usuário é capitão
            if request.user.competitor.is_captain():
                robot.team = request.user.competitor.team
                robot.save()
                return redirect('robot_list')
    else:
        form = RobotForm()
    return render(request, 'register_robot.html', {'form': form})
