import json

"""
roster has 
1) course id (CSCI 1511)
2) section (01966)
3) list of students
4) semester
"""

def get_class_and_section() -> dict:
    """Prompt for the class number and class section"""
    course_info = {}
    # prompt for class
    course_number = input("Course Number: ")
    course_section = input("Course Section Number: ")

    print(f"You're adding the following course: {course_number} section: {course_section}")
    answer = input("Is this correct (y/n)?")
    if answer != 'y':
        # we'll worry about this later
        raise NotImplemented("havn't dealt with confirming course info redos")

    course_info['course_number'] = course_number
    course_info['course_section'] = course_section

    return course_info

def add_students_to_course(course_info: dict) -> dict:
    """Add student list to the course's student roster"""

    student_list = get_students()

    course_info['roster'] = student_list

    return course_info

def get_students() -> list:
    """Get students' names one at a time"""
    student_list = []

    print(f"Add students one at a time for course {course_info['course_number']}. Enter 'done' when finished.")
    while response != 'done':
        student_name = input(f"Student to add: ")
        student_list.append(student_name)

    return student_list

def get_semester() -> dict:
    """Get semester information"""
    semester_info = {}
    semester = input("Semester: ")

    print(f"You're adding the following semester: {semester}")
    answer = input("Is this correct (y/n)?")
    if answer != 'y':
        # we'll worry about this later
        raise NotImplemented("havn't dealt with confirming course info redos")

    # there may be more information to tack onto the semester, but right now this is enough

    semester_info['semester'] = semester
    return semester_info

def add_classes_to_semester(semester_info: dict) -> dict:
    """Allow users to add classes to a semester"""

    semester_info['classes'] = []

    answer = input("Please enter classes to add to semester. When complete, enter done")
    while answer != done:
        semester_info['classes'].append(get_class_and_section())

    return semester_info

def fetch_semester_year(semester_info: dict) -> str:
    
    return(semester_info['semester'])


    








    

    


