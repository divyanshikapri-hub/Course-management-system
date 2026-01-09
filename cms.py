class CourseManagementSystem:
    def __init__(self):
        self.courses = {}

    def addCourse(self, course_id, name):
        if course_id not in self.courses:
            self.courses[course_id] = {"name": name, "prereq": set()}

    def listPrerequisites(self, course_id):
        if course_id not in self.courses:
            return []
        
        all_prereqs = set() 
        def collect(c_id):
            for prereq in self.courses[c_id]["prereq"]:
                if prereq  not in all_prereqs:
                    all_prereqs.add(prereq)
                    collect(prereq)
        collect(course_id)
        return list(all_prereqs)

    def addPrerequisite(self, course_id, prerequisite_id):
        if course_id not in self.courses or prerequisite_id not in self.courses:
            return False
        if course_id == prerequisite_id:
            return False
        if course_id in self.listPrerequisites(prerequisite_id):
            print(f"Error: Adding {prerequisite_id} as a prereq to {course_id} creates a cycle.")
            return False
        
        self.courses[course_id]["prereq"].add(prerequisite_id)
        return True

    def canEnroll(self, course_id, completed_courses):
        if course_id not in self.courses:
            return False
            
        required = self.listPrerequisites(course_id)
        return all(course in completed_courses for course in required)
#examples
cms = CourseManagementSystem()
cms.addCourse("CS101", "Intro to CS")
cms.addCourse("CS201", "Data Structures")
cms.addCourse("CS301", "Algorithms")
cms.addPrerequisite("CS201", "CS101")
cms.addPrerequisite("CS301", "CS201")
print(cms.listPrerequisites('CS301')) 
print(cms.canEnroll('CS301', ['CS101', 'CS201']))
