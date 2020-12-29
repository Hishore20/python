class Instructor:
    def __init__(self, name, avg_feedback, technology_skill, experience):
        self.__inst_name = name
        self.__inst_avg_feedback = avg_feedback
        self.__inst_tech_skill = technology_skill
        self.__inst_exp = experience
        
    def check_eligibility(self):
        if self.__inst_exp > 3:
            if self.__inst_avg_feedback >= 4.5:
                return True
            else:
                if self.__inst_avg_feedback >= 4:
                    return True
            return False
            
    def allocate_course(self, technology):
        if self.check_eligibility():
            if technology in self.__inst_tech_skill:
                return True
            else:
                return False
        return False
def main():
    name = input("Enter Instructor Name: ")
    feedback = float(input("Enter average feedback: "))
    exp = int(input("Enter experience "))
    tech_skill = list()
    n = int(input("Enter no. technology skills known: "))
    print("Enter Skills")
    for i in range(0, n):
        tech_skill.append(input("Skill Name: "))
    inst_obj = Instructor(name, feedback, tech_skill, exp)
    tech = input("Enter the course to allocate to him: ")
    if inst_obj.allocate_course(tech):
        print("The instructor is eligible for the course")
    else:
        print("The instructor is not eligible for the course")
        
main()
