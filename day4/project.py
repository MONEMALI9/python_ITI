import datetime

class Project:
    def __init__(self, title, details, total_target, start_time, end_time):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_time = start_time
        self.end_time = end_time

class ProjectCampaign:
    def __init__(self):
        self.projects = []
    
    def create_project(self):
        title = input("Enter the project title: ")
        details = input("Enter project details: ")
        total_target = float(input("Enter total target amount (EGP): "))
        start_time = input("Enter campaign start time (YYYY-MM-DD): ")
        end_time = input("Enter campaign end time (YYYY-MM-DD): ")
        
        try:
            start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d")
            end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return
        
        project = Project(title, details, total_target, start_time, end_time)
        self.projects.append(project)
        print("Project created successfully.")
    
    def view_projects(self):
        if not self.projects:
            print("No projects available.")
            return
        for index, project in enumerate(self.projects, start=1):
            print(f"Project {index}: {project.title}")
            print(f"Details: {project.details}")
            print(f"Total Target: {project.total_target} EGP")
            print(f"Start Time: {project.start_time.strftime('%Y-%m-%d')}")
            print(f"End Time: {project.end_time.strftime('%Y-%m-%d')}")
            print("=" * 30)
    
    def edit_project(self):
        self.view_projects()
        choice = int(input("Enter the project number to edit: ")) - 1
        if choice < 0 or choice >= len(self.projects):
            print("Invalid project number.")
            return
        project = self.projects[choice]
        
        title = input("Enter the new project title: ")
        details = input("Enter new project details: ")
        total_target = float(input("Enter new total target amount (EGP): "))
        
        project.title = title
        project.details = details
        project.total_target = total_target
        print("Project updated successfully.")
    
    def delete_project(self):
        self.view_projects()
        choice = int(input("Enter the project number to delete: ")) - 1
        if choice < 0 or choice >= len(self.projects):
            print("Invalid project number.")
            return
        del self.projects[choice]
        print("Project deleted successfully.")
    
    def search_projects_by_date(self):
        search_date = input("Enter the search date (YYYY-MM-DD): ")
        try:
            search_date = datetime.datetime.strptime(search_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format.")
            return
        found_projects = [project for project in self.projects if project.start_time.date() == search_date]
        
        if not found_projects:
            print("No projects found for the specified date.")
            return
        
        print(f"Projects on {search_date}:")
        for project in found_projects:
            print(project.title)
        
if __name__ == "__main__":
    campaign = ProjectCampaign()
    
    while True:
        print("Options:")
        print("1. Create Project")
        print("2. View Projects")
        print("3. Edit Project")
        print("4. Delete Project")
        print("5. Search Projects by Date")
        print("6. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            campaign.create_project()
        elif choice == "2":
            campaign.view_projects()
        elif choice == "3":
            campaign.edit_project()
        elif choice == "4":
            campaign.delete_project()
        elif choice == "5":
            campaign.search_projects_by_date()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
