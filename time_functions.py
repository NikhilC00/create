#Functions for Homework Time Calculator
time_per_hw = .5
time_per_test = 1
time_per_project = 2

##########ASK USER FUNCTIONS##########

#Ask User for Start Time (tested)
def ask_time_start():
    print '\nWhat time will you start working'
    print 'Note: Please write the time as military time hh:mm (Ex: 13:30)\n\t'
    time_start = raw_input('Start Time: ')
    return time_start

#Ask User for End Time (tested)
def ask_time_end():
    print '\nWhat time will you stop working'
    print 'Note: Please write the time as military time hh:mm (Ex: 13:30)\n\t'
    time_stop = raw_input('Stop Time: ')
    return time_stop

#Ask User for Homework Assignments (tested)
def ask_number_hw():
    print '\nHow many homework assignments do you have'
    print 'Note: Please enter an integer value\n\t'
    hw_num = input('Number of Homework Assignments: ')
    return hw_num

#Ask User for Projects (tested)
def ask_number_project():
    print '\nHow many projects do you have'
    print 'Note: Please enter an integer value\n\t'
    project_num = input('Number of Projects: ')
    return project_num

#Ask User for Tests (tested)
def ask_number_test():
    print '\nHow many tests do you have'
    print 'Note: Please enter an integer value\n\t'
    test_num = input('Number of Tests: ')
    return test_num

##########MATH CALCULATIONS FOR TIME##########

#Find Total Work Time (tested)
def work_time(hw_num, project_num, test_num):
    total_time = hw_num*time_per_hw + project_num*time_per_project + test_num*time_per_test
    return total_time

#Convert User Time Input to Hours (tested)
def hours_from_time(time):
    hours = int(time[0])*10 + int(time[1])
    return hours

#Convert User Time Input to Minutes (tested)
def minutes_from_time(time):
    minutes = int(time[3])*10 + int(time[4])
    return minutes

def wrap_time_hours(hours):
    if(hours >= 24):
        return hours - 24
    else:
        return hours

#Return the amount of hours between Start and End Time (tested)
def user_time_hours(start_time, end_time):
    user_hours = hours_from_time(end_time) - hours_from_time(start_time)
    user_minutes = minutes_from_time(end_time) - minutes_from_time(start_time)
    if(user_hours < 0):
        user_hours = (24 - hours_from_time(start_time)) + hours_from_time(end_time)
                      
    if(user_minutes < 0):
        user_hours = user_hours-1
    return user_hours

#Return the amount of minutes between Start and End Time (tested)      
def user_time_minutes(start_time, end_time):
    user_minutes = minutes_from_time(end_time) - minutes_from_time(start_time)
    if(user_minutes < 0):
        user_minutes = 60 + user_minutes
    return user_minutes

def left_over_hours(user_hours, work_time):
    if(work_time - int(work_time) == 0):
        return user_hours - work_time
    else:
        return user_hours - int(work_time) - 1

def left_over_minutes(user_minutes, work_time):
    work_time = work_time - int(work_time)
    if(work_time == 0):
        return 0
    else:
        minutes_left = user_minutes - work_time*60
        if(minutes_left < 0):
            return 60-minutes_left
        else:
            return minutes_left

def end_time(user_time, work_time):
    end_hours = 0
    end_minutes = 0
    user_hours = hours_from_time(user_time)
    user_minutes = float(minutes_from_time(user_time))/60
    work_hours = int(work_time)
    work_minutes = work_time - int(work_time)
    
    if(work_time - int(work_time) == 0):#No HW Assign
        end_hours = wrap_time_hours(user_hours + work_hours)
        end_minutes = user_minutes
    else:#Some HW Assign
        if(user_minutes + work_minutes >= 1):
            end_hours = wrap_time_hours(user_hours + work_hours + 1)
            end_minutes = (user_minutes + work_minutes - 1)
        else:
            end_hours = wrap_time_hours(hours_from_time(user_time) + work_hours)
            end_minutes = user_minutes + work_minutes

    end_minutes = int(end_minutes*60)
    if(end_minutes < 10):
        return (str(end_hours) + ":0" + str(end_minutes))
    return (str(end_hours) + ":" + str(end_minutes))

    
#####Tests#####

def main():
    startTime = ask_time_start()
    hw = ask_number_hw()
    project = ask_number_project()
    test = ask_number_test()
    workTime = work_time(hw, project, test)
    endTime = end_time(startTime, workTime)
    print '\nYou will get to sleep at', endTime

main()
