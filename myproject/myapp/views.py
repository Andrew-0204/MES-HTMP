from django.shortcuts import render
from .models import MonitorCnc,MonitorMachine,MonitorProduct,MonitorProductionOutput,MonitorTool,MonitorWorker
# Create your views here.


class Status:
    

    def __init__(self, num, time,timperday,status_before) -> None:
        self.status = num
        self.status_time = time
        self.status_time_per_day = timperday
        self.status_before = status_before

class CNC:
    def __init__(self) -> None:
        self.status_history = [0]
        self.database = 0
        self.status = 0
        
    

list_machine = MonitorMachine.objects.values_list("id_check", flat=True).order_by("id_check")
list_cnc = []
list_state = ['STOP'] *20
for machine in list_machine:
    cnc = CNC()
    cnc.status_history.append(Status(0,0,0,0))
    list_cnc.append(cnc)



def index(request):

    global list_machine, list_cnc,list_state
            
    state_dict = {
        "0": 'STOP',
        "1": 'ERROR',
        "2": 'DONE',
        "3": 'ON',
    }

    i = 0
    on_sum= 0 
    err_sum=0 
    done_sum=0 
    stop_sum =0

    for cnc in list_cnc:
        # Thời điểm hiện tại
        cnc.database = list(MonitorCnc.objects.filter(id=list_machine[i]))[-1]
        
        cnc.status = state_dict[str(cnc.database.status)]

        if (cnc.status == 'ERROR'):
            err_sum = err_sum+1
        elif (cnc.status == 'DONE'):
            done_sum= done_sum+1
        elif (cnc.status == 'ON'):
            on_sum=on_sum+1
        elif(cnc.status == 'STOP'):
            stop_sum= stop_sum+1
        

        

        if (cnc.status != list_state[i]):
            minute = list(MonitorCnc.objects.filter(id=list_machine[i]))[-1].create_at.minute 
            hour = list(MonitorCnc.objects.filter(id=list_machine[i]))[-1].create_at.hour 

            #CẦN TỐI ƯU CODE TÍNH THỜI GIAN TRONG NGÀY
            time = hour*60 +minute #Thời gian tính từ 0h
            time_per_day = ((time - cnc.status_history[-1].status_time)/1440)*100

            status1 = Status(cnc.status, time, time_per_day, list_state[i])
            cnc.status_history.append(status1)
            list_state[i] = cnc.status
            
        i=i+1
    
    cnc_sum = len(list_cnc)
    
    context = {
        
        'on_sum':on_sum,
        'err_sum': err_sum,
        'done_sum':done_sum,
        'stop_sum':stop_sum,
        'cnc_sum'  : cnc_sum,
        'list_cnc' : list_cnc
        
    }
    return render (request,'index.html',context)


def detail(request,pk):
    cnc = list(MonitorCnc.objects.filter(id=pk))[-1]

    for cnc in list_cnc:
        if cnc.database.id.id_check == pk:
            cnc_detail = cnc
    return render(request,'detail.html',{'cnc' :cnc_detail})