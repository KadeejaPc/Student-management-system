from django.shortcuts import render
from login.models import Internal
from login.models import Feedback
from login.models import FeedbackReply
from login.models import Attendence
from login.models import Student
# Create your views here.


def vnot(request):
    uid=str(request.session['uid'])
    objlist = Attendence.objects.filter(s_id=uid)

    context = {
        'objval': objlist,

    }
    return render(request, 'fadv/view_notice.html',context)
def vatt(request):
    uid = str(request.session['uid'])
    objlist = Attendence.objects.filter(s_id=uid)

    context = {
        'objval': objlist,

    }
    return render(request, 'fadv/view_attandance.html',context)
def postfeed(request):
    if request.method == "POST":
        obj = Feedback()
        obj.uid = str(request.session['uid'])
        obj.feedback = request.POST.get("fb")

        obj.save()

    return render(request, 'fadv/post_feedback.html')
def vpro(request):
    uid = str(request.session['uid'])
    objlist = Student.objects.filter(s_id=uid)

    context = {
        'objval': objlist,

    }
    if request.method == "POST":
        obj = Student()
        obj.t_id = request.POST.get("tid")
        obj.cid = request.POST.get("cn")
        obj.sub_name = request.POST.get("sub")
        obj.save()

    return render(request, 'fadv/view_profile.html',context)


def vinternal(request):
    uid = str(request.session['uid'])
    objlist = Internal.objects.filter(s_id=uid)

    context = {
        'objval': objlist,

    }

    return render(request, 'fadv/view_internal.html',context)
def rply(request,idd):
    uid = str(request.session['uid'])
    if request.method == "POST":
        obj = FeedbackReply()
        obj.std_id = uid
        obj.fid = idd
        obj.reply = request.POST.get("reply")
        obj.save()

    return render(request, 'fadv/p_rpl.html',)