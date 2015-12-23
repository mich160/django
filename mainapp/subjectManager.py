from mainapp.models import Subject, Teacher, Class, Lesson
import xml.etree.ElementTree as ET
import datetime

daysLookup = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
}

classNumberHourLookup = {
    '1': datetime.time(8),
    '2': datetime.time(9),
    '3': datetime.time(10),
    '4': datetime.time(11),
    '5': datetime.time(12),
    '6': datetime.time(13),
    '7': datetime.time(14),
    '8': datetime.time(15)
}


def manage():
    tree = ET.parse('D:\django\mainapp\classSchedule.xml')

    for cls in tree.getroot():
        className = cls.find('classname').text
        for day in cls.find('timetable'):
            dayName = day.tag
            for subject in day:
                subjectName = subject.find('name').text
                teacher = subject.find('teacher').text
                lessonTime = subject.find('lesson').text

                clz = Class.objects.get(name=className)
                t = Teacher.objects.get(tempFullName=teacher)
                sub = None
                try:
                    sub = Subject.objects.get(name=subjectName, clazz=clz, teacher=t)
                except:
                    sub = Subject(name=subjectName, clazz=clz, teacher=t)
                    sub.save()

                lessonDateTime = datetime.datetime.combine(
                    next_weekday(datetime.date.today() + datetime.timedelta(days=4), daysLookup[dayName]),
                    classNumberHourLookup[lessonTime])

                les = None
                try:
                    les = Lesson.objects.get(subject=sub, date=lessonDateTime)
                except:
                    les = Lesson(subject=sub, date=lessonDateTime)
                    les.save()

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)
