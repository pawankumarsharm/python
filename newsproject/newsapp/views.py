from django.shortcuts import render

def index(request):
    return render(request,'newsapp/index.html')

def moviesinfo(request):
    head_msg='Latest Movies information'
    msg1='Akshay kumar is going to work in suryawanshi'
    msg2='Salman going to marraige soon'
    msg3='Taimur is flutting with aliya bhat'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3 }
    return render(request,'newsapp/mnews.html',context=my_dict)

def sportsinfo(request):
    head_msg='Latest sports information'
    msg1='Should Dhoni take retirement from cricket?'
    msg2='Virat Kohli is going to complete 100 centuries in upcoming 2 year'
    msg3='Hardik pandya is going become a father of son'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/snews.html',context=my_dict)

def politicsinfo(request):
    head_msg='Latest politics  information'
    msg1='Narendra Modi is going to apply caa,nrc &nrp'
    msg2='Hemant soren called the pravasi majdur from flight'
    msg3='Why Rahul Gandhi name is pappu?'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/pnews.html',context=my_dict)
